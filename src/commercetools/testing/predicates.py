"""This module implements a parser for the commercetools predicate query
language.

It uses the pratt algorithm.

"""

import ast
import logging
import operator
import re
import typing
from functools import partial

import marshmallow

logger = logging.getLogger(__name__)

token_pat = re.compile(
    r"""
    (
        (?:\d+\.\d+) |       # Floats
        (?:\d+) |            # Integers
        "(?:\\.|[^"\\])*" |  # Double quoted strings
        '(?:\\.|[^'\\])*' |  # Single quoted strings
        (?:true|false)       # Booleans
    )
    |
    (
        (?:[a-zA-Z_][a-zA-Z0-9_-]+)     # keywords

    )
    |
    (
        (?:[<>!=]+) |         # symbols
        (?:[^\s])             # symbols
     )
""",
    re.VERBOSE,
)


class Tokenizer:
    def __init__(self, parser):
        self.parser = parser
        self.combined_tokens: typing.List[typing.List[str]] = []
        self._iterator = None

    def register_token_combination(self, tokens: typing.List[str]):
        self.combined_tokens.append(tokens)

    def tokenize(self, program):
        self._iterator = self._get_tokens(program)

    def __next__(self):
        return next(self._iterator)

    def _get_tokens(self, program) -> typing.Generator["Symbol", None, None]:
        buf: typing.List[str] = []
        for match in token_pat.finditer(program):
            value, identifier, symbol = match.groups()

            if identifier:
                for combination in self.combined_tokens:
                    i = len(buf)
                    if combination[i] == identifier:
                        buf.append(identifier)

                        if buf == combination:
                            identifier = " ".join(buf)
                            buf.clear()
                        break
                else:
                    for item in buf:
                        yield self.get_symbol(item, NameToken)
                    buf.clear()

                if buf:
                    continue
                yield self.get_symbol(identifier, NameToken)
            else:
                if buf:
                    for item in buf:
                        yield self.get_symbol(item, NameToken)
                    buf.clear()

                if value:
                    yield LiteralToken(self.parser, value)

                elif symbol:
                    yield self.get_symbol(symbol)

        yield self.parser.symbol_table["(end)"]

    def get_symbol(self, symbol, fallback=None):
        s = self.parser.symbol_table.get(symbol)
        if s:
            return s(self.parser, symbol)
        elif fallback:
            return NameToken(self.parser, symbol)
        else:
            raise ValueError("No symbol found for %r", symbol)


class Symbol:
    identifier: typing.Optional[str] = None
    lbp: typing.Optional[int] = None

    def __init__(self, parser, value):
        self.value = value
        self.parser = parser
        self.first = None
        self.second = None

    def nud(self):
        raise SyntaxError(
            "Syntax error (%r, token=%r)." % (self.identifier, self.__class__.__name__)
        )

    def led(self, left):
        raise SyntaxError("Unknown operator (%r)." % self.identifier)

    def __repr__(self):
        return "Symbol(identifier=%r, value=%r)" % (self.identifier, self.value)


class Parser:
    def __init__(self):
        self.symbol_table: typing.Dict[str, typing.Type[Symbol]] = {}
        self._peek: typing.Optional[Symbol] = None
        self.token: typing.Optional[Symbol] = None
        self.tokenizer = Tokenizer(self)

    def parse(self, program):
        self.tokenizer.tokenize(program)
        self.advance()
        assert self.token is not None

    def next(self):
        return next(self.tokenizer)

    def expression(self, rbp=0):
        assert self.token is not None
        t = self.token
        self.advance()
        left = t.nud()

        # t = age, left = ast.Name
        # self.token = not
        while rbp < self.token.lbp:
            t = self.token
            self.advance()
            left = t.led(left)
        return left

    def advance(self, identifier=None):
        if identifier and self.token and self.token.identifier != identifier:
            raise SyntaxError(
                "Expected %r, received %r" % (identifier, self.token.identifier)
            )

        if self._peek:
            self.token = self._peek
            self._peek = None
        else:
            self.token = self.next()

    def peek(self):
        if self._peek:
            return self._peek
        self._peek = self.next()
        return self._peek

    def define(self, sid, bp=0, symbol_class=Symbol):
        symbol_table = self.symbol_table
        sym: Symbol = typing.cast(
            Symbol,
            type(
                symbol_class.__name__, (symbol_class,), {"identifier": sid, "lbp": bp}
            ),
        )
        symbol_table[sid] = sym

        def wrapper(val):
            val.id = sid
            val.lbp = sym.lbp
            symbol_table[sid] = val
            return val

        if " " in sid:
            self.tokenizer.register_token_combination(sid.split())

        return wrapper


class Infix(Symbol):
    rightAssoc = False
    _logical_map = {"and": ast.And(), "or": ast.Or()}

    def led(self, left: Symbol):
        self.first = left
        rbp = self.lbp - int(self.rightAssoc)
        self.second = self.parser.expression(rbp)
        return self

    def __repr__(self):
        return "<'%s'>(%s, %s)" % (self.value, self.first, self.second)

    def ast(self, context: "Context"):
        lhs = self.first.ast(context)
        if self.second:
            rhs = self.second.ast(context)

            if self.value in self._logical_map:
                return ast.BoolOp(op=self._logical_map[self.value], values=[lhs, rhs])
            else:
                path = list(context.stack)
                path.append(self.first.value)

                return ast.Call(
                    func=ast.Name(id="filter_field", ctx=ast.Load()),
                    args=[
                        ast.Name(id="obj", ctx=ast.Load()),
                        ast.List(elts=[ast.Str(s=i) for i in path], ctx=ast.Load()),
                        ast.Str(s=self.value),
                        rhs,
                    ],
                    keywords=[],
                )
        return ast.Name(id="not", ctx=ast.Load())


class InfixR(Infix):
    rightAssoc = True

    def nud(self):
        self.first = self.parser.expression(2000)
        return self

    def ast(self, context=None):
        return ast.UnaryOp(op=ast.Not(), operand=self.first.ast(context))


class BinOp(Symbol):
    def __init__(self, value):
        self.lhs = None
        self.rhs = None

    def __repr__(self):
        parts = [self.lhs, self.identifier, self.rhs]
        return "BinOp(%s)" % " ".join(map(str, filter(None, parts)))


class Prefix(Symbol):
    def led(self):
        return self

    def nud(self):
        self.first = self.parser.expression(2000)
        return self

    def ast(self, context=None):
        return self.first.ast(context)
        return ast.UnaryOp(op=ast.Not(), operand=self.first.ast(context))

    def __repr__(self):
        return "<'%s'>(%s)" % (self.value, repr(self.first))


class LParen(Symbol):
    first: typing.Union[Symbol, list]

    def led(self, left: Symbol):
        self.first = left
        self.second = []
        while self.parser.token.identifier != ")":
            self.second.append(self.parser.expression())
        self.parser.advance(")")
        return self

    def nud(self):
        self.first = []
        self.second = []
        comma = False
        if self.parser.token.identifier != ")":
            while 1:
                if self.parser.token.identifier == ")":
                    break
                self.first.append(self.parser.expression())
                if self.parser.token.identifier != ",":
                    break
                comma = True
                self.parser.advance(",")
        self.parser.advance(")")
        if not self.first or comma:
            return self  # tuple
        else:
            return self.first[0]

    def ast(self, context: "Context"):
        if not self.second:
            return ast.Tuple(
                elts=[item.ast(context) for item in self.first], ctx=ast.Load()
            )
        context.stack.append(self.first.value)
        node = self.second[0].ast(context)
        context.stack.pop()
        return node

    def __repr__(self):
        parts = [self.first, self.second]
        return "LParen(%s)" % " ".join(map(repr, filter(None, parts)))


class LiteralToken(Symbol):
    identifier = "(literal)"
    lbp = 0

    def nud(self):
        return self

    def ast(self, context: "Context"):
        if self.value.isdigit():
            return ast.Num(n=int(self.value))
        if self.value in ["true", "false"]:
            return ast.NameConstant(self.parse_bool(self.value))
        else:
            return ast.Str(s=self.value[1:-1])

    def parse_bool(self, value) -> bool:
        return value == "true"


class LogicalToken(Symbol):
    identifier = "(logical)"
    lbp = 0

    def nud(self):
        return self


class NameToken(Symbol):
    identifier: str = "(name)"
    lbp: int = 0

    def nud(self):
        return self

    def ast(self, context: "Context"):
        return ast.Name(id=self.value, ctx=ast.Load())


class Constant(Symbol):
    identifier = "(constant)"
    lbp = 0

    def nud(self):
        return self

    def ast(self, context: "Context"):
        return ast.Constant(value=None, ctx=ast.Load())


class FunctionCall(Symbol):
    lbp = 0

    def nud(self):
        self.first = self.parser.expression(2000)
        return self

    def ast(self, context: "Context"):
        node = self.first.ast(context)
        node.elts.insert(0, ast.Str(s=self.value))
        return node


parser = Parser()

parser.define("<>", 60, Infix)
parser.define("in", 60, Infix)
parser.define("not in", 70, Infix)
parser.define("is", 60, Infix)
parser.define("is not", 60, Infix)
parser.define("defined", 60, Constant)
parser.define("within", 60, Infix)
parser.define("contains any", 60, Infix)
parser.define("contains all", 60, Infix)
parser.define("not", 90, InfixR)
parser.define("=", 60, Infix)

parser.define("and", 30, Infix)
parser.define("or", 30, Infix)

parser.define("(", 90, LParen)
parser.define("circle", 60, FunctionCall)
parser.define(")")
parser.define(">=", 60, Infix)
parser.define("<=", 60, Infix)
parser.define(">", 60, Infix)
parser.define("<", 60, Infix)
parser.define(",")
parser.define("(end)")


class Context:
    def __init__(self):
        self.stack: typing.List[str] = []

    def __repr__(self):
        return "Context(stack=%r)" % self.stack


class PredicateFilter:
    operators = {
        "<": operator.lt,
        "=<": operator.le,
        ">": operator.gt,
        ">=": operator.ge,
        "=": operator.eq,
        "!=": operator.ne,
        "<>": operator.ne,
        "is not": operator.is_not,
        "in": operator.contains,
    }

    def __init__(self, predicate, schema):
        self.predicate = predicate
        self.schema = schema
        ast_node = self.parse(predicate)
        self._code = compile(ast_node, "internal.py", mode="eval")
        logger.info("Compiled python code: %s", ast.dump(ast_node))

    def match(self, obj):
        try:
            return eval(self._code, {}, {"obj": obj, "filter_field": self.filter_field})
        except TypeError as exc:
            return False

    def _get_schema_fields(self, schema):
        result = {}
        for name, field in schema._declared_fields.items():
            key = field.data_key or name
            result[key] = field
        return result

    def filter_field(
        self,
        obj: typing.Dict[typing.Any, typing.Any],
        path: typing.List[str],
        operator_value: str,
        value: typing.Any,
        schema=None,
    ):
        if schema is None:
            schema = self.schema

        schema_field: typing.Optional[marshmallow.fields.Field] = None

        for i, key in enumerate(path):
            fields = self._get_schema_fields(schema)
            schema_field = self.case_insensitive_get(fields, key, None)

            # Query field doesn't exist
            if schema_field is None:
                raise ValueError("No field %s on schema %s" % (key, schema))
            assert schema_field is not None

            if isinstance(schema_field, marshmallow.fields.Nested):
                schema = schema_field.schema

            # Get value
            if isinstance(obj, dict):
                obj = self.case_insensitive_get(obj, key, {})
                if isinstance(schema_field, marshmallow.fields.Dict):
                    path = path[i + 1 :]
                    break

            elif isinstance(obj, list):
                return any(
                    self.filter_field(
                        child_doc, path[i:], operator_value, value, schema=schema
                    )
                    for child_doc in obj
                )

        is_sequence_value = False

        if isinstance(schema_field, marshmallow.fields.Dict):
            obj = schema_field._deserialize(obj, None, None)
            assert len(path) == 1
            obj = self.case_insensitive_get(obj, path[0], None)
        else:
            if obj is not None:
                obj = schema_field._deserialize(obj, None, None)
            if value is not None:
                is_sequence_value = isinstance(value, tuple) or isinstance(value, list)
                if is_sequence_value:
                    deserialize = partial(
                        schema_field._deserialize, attr=None, data=None
                    )
                    value = list(map(deserialize, value))
                else:
                    value = schema_field._deserialize(value, None, None)

        op = self.operators[operator_value]

        # Case insensitive comparison for strings
        if isinstance(obj, str):
            obj = obj.lower()
        if isinstance(value, str):
            value = value.lower()
        elif is_sequence_value:
            value = [x.lower() if isinstance(x, str) else x for x in value]
            if operator_value == "in":
                return op(value, obj)

        # allow comparing single values with 'in' syntax
        if operator_value == "in" and not isinstance(value, list):
            return op([value], obj)

        return op(obj, value)

    def case_insensitive_get(sef, dict, key, default=None):
        for k, v in dict.items():
            if k.lower() == key.lower():
                return v
        return default

    def parse(self, program):
        expr = parser.parse(program)
        expr = parser.expression()

        context = Context()

        node = ast.Expression(body=expr.ast(context))
        for child in ast.walk(node):
            child.lineno = 0
            child.col_offset = 0

        return node

import ast
import logging
import re

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
        self.combined_tokens = []
        self._iterator = None

    def register_token_combination(self, tokens):
        self.combined_tokens.append(tokens)

    def tokenize(self, program):
        self._iterator = self._get_tokens(program)

    def __next__(self):
        return next(self._iterator)

    def _get_tokens(self, program):
        buf = []
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
    identifier = None
    lbp = None

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
        raise SyntaxError("Unknown operator (%r)." % self.id)

    def __repr__(self):
        return "Symbol(identifier=%r, value=%r)" % (self.identifier, self.value)


class Parser:
    def __init__(self):
        self.symbol_table = {}
        self._peek = None
        self.tokenizer = Tokenizer(self)

    def parse(self, program):
        self.tokenizer.tokenize(program)
        self.advance()
        assert self.token is not None

    def next(self):
        return next(self.tokenizer)

    def expression(self, rbp=0):
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
        if identifier and self.token.identifier != identifier:
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
        sym = symbol_table[sid] = type(
            symbol_class.__name__, (symbol_class,), {"identifier": sid, "lbp": bp}
        )

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
    _operator_map = {"in": ast.In(), ">": ast.Gt(), "<": ast.Lt(), "=": ast.Eq()}
    _logical_map = {"and": ast.And(), "or": ast.Or()}

    def led(self, left):
        self.first = left
        rbp = self.lbp - int(self.rightAssoc)
        self.second = self.parser.expression(rbp)

        return self

    def __repr__(self):
        return "<'%s'>(%s, %s)" % (self.value, self.first, self.second)

    def ast(self, context=None):
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
        out = [self.lhs, self.identifier, self.rhs]
        out = map(str, filter(None, out))
        return "BinOp(" + " ".join(out) + ")"


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
    def led(self, left):
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

    def ast(self, context=None):
        if not self.second:
            return ast.Tuple(
                elts=[item.ast(context) for item in self.first], ctx=ast.Load()
            )
        context.stack.append(self.first.value)
        return self.second[0].ast(context)

    def __repr__(self):
        out = [self.first, self.second]
        out = map(repr, filter(None, out))
        return "LParen(" + " ".join(out) + ")"


class LiteralToken(Symbol):
    identifier = "(literal)"
    lbp = 0

    def nud(self):
        return self

    def ast(self, context=None):
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
    identifier = "(name)"
    lbp = 0

    def nud(self):
        return self

    def ast(self, context=None):
        return ast.Name(id=self.value, ctx=ast.Load())


class Constant(Symbol):
    identifier = "(constant)"
    lbp = 0

    def nud(self):
        return self

    def ast(self, context=None):
        return ast.Name(id="None", ctx=ast.Load())


class FunctionCall(Symbol):
    lbp = 0

    def nud(self):
        self.first = self.parser.expression(2000)
        return self

    def ast(self, context):
        node = self.first.ast()
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
parser.define(">", 60, Infix)
parser.define("<", 60, Infix)
parser.define(",")
parser.define("(end)")


class Context:
    def __init__(self):
        self.stack = []


class PredicateFilter:
    def __init__(self, predicate):
        self.predicate = predicate
        ast_node = self.parse(predicate)
        self._code = compile(ast_node, "internal.py", mode="eval")
        logger.info("Compiled python code:", ast.dump(ast_node))

    def match(self, obj):
        try:
            return eval(self._code, {}, {"obj": obj, "filter_field": self.filter_field})
        except TypeError as exc:
            return False

    def filter_field(self, obj, path, operator, value):
        for i, key in enumerate(path):
            if isinstance(obj, list):
                return any(
                    self.filter_field(child_doc, path[i:], operator, value)
                    for child_doc in obj
                )
            if isinstance(obj, dict):
                obj = self.case_insensitive_get(obj, key, {})

        if isinstance(obj, str):
            obj = obj.lower()
        if isinstance(value, str):
            value = value.lower()

        return obj == value

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

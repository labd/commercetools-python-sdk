import ast
import keyword
import re
import textwrap
import typing
from collections import defaultdict

import astunparse


def snakeit(name) -> typing.Optional[str]:
    if not name:
        return None

    name = name.replace("OAuth", "OAUTH")
    name = name.replace(".", "_")

    # https://stackoverflow.com/questions/1175208/
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    val = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
    if keyword.iskeyword(val):
        val = val + "_"

    val = val.replace("-", "_")
    val = val.replace("__", "_")
    return val


def create_codename(value):
    if value.startswith("/"):
        values = re.findall("/([^\/]+)", value)
        value = values[0]
    return snakeit(value)


def create_method_name(value):
    if value.startswith("/"):
        values = re.findall("/([^\/]+)", value)
        value = "_".join(values)
    return snakeit(value)


def extract_name(value):
    if not value:
        return None
    if "|" in value:
        found = value.split("|")[0]
        return found.strip()
    return value


def class_name(val) -> str:
    return val[0].upper() + val[1:]


def enum_attr(val) -> str:
    val = val.replace("-", "_")
    val = snakeit(val)
    if val:
        val = val.upper()
        if keyword.iskeyword(val):
            val += "_"
    return val


def merge_imports(imports) -> typing.List[ast.AST]:
    importfrom_nodes: typing.Dict[str, typing.Dict[str, ast.AST]] = defaultdict(dict)
    import_nodes = set()
    for node in imports:
        if isinstance(node, ast.ImportFrom):
            for alias in node.names:
                importfrom_nodes[node.module][alias.name] = alias
        else:
            for alias in node.names:
                import_nodes.add(alias.name)

    result: typing.List[ast.AST] = []
    for name in sorted(import_nodes):
        result.append(ast.Import(names=[ast.alias(name=name, asname=None)], level=0))
    for name, aliases in importfrom_nodes.items():
        result.append(ast.ImportFrom(module=name, names=aliases.values(), level=0))

    return result


def reorder_class_definitions(definitions):
    """From https://stackoverflow.com/questions/5287516 :P

    "arg" is a dependency dictionary in which
    the values are the dependencies of their respective keys.

    """
    graph = {}
    for node in definitions:
        graph[node.name] = [astunparse.unparse(b).strip() for b in node.bases]

    d = dict((k, set(graph[k])) for k in graph)
    r = []
    while d:
        # values not in keys (items without dep)
        t = set(i for v in d.values() for i in v) - set(d.keys())
        # and keys without value (items without dep)
        t.update(k for k, v in d.items() if not v)
        # can be done right away
        r.append(t)
        # and cleaned up
        d = dict(((k, v - t) for k, v in d.items() if v))

    nodes = {node.name: node for node in definitions}

    result = []
    for items in r:
        for name in sorted(items):
            if name in nodes:
                result.append(nodes[name])
            elif not name.startswith(("enum.", "typing.", "marshmallow.")):
                pass
    return result


def format_docstring(val, indent=1):
    lines = [l.strip() for l in val.split("\n")]
    newlines = []
    indent_str = " " * (4 * indent)
    width = 79 - len(indent_str)

    initial_line = lines.pop(0)
    if "." in initial_line:
        first, second = initial_line.split(".", 1)
        initial_line = first + "."
        if second.strip():
            lines.insert(0, second.strip())

    short = textwrap.wrap(initial_line, width=width, subsequent_indent=indent_str)
    if not lines:
        return "\n".join(short)

    extra = textwrap.wrap(
        "\n".join(lines).strip(),
        width=width + 10,
        initial_indent=indent_str,
        subsequent_indent=indent_str,
    )
    docstring = "\n".join(short) + "\n\n" + "\n".join(extra)
    return docstring.strip() + ("\n" + indent_str)

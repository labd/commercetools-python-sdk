import ast
import keyword
import re
import typing
from collections import defaultdict

import astunparse


def snakeit(name) -> typing.Optional[str]:
    if not name:
        return None

    name = name.replace('OAuth', 'OAUTH')

    # https://stackoverflow.com/questions/1175208/
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    val = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
    if keyword.iskeyword(val):
        val = val + "_"
    return val


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

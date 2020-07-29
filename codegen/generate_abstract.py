import ast
import typing
from collections import defaultdict


class AbstractModuleGenerator:
    def __init__(self):
        self._import_set: typing.Dict[
            str, typing.Set[typing.Tuple[str, str]]
        ] = defaultdict(set)
        self._import_nodes: typing.Dict[str, typing.List[ast.AST]] = defaultdict(list)

    def add_import_statement(self, source, module_name, *subpackages):
        key = (module_name, subpackages)
        if key in self._import_set[source]:
            return
        if subpackages:
            node = ast.ImportFrom(
                module=module_name,
                names=[ast.alias(name=pkg, asname=None) for pkg in subpackages],
                level=0,
            )
        else:
            node = ast.Import(names=[ast.alias(name=module_name, asname=None)], level=0)
        self._import_set[source].add(key)
        self._import_nodes[source].append(node)

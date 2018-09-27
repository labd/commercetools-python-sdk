import ast


class AbstractModuleGenerator:
    def __init__(self):
        self._import_set = set()

    def add_import_statement(self, module_name, *subpackages):
        key = (module_name, subpackages)
        if key in self._import_set:
            return
        if subpackages:
            node = ast.ImportFrom(
                module=module_name,
                names=[ast.alias(name=pkg, asname=None) for pkg in subpackages],
            )
        else:
            node = ast.Import(names=[ast.alias(name=module_name, asname=None)], level=0)
        self._import_set.add(key)
        self._import_nodes.append(node)

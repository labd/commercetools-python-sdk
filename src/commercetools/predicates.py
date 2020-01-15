import json
from collections.abc import Collection
from decimal import Decimal
from functools import reduce


class QueryPredicate:
    AND = "AND"
    OR = "OR"

    _operators = {
        "exact": "=",
        "gte": ">=",
        "in": "in",
        "lte": "=<",
        "lt": "<",
        "gt": ">",
        "is_defined": ("is defined", "is not defined"),
        "contains_all": "contains all",
        "contains_any": "contains any",
    }

    def __init__(self, **filters: str) -> None:
        self._siblings = filters.pop("_siblings", [])
        self._filters = filters

    def __str__(self) -> str:
        result = []

        for key, value in self._filters.items():
            fields = key.split("__")
            operator = fields.pop()
            if operator not in self._operators:
                fields.append(operator)
                operator = "exact"

            lhs = fields.pop()
            val = self._clause(lhs, operator, value)
            fields.append(val)
            result.append(reduce(lambda x, y: f"{y}({x})", fields[::-1]))

        val = " AND ".join(result)
        if self._siblings:
            return reduce(
                lambda x, y: f"({x}) {y.connector} ({y.query_predicate})",
                self._siblings,
                val,
            )
        return val

    def __or__(self, other):
        _siblings = self._siblings[:] + [_SiblingQueryPredicate(self.OR, other)]
        return self.__class__(**self._filters, _siblings=_siblings)

    def __and__(self, other):
        _siblings = self._siblings[:] + [_SiblingQueryPredicate(self.AND, other)]
        return self.__class__(**self._filters, _siblings=_siblings)

    def _clause(self, lhs, operator, rhs) -> str:
        assert operator in self._operators

        if isinstance(rhs, dict):
            rhs = self.__class__(**rhs)
            return "%s(%s)" % (lhs, rhs)

        if isinstance(rhs, self.__class__):
            return "%s(%s)" % (lhs, rhs)

        op = self._operators[operator]
        if isinstance(op, tuple):
            return "%s %s" % (lhs, op[0 if rhs else 1])
        else:
            rhs = self._escape_value(rhs)
            return "%s %s %s" % (lhs, op, rhs)

    def _escape_value(self, value) -> str:
        if isinstance(value, self.__class__):
            return "(%s)" % value
        if isinstance(value, Decimal):
            return str(value)
        if not isinstance(value, str) and isinstance(value, Collection):
            return "(%s)" % (", ".join(self._escape_value(v) for v in value))
        return json.dumps(value)


class _SiblingQueryPredicate:
    def __init__(self, connector: str, query_predicate: QueryPredicate):
        self.connector = connector
        self.query_predicate = query_predicate

import ast
import re

import pytest

from commercetools.testing import predicates


@pytest.mark.parametrize(
    "predicate",
    [
        "age <> 42",
        r'not (name = "P\"eter" and age < 42)',
        "age not in (42, 43, 44)",
        'tags contains all ("a", "b", "c")',
        'tags contains all ("a", "b", "c")',
        'name = "Peter" or name = "Barbara D"',
        'name in ("Peter", "Barbara")',
        "name is not defined",
        "geoLocation within circle(13.37770, 52.51627, 1000)",
        "isDefault = true",
        "isDefault = false",
        'variants(attributes(name="attribute-name" and value(centAmount > 999 and centAmount < 1001 and currencyCode="EUR")))',
    ],
)
def test_tokenize(predicate):
    predicates.PredicateFilter(predicate)

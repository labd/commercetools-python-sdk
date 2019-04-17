import ast
import re

import pytest

from commercetools import schemas
from commercetools.testing import predicates


@pytest.mark.parametrize(
    "predicate",
    [
        "age <> 42",
        "age >= 42",
        "age <= 42",
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
    predicates.PredicateFilter(predicate, schema=None)


@pytest.mark.parametrize(
    "predicate,paths",
    [
        (
            'slug(nl-uk = "test-categorie" or nl-nl = "test-categorie")',
            [["slug", "nl-uk"], ["slug", "nl-nl"]],
        ),
        (
            'slug(nl-be = "test-categorie") and masterVariant is not defined',
            [["slug", "nl-be"], ["masterVariant"]],
        ),
    ],
)
def test_filter(predicate, paths):
    pf = predicates.PredicateFilter(predicate, schema=schemas.ProductDataSchema)

    found_paths = []

    org_filter_field = pf.filter_field

    def mock_filter_field(obj, path, operator, value):
        found_paths.append(path)
        return org_filter_field(obj, path, operator, value)

    pf.filter_field = mock_filter_field
    pf.match({"slug": {"nl-BE": "test-categorie"}})
    assert paths == found_paths

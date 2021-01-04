import pytest

from commercetools.platform.models._schemas.product import ProductDataSchema
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
        'custom(fields(someCustomField="123123123")) and createdAt >= "2019-10-15T14:12:36.464465"',
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
    pf = predicates.PredicateFilter(predicate, schema=ProductDataSchema)

    found_paths = []

    org_filter_field = pf.filter_field

    def mock_filter_field(obj, path, operator, value):
        found_paths.append(path)
        return org_filter_field(obj, path, operator, value)

    pf.filter_field = mock_filter_field
    pf.match({"slug": {"nl-BE": "test-categorie"}})
    assert paths == found_paths


def test_in_filter():
    skus = '("1337", "1338")'
    predicate = f"masterVariant(sku in {skus}) or variants(sku in {skus})"
    pf = predicates.PredicateFilter(predicate, schema=ProductDataSchema)

    product_data = {
        "masterVariant": {"sku": "1337"},
        "variants": [{"sku": "1338"}, {"sku": "1339"}],
    }
    assert pf.match(product_data) is True

    product_data = {
        "masterVariant": {"sku": "1444"},
        "variants": [{"sku": "1338"}, {"sku": "1339"}],
    }
    assert pf.match(product_data) is True

    product_data = {
        "masterVariant": {"sku": "1444"},
        "variants": [{"sku": "1438"}, {"sku": "1139"}],
    }
    assert pf.match(product_data) is False

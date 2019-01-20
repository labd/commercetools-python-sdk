from commercetools.predicates import QueryPredicate


def test_simple():
    obj = QueryPredicate(masterVariant__prices__country="NL")
    assert str(obj) == 'masterVariant(prices(country = "NL"))'


def test_two_filters():
    obj = QueryPredicate(
        masterVariant__slug__nl="some-slug", masterVariant__prices__country="NL"
    )
    assert (
        str(obj)
        == 'masterVariant(slug(nl = "some-slug")) AND masterVariant(prices(country = "NL"))'
    )


def test_dict_format():
    obj = QueryPredicate(**{"masterVariant__slug__en-GB": "something"})
    assert str(obj) == 'masterVariant(slug(en-GB = "something"))'


def test_nested_dict():
    obj = QueryPredicate(masterVariant={"slug__en-GB": "something", "prices": 100})
    assert str(obj) == 'masterVariant(slug(en-GB = "something") AND prices = 100)'

    obj = QueryPredicate(supplyChannel={"id": 100, "sku": "S001"})
    assert str(obj) == 'supplyChannel(id = 100 AND sku = "S001")'


def test_is_defined():
    obj = QueryPredicate(
        masterVariant__slug__is_defined=True, masterVariant__prices__is_defined=False
    )
    assert (
        str(obj)
        == "masterVariant(slug is defined) AND masterVariant(prices is not defined)"
    )


def test_gte():
    obj = QueryPredicate(
        masterVariant__slug__nl__exact="some-slug",
        masterVariant__prices__amount__gte=100,
    )
    assert (
        str(obj)
        == 'masterVariant(slug(nl = "some-slug")) AND masterVariant(prices(amount >= 100))'
    )


def test_qp_contains_any():
    obj = QueryPredicate(masterVariant__slug__nl__contains_any=["slug-1", "slug-2"])
    assert str(obj) == 'masterVariant(slug(nl contains any ("slug-1", "slug-2")))'


def test_qp_or():
    obj = QueryPredicate(
        masterVariant__slug=QueryPredicate(nl="test-nl") | QueryPredicate(en="test-en")
    )
    assert str(obj) == 'masterVariant(slug(nl = "test-nl" OR en = "test-en"))'


def test_qp_and():
    obj = QueryPredicate(
        masterVariant__slug=QueryPredicate(nl="test-nl") & QueryPredicate(en="test-en")
    )
    assert str(obj) == 'masterVariant(slug(nl = "test-nl" AND en = "test-en"))'

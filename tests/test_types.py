from commercetools import types


def test_non_equality():
    obj_1 = types.ProductDraft(
        slug=types.LocalizedString(en="test-2"),
        name=types.LocalizedString(en="test-1"),
        product_type=types.ProductTypeResourceIdentifier(key="dummy"),
    )
    obj_2 = types.ProductDraft(
        slug=types.LocalizedString(en="test-1"),
        name=types.LocalizedString(en="test-1"),
        product_type=types.ProductTypeResourceIdentifier(key="dummy"),
    )
    assert obj_1 != obj_2


def test_equality():
    obj_1 = types.ProductDraft(
        slug=types.LocalizedString(en="test-1"),
        name=types.LocalizedString(en="test-1"),
        product_type=types.ProductTypeResourceIdentifier(key="dummy"),
    )
    obj_2 = types.ProductDraft(
        slug=types.LocalizedString(en="test-1"),
        name=types.LocalizedString(en="test-1"),
        product_type=types.ProductTypeResourceIdentifier(key="dummy"),
    )
    assert obj_1 == obj_2

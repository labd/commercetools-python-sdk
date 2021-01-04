from commercetools.platform import models


def test_non_equality():
    obj_1 = models.ProductDraft(
        slug=models.LocalizedString(en="test-2"),
        name=models.LocalizedString(en="test-1"),
        product_type=models.ProductTypeResourceIdentifier(key="dummy"),
    )
    obj_2 = models.ProductDraft(
        slug=models.LocalizedString(en="test-1"),
        name=models.LocalizedString(en="test-1"),
        product_type=models.ProductTypeResourceIdentifier(key="dummy"),
    )
    assert obj_1 != obj_2


def test_equality():
    obj_1 = models.ProductDraft(
        slug=models.LocalizedString(en="test-1"),
        name=models.LocalizedString(en="test-1"),
        product_type=models.ProductTypeResourceIdentifier(key="dummy"),
    )
    obj_2 = models.ProductDraft(
        slug=models.LocalizedString(en="test-1"),
        name=models.LocalizedString(en="test-1"),
        product_type=models.ProductTypeResourceIdentifier(key="dummy"),
    )
    assert obj_1 == obj_2

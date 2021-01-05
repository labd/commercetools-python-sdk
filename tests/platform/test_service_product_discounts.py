from commercetools.platform import models


def test_product_discount_get_by_id(old_client):
    product_discount = old_client.product_discounts.create(
        models.ProductDiscountDraft(
            name=models.LocalizedString(nl="test-discount"),
            predicate="",
            value=models.ProductDiscountValueRelativeDraft(permyriad=10),
            is_active=True,
            sort_order="",
        )
    )

    assert product_discount.id

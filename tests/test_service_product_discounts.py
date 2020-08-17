from commercetools import types


def test_product_discount_get_by_id(client):
    product_discount = client.product_discounts.create(
        types.ProductDiscountDraft(
            name=types.LocalizedString(nl="test-discount"),
            predicate="",
            value=types.ProductDiscountValueRelativeDraft(permyriad=10),
            is_active=True,
            sort_order="",
        )
    )

    assert product_discount.id

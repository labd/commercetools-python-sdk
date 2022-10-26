from commercetools.platform import models
from commercetools.platform.client import Client


def test_product_discount_with_id_get(ct_platform_client: Client):
    product_discount = (
        ct_platform_client.with_project_key("unittest")
        .product_discounts()
        .post(
            models.ProductDiscountDraft(
                name=models.LocalizedString(nl="test-discount"),
                predicate="",
                value=models.ProductDiscountValueRelativeDraft(permyriad=10),
                is_active=True,
                sort_order="",
            )
        )
    )
    assert product_discount
    assert product_discount.id

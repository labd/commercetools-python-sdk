import pytest

from commercetools import CommercetoolsError
from commercetools.platform import models


def test_correlation_id_is_set_in_exception(old_client):
    product = old_client.products.create(
        models.ProductDraft(
            key="test-product",
            name=models.LocalizedString(en=f"my-product"),
            slug=models.LocalizedString(en=f"my-product"),
            product_type=models.ProductTypeResourceIdentifier(key="dummy"),
        )
    )

    product = old_client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            models.ProductChangeSlugAction(slug=models.LocalizedString(nl="nl-slug2"))
        ],
    )

    # This should raise a version conflict error
    with pytest.raises(CommercetoolsError) as exc:
        old_client.products.update_by_id(
            id=product.id,
            version=1,
            actions=[
                models.ProductChangeSlugAction(
                    slug=models.LocalizedString(nl="nl-slug3")
                )
            ],
        )

    assert exc.value.correlation_id is not None

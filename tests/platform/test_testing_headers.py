import pytest

from commercetools import CommercetoolsError
from commercetools.platform import models
from commercetools.platform.client import Client


def test_correlation_id_is_set_in_exception(ct_platform_client: Client):
    product = (
        ct_platform_client.with_project_key("foo")
        .products()
        .post(
            models.ProductDraft(
                key="test-product",
                name=models.LocalizedString(en=f"my-product"),
                slug=models.LocalizedString(en=f"my-product"),
                product_type=models.ProductTypeResourceIdentifier(key="dummy"),
            )
        )
    )

    product = (
        ct_platform_client.with_project_key("foo")
        .products()
        .with_id(product.id)
        .post(
            models.ProductUpdate(
                version=product.version,
                actions=[
                    models.ProductChangeSlugAction(
                        slug=models.LocalizedString(nl="nl-slug2")
                    )
                ],
            )
        )
    )

    # This should raise a version conflict error
    with pytest.raises(CommercetoolsError) as exc:
        product = (
            ct_platform_client.with_project_key("foo")
            .products()
            .with_id(product.id)
            .post(
                models.ProductUpdate(
                    version=1,  # conflicting version
                    actions=[
                        models.ProductChangeSlugAction(
                            slug=models.LocalizedString(nl="nl-slug2")
                        )
                    ],
                )
            )
        )

    assert exc.value.correlation_id is not None

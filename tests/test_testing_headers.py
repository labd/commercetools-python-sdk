import pytest

from commercetools import CommercetoolsError, types


def test_correlation_id_is_set_in_exception(client):
    product = client.products.create(types.ProductDraft(key="test-product"))

    product = client.products.update_by_id(
        id=product.id,
        version=product.version,
        actions=[
            types.ProductChangeSlugAction(slug=types.LocalizedString(nl="nl-slug2"))
        ],
    )

    # This should raise a version conflict error
    with pytest.raises(CommercetoolsError) as exc:
        client.products.update_by_id(
            id=product.id,
            version=1,
            actions=[
                types.ProductChangeSlugAction(slug=types.LocalizedString(nl="nl-slug3"))
            ],
        )

    assert exc.value.correlation_id is not None

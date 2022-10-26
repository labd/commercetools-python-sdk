import pytest
from requests.exceptions import HTTPError

from commercetools.platform import models
from commercetools.platform.client import Client


def test_product_types_with_id_get(ct_platform_client: Client):
    product_type = (
        ct_platform_client.with_project_key("unittest")
        .product_types()
        .post(
            models.ProductTypeDraft(
                key="test-product-type", name="test", description="something"
            )
        )
    )

    assert product_type.id
    assert product_type.key == "test-product-type"

    product_type = (
        ct_platform_client.with_project_key("unittest")
        .product_types()
        .with_id(product_type.id)
        .get()
    )
    assert product_type.id
    assert product_type.key == "test-product-type"

    with pytest.raises(HTTPError) as e:
        ct_platform_client.with_project_key("unittest").product_types().with_id(
            "invalid"
        ).get()


def test_product_types_get_by_key(ct_platform_client: Client):
    product_type = (
        ct_platform_client.with_project_key("unittest")
        .product_types()
        .post(
            models.ProductTypeDraft(
                key="test-product-type", name="test", description="something"
            )
        )
    )

    assert product_type.id
    assert product_type.key == "test-product-type"

    product_type = (
        ct_platform_client.with_project_key("unittest")
        .product_types()
        .with_key("test-product-type")
        .get()
    )
    assert product_type.id
    assert product_type.key == "test-product-type"

    with pytest.raises(HTTPError) as e:
        ct_platform_client.with_project_key("unittest").product_types().with_id(
            "invalid"
        ).get()


def test_product_type_query(ct_platform_client: Client):
    ct_platform_client.with_project_key("unittest").product_types().post(
        models.ProductTypeDraft(
            key="test-product-type1", name="test-1", description="something"
        )
    )
    ct_platform_client.with_project_key("unittest").product_types().post(
        models.ProductTypeDraft(
            key="test-product-type2", name="test-2", description="something"
        )
    )

    # single sort query
    result = (
        ct_platform_client.with_project_key("unittest")
        .product_types()
        .get(sort="id asc")
    )
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = (
        ct_platform_client.with_project_key("unittest")
        .product_types()
        .get(sort=["id asc", "name asc"])
    )
    assert len(result.results) == 2
    assert result.total == 2


def test_product_update(ct_platform_client: Client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    product_type = (
        ct_platform_client.with_project_key("unittest")
        .product_types()
        .post(
            models.ProductTypeDraft(
                key="test-product-type", name="test", description="something"
            )
        )
    )

    assert product_type.id
    assert product_type.key == "test-product-type"

    product_type = (
        ct_platform_client.with_project_key("unittest")
        .product_types()
        .with_id(product_type.id)
        .post(models.ProductTypeUpdate(version=product_type.version, actions=[]))
    )
    assert product_type.key == "test-product-type"

    product_type = (
        ct_platform_client.with_project_key("test")
        .product_types()
        .with_key(key="test-product-type")
        .post(models.ProductTypeUpdate(version=product_type.version, actions=[]))
    )
    assert product_type.key == "test-product-type"


def test_product_update_attribute_constraint_change(ct_platform_client: Client):
    attribute_name = "testConstraint"
    product_type = (
        ct_platform_client.with_project_key("unittest")
        .product_types()
        .post(
            models.ProductTypeDraft(
                key="test-product-type",
                name="test",
                description="something",
                attributes=[
                    models.AttributeDefinitionDraft(
                        type=models.AttributeTextType(),
                        name=attribute_name,
                        label=models.LocalizedString({"en": "testConstraint"}),
                        is_required=False,
                        attribute_constraint=models.AttributeConstraintEnum.SAME_FOR_ALL,
                    )
                ],
            )
        )
    )

    assert product_type.id
    assert product_type.key == "test-product-type"
    assert (
        product_type.attributes[0].attribute_constraint
        == models.AttributeConstraintEnum.SAME_FOR_ALL
    )

    product_type = (
        ct_platform_client.with_project_key("unittest")
        .product_types()
        .with_id(
            product_type.id,
        )
        .post(
            models.ProductTypeUpdate(
                version=product_type.version,
                actions=[
                    models.ProductTypeChangeAttributeConstraintAction(
                        attribute_name=attribute_name,
                        new_value=models.AttributeConstraintEnumDraft.NONE,
                    )
                ],
            )
        )
    )

    assert product_type.key == "test-product-type"
    assert (
        product_type.attributes[0].attribute_constraint
        == models.AttributeConstraintEnum.NONE
    )

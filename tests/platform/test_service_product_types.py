import pytest
from requests.exceptions import HTTPError

from commercetools.platform import models


def test_product_types_get_by_id(old_client):
    product_type = old_client.product_types.create(
        models.ProductTypeDraft(
            key="test-product-type", name="test", description="something"
        )
    )

    assert product_type.id
    assert product_type.key == "test-product-type"

    product_type = old_client.product_types.get_by_id(product_type.id)
    assert product_type.id
    assert product_type.key == "test-product-type"

    with pytest.raises(HTTPError) as e:
        old_client.product_types.get_by_id("invalid")


def test_product_types_get_by_key(old_client):
    product_type = old_client.product_types.create(
        models.ProductTypeDraft(
            key="test-product-type", name="test", description="something"
        )
    )

    assert product_type.id
    assert product_type.key == "test-product-type"

    product_type = old_client.product_types.get_by_key("test-product-type")
    assert product_type.id
    assert product_type.key == "test-product-type"

    with pytest.raises(HTTPError) as e:
        old_client.product_types.get_by_key("invalid")


def test_product_type_query(old_client):
    old_client.product_types.create(
        models.ProductTypeDraft(
            key="test-product-type1", name="test-1", description="something"
        )
    )
    old_client.product_types.create(
        models.ProductTypeDraft(
            key="test-product-type2", name="test-2", description="something"
        )
    )

    # single sort query
    result = old_client.product_types.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = old_client.product_types.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_product_update(old_client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    product_type = old_client.product_types.create(
        models.ProductTypeDraft(
            key="test-product-type", name="test", description="something"
        )
    )

    assert product_type.id
    assert product_type.key == "test-product-type"

    product_type = old_client.product_types.update_by_id(
        id=product_type.id, version=product_type.version, actions=[]
    )
    assert product_type.key == "test-product-type"

    product_type = old_client.product_types.update_by_key(
        key="test-product-type", version=product_type.version, actions=[]
    )
    assert product_type.key == "test-product-type"


def test_product_update_attribute_constraint_change(old_client):
    attribute_name = "testConstraint"
    product_type = old_client.product_types.create(
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

    assert product_type.id
    assert product_type.key == "test-product-type"
    assert (
        product_type.attributes[0].attribute_constraint
        == models.AttributeConstraintEnum.SAME_FOR_ALL
    )

    product_type = old_client.product_types.update_by_id(
        id=product_type.id,
        version=product_type.version,
        actions=[
            models.ProductTypeChangeAttributeConstraintAction(
                attribute_name=attribute_name,
                new_value=models.AttributeConstraintEnumDraft.NONE,
            )
        ],
    )

    assert product_type.key == "test-product-type"
    assert (
        product_type.attributes[0].attribute_constraint
        == models.AttributeConstraintEnum.NONE
    )

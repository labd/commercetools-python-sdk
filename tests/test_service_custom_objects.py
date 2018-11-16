import pytest
from requests.exceptions import HTTPError

from commercetools import types


def test_custom_object_get_by_id(client):
    custom_object = client.custom_objects.create_or_update(
        types.CustomObjectDraft(container="unittest", key="test-object", value=1234)
    )

    assert custom_object.id
    assert custom_object.container == "unittest"
    assert custom_object.key == "test-object"
    assert custom_object.value == 1234

    custom_object = client.custom_objects.get_by_id(custom_object.id)
    assert custom_object.container == "unittest"
    assert custom_object.key == "test-object"
    assert custom_object.value == 1234

    with pytest.raises(HTTPError):
        client.custom_objects.get_by_id("invalid")


def test_custom_object_query(client):
    client.custom_objects.create_or_update(
        types.CustomObjectDraft(container="unittest", key="test-object-1", value=1234)
    )
    client.custom_objects.create_or_update(
        types.CustomObjectDraft(container="unittest", key="test-object-2", value=1234)
    )

    # single sort query
    result = client.custom_objects.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = client.custom_objects.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_custom_object_update(client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    custom_object = client.custom_objects.create_or_update(
        types.CustomObjectDraft(container="unittest", key="test-object-1", value=1234)
    )
    assert custom_object.key == "test-object-1"

    custom_object = client.custom_objects.create_or_update(
        types.CustomObjectDraft(container="unittest", key="test-object-1", value=2345)
    )
    assert custom_object.key == "test-object-1"

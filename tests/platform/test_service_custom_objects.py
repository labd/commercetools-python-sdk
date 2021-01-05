import pytest
from requests.exceptions import HTTPError

from commercetools.platform import models


def test_custom_object_get_by_container_and_key(old_client):
    custom_object = old_client.custom_objects.create_or_update(
        models.CustomObjectDraft(container="unittest", key="test-object", value=1234)
    )

    assert custom_object.id
    assert custom_object.container == "unittest"
    assert custom_object.key == "test-object"
    assert custom_object.value == 1234

    custom_object = old_client.custom_objects.get_by_container_and_key(
        "unittest", "test-object"
    )
    assert custom_object.container == "unittest"
    assert custom_object.key == "test-object"
    assert custom_object.value == 1234

    with pytest.raises(HTTPError):
        old_client.custom_objects.get_by_container_and_key("invalid", "invalid")


def test_custom_object_query(old_client):
    old_client.custom_objects.create_or_update(
        models.CustomObjectDraft(container="unittest", key="test-object-1", value=1234)
    )
    old_client.custom_objects.create_or_update(
        models.CustomObjectDraft(container="unittest", key="test-object-2", value=1234)
    )

    # single sort query
    result = old_client.custom_objects.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = old_client.custom_objects.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_custom_object_update(old_client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    """
    custom_object = old_client.custom_objects.create_or_update(
        models.CustomObjectDraft(container="unittest", key="test-object-1", value=1234)
    )
    assert custom_object.key == "test-object-1"
    assert custom_object.value == 1234
    assert custom_object.version == 1

    custom_object = old_client.custom_objects.create_or_update(
        models.CustomObjectDraft(container="unittest", key="test-object-1", value=2345)
    )
    assert custom_object.key == "test-object-1"
    assert custom_object.value == 2345
    assert custom_object.version == 2

    # And another key
    custom_object = old_client.custom_objects.create_or_update(
        models.CustomObjectDraft(container="unittest", key="test-object-2", value=3456)
    )
    assert custom_object.key == "test-object-2"
    assert custom_object.value == 3456
    assert custom_object.version == 1


def test_custom_object_query_by_container(old_client):
    """Test filtering by container."""
    old_client.custom_objects.create_or_update(
        models.CustomObjectDraft(container="unittest", key="test-object-1", value=1234)
    )
    old_client.custom_objects.create_or_update(
        models.CustomObjectDraft(container="unittest", key="test-object-2", value=1234)
    )
    old_client.custom_objects.create_or_update(
        models.CustomObjectDraft(container="unittest2", key="test-object-1", value=1234)
    )

    result = old_client.custom_objects.query_by_container("unittest")
    assert len(result.results) == 2
    assert result.total == 2

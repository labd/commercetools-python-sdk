import pytest
from requests.exceptions import HTTPError

from commercetools.platform import models
from commercetools.platform.client import Client


def test_custom_object_get_by_container_and_key(ct_platform_client: Client):
    custom_object = (
        ct_platform_client.with_project_key("unittest")
        .custom_objects()
        .post(
            models.CustomObjectDraft(
                container="unittest", key="test-object", value=1234
            )
        )
    )

    assert custom_object
    assert custom_object.id
    assert custom_object.container == "unittest"
    assert custom_object.key == "test-object"
    assert custom_object.value == 1234

    custom_object = (
        ct_platform_client.with_project_key("unittest")
        .custom_objects()
        .with_container_and_key("unittest", "test-object")
        .get()
    )
    assert custom_object.container == "unittest"
    assert custom_object.key == "test-object"
    assert custom_object.value == 1234

    with pytest.raises(HTTPError):
        ct_platform_client.with_project_key(
            "unittest"
        ).custom_objects().with_container_and_key("invalid", "invalid").get()


def test_custom_object_query(ct_platform_client: Client):
    ct_platform_client.with_project_key("unittest").custom_objects().post(
        models.CustomObjectDraft(container="unittest", key="test-object-1", value=1234)
    )
    ct_platform_client.with_project_key("unittest").custom_objects().post(
        models.CustomObjectDraft(container="unittest", key="test-object-2", value=1234)
    )

    # single sort query
    result = (
        ct_platform_client.with_project_key("unittest")
        .custom_objects()
        .get(sort="id asc")
    )
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = (
        ct_platform_client.with_project_key("unittest")
        .custom_objects()
        .get(sort=["id asc", "name asc"])
    )
    assert len(result.results) == 2
    assert result.total == 2


def test_custom_object_update(ct_platform_client: Client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    """
    custom_object = (
        ct_platform_client.with_project_key("unittest")
        .custom_objects()
        .post(
            models.CustomObjectDraft(
                container="unittest", key="test-object-1", value=1234
            )
        )
    )
    assert custom_object.key == "test-object-1"
    assert custom_object.value == 1234
    assert custom_object.version == 1

    custom_object = (
        ct_platform_client.with_project_key("unittest")
        .custom_objects()
        .post(
            models.CustomObjectDraft(
                container="unittest", key="test-object-1", value=2345
            )
        )
    )
    assert custom_object.key == "test-object-1"
    assert custom_object.value == 2345
    assert custom_object.version == 2

    # And another key
    custom_object = (
        ct_platform_client.with_project_key("unittest")
        .custom_objects()
        .post(
            models.CustomObjectDraft(
                container="unittest", key="test-object-2", value=3456
            )
        )
    )
    assert custom_object.key == "test-object-2"
    assert custom_object.value == 3456
    assert custom_object.version == 1


def test_custom_object_query_by_container(ct_platform_client: Client):
    """Test filtering by container."""
    ct_platform_client.with_project_key("unittest").custom_objects().post(
        models.CustomObjectDraft(container="unittest", key="test-object-1", value=1234)
    )
    ct_platform_client.with_project_key("unittest").custom_objects().post(
        models.CustomObjectDraft(container="unittest", key="test-object-2", value=1234)
    )
    ct_platform_client.with_project_key("unittest").custom_objects().post(
        models.CustomObjectDraft(container="unittest2", key="test-object-1", value=1234)
    )

    result = (
        ct_platform_client.with_project_key("unittest")
        .custom_objects()
        .with_container("unittest")
        .get()
    )
    assert len(result.results) == 2
    assert result.total == 2


def test_delete_by_container_and_key(ct_platform_client: Client):
    custom_object = (
        ct_platform_client.with_project_key("unittest")
        .custom_objects()
        .post(
            models.CustomObjectDraft(
                container="unittest", key="test-object-1", value=1234
            )
        )
    )
    assert custom_object.id
    assert custom_object.key == "test-object-1"
    deleted_object = (
        ct_platform_client.with_project_key("unittest")
        .custom_objects()
        .with_container_and_key(
            container=custom_object.container, key=custom_object.key
        )
        .delete()
    )

    assert deleted_object.key == "test-object-1"

    with pytest.raises(HTTPError):
        ct_platform_client.with_project_key(
            "unittest"
        ).custom_objects().with_container_and_key(
            container=custom_object.container, key=custom_object.key
        ).delete()

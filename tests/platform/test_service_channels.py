import pytest
from requests.exceptions import HTTPError

from commercetools.platform import models
from commercetools.platform.client import Client


def test_channel_with_id_get(ct_platform_client: Client):
    channel = (
        ct_platform_client.with_project_key("unittest")
        .channels()
        .post(
            models.ChannelDraft(
                key="test-channel", roles=[models.ChannelRoleEnum.INVENTORY_SUPPLY]
            )
        )
    )

    assert channel.id
    assert channel.key == "test-channel"

    channel = (
        ct_platform_client.with_project_key("unittest")
        .channels()
        .with_id(channel.id)
        .get()
    )
    assert channel.id
    assert channel.key == "test-channel"

    with pytest.raises(HTTPError):
        ct_platform_client.with_project_key("unittest").channels().with_id(
            "invalid"
        ).get()


def test_channel_query(ct_platform_client: Client):
    ct_platform_client.with_project_key("unittest").channels().post(
        models.ChannelDraft(
            key="test-channel1", roles=[models.ChannelRoleEnum.INVENTORY_SUPPLY]
        )
    )
    ct_platform_client.with_project_key("unittest").channels().post(
        models.ChannelDraft(
            key="test-channel2", roles=[models.ChannelRoleEnum.INVENTORY_SUPPLY]
        )
    )

    # single sort query
    result = (
        ct_platform_client.with_project_key("unittest").channels().get(sort="id asc")
    )
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = (
        ct_platform_client.with_project_key("unittest")
        .channels()
        .get(sort=["id asc", "name asc"])
    )
    assert len(result.results) == 2
    assert result.total == 2


def test_channel_update(ct_platform_client: Client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    channel = (
        ct_platform_client.with_project_key("unittest")
        .channels()
        .post(
            models.ChannelDraft(
                key="test-channel",
                name=models.LocalizedString(nl="nl-channel"),
                roles=[models.ChannelRoleEnum.INVENTORY_SUPPLY],
            )
        )
    )
    assert channel.key == "test-channel"

    channel = (
        ct_platform_client.with_project_key("unittest")
        .channels()
        .with_id(channel.id)
        .post(
            models.ChannelUpdate(
                version=channel.version,
                actions=[
                    models.ChannelChangeNameAction(
                        name=models.LocalizedString(nl="nl-channel2")
                    )
                ],
            )
        )
    )

import pytest
from requests.exceptions import HTTPError

from commercetools.platform import models


def test_channel_get_by_id(client):
    channel = client.channels.create(
        models.ChannelDraft(
            key="test-channel", roles=[models.ChannelRoleEnum.INVENTORY_SUPPLY]
        )
    )

    assert channel.id
    assert channel.key == "test-channel"

    channel = client.channels.get_by_id(channel.id)
    assert channel.id
    assert channel.key == "test-channel"

    with pytest.raises(HTTPError):
        client.channels.get_by_id("invalid")


def test_channel_query(client):
    client.channels.create(
        models.ChannelDraft(
            key="test-channel1", roles=[models.ChannelRoleEnum.INVENTORY_SUPPLY]
        )
    )
    client.channels.create(
        models.ChannelDraft(
            key="test-channel2", roles=[models.ChannelRoleEnum.INVENTORY_SUPPLY]
        )
    )

    # single sort query
    result = client.channels.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = client.channels.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


def test_channel_update(client):
    """Test the return value of the update methods.

    It doesn't test the actual update itself.
    TODO: See if this is worth testing since we're using a mocking backend
    """
    channel = client.channels.create(
        models.ChannelDraft(
            key="test-channel",
            name=models.LocalizedString(nl="nl-channel"),
            roles=[models.ChannelRoleEnum.INVENTORY_SUPPLY],
        )
    )
    assert channel.key == "test-channel"

    channel = client.channels.update_by_id(
        id=channel.id,
        version=channel.version,
        actions=[
            models.ChannelChangeNameAction(name=models.LocalizedString(nl="nl-channel2"))
        ],
    )

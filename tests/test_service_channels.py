import pytest
from requests.exceptions import HTTPError

from commercetools import types


def test_channel_get_by_id(client):
    channel = client.channels.create(
        types.ChannelDraft(
            key="test-channel", roles=[types.ChannelRoleEnum.INVENTORY_SUPPLY]
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
        types.ChannelDraft(
            key="test-channel1", roles=[types.ChannelRoleEnum.INVENTORY_SUPPLY]
        )
    )
    client.channels.create(
        types.ChannelDraft(
            key="test-channel2", roles=[types.ChannelRoleEnum.INVENTORY_SUPPLY]
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
        types.ChannelDraft(
            key="test-channel",
            name=types.LocalizedString(nl="nl-channel"),
            roles=[types.ChannelRoleEnum.INVENTORY_SUPPLY],
        )
    )
    assert channel.key == "test-channel"

    channel = client.channels.update_by_id(
        id=channel.id,
        version=channel.version,
        actions=[
            types.ChannelChangeNameAction(name=types.LocalizedString(nl="nl-channel2"))
        ],
    )

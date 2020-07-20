import pytest

from commercetools import CommercetoolsError, types


def test_store_flow(client, store_draft):
    store = client.stores.create(store_draft)

    assert store.id

    deleted_store = client.stores.delete_by_id(store.id)

    assert store.id == deleted_store.id


@pytest.fixture
def store_draft():
    return types.StoreDraft(
        key="test store", name=types.LocalizedString({"en": "test store"})
    )


def test_update_actions(commercetools_api, client, store_draft):
    store = client.stores.create(store_draft)

    assert store.languages is None

    store = client.stores.update_by_id(
        store.id,
        store.version,
        actions=[types.StoreSetLanguagesAction(languages=["en-US"])],
    )

    assert store.languages == ["en-US"]


def test_channels_are_set(commercetools_api, client, store_draft):
    store = client.stores.create(store_draft)

    assert store.distribution_channels == []

    channel = client.channels.create(
        types.ChannelDraft(
            key="FOO", roles=[types.ChannelRoleEnum.PRODUCT_DISTRIBUTION]
        )
    )

    store = client.stores.update_by_id(
        store.id,
        store.version,
        actions=[
            types.StoresSetDistributionChannelsAction(
                distribution_channels=[types.ChannelResourceIdentifier(key="FOO")]
            )
        ],
    )

    assert store.distribution_channels[0].id == channel.id


def test_channel_errors(commercetools_api, client, store_draft):
    store = client.stores.create(store_draft)

    client.channels.create(
        types.ChannelDraft(key="BAR", roles=[types.ChannelRoleEnum.INVENTORY_SUPPLY])
    )

    with pytest.raises(CommercetoolsError):
        client.stores.update_by_id(
            store.id,
            store.version,
            actions=[
                types.StoresSetDistributionChannelsAction(
                    distribution_channels=[types.ChannelResourceIdentifier(key="BAR")]
                )
            ],
        )


def test_store_channel_create(commercetools_api, client, store_draft):
    channel = client.channels.create(
        types.ChannelDraft(
            key="FOO", roles=[types.ChannelRoleEnum.PRODUCT_DISTRIBUTION]
        )
    )
    store_draft.distribution_channels = [types.ChannelResourceIdentifier(key="FOO")]

    store = client.stores.create(store_draft)

    assert store.distribution_channels[0].id == channel.id

import pytest

from commercetools import CommercetoolsError
from commercetools.platform import models


def test_store_flow(old_client, store_draft):
    store = old_client.stores.create(store_draft)

    assert store.id

    deleted_store = old_client.stores.delete_by_id(store.id, version=store.version)

    assert store.id == deleted_store.id


@pytest.fixture
def store_draft():
    return models.StoreDraft(
        key="test store", name=models.LocalizedString({"en": "test store"})
    )


def test_update_actions(commercetools_api, old_client, store_draft):
    store = old_client.stores.create(store_draft)

    assert store.languages is None

    store = old_client.stores.update_by_id(
        store.id,
        store.version,
        actions=[models.StoreSetLanguagesAction(languages=["en-US"])],
    )

    assert store.languages == ["en-US"]


def test_channels_are_set(commercetools_api, old_client, store_draft):
    store = old_client.stores.create(store_draft)

    assert store.distribution_channels == []

    channel = old_client.channels.create(
        models.ChannelDraft(
            key="FOO", roles=[models.ChannelRoleEnum.PRODUCT_DISTRIBUTION]
        )
    )

    store = old_client.stores.update_by_id(
        store.id,
        store.version,
        actions=[
            models.StoresSetDistributionChannelsAction(
                distribution_channels=[models.ChannelResourceIdentifier(key="FOO")]
            )
        ],
    )

    assert store.distribution_channels[0].id == channel.id


def test_channel_errors(commercetools_api, old_client, store_draft):
    store = old_client.stores.create(store_draft)

    old_client.channels.create(
        models.ChannelDraft(key="BAR", roles=[models.ChannelRoleEnum.INVENTORY_SUPPLY])
    )

    with pytest.raises(CommercetoolsError):
        old_client.stores.update_by_id(
            store.id,
            store.version,
            actions=[
                models.StoresSetDistributionChannelsAction(
                    distribution_channels=[models.ChannelResourceIdentifier(key="BAR")]
                )
            ],
        )


def test_store_channel_create(commercetools_api, old_client, store_draft):
    channel = old_client.channels.create(
        models.ChannelDraft(
            key="FOO", roles=[models.ChannelRoleEnum.PRODUCT_DISTRIBUTION]
        )
    )
    store_draft.distribution_channels = [models.ChannelResourceIdentifier(key="FOO")]

    store = old_client.stores.create(store_draft)

    assert store.distribution_channels[0].id == channel.id

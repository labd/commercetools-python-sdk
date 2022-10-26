import pytest

from commercetools import CommercetoolsError
from commercetools.platform import models
from commercetools.platform.client import Client


def test_store_flow(ct_platform_client: Client, store_draft):
    store = ct_platform_client.with_project_key("foo").stores().post(store_draft)

    assert store.id

    deleted_store = (
        ct_platform_client.with_project_key("foo")
        .stores()
        .with_id(store.id)
        .delete(version=store.version)
    )

    assert store.id == deleted_store.id


@pytest.fixture
def store_draft():
    return models.StoreDraft(
        key="test store", name=models.LocalizedString({"en": "test store"})
    )


def test_update_actions(commercetools_api, ct_platform_client: Client, store_draft):
    store = ct_platform_client.with_project_key("foo").stores().post(store_draft)

    assert store.languages is None

    store = (
        ct_platform_client.with_project_key("foo")
        .stores()
        .with_id(
            store.id,
        )
        .post(
            models.StoreUpdate(
                version=store.version,
                actions=[models.StoreSetLanguagesAction(languages=["en-US"])],
            )
        )
    )

    assert store.languages == ["en-US"]


def test_channels_are_set(commercetools_api, ct_platform_client: Client, store_draft):
    store = ct_platform_client.with_project_key("foo").stores().post(store_draft)

    assert store.distribution_channels == []

    channel = (
        ct_platform_client.with_project_key("foo")
        .channels()
        .post(
            models.ChannelDraft(
                key="FOO", roles=[models.ChannelRoleEnum.PRODUCT_DISTRIBUTION]
            )
        )
    )

    store = (
        ct_platform_client.with_project_key("foo")
        .stores()
        .with_id(
            store.id,
        )
        .post(
            models.StoreUpdate(
                version=store.version,
                actions=[
                    models.StoreSetDistributionChannelsAction(
                        distribution_channels=[
                            models.ChannelResourceIdentifier(key="FOO")
                        ]
                    )
                ],
            )
        )
    )

    assert store.distribution_channels[0].id == channel.id


def test_channel_errors(commercetools_api, ct_platform_client: Client, store_draft):
    store = ct_platform_client.with_project_key("foo").stores().post(store_draft)

    ct_platform_client.with_project_key("foo").channels().post(
        models.ChannelDraft(key="BAR", roles=[models.ChannelRoleEnum.INVENTORY_SUPPLY])
    )

    with pytest.raises(CommercetoolsError):
        (
            ct_platform_client.with_project_key("foo")
            .stores()
            .with_id(store.id)
            .post(
                models.StoreUpdate(
                    version=store.version,
                    actions=[
                        models.StoreSetDistributionChannelsAction(
                            distribution_channels=[
                                models.ChannelResourceIdentifier(key="BAR")
                            ]
                        )
                    ],
                )
            )
        )


def test_store_channel_create(
    commercetools_api, ct_platform_client: Client, store_draft
):
    channel = (
        ct_platform_client.with_project_key("foo")
        .channels()
        .post(
            models.ChannelDraft(
                key="FOO", roles=[models.ChannelRoleEnum.PRODUCT_DISTRIBUTION]
            )
        )
    )
    store_draft.distribution_channels = [models.ChannelResourceIdentifier(key="FOO")]

    store = ct_platform_client.with_project_key("foo").stores().post(store_draft)

    assert store.distribution_channels[0].id == channel.id

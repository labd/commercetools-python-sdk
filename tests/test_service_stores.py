import pytest

from commercetools import types


def test_store_flow(client, store_draft):
    store = client.stores.create(store_draft)

    assert store.id

    deleted_store = client.stores.delete_by_id(store.id)

    assert store.id == deleted_store.id


@pytest.fixture
def store_draft():
    return types.StoreDraft(
        key="test store",
        name=types.LocalizedString({"en": "test store"})
    )

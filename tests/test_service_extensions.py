from commercetools import types


def test_extension_create(client):
    extension = client.extensions.create(types.ExtensionDraft())
    assert extension.id


def test_extension_get_by_id(client):
    extension = client.extensions.create(types.ExtensionDraft())
    assert extension.id

    extension = client.extensions.get_by_id(extension.id)
    assert extension.id

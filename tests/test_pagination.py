import pytest

from commercetools import paginators, types


def test_page_paginator(client):
    for i in range(100):
        client.products.create(
            types.ProductDraft(name=types.LocalizedString(en=f"Product {i}"))
        )

    paginator = paginators.Paginator(client.products.query, sort=["id asc", "name asc"])

    items = []
    for product in paginator:
        items.append(product)
    assert len(items) == 100


def test_page_paginator_slice_start(client):
    for i in range(100):
        client.products.create(
            types.ProductDraft(name=types.LocalizedString(en=f"Product {i}"))
        )

    paginator = paginators.Paginator(client.products.query, sort=["id asc", "name asc"])

    items = []
    for product in paginator[20:]:
        items.append(product)
        if len(items) > 80:
            assert False
    assert len(items) == 80


def test_page_paginator_slice_stop(client):
    for i in range(100):
        client.products.create(
            types.ProductDraft(name=types.LocalizedString(en=f"Product {i}"))
        )

    paginator = paginators.Paginator(client.products.query, sort=["id asc", "name asc"])

    items = []
    for product in paginator[:-20]:
        items.append(product)
        if len(items) > 80:
            assert False
    assert len(items) == 80


def test_page_paginator_slice_start_stop(client):
    for i in range(100):
        client.products.create(
            types.ProductDraft(name=types.LocalizedString(en=f"Product {i}"))
        )

    paginator = paginators.Paginator(client.products.query, sort=["id asc", "name asc"])

    items = []
    for product in paginator[20:-20]:
        items.append(product)
        if len(items) > 60:
            assert False
    assert len(items) == 60


def test_cursor_paginator(client):
    for i in range(100):
        client.products.create(
            types.ProductDraft(name=types.LocalizedString(en=f"Product {i}"))
        )

    paginator = paginators.CursorPaginator(
        client.products.query, sort=["id asc", "name asc"]
    )

    items = []
    for product in paginator:
        items.append(product)
    assert len(items) == 100


def test_cursor_paginator_slice_start(client):
    for i in range(100):
        client.products.create(
            types.ProductDraft(name=types.LocalizedString(en=f"Product {i}"))
        )

    paginator = paginators.CursorPaginator(
        client.products.query, sort=["id asc", "name asc"]
    )

    items = []
    with pytest.raises(ValueError):
        for product in paginator[10:]:
            items.append(product)


def test_cursor_paginator_slice_stop(client):
    for i in range(100):
        client.products.create(
            types.ProductDraft(name=types.LocalizedString(en=f"Product {i}"))
        )

    paginator = paginators.CursorPaginator(
        client.products.query, sort=["id asc", "name asc"]
    )

    items = []
    for product in paginator[:90]:
        items.append(product)

    assert len(items) == 90

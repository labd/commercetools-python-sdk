import pytest

from commercetools import paginators
from commercetools.platform import models


def create_products(old_client):
    for i in range(100):
        old_client.products.create(
            models.ProductDraft(
                key=f"test-product-{i}",
                product_type=models.ProductTypeResourceIdentifier(key="dummy"),
                name=models.LocalizedString(en=f"my-product-{i}"),
                slug=models.LocalizedString(en=f"my-product-{i}"),
            )
        )


def test_page_paginator(old_client):
    create_products(old_client)
    paginator = paginators.Paginator(old_client.products.query, sort=["id asc", "name asc"])

    items = []
    for product in paginator:
        items.append(product)
    assert len(items) == 100


def test_page_paginator_slice_start(old_client):
    create_products(old_client)
    paginator = paginators.Paginator(old_client.products.query, sort=["id asc", "name asc"])

    items = []
    for product in paginator[20:]:
        items.append(product)
        if len(items) > 80:
            assert False
    assert len(items) == 80


def test_page_paginator_slice_stop(old_client):
    create_products(old_client)
    paginator = paginators.Paginator(old_client.products.query, sort=["id asc", "name asc"])

    items = []
    for product in paginator[:-20]:
        items.append(product)
        if len(items) > 80:
            assert False
    assert len(items) == 80


def test_page_paginator_slice_start_stop(old_client):
    create_products(old_client)
    paginator = paginators.Paginator(old_client.products.query, sort=["id asc", "name asc"])

    items = []
    for product in paginator[20:-20]:
        items.append(product)
        if len(items) > 60:
            assert False
    assert len(items) == 60


def test_cursor_paginator(old_client):
    create_products(old_client)
    paginator = paginators.CursorPaginator(
        old_client.products.query, sort=["id asc", "name asc"]
    )

    items = []
    for product in paginator:
        items.append(product)
    assert len(items) == 100


def test_cursor_paginator_slice_start(old_client):
    create_products(old_client)
    paginator = paginators.CursorPaginator(
        old_client.products.query, sort=["id asc", "name asc"]
    )

    items = []
    with pytest.raises(ValueError):
        for product in paginator[10:]:
            items.append(product)


def test_cursor_paginator_slice_stop(old_client):
    create_products(old_client)
    paginator = paginators.CursorPaginator(
        old_client.products.query, sort=["id asc", "name asc"]
    )

    items = []
    for product in paginator[:90]:
        items.append(product)

    assert len(items) == 90

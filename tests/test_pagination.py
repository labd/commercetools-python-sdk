import pytest

from commercetools import paginators
from commercetools.contrib.pytest import ct_platform_client
from commercetools.platform import models
from commercetools.platform.client import Client
from commercetools.platform.client.by_project_key_request_builder import (
    ByProjectKeyRequestBuilder,
)


def create_products(client: ByProjectKeyRequestBuilder):
    for i in range(100):
        client.products().post(
            models.ProductDraft(
                key=f"test-product-{i}",
                product_type=models.ProductTypeResourceIdentifier(key="dummy"),
                name=models.LocalizedString(en=f"my-product-{i}"),
                slug=models.LocalizedString(en=f"my-product-{i}"),
            )
        )


def test_page_paginator(ct_platform_client: Client):
    client = ct_platform_client.with_project_key("unittest")
    create_products(client)

    paginator = paginators.Paginator(client.products().get, sort=["id asc", "name asc"])

    items = []
    for product in paginator:
        items.append(product)
    assert len(items) == 100


def test_page_paginator_slice_start(ct_platform_client: Client):
    client = ct_platform_client.with_project_key("unittest")
    create_products(client)

    paginator = paginators.Paginator(client.products().get, sort=["id asc", "name asc"])

    items = []
    for product in paginator[20:]:
        items.append(product)
        if len(items) > 80:
            assert False
    assert len(items) == 80


def test_page_paginator_slice_stop(ct_platform_client: Client):
    client = ct_platform_client.with_project_key("unittest")
    create_products(client)

    paginator = paginators.Paginator(client.products().get, sort=["id asc", "name asc"])

    items = []
    for product in paginator[:-20]:
        items.append(product)
        if len(items) > 80:
            assert False
    assert len(items) == 80


def test_page_paginator_slice_start_stop(ct_platform_client: Client):
    client = ct_platform_client.with_project_key("unittest")
    create_products(client)

    paginator = paginators.Paginator(client.products().get, sort=["id asc", "name asc"])

    items = []
    for product in paginator[20:-20]:
        items.append(product)
        if len(items) > 60:
            assert False
    assert len(items) == 60


def test_cursor_paginator(ct_platform_client: Client):
    client = ct_platform_client.with_project_key("unittest")
    create_products(client)

    paginator = paginators.CursorPaginator(
        client.products().get, sort=["id asc", "name asc"]
    )

    items = []
    for product in paginator:
        items.append(product)
    assert len(items) == 100


def test_cursor_paginator_slice_start(ct_platform_client: Client):
    client = ct_platform_client.with_project_key("unittest")
    create_products(client)

    paginator = paginators.CursorPaginator(
        client.products().get, sort=["id asc", "name asc"]
    )

    items = []
    with pytest.raises(ValueError):
        for product in paginator[10:]:
            items.append(product)


def test_cursor_paginator_slice_stop(ct_platform_client: Client):
    client = ct_platform_client.with_project_key("unittest")
    create_products(client)

    paginator = paginators.CursorPaginator(
        client.products().get, sort=["id asc", "name asc"]
    )

    items = []
    for product in paginator[:90]:
        items.append(product)

    assert len(items) == 90

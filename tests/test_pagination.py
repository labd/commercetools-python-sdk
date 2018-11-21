from commercetools import paginators, types


def test_page_paginator(client):
    for i in range(100):
        client.products.create(
            types.ProductDraft(name=types.LocalizedString(en=f"Product {i}"))
        )

    paginator = paginators.Paginator(page_size=20)
    products = paginator.paginate(client.products.query, sort=["id asc", "name asc"])

    items = []
    for product in products:
        items.append(product)
    assert len(items) == 100

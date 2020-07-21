import os

import requests

from commercetools import Client
from commercetools.types import (
    ChannelDraft,
    ChannelResourceIdentifier,
    ChannelRoleEnum,
    LocalizedString,
    ProductDraft,
    StoreDraft,
)


def test_http_server(commercetools_client, commercetools_http_server):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    client = Client(
        project_key="unittest",
        client_id="client-id",
        client_secret="client-secret",
        scope=[],
        url=commercetools_http_server.api_url,
        token_url=f"{commercetools_http_server.api_url}/oauth/token",
    )

    query_result = client.products.query()
    assert query_result.count == 0
    product = client.products.create(ProductDraft(name=LocalizedString(nl="Testje")))

    client.products.get_by_id(product.id)
    url = commercetools_http_server.api_url + f"/unittest/products/{product.id}"
    response = requests.get(url, headers={"Authorization": "Bearer token"})

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["masterData"]["staged"]["name"]["nl"] == "Testje"


def test_http_server_expanding(commercetools_client, commercetools_http_server):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    client = Client(
        project_key="unittest",
        client_id="client-id",
        client_secret="client-secret",
        scope=[],
        url=commercetools_http_server.api_url,
        token_url=f"{commercetools_http_server.api_url}/oauth/token",
    )

    client.channels.create(
        ChannelDraft(key="FOO", roles=[ChannelRoleEnum.PRODUCT_DISTRIBUTION])
    )

    store = client.stores.create(
        StoreDraft(
            key="FOO", distribution_channels=[ChannelResourceIdentifier(key="FOO")]
        )
    )

    url = commercetools_http_server.api_url + f"/unittest/stores/{store.id}"
    response = requests.get(
        url,
        params={"expand": "distributionChannels[*]"},
        headers={"Authorization": "Bearer token"},
    )

    assert response.status_code == 200, response.text
    data = response.json()

    assert data["distributionChannels"][0]["obj"]["key"] == "FOO"

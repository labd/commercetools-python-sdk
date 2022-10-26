import os

import requests

from commercetools.platform import models
from commercetools.platform.client import Client
from commercetools.platform.models import (
    ChannelDraft,
    ChannelResourceIdentifier,
    ChannelRoleEnum,
    ProductDraft,
    ProductTypeResourceIdentifier,
    StoreDraft,
)


def test_http_server(ct_platform_client, commercetools_http_server):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    client = Client(
        client_id="client-id",
        client_secret="client-secret",
        scope=[],
        url=commercetools_http_server.api_url,
        token_url=f"{commercetools_http_server.api_url}/oauth/token",
    )

    query_result = ct_platform_client.with_project_key("unittest").products().get()
    assert query_result.count == 0
    product = (
        client.with_project_key("unittest")
        .products()
        .post(
            ProductDraft(
                key="test-product",
                product_type=ProductTypeResourceIdentifier(key="dummy"),
                name={"nl": "Testje"},
                slug={"en": "foo-bar"},
            )
        )
    )

    client.with_project_key("unittes").products().with_id(product.id).get()
    url = commercetools_http_server.api_url + f"/unittest/products/{product.id}"
    response = requests.get(url, headers={"Authorization": "Bearer token"})

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["masterData"]["staged"]["name"]["nl"] == "Testje"


def test_http_server_expanding(ct_platform_client: Client, commercetools_http_server):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    client = Client(
        client_id="client-id",
        client_secret="client-secret",
        scope=[],
        url=commercetools_http_server.api_url,
        token_url=f"{commercetools_http_server.api_url}/oauth/token",
    )

    client.with_project_key("unittest").channels().post(
        ChannelDraft(key="FOO", roles=[ChannelRoleEnum.PRODUCT_DISTRIBUTION])
    )

    store = (
        client.with_project_key("unittest")
        .stores()
        .post(
            StoreDraft(
                name=models.LocalizedString(nl="foo"),
                key="FOO",
                distribution_channels=[ChannelResourceIdentifier(key="FOO")],
            )
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

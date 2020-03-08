import pytest
import requests

from commercetools import Client
from commercetools.types import LocalizedString, ProductDraft


def test_http_server(commercetools_client, commercetools_http_server):
    import os

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

import requests

from commercetools.types import LocalizedString, ProductDraft


def test_http_server(commercetools_client, commercetools_http_server):
    product = commercetools_client.products.create(
        ProductDraft(name=LocalizedString(nl="Testje"))
    )

    commercetools_client.products.get_by_id(product.id)
    url = commercetools_http_server.api_url + f"/unittest/products/{product.id}"
    response = requests.get(url, headers={"Authorization": "Bearer token"})

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["masterData"]["staged"]["name"]["nl"] == "Testje"

# Generated file, please do not change!!!
import typing

from ...models.product_discount import ProductDiscount, ProductDiscountMatchQuery


class ByProjectKeyProductDiscountsMatchingRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def post(
        self,
        body: "ProductDiscountMatchQuery",
        *,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductDiscount":
        return self._client._post(
            endpoint=f"/{self._project_key}/product-discounts/matching",
            params={},
            data_object=body,
            response_class=ProductDiscount,
            headers={"Content-Type": "application/json", **headers},
        )

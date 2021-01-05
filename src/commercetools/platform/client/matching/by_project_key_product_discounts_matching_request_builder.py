# Generated file, please do not change!!!
import typing

from ...models.product_discount import ProductDiscount, ProductDiscountMatchQuery

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductDiscountsMatchingRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def post(
        self,
        body: "ProductDiscountMatchQuery",
        *,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductDiscount":
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/product-discounts/matching",
            params={},
            data_object=body,
            response_class=ProductDiscount,
            headers={"Content-Type": "application/json", **headers},
        )

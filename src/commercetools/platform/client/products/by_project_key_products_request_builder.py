# Generated file, please do not change!!!
import typing

from ...models.error import ErrorResponse
from ...models.product import Product, ProductDraft, ProductPagedQueryResponse
from .by_project_key_products_by_id_request_builder import (
    ByProjectKeyProductsByIDRequestBuilder,
)
from .by_project_key_products_key_by_key_request_builder import (
    ByProjectKeyProductsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeyProductsKeyByKeyRequestBuilder:
        return ByProjectKeyProductsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyProductsByIDRequestBuilder:
        return ByProjectKeyProductsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: str = None,
        price_channel: str = None,
        locale_projection: str = None,
        store_projection: str = None,
        expand: typing.List["str"] = None,
        sort: typing.List["str"] = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: typing.List["str"] = None,
        predicate_var: typing.Dict[str, typing.List["str"]] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["ProductPagedQueryResponse"]:
        """You can use the query endpoint to get the full representations of products.
        REMARK: We suggest to use the performance optimized search endpoint which has a bunch functionalities,
        the query API lacks like sorting on custom attributes, etc.

        """
        params = {
            "priceCurrency": price_currency,
            "priceCountry": price_country,
            "priceCustomerGroup": price_customer_group,
            "priceChannel": price_channel,
            "localeProjection": locale_projection,
            "storeProjection": store_projection,
            "expand": expand,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "where": where,
        }
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/products",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ProductPagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)

    def post(
        self,
        body: "ProductDraft",
        *,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: str = None,
        price_channel: str = None,
        locale_projection: str = None,
        store_projection: str = None,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Product"]:
        """To create a new product, send a representation that is going to become the initial staged representation
        of the new product in the master catalog. If price selection query parameters are provided,
        the selected prices will be added to the response.

        """
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/products",
            params={
                "priceCurrency": price_currency,
                "priceCountry": price_country,
                "priceCustomerGroup": price_customer_group,
                "priceChannel": price_channel,
                "localeProjection": locale_projection,
                "storeProjection": store_projection,
                "expand": expand,
            },
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 201:
            return Product.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        elif response.status_code == 200:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)

# Generated file, please do not change!!!
import typing

from ...models.product import Product, ProductDraft, ProductPagedQueryResponse
from .by_project_key_products_by_id_request_builder import (
    ByProjectKeyProductsByIDRequestBuilder,
)
from .by_project_key_products_key_by_key_request_builder import (
    ByProjectKeyProductsKeyByKeyRequestBuilder,
)


class ByProjectKeyProductsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyProductsKeyByKeyRequestBuilder:
        return ByProjectKeyProductsKeyByKeyRequestBuilder(
            key=key,
            projectKey=self._project_key,
            client=self._client,
        )

    def withId(self, ID: str) -> ByProjectKeyProductsByIDRequestBuilder:
        return ByProjectKeyProductsByIDRequestBuilder(
            ID=ID,
            projectKey=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        price_currency: "str" = None,
        price_country: "str" = None,
        price_customer_group: "str" = None,
        price_channel: "str" = None,
        locale_projection: "str" = None,
        store_projection: "str" = None,
        expand: "str" = None,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        where: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductPagedQueryResponse":
        """You can use the query endpoint to get the full representations of products.
        REMARK: We suggest to use the performance optimized search endpoint which has a bunch functionalities,
        the query API lacks like sorting on custom attributes, etc.

        """
        return self._client._get(
            endpoint=f"/{self._project_key}/products",
            params={
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
            },
            response_class=ProductPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ProductDraft",
        *,
        price_currency: "str" = None,
        price_country: "str" = None,
        price_customer_group: "str" = None,
        price_channel: "str" = None,
        locale_projection: "str" = None,
        store_projection: "str" = None,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Product":
        """To create a new product, send a representation that is going to become the initial staged representation
        of the new product in the master catalog. If price selection query parameters are provided,
        the selected prices will be added to the response.

        """
        return self._client._post(
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
            data_object=body,
            response_class=Product,
            headers={"Content-Type": "application/json", **headers},
        )

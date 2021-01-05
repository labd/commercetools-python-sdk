# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.product import Product

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductsKeyByKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _key: str

    def __init__(
        self,
        project_key: str,
        key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._key = key
        self._client = client

    def get(
        self,
        *,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: str = None,
        price_channel: str = None,
        locale_projection: str = None,
        store_projection: str = None,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Product":
        """Gets the full representation of a product by Key."""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/products/key={self._key}",
            params={
                "priceCurrency": price_currency,
                "priceCountry": price_country,
                "priceCustomerGroup": price_customer_group,
                "priceChannel": price_channel,
                "localeProjection": locale_projection,
                "storeProjection": store_projection,
                "expand": expand,
            },
            response_class=Product,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: str = None,
        price_channel: str = None,
        locale_projection: str = None,
        store_projection: str = None,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Product":
        """Update Product by key"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/products/key={self._key}",
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

    def delete(
        self,
        *,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: str = None,
        price_channel: str = None,
        locale_projection: str = None,
        store_projection: str = None,
        version: int,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Product":
        """Delete Product by key"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/products/key={self._key}",
            params={
                "priceCurrency": price_currency,
                "priceCountry": price_country,
                "priceCustomerGroup": price_customer_group,
                "priceChannel": price_channel,
                "localeProjection": locale_projection,
                "storeProjection": store_projection,
                "version": version,
                "expand": expand,
            },
            response_class=Product,
            headers=headers,
        )

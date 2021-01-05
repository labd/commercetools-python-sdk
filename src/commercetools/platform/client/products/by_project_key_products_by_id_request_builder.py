# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.product import Product
from ..images.by_project_key_products_by_id_images_request_builder import (
    ByProjectKeyProductsByIDImagesRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductsByIDRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _id: str

    def __init__(
        self,
        project_key: str,
        id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._id = id
        self._client = client

    def images(self) -> ByProjectKeyProductsByIDImagesRequestBuilder:
        return ByProjectKeyProductsByIDImagesRequestBuilder(
            project_key=self._project_key,
            id=self._id,
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
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Product":
        """Gets the full representation of a product by ID."""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/products/{self._id}",
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
        """Update Product by ID"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/products/{self._id}",
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
        """Delete Product by ID"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/products/{self._id}",
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

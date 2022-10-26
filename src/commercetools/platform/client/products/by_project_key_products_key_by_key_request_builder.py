# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.error import ErrorResponse
from ...models.product import Product, ProductUpdate
from ..product_selections.by_project_key_products_key_by_key_product_selections_request_builder import (
    ByProjectKeyProductsKeyByKeyProductSelectionsRequestBuilder,
)

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

    def product_selections(
        self,
    ) -> ByProjectKeyProductsKeyByKeyProductSelectionsRequestBuilder:
        return ByProjectKeyProductsKeyByKeyProductSelectionsRequestBuilder(
            project_key=self._project_key,
            key=self._key,
            client=self._client,
        )

    def get(
        self,
        *,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: str = None,
        price_channel: str = None,
        locale_projection: typing.List["str"] = None,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Product"]:
        """If [Price selection](ctp:api:type:ProductPriceSelection) query parameters are provided, the selected Prices are added to the response."""
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/products/key={self._key}",
            params={
                "priceCurrency": price_currency,
                "priceCountry": price_country,
                "priceCustomerGroup": price_customer_group,
                "priceChannel": price_channel,
                "localeProjection": locale_projection,
                "expand": expand,
            },
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Product.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

    def head(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional[None]:
        """Checks if a Product exists for a given `key`. Returns a `200 OK` status if the Product exists or a `404 Not Found` otherwise."""
        headers = {} if headers is None else headers
        response = self._client._head(
            endpoint=f"/{self._project_key}/products/key={self._key}",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return None
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

    def post(
        self,
        body: "ProductUpdate",
        *,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: str = None,
        price_channel: str = None,
        locale_projection: typing.List["str"] = None,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Product"]:
        """A failed response can return a [DuplicatePriceScope](ctp:api:type:DuplicatePriceScopeError), [DuplicateVariantValues](ctp:api:type:DuplicateVariantValuesError), [DuplicateAttributeValue](ctp:api:type:DuplicateAttributeValueError), or [DuplicateAttributeValues](ctp:api:type:DuplicateAttributeValuesError) error."""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/products/key={self._key}",
            params={
                "priceCurrency": price_currency,
                "priceCountry": price_country,
                "priceCustomerGroup": price_customer_group,
                "priceChannel": price_channel,
                "localeProjection": locale_projection,
                "expand": expand,
            },
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 200:
            return Product.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

    def delete(
        self,
        *,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: str = None,
        price_channel: str = None,
        locale_projection: typing.List["str"] = None,
        version: int,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Product"]:
        """If [Price selection](ctp:api:type:ProductPriceSelection) query parameters are provided, the selected Prices are added to the response.
        Produces the [ProductDeleted](/projects/messages#product-deleted) Message.
        """
        headers = {} if headers is None else headers
        response = self._client._delete(
            endpoint=f"/{self._project_key}/products/key={self._key}",
            params={
                "priceCurrency": price_currency,
                "priceCountry": price_country,
                "priceCustomerGroup": price_customer_group,
                "priceChannel": price_channel,
                "localeProjection": locale_projection,
                "version": version,
                "expand": expand,
            },
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Product.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

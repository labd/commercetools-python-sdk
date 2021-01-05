# Generated file, please do not change!!!
import typing

from ...models.product import ProductProjection


class ByProjectKeyProductProjectionsKeyByKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _key: str

    def __init__(
        self,
        projectKey: str,
        key: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._key = key
        self._client = client

    def get(
        self,
        *,
        staged: "bool" = None,
        price_currency: "str" = None,
        price_country: "str" = None,
        price_customer_group: "str" = None,
        price_channel: "str" = None,
        locale_projection: "str" = None,
        store_projection: "str" = None,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductProjection":
        """Gets the current or staged representation of a product found by Key.
        When used with an API client that has the view_published_products:{projectKey} scope,
        this endpoint only returns published (current) product projections.

        """
        return self._client._get(
            endpoint=f"/{self._project_key}/product-projections/key={self._key}",
            params={
                "staged": staged,
                "priceCurrency": price_currency,
                "priceCountry": price_country,
                "priceCustomerGroup": price_customer_group,
                "priceChannel": price_channel,
                "localeProjection": locale_projection,
                "storeProjection": store_projection,
                "expand": expand,
            },
            response_class=ProductProjection,
            headers=headers,
        )

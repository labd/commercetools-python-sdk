# Generated file, please do not change!!!
import typing

from ...models.product import ProductProjectionPagedSearchResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductProjectionsSearchRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def post(self, *, headers: typing.Dict[str, str] = None) -> None:
        """Search Product Projection"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/product-projections/search",
            params={},
            response_class=None,
            headers=headers,
        )

    def get(
        self,
        *,
        fuzzy: bool = None,
        fuzzy_level: float = None,
        mark_matching_variants: bool,
        staged: bool = None,
        filter: str = None,
        filter_facets: str = None,
        filter_query: str = None,
        facet: str = None,
        text: typing.Dict[str, str] = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: str = None,
        price_channel: str = None,
        locale_projection: str = None,
        store_projection: str = None,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductProjectionPagedSearchResponse":
        """Search Product Projection"""
        params = {
            "fuzzy": fuzzy,
            "fuzzyLevel": fuzzy_level,
            "markMatchingVariants": mark_matching_variants,
            "staged": staged,
            "filter": filter,
            "filter.facets": filter_facets,
            "filter.query": filter_query,
            "facet": facet,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "priceCurrency": price_currency,
            "priceCountry": price_country,
            "priceCustomerGroup": price_customer_group,
            "priceChannel": price_channel,
            "localeProjection": locale_projection,
            "storeProjection": store_projection,
            "expand": expand,
        }
        text and params.update({f"text.{k}": v for k, v in text.items()})
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/product-projections/search",
            params=params,
            response_class=ProductProjectionPagedSearchResponse,
            headers=headers,
        )

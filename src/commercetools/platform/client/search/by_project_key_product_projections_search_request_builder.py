# Generated file, please do not change!!!
import typing

from ...models.product import ProductProjectionPagedSearchResponse


class ByProjectKeyProductProjectionsSearchRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def post(self, *, headers: typing.Dict[str, str] = None) -> None:
        """Search Product Projection"""
        return self._client._post(
            endpoint=f"/{self._project_key}/product-projections/search",
            params={},
            response_class=None,
            headers=headers,
        )

    def get(
        self,
        *,
        fuzzy: "bool" = None,
        fuzzy_level: "float" = None,
        mark_matching_variants: "bool",
        staged: "bool" = None,
        filter: "str" = None,
        filter_facets: "str" = None,
        filter_query: "str" = None,
        facet: "str" = None,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        price_currency: "str" = None,
        price_country: "str" = None,
        price_customer_group: "str" = None,
        price_channel: "str" = None,
        locale_projection: "str" = None,
        store_projection: "str" = None,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductProjectionPagedSearchResponse":
        """Search Product Projection"""
        return self._client._get(
            endpoint=f"/{self._project_key}/product-projections/search",
            params={
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
            },
            response_class=ProductProjectionPagedSearchResponse,
            headers=headers,
        )

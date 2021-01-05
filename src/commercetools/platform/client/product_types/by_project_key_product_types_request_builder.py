# Generated file, please do not change!!!
import typing

from ...models.product_type import (
    ProductType,
    ProductTypeDraft,
    ProductTypePagedQueryResponse,
)
from .by_project_key_product_types_by_id_request_builder import (
    ByProjectKeyProductTypesByIDRequestBuilder,
)
from .by_project_key_product_types_key_by_key_request_builder import (
    ByProjectKeyProductTypesKeyByKeyRequestBuilder,
)


class ByProjectKeyProductTypesRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyProductTypesKeyByKeyRequestBuilder:
        return ByProjectKeyProductTypesKeyByKeyRequestBuilder(
            key=key,
            projectKey=self._project_key,
            client=self._client,
        )

    def withId(self, ID: str) -> ByProjectKeyProductTypesByIDRequestBuilder:
        return ByProjectKeyProductTypesByIDRequestBuilder(
            ID=ID,
            projectKey=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: "str" = None,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        where: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductTypePagedQueryResponse":
        """Query product-types"""
        return self._client._get(
            endpoint=f"/{self._project_key}/product-types",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=ProductTypePagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ProductTypeDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductType":
        """Create ProductType"""
        return self._client._post(
            endpoint=f"/{self._project_key}/product-types",
            params={"expand": expand},
            data_object=body,
            response_class=ProductType,
            headers={"Content-Type": "application/json", **headers},
        )

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

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductTypesRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeyProductTypesKeyByKeyRequestBuilder:
        return ByProjectKeyProductTypesKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyProductTypesByIDRequestBuilder:
        return ByProjectKeyProductTypesByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: str = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: str = None,
        predicate_var: typing.Dict[str, str] = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductTypePagedQueryResponse":
        """Query product-types"""
        params = {
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
        return self._client._get(
            endpoint=f"/{self._project_key}/product-types",
            params=params,
            response_class=ProductTypePagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ProductTypeDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ProductType":
        """Create ProductType"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/product-types",
            params={"expand": expand},
            data_object=body,
            response_class=ProductType,
            headers={"Content-Type": "application/json", **headers},
        )

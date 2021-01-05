# Generated file, please do not change!!!
import typing

from ...models.discount_code import (
    DiscountCode,
    DiscountCodeDraft,
    DiscountCodePagedQueryResponse,
)
from .by_project_key_discount_codes_by_id_request_builder import (
    ByProjectKeyDiscountCodesByIDRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyDiscountCodesRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_id(self, id: str) -> ByProjectKeyDiscountCodesByIDRequestBuilder:
        return ByProjectKeyDiscountCodesByIDRequestBuilder(
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
    ) -> "DiscountCodePagedQueryResponse":
        """Query discount-codes"""
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
            endpoint=f"/{self._project_key}/discount-codes",
            params=params,
            response_class=DiscountCodePagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "DiscountCodeDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "DiscountCode":
        """Create DiscountCode"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/discount-codes",
            params={"expand": expand},
            data_object=body,
            response_class=DiscountCode,
            headers={"Content-Type": "application/json", **headers},
        )

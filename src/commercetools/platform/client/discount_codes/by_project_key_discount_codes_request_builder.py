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


class ByProjectKeyDiscountCodesRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withId(self, ID: str) -> ByProjectKeyDiscountCodesByIDRequestBuilder:
        return ByProjectKeyDiscountCodesByIDRequestBuilder(
            ID=ID, projectKey=self._project_key, client=self._client
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
    ) -> "DiscountCodePagedQueryResponse":
        """Query discount-codes
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/discount-codes",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=DiscountCodePagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "DiscountCodeDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "DiscountCode":
        """Create DiscountCode
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/discount-codes",
            params={"expand": expand},
            data_object=body,
            response_object=DiscountCode,
            headers={"Content-Type": "application/json", **headers},
        )

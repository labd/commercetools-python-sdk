# Generated file, please do not change!!!
import typing

from ...models.customer_group import (
    CustomerGroup,
    CustomerGroupDraft,
    CustomerGroupPagedQueryResponse,
)
from .by_project_key_customer_groups_by_id_request_builder import (
    ByProjectKeyCustomerGroupsByIDRequestBuilder,
)
from .by_project_key_customer_groups_key_by_key_request_builder import (
    ByProjectKeyCustomerGroupsKeyByKeyRequestBuilder,
)


class ByProjectKeyCustomerGroupsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyCustomerGroupsKeyByKeyRequestBuilder:
        return ByProjectKeyCustomerGroupsKeyByKeyRequestBuilder(
            key=key, projectKey=self._project_key, client=self._client
        )

    def withId(self, ID: str) -> ByProjectKeyCustomerGroupsByIDRequestBuilder:
        return ByProjectKeyCustomerGroupsByIDRequestBuilder(
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
    ) -> "CustomerGroupPagedQueryResponse":
        """Query customer-groups
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/customer-groups",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=CustomerGroupPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "CustomerGroupDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CustomerGroup":
        """Create CustomerGroup
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/customer-groups",
            params={"expand": expand},
            data_object=body,
            response_object=CustomerGroup,
            headers={"Content-Type": "application/json", **headers},
        )

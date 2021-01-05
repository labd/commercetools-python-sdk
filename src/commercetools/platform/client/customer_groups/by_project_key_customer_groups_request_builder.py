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

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCustomerGroupsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeyCustomerGroupsKeyByKeyRequestBuilder:
        return ByProjectKeyCustomerGroupsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyCustomerGroupsByIDRequestBuilder:
        return ByProjectKeyCustomerGroupsByIDRequestBuilder(
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
    ) -> "CustomerGroupPagedQueryResponse":
        """Query customer-groups"""
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
            endpoint=f"/{self._project_key}/customer-groups",
            params=params,
            response_class=CustomerGroupPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "CustomerGroupDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CustomerGroup":
        """Create CustomerGroup"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/customer-groups",
            params={"expand": expand},
            data_object=body,
            response_class=CustomerGroup,
            headers={"Content-Type": "application/json", **headers},
        )

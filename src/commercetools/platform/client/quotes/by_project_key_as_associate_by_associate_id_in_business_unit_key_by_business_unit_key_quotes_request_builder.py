# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.error import ErrorResponse
from ...models.quote import QuotePagedQueryResponse
from .by_project_key_as_associate_by_associate_id_in_business_unit_key_by_business_unit_key_quotes_by_id_request_builder import (
    ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuotesByIDRequestBuilder,
)
from .by_project_key_as_associate_by_associate_id_in_business_unit_key_by_business_unit_key_quotes_key_by_key_request_builder import (
    ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuotesKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuotesRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _associate_id: str
    _business_unit_key: str

    def __init__(
        self,
        project_key: str,
        associate_id: str,
        business_unit_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._associate_id = associate_id
        self._business_unit_key = business_unit_key
        self._client = client

    def with_key(
        self, key: str
    ) -> ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuotesKeyByKeyRequestBuilder:
        return ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuotesKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            associate_id=self._associate_id,
            business_unit_key=self._business_unit_key,
            client=self._client,
        )

    def with_id(
        self, id: str
    ) -> ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuotesByIDRequestBuilder:
        return ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuotesByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            associate_id=self._associate_id,
            business_unit_key=self._business_unit_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        sort: typing.List["str"] = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: typing.List["str"] = None,
        predicate_var: typing.Dict[str, typing.List["str"]] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["QuotePagedQueryResponse"]:
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
        response = self._client._get(
            endpoint=f"/{self._project_key}/as-associate/{self._associate_id}/in-business-unit/key={self._business_unit_key}/quotes",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return QuotePagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def head(
        self,
        *,
        where: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional[None]:
        """Checks if a Quote exists for a given Query Predicate. Returns a `200 OK` status if any Quotes match the Query Predicate or a `404 Not Found` otherwise."""
        headers = {} if headers is None else headers
        response = self._client._head(
            endpoint=f"/{self._project_key}/as-associate/{self._associate_id}/in-business-unit/key={self._business_unit_key}/quotes",
            params={"where": where},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return None
        elif response.status_code == 404:
            return None
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

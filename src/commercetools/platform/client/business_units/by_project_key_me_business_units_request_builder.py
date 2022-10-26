# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.business_unit import BusinessUnit, BusinessUnitPagedQueryResponse
from ...models.error import ErrorResponse
from ...models.me import MyBusinessUnitDraft
from .by_project_key_me_business_units_by_id_request_builder import (
    ByProjectKeyMeBusinessUnitsByIDRequestBuilder,
)
from .by_project_key_me_business_units_key_by_key_request_builder import (
    ByProjectKeyMeBusinessUnitsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyMeBusinessUnitsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_id(self, id: str) -> ByProjectKeyMeBusinessUnitsByIDRequestBuilder:
        return ByProjectKeyMeBusinessUnitsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def with_key(self, key: str) -> ByProjectKeyMeBusinessUnitsKeyByKeyRequestBuilder:
        return ByProjectKeyMeBusinessUnitsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
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
    ) -> typing.Optional["BusinessUnitPagedQueryResponse"]:
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
            endpoint=f"/{self._project_key}/me/business-units",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return BusinessUnitPagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

    def head(
        self,
        *,
        where: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional[None]:
        """Checks if a BusinessUnit exists for a given Query Predicate. Returns a `200 OK` status if any BusinessUnits match the Query Predicate or a `404 Not Found` otherwise."""
        headers = {} if headers is None else headers
        response = self._client._head(
            endpoint=f"/{self._project_key}/me/business-units",
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

    def post(
        self,
        body: "MyBusinessUnitDraft",
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["BusinessUnit"]:
        """Automatically assigns the Associate to the Business Unit in the default [Associate Role](ctp:api:type:AssociateRole) defined in [BusinessUnitConfiguration](ctp:api:type:BusinessUnitConfiguration). If there is no default Associate Role configured, this request fails with an [InvalidOperation](ctp:api:type:InvalidOperationError) error. When creating a Division, the Associate must have the `AddChildUnits` [Permission](ctp:api:type:Permission) in the parent unit. If the required [Permission](/projects/associate-roles#permission) is missing, an [AssociateMissingPermission](/errors#associatemissingpermission) error is returned."""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/me/business-units",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code in (201, 200):
            return BusinessUnit.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

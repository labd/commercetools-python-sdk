# Generated file, please do not change!!!
import typing

from ...models.custom_object import (
    CustomObject,
    CustomObjectDraft,
    CustomObjectPagedQueryResponse,
)
from ...models.error import ErrorResponse
from .by_project_key_custom_objects_by_container_by_key_request_builder import (
    ByProjectKeyCustomObjectsByContainerByKeyRequestBuilder,
)
from .by_project_key_custom_objects_by_container_request_builder import (
    ByProjectKeyCustomObjectsByContainerRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCustomObjectsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_container_and_key(
        self, container: str, key: str
    ) -> ByProjectKeyCustomObjectsByContainerByKeyRequestBuilder:
        return ByProjectKeyCustomObjectsByContainerByKeyRequestBuilder(
            container=container,
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_container(
        self, container: str
    ) -> ByProjectKeyCustomObjectsByContainerRequestBuilder:
        return ByProjectKeyCustomObjectsByContainerRequestBuilder(
            container=container,
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
    ) -> typing.Optional["CustomObjectPagedQueryResponse"]:
        """The query endpoint allows to retrieve custom objects in a specific container or all custom objects.
        For performance reasons, it is highly advisable to query only for custom objects in a container by using
        the container field in the where predicate.

        """
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
            endpoint=f"/{self._project_key}/custom-objects",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return CustomObjectPagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)

    def post(
        self,
        body: "CustomObjectDraft",
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["CustomObject"]:
        """Creates a new custom object or updates an existing custom object.
        If an object with the given container/key exists,
        the object will be replaced with the new value and the version is incremented.
        If the request contains a version and an object with the given container/key exists then the version
        must match the version of the existing object. Concurrent updates for the same custom object still can result
        in a Conflict (409) even if the version is not provided.
        Fields with null values will not be saved.

        """
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/custom-objects",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 201:
            return CustomObject.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        elif response.status_code == 200:
            return None
        raise ValueError("Unhandled status code %s", response.status_code)

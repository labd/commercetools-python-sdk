# Generated file, please do not change!!!
import typing

from ...models.custom_object import (
    CustomObject,
    CustomObjectDraft,
    CustomObjectPagedQueryResponse,
)
from .by_project_key_custom_objects_by_container_by_key_request_builder import (
    ByProjectKeyCustomObjectsByContainerByKeyRequestBuilder,
)
from .by_project_key_custom_objects_by_container_request_builder import (
    ByProjectKeyCustomObjectsByContainerRequestBuilder,
)


class ByProjectKeyCustomObjectsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withContainerAndKey(
        self, container: str, key: str
    ) -> ByProjectKeyCustomObjectsByContainerByKeyRequestBuilder:
        return ByProjectKeyCustomObjectsByContainerByKeyRequestBuilder(
            container=container,
            key=key,
            projectKey=self._project_key,
            client=self._client,
        )

    def withContainer(
        self, container: str
    ) -> ByProjectKeyCustomObjectsByContainerRequestBuilder:
        return ByProjectKeyCustomObjectsByContainerRequestBuilder(
            container=container,
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
    ) -> "CustomObjectPagedQueryResponse":
        """The query endpoint allows to retrieve custom objects in a specific container or all custom objects.
        For performance reasons, it is highly advisable to query only for custom objects in a container by using
        the container field in the where predicate.

        """
        return self._client._get(
            endpoint=f"/{self._project_key}/custom-objects",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=CustomObjectPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "CustomObjectDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CustomObject":
        """Creates a new custom object or updates an existing custom object.
        If an object with the given container/key exists,
        the object will be replaced with the new value and the version is incremented.
        If the request contains a version and an object with the given container/key exists then the version
        must match the version of the existing object. Concurrent updates for the same custom object still can result
        in a Conflict (409) even if the version is not provided.
        Fields with null values will not be saved.

        """
        return self._client._post(
            endpoint=f"/{self._project_key}/custom-objects",
            params={"expand": expand},
            data_object=body,
            response_class=CustomObject,
            headers={"Content-Type": "application/json", **headers},
        )

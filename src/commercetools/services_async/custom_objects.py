# DO NOT EDIT! This file is automatically generated
import typing

from marshmallow import fields

from commercetools import schemas, types
from commercetools.helpers import OptionalList, RemoveEmptyValuesMixin
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _CustomObjectQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _CustomObjectDeleteSchema(
    traits.VersionedSchema, traits.ExpandableSchema, traits.DataErasureSchema
):
    version = OptionalList(fields.String(), required=False)


class CustomObjectService(abstract.AbstractService):
    """Store custom JSON values."""

    def get_by_container_and_key(
        self, container, key, *, expand: OptionalListStr = None
    ) -> typing.Awaitable[types.CustomObject]:
        """Get CustomObject by container and key"""
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"custom-objects/{container}/{key}",
            params=params,
            schema_cls=schemas.CustomObjectSchema,
        )

    def get_by_id(
        self, id: str, *, expand: OptionalListStr = None
    ) -> typing.Awaitable[types.CustomObject]:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"custom-objects/{id}",
            params=params,
            schema_cls=schemas.CustomObjectSchema,
        )

    def query(
        self,
        *,
        expand: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: OptionalListStr = None,
        predicate_var: typing.Dict[str, str] = None,
    ) -> typing.Awaitable[types.CustomObjectPagedQueryResponse]:
        """The query endpoint allows to retrieve custom objects in a specific
        container or all custom objects.

        For performance reasons, it is highly advisable to query only for custom
        objects in a container by using the container field in the where
        predicate.   Store custom JSON values.
        """
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
                "predicate_var": predicate_var,
            },
            _CustomObjectQuerySchema,
        )
        return self._client._get(
            endpoint="custom-objects",
            params=params,
            schema_cls=schemas.CustomObjectPagedQueryResponseSchema,
        )

    def create_or_update(
        self, draft: types.CustomObjectDraft, *, expand: OptionalListStr = None
    ) -> typing.Awaitable[types.CustomObject]:
        """Creates a new custom object or updates an existing custom object.

        If an object with the given container/key exists, the object will be
        replaced with the new value and the version is incremented. If the
        request contains a version and an object with the given container/key
        exists then the version must match the version of the existing object.
        Concurrent updates for the same custom object still can result in a
        Conflict (409) even if the version is not provided. Fields with null
        values will not be saved.   Store custom JSON values.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="custom-objects",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.CustomObjectDraftSchema,
            response_schema_cls=schemas.CustomObjectSchema,
        )

    def create(
        self, draft: types.CustomObjectDraft, *, expand: OptionalListStr = None
    ) -> typing.Awaitable[types.CustomObject]:
        """Creates a new custom object or updates an existing custom object.

        If an object with the given container/key exists, the object will be
        replaced with the new value and the version is incremented. If the
        request contains a version and an object with the given container/key
        exists then the version must match the version of the existing object.
        Concurrent updates for the same custom object still can result in a
        Conflict (409) even if the version is not provided. Fields with null
        values will not be saved.   Store custom JSON values.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="custom-objects",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.CustomObjectDraftSchema,
            response_schema_cls=schemas.CustomObjectSchema,
        )

    def delete_by_container_and_key(
        self,
        container,
        key,
        *,
        data_erasure: bool = None,
        version: str = None,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> typing.Awaitable[types.CustomObject]:
        """Delete CustomObject by container and key"""
        params = self._serialize_params(
            {"dataErasure": data_erasure, "version": version, "expand": expand},
            _CustomObjectDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"custom-objects/{container}/{key}",
            params=params,
            response_schema_cls=schemas.CustomObjectSchema,
            force_delete=force_delete,
        )

    def delete_by_id(
        self,
        id: str,
        *,
        version: str = None,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> typing.Awaitable[types.CustomObject]:
        """The version control is optional.

        If the query contains a version, then it must match the version of the
        object.
        """
        params = self._serialize_params(
            {"version": version, "expand": expand, "dataErasure": data_erasure},
            _CustomObjectDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"custom-objects/{id}",
            params=params,
            response_schema_cls=schemas.CustomObjectSchema,
            force_delete=force_delete,
        )

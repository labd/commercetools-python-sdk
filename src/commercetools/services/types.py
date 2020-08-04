# DO NOT EDIT! This file is automatically generated
import typing

from commercetools._schemas._type import (
    TypeDraftSchema,
    TypePagedQueryResponseSchema,
    TypeSchema,
    TypeUpdateSchema,
)
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.types._type import (
    Type,
    TypeDraft,
    TypePagedQueryResponse,
    TypeUpdate,
    TypeUpdateAction,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _TypeQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _TypeUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _TypeDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class TypeService(abstract.AbstractService):
    """Types define custom fields that are used to enhance resources as you need."""

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> Type:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"types/{id}", params=params, schema_cls=TypeSchema
        )

    def get_by_key(self, key: str, *, expand: OptionalListStr = None) -> Type:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"types/key={key}", params=params, schema_cls=TypeSchema
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
    ) -> TypePagedQueryResponse:
        """Types define custom fields that are used to enhance resources as you
        need.
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
            _TypeQuerySchema,
        )
        return self._client._get(
            endpoint="types", params=params, schema_cls=TypePagedQueryResponseSchema
        )

    def create(self, draft: TypeDraft, *, expand: OptionalListStr = None) -> Type:
        """Types define custom fields that are used to enhance resources as you
        need.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="types",
            params=params,
            data_object=draft,
            request_schema_cls=TypeDraftSchema,
            response_schema_cls=TypeSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[TypeUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Type:
        params = self._serialize_params({"expand": expand}, _TypeUpdateSchema)
        update_action = TypeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"types/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=TypeUpdateSchema,
            response_schema_cls=TypeSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[TypeUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Type:
        params = self._serialize_params({"expand": expand}, _TypeUpdateSchema)
        update_action = TypeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"types/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=TypeUpdateSchema,
            response_schema_cls=TypeSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> Type:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _TypeDeleteSchema
        )
        return self._client._delete(
            endpoint=f"types/{id}",
            params=params,
            response_schema_cls=TypeSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> Type:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _TypeDeleteSchema
        )
        return self._client._delete(
            endpoint=f"types/key={key}",
            params=params,
            response_schema_cls=TypeSchema,
            force_delete=force_delete,
        )

# DO NOT EDIT! This file is automatically generated
import typing

from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.platform.models.store import (
    Store,
    StoreDraft,
    StorePagedQueryResponse,
    StoreUpdate,
    StoreUpdateAction,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _StoreQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _StoreUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _StoreDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class StoreService(abstract.AbstractService):
    """Stores let you model the context your customers shop in."""

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> Store:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"stores/{id}", params=params, response_class=Store
        )

    def get_by_key(self, key: str, *, expand: OptionalListStr = None) -> Store:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"stores/key={key}", params=params, response_class=Store
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
    ) -> StorePagedQueryResponse:
        """Stores let you model the context your customers shop in."""
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "with_total": with_total,
                "where": where,
                "predicate_var": predicate_var,
            },
            _StoreQuerySchema,
        )
        return self._client._get(
            endpoint="stores", params=params, response_class=StorePagedQueryResponse
        )

    def create(self, draft: StoreDraft, *, expand: OptionalListStr = None) -> Store:
        """Stores let you model the context your customers shop in."""
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="stores", params=params, data_object=draft, response_class=Store
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[StoreUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Store:
        params = self._serialize_params({"expand": expand}, _StoreUpdateSchema)
        update_action = StoreUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"stores/{id}",
            params=params,
            data_object=update_action,
            response_class=Store,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[StoreUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Store:
        params = self._serialize_params({"expand": expand}, _StoreUpdateSchema)
        update_action = StoreUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"stores/key={key}",
            params=params,
            data_object=update_action,
            response_class=Store,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> Store:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _StoreDeleteSchema
        )
        return self._client._delete(
            endpoint=f"stores/{id}",
            params=params,
            response_class=Store,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> Store:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _StoreDeleteSchema
        )
        return self._client._delete(
            endpoint=f"stores/key={key}",
            params=params,
            response_class=Store,
            force_delete=force_delete,
        )

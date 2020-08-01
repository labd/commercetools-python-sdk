# DO NOT EDIT! This file is automatically generated
import typing

from commercetools import schemas, types
from commercetools.services import abstract, traits
from commercetools.typing import OptionalListStr


class _ShoppingListQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _ShoppingListUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _ShoppingListDeleteSchema(
    traits.VersionedSchema, traits.ExpandableSchema, traits.DataErasureSchema
):
    pass


class ShoppingListService(abstract.AbstractService):
    """shopping-lists e.

    g. for wishlist support
    """

    def get_by_id(
        self, id: str, *, expand: OptionalListStr = None
    ) -> types.ShoppingList:
        """Gets a shopping list by ID."""
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"shopping-lists/{id}",
            params=params,
            schema_cls=schemas.ShoppingListSchema,
        )

    def get_by_key(
        self, key: str, *, expand: OptionalListStr = None
    ) -> types.ShoppingList:
        """Gets a shopping list by Key."""
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"shopping-lists/key={key}",
            params=params,
            schema_cls=schemas.ShoppingListSchema,
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
    ) -> types.ShoppingListPagedQueryResponse:
        """shopping-lists e.g. for wishlist support
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
            _ShoppingListQuerySchema,
        )
        return self._client._get(
            endpoint="shopping-lists",
            params=params,
            schema_cls=schemas.ShoppingListPagedQueryResponseSchema,
        )

    def create(
        self, draft: types.ShoppingListDraft, *, expand: OptionalListStr = None
    ) -> types.ShoppingList:
        """shopping-lists e.g. for wishlist support
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="shopping-lists",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.ShoppingListDraftSchema,
            response_schema_cls=schemas.ShoppingListSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.ShoppingListUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.ShoppingList:
        params = self._serialize_params({"expand": expand}, _ShoppingListUpdateSchema)
        update_action = types.ShoppingListUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"shopping-lists/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.ShoppingListUpdateSchema,
            response_schema_cls=schemas.ShoppingListSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[types.ShoppingListUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.ShoppingList:
        """Update a shopping list found by its Key."""
        params = self._serialize_params({"expand": expand}, _ShoppingListUpdateSchema)
        update_action = types.ShoppingListUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"shopping-lists/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.ShoppingListUpdateSchema,
            response_schema_cls=schemas.ShoppingListSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> types.ShoppingList:
        params = self._serialize_params(
            {"version": version, "expand": expand, "dataErasure": data_erasure},
            _ShoppingListDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"shopping-lists/{id}",
            params=params,
            response_schema_cls=schemas.ShoppingListSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> types.ShoppingList:
        params = self._serialize_params(
            {"version": version, "expand": expand, "dataErasure": data_erasure},
            _ShoppingListDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"shopping-lists/key={key}",
            params=params,
            response_schema_cls=schemas.ShoppingListSchema,
            force_delete=force_delete,
        )

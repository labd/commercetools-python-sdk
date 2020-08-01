# DO NOT EDIT! This file is automatically generated
import typing

from commercetools import schemas, types
from commercetools.services import abstract, traits
from commercetools.typing import OptionalListStr


class _CartDiscountQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _CartDiscountUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _CartDiscountDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class CartDiscountService(abstract.AbstractService):
    """Cart discounts are used to change the prices of different elements within a
    cart."""

    def get_by_id(
        self, id: str, *, expand: OptionalListStr = None
    ) -> types.CartDiscount:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"cart-discounts/{id}",
            params=params,
            schema_cls=schemas.CartDiscountSchema,
        )

    def get_by_key(
        self, key: str, *, expand: OptionalListStr = None
    ) -> types.CartDiscount:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"cart-discounts/key={key}",
            params=params,
            schema_cls=schemas.CartDiscountSchema,
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
    ) -> types.CartDiscountPagedQueryResponse:
        """Cart discounts are used to change the prices of different elements within
        a cart.
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
            _CartDiscountQuerySchema,
        )
        return self._client._get(
            endpoint="cart-discounts",
            params=params,
            schema_cls=schemas.CartDiscountPagedQueryResponseSchema,
        )

    def create(
        self, draft: types.CartDiscountDraft, *, expand: OptionalListStr = None
    ) -> types.CartDiscount:
        """Cart discounts are used to change the prices of different elements within
        a cart.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="cart-discounts",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.CartDiscountDraftSchema,
            response_schema_cls=schemas.CartDiscountSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.CartDiscountUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.CartDiscount:
        params = self._serialize_params({"expand": expand}, _CartDiscountUpdateSchema)
        update_action = types.CartDiscountUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"cart-discounts/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.CartDiscountUpdateSchema,
            response_schema_cls=schemas.CartDiscountSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[types.CartDiscountUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.CartDiscount:
        params = self._serialize_params({"expand": expand}, _CartDiscountUpdateSchema)
        update_action = types.CartDiscountUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"cart-discounts/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.CartDiscountUpdateSchema,
            response_schema_cls=schemas.CartDiscountSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> types.CartDiscount:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _CartDiscountDeleteSchema
        )
        return self._client._delete(
            endpoint=f"cart-discounts/{id}",
            params=params,
            response_schema_cls=schemas.CartDiscountSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> types.CartDiscount:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _CartDiscountDeleteSchema
        )
        return self._client._delete(
            endpoint=f"cart-discounts/key={key}",
            params=params,
            response_schema_cls=schemas.CartDiscountSchema,
            force_delete=force_delete,
        )

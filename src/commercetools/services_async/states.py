# DO NOT EDIT! This file is automatically generated
import typing

from commercetools import schemas, types
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _StateQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _StateUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _StateDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class StateService(abstract.AbstractService):
    """The commercetools platform allows you to model states of certain objects,
    such as orders, line items, products,

    reviews, and payments in order to define finite state machines reflecting the
    business logic you'd like to implement.
    """

    def get_by_id(
        self, id: str, *, expand: OptionalListStr = None
    ) -> typing.Awaitable[types.State]:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"states/{id}", params=params, schema_cls=schemas.StateSchema
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
    ) -> typing.Awaitable[types.StatePagedQueryResponse]:
        """The commercetools platform allows you to model states of certain objects,
        such as orders, line items, products, reviews, and payments in order to
        define finite state machines reflecting the business logic you'd like to
        implement.
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
            _StateQuerySchema,
        )
        return self._client._get(
            endpoint="states",
            params=params,
            schema_cls=schemas.StatePagedQueryResponseSchema,
        )

    def create(
        self, draft: types.StateDraft, *, expand: OptionalListStr = None
    ) -> typing.Awaitable[types.State]:
        """The commercetools platform allows you to model states of certain objects,
        such as orders, line items, products, reviews, and payments in order to
        define finite state machines reflecting the business logic you'd like to
        implement.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="states",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.StateDraftSchema,
            response_schema_cls=schemas.StateSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.StateUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> typing.Awaitable[types.State]:
        params = self._serialize_params({"expand": expand}, _StateUpdateSchema)
        update_action = types.StateUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"states/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.StateUpdateSchema,
            response_schema_cls=schemas.StateSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> typing.Awaitable[types.State]:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _StateDeleteSchema
        )
        return self._client._delete(
            endpoint=f"states/{id}",
            params=params,
            response_schema_cls=schemas.StateSchema,
            force_delete=force_delete,
        )

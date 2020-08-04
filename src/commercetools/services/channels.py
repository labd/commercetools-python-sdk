# DO NOT EDIT! This file is automatically generated
import typing

from commercetools._schemas._channel import (
    ChannelDraftSchema,
    ChannelPagedQueryResponseSchema,
    ChannelSchema,
    ChannelUpdateSchema,
)
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.types._channel import (
    Channel,
    ChannelDraft,
    ChannelPagedQueryResponse,
    ChannelUpdate,
    ChannelUpdateAction,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _ChannelQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _ChannelUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _ChannelDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class ChannelService(abstract.AbstractService):
    """Channels represent a source or destination of different entities.

    They can be used to model warehouses or stores.
    """

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> Channel:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"channels/{id}", params=params, schema_cls=ChannelSchema
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
    ) -> ChannelPagedQueryResponse:
        """Channels represent a source or destination of different entities. They
        can be used to model warehouses or stores.
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
            _ChannelQuerySchema,
        )
        return self._client._get(
            endpoint="channels",
            params=params,
            schema_cls=ChannelPagedQueryResponseSchema,
        )

    def create(self, draft: ChannelDraft, *, expand: OptionalListStr = None) -> Channel:
        """Channels represent a source or destination of different entities. They
        can be used to model warehouses or stores.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="channels",
            params=params,
            data_object=draft,
            request_schema_cls=ChannelDraftSchema,
            response_schema_cls=ChannelSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[ChannelUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Channel:
        params = self._serialize_params({"expand": expand}, _ChannelUpdateSchema)
        update_action = ChannelUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"channels/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=ChannelUpdateSchema,
            response_schema_cls=ChannelSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> Channel:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _ChannelDeleteSchema
        )
        return self._client._delete(
            endpoint=f"channels/{id}",
            params=params,
            response_schema_cls=ChannelSchema,
            force_delete=force_delete,
        )

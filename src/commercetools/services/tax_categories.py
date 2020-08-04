# DO NOT EDIT! This file is automatically generated
import typing

from commercetools._schemas._tax_category import (
    TaxCategoryDraftSchema,
    TaxCategoryPagedQueryResponseSchema,
    TaxCategorySchema,
    TaxCategoryUpdateSchema,
)
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.types._tax_category import (
    TaxCategory,
    TaxCategoryDraft,
    TaxCategoryPagedQueryResponse,
    TaxCategoryUpdate,
    TaxCategoryUpdateAction,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _TaxCategoryQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _TaxCategoryUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _TaxCategoryDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class TaxCategoryService(abstract.AbstractService):
    """Tax Categories define how products are to be taxed in different countries."""

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> TaxCategory:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"tax-categories/{id}", params=params, schema_cls=TaxCategorySchema
        )

    def get_by_key(self, key: str, *, expand: OptionalListStr = None) -> TaxCategory:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"tax-categories/key={key}",
            params=params,
            schema_cls=TaxCategorySchema,
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
    ) -> TaxCategoryPagedQueryResponse:
        """Tax Categories define how products are to be taxed in different
        countries.
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
            _TaxCategoryQuerySchema,
        )
        return self._client._get(
            endpoint="tax-categories",
            params=params,
            schema_cls=TaxCategoryPagedQueryResponseSchema,
        )

    def create(
        self, draft: TaxCategoryDraft, *, expand: OptionalListStr = None
    ) -> TaxCategory:
        """Tax Categories define how products are to be taxed in different
        countries.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="tax-categories",
            params=params,
            data_object=draft,
            request_schema_cls=TaxCategoryDraftSchema,
            response_schema_cls=TaxCategorySchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[TaxCategoryUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> TaxCategory:
        params = self._serialize_params({"expand": expand}, _TaxCategoryUpdateSchema)
        update_action = TaxCategoryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"tax-categories/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=TaxCategoryUpdateSchema,
            response_schema_cls=TaxCategorySchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[TaxCategoryUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> TaxCategory:
        params = self._serialize_params({"expand": expand}, _TaxCategoryUpdateSchema)
        update_action = TaxCategoryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"tax-categories/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=TaxCategoryUpdateSchema,
            response_schema_cls=TaxCategorySchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> TaxCategory:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _TaxCategoryDeleteSchema
        )
        return self._client._delete(
            endpoint=f"tax-categories/{id}",
            params=params,
            response_schema_cls=TaxCategorySchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> TaxCategory:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _TaxCategoryDeleteSchema
        )
        return self._client._delete(
            endpoint=f"tax-categories/key={key}",
            params=params,
            response_schema_cls=TaxCategorySchema,
            force_delete=force_delete,
        )

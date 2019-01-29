import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ProductDiscountsModel(BaseModel):
    _primary_type_name = "product-discount"
    _resource_schema = schemas.ProductDiscountSchema

    def _create_from_draft(
        self, draft: types.ProductDiscountDraft, id: typing.Optional[str] = None
    ) -> types.ProductDiscount:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.ProductDiscount(
            id=str(object_id),
            version=1,
            name=draft.name,
            description=draft.description,
            value=draft.value,
            predicate=draft.predicate,
            sort_order=draft.sort_order,
            references=[],
            is_active=draft.is_active,
            valid_from=draft.valid_from,
            valid_until=draft.valid_until,
        )


class ProductDiscountsBackend(ServiceBackend):
    service_path = "product-discounts"
    model_class = ProductDiscountsModel

    _schema_draft = schemas.ProductDiscountDraftSchema
    _schema_update = schemas.ProductDiscountUpdateSchema
    _schema_query_response = schemas.ProductDiscountPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]

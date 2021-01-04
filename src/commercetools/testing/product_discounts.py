import datetime
import typing
import uuid

from commercetools.platform import models
from commercetools.platform.models._schemas.product_discount import (
    ProductDiscountDraftSchema,
    ProductDiscountPagedQueryResponseSchema,
    ProductDiscountSchema,
    ProductDiscountUpdateSchema,
)
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ProductDiscountsModel(BaseModel):
    _primary_type_name = "product-discount"
    _resource_schema = ProductDiscountSchema

    def _create_from_draft(
        self, draft: models.ProductDiscountDraft, id: typing.Optional[str] = None
    ) -> models.ProductDiscount:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return models.ProductDiscount(
            id=str(object_id),
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
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

    _schema_draft = ProductDiscountDraftSchema
    _schema_update = ProductDiscountUpdateSchema
    _schema_query_response = ProductDiscountPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]

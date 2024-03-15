import copy
import datetime
import typing
import uuid

from commercetools.platform import models
from commercetools.platform.models._schemas.cart_discount import (
    CartDiscountDraftSchema,
    CartDiscountPagedQueryResponseSchema,
    CartDiscountSchema,
    CartDiscountUpdateSchema,
)
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import (
    update_attribute,
    update_datetime_attribute,
    update_enum_attribute,
)


class CartDiscountsModel(BaseModel):
    _resource_schema = CartDiscountSchema
    _primary_type_name = "cart-discounts"
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: models.CartDiscountDraft, id: typing.Optional[str] = None
    ) -> models.CartDiscount:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return models.CartDiscount(
            id=str(object_id),
            version=1,
            key=draft.key,
            name=draft.name,
            description=draft.description,
            value=draft.value,
            target=draft.target,
            cart_predicate=draft.cart_predicate,
            is_active=draft.is_active or False,
            references=[],
            stacking_mode=draft.stacking_mode or models.StackingMode.STACKING,
            sort_order=draft.sort_order,
            valid_from=draft.valid_from,
            valid_until=draft.valid_until,
            requires_discount_code=draft.requires_discount_code,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            custom=utils.create_from_draft(draft.custom),
            stores=[],
        )


class CartDiscountsBackend(ServiceBackend):
    service_path = "cart-discounts"
    model_class = CartDiscountsModel
    _schema_draft = CartDiscountDraftSchema
    _schema_update = CartDiscountUpdateSchema
    _schema_query_response = CartDiscountPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]

    _actions = {
        "setKey": update_attribute("key", "key"),
        "changeSortOrder": update_attribute("sortOrder", "sort_order"),
        "changeTarget": update_enum_attribute("target", "target"),
        "changeIsActive": update_attribute("isActive", "is_active"),
        "setName": update_attribute("name", "name"),
        "setDescription": update_attribute("description", "description"),
        "setCartPredicate": update_attribute("cartPredicate", "cart_predicate"),
        "setValidFrom": update_datetime_attribute("validFrom", "valid_from"),
        "setValidUntil": update_datetime_attribute("validUntil", "valid_until"),
    }

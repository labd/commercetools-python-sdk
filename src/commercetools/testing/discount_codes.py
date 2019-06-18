import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import update_attribute


class DiscountCodesModel(BaseModel):
    _resource_schema = schemas.DiscountCodeSchema
    _primary_type_name = "discount-code"

    def _create_from_draft(
        self, draft: types.DiscountCodeDraft, id: typing.Optional[str] = None
    ) -> types.DiscountCode:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.DiscountCode(
            id=str(object_id),
            version=1,
            name=draft.name,
            description=draft.description,
            code=draft.code,
            cart_discounts=draft.cart_discounts,
            cart_predicate=draft.cart_predicate,
            is_active=draft.is_active or False,
            max_applications=draft.max_applications,
            max_applications_per_customer=draft.max_applications_per_customer,
            groups=draft.groups or [],
            references=[],
            valid_from=draft.valid_from,
            valid_until=draft.valid_until,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            custom=utils.create_from_draft(draft.custom),
        )


class DiscountCodesBackend(ServiceBackend):
    service_path = "discount-codes"
    model_class = DiscountCodesModel
    _schema_draft = schemas.DiscountCodeDraftSchema
    _schema_update = schemas.DiscountCodeUpdateSchema
    _schema_query_response = schemas.DiscountCodePagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]

    _actions = {
        "changeIsActive": update_attribute("isActive", "is_active"),
        "setName": update_attribute("name", "name"),
        "setDescription": update_attribute("description", "description"),
        "setCartPredicate": update_attribute("cartPredicate", "cart_predicate"),
        "setMaxApplications": update_attribute("maxApplications", "max_applications"),
        "setMaxApplicationsPerCustomer": update_attribute(
            "maxApplicationsPerCustomer", "max_applications_per_customer"),
    }

import datetime
import random
import string
import typing
import uuid

from commercetools.platform import models
from commercetools.platform.models._schemas.tax_category import (
    TaxCategoryDraftSchema,
    TaxCategoryPagedQueryResponseSchema,
    TaxCategorySchema,
    TaxCategoryUpdateSchema,
    TaxRateSchema,
)
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import (
    update_attribute,
    update_attribute_add_item,
    update_attribute_delete_item_by_id,
)


def generate_tax_rate_id():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=6))


class TaxCategoryModel(BaseModel):
    _primary_type_name = "tax-category"
    _resource_schema = TaxCategorySchema
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: models.TaxCategoryDraft, id: typing.Optional[str] = None
    ) -> models.TaxCategory:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return models.TaxCategory(
            id=str(object_id),
            key=draft.key,
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            name=draft.name,
            description=draft.description,
            rates=self._create_rates(draft.rates),
        )

    def _create_rates(
        self, drafts: typing.Optional[typing.List[models.TaxRateDraft]]
    ) -> typing.List[models.TaxRate]:
        result: typing.List[models.TaxRate] = []
        if not drafts:
            return result
        for draft in drafts:
            obj = models.TaxRate(
                id=generate_tax_rate_id(),
                name=draft.name,
                amount=draft.amount,
                included_in_price=draft.included_in_price,
                country=draft.country,
                state=draft.state,
                sub_rates=draft.sub_rates,
            )
            result.append(obj)
        return result


def add_tax_rate_action():
    return update_attribute_add_item(
        "rates", "tax_rate", TaxRateSchema, generate_tax_rate_id
    )


def replace_tax_rate_action():
    delete_action = update_attribute_delete_item_by_id("rates", "tax_rate_id")
    add_action = add_tax_rate_action()

    def updater(self, obj, action):
        obj = delete_action(self, obj, action)
        return add_action(self, obj, action)

    return updater


class TaxCategoryBackend(ServiceBackend):
    service_path = "tax-categories"
    model_class = TaxCategoryModel
    _schema_draft = TaxCategoryDraftSchema
    _schema_update = TaxCategoryUpdateSchema
    _schema_query_response = TaxCategoryPagedQueryResponseSchema

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
        "changeName": update_attribute("name", "name"),
        "setKey": update_attribute("key", "key"),
        "setDescription": update_attribute("description", "description"),
        "addTaxRate": add_tax_rate_action(),
        "removeTaxRate": update_attribute_delete_item_by_id("rates", "tax_rate_id"),
        "replaceTaxRate": replace_tax_rate_action(),
    }

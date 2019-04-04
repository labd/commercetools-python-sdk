import datetime
import uuid
from typing import Optional

from commercetools import schemas, types
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ShoppingListModel(BaseModel):
    _resource_schema = schemas.ShoppingListSchema
    _primary_type_name = "shopping-list"

    def _create_line_item_from_draft(
        self, line_item_draft: types.ShoppingListLineItemDraft
    ) -> types.ShoppingListLineItem:
        return types.ShoppingListLineItem(
            id=str(uuid.uuid4()),
            added_at=datetime.datetime.now(datetime.timezone.utc),
            custom=utils.create_from_draft(line_item_draft.custom),
            deactivated_at=None,
            name=types.LocalizedString({"en": "FRUIT MIX STAGE 1"}),
            product_id=line_item_draft.product_id,
            product_type=types.ProductTypeReference(
                id="9faf6335-7618-4f8b-a11d-c0f832b733c1"
            ),
            product_slug=types.LocalizedString({"en": "fruit-mix-stage-1"}),
            quantity=line_item_draft.quantity,
            variant=types.ProductVariant(
                id=1,
                sku="982218931672529",
                prices=[
                    types.Price(
                        id="fb424988-79b3-4418-8730-9f324025a13c",
                        value=types.Money(cent_amount=1000, currency_code="GBP"),
                    )
                ],
            ),
            variant_id=line_item_draft.variant_id,
        )

    def _create_line_item_text_from_draft(
        self, text_line_item_draft: types.TextLineItemDraft
    ) -> types.TextLineItem:
        return types.TextLineItem(
            id=str(uuid.uuid4()),
            added_at=datetime.datetime.now(datetime.timezone.utc),
            custom=utils.create_from_draft(text_line_item_draft.custom),
            description=text_line_item_draft.description,
            name=text_line_item_draft.name,
            quantity=text_line_item_draft.quantity,
        )

    def _create_from_draft(
        self, draft: types.ShoppingListDraft, id: Optional[str] = None
    ) -> types.ShoppingList:
        object_id = str(uuid.UUID(id)) if id is not None else uuid.uuid4()

        line_items = None
        if draft.line_items:
            line_items = [
                self._create_line_item_from_draft(line_item)
                for line_item in draft.line_items
            ]

        text_line_items = None
        if draft.text_line_items:
            text_line_items = [
                self._create_line_item_text_from_draft(text_line_item)
                for text_line_item in draft.text_line_items
            ]

        return types.ShoppingList(
            id=str(object_id),
            version=1,
            custom=utils.create_from_draft(draft.custom),
            customer=draft.customer,
            delete_days_after_last_modification=draft.delete_days_after_last_modification,
            description=draft.description,
            key=draft.key,
            line_items=line_items,
            name=draft.name,
            slug=draft.slug,
            text_line_items=text_line_items,
            anonymous_id=draft.anonymous_id,
        )


class ShoppingListBackend(ServiceBackend):
    service_path = "shopping-lists"
    model_class = ShoppingListModel
    _schema_draft = schemas.ShoppingListDraftSchema
    _schema_update = schemas.ShoppingListUpdateSchema
    _schema_query_response = schemas.ShoppingListPagedQueryResponseSchema

    def urls(self) -> list:
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

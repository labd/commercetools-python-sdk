# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class MyShoppingListSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="createdBy",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )
    description = LocalizedStringField(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShoppingListLineItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lineItems",
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    slug = LocalizedStringField(allow_none=True, missing=None)
    text_line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TextLineItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="textLineItems",
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MyShoppingList(**data)


class ShoppingListSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="createdBy",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )
    description = LocalizedStringField(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShoppingListLineItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lineItems",
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    slug = LocalizedStringField(allow_none=True, missing=None)
    text_line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TextLineItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="textLineItems",
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShoppingList(**data)


class ShoppingListDraftSchema(marshmallow.Schema):
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )
    description = LocalizedStringField(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShoppingListLineItemDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lineItems",
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    slug = LocalizedStringField(allow_none=True, missing=None)
    text_line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TextLineItemDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="textLineItems",
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShoppingListDraft(**data)


class ShoppingListLineItemSchema(marshmallow.Schema):
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    deactivated_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="deactivatedAt"
    )
    id = marshmallow.fields.String(allow_none=True, missing=None)
    name = LocalizedStringField(allow_none=True, missing=None)
    product_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="productId"
    )
    product_slug = LocalizedStringField(
        allow_none=True, missing=None, data_key="productSlug"
    )
    product_type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product_type.ProductTypeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productType",
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductVariantSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShoppingListLineItem(**data)


class ShoppingListLineItemDraftSchema(marshmallow.Schema):
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    product_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="productId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShoppingListLineItemDraft(**data)


class ShoppingListPagedQueryResponseSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShoppingListSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShoppingListPagedQueryResponse(**data)


class ShoppingListReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShoppingListSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ShoppingListReference(**data)


class ShoppingListResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ShoppingListResourceIdentifier(**data)


class ShoppingListUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addLineItem": helpers.absmod(
                    __name__, ".ShoppingListAddLineItemActionSchema"
                ),
                "addTextLineItem": helpers.absmod(
                    __name__, ".ShoppingListAddTextLineItemActionSchema"
                ),
                "changeLineItemQuantity": helpers.absmod(
                    __name__, ".ShoppingListChangeLineItemQuantityActionSchema"
                ),
                "changeLineItemsOrder": helpers.absmod(
                    __name__, ".ShoppingListChangeLineItemsOrderActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".ShoppingListChangeNameActionSchema"
                ),
                "changeTextLineItemName": helpers.absmod(
                    __name__, ".ShoppingListChangeTextLineItemNameActionSchema"
                ),
                "changeTextLineItemQuantity": helpers.absmod(
                    __name__, ".ShoppingListChangeTextLineItemQuantityActionSchema"
                ),
                "changeTextLineItemsOrder": helpers.absmod(
                    __name__, ".ShoppingListChangeTextLineItemsOrderActionSchema"
                ),
                "removeLineItem": helpers.absmod(
                    __name__, ".ShoppingListRemoveLineItemActionSchema"
                ),
                "removeTextLineItem": helpers.absmod(
                    __name__, ".ShoppingListRemoveTextLineItemActionSchema"
                ),
                "setAnonymousId": helpers.absmod(
                    __name__, ".ShoppingListSetAnonymousIdActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".ShoppingListSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".ShoppingListSetCustomTypeActionSchema"
                ),
                "setCustomer": helpers.absmod(
                    __name__, ".ShoppingListSetCustomerActionSchema"
                ),
                "setDeleteDaysAfterLastModification": helpers.absmod(
                    __name__,
                    ".ShoppingListSetDeleteDaysAfterLastModificationActionSchema",
                ),
                "setDescription": helpers.absmod(
                    __name__, ".ShoppingListSetDescriptionActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".ShoppingListSetKeyActionSchema"),
                "setLineItemCustomField": helpers.absmod(
                    __name__, ".ShoppingListSetLineItemCustomFieldActionSchema"
                ),
                "setLineItemCustomType": helpers.absmod(
                    __name__, ".ShoppingListSetLineItemCustomTypeActionSchema"
                ),
                "setSlug": helpers.absmod(__name__, ".ShoppingListSetSlugActionSchema"),
                "setTextLineItemCustomField": helpers.absmod(
                    __name__, ".ShoppingListSetTextLineItemCustomFieldActionSchema"
                ),
                "setTextLineItemCustomType": helpers.absmod(
                    __name__, ".ShoppingListSetTextLineItemCustomTypeActionSchema"
                ),
                "setTextLineItemDescription": helpers.absmod(
                    __name__, ".ShoppingListSetTextLineItemDescriptionActionSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShoppingListUpdate(**data)


class ShoppingListUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListUpdateAction(**data)


class TextLineItemSchema(marshmallow.Schema):
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    description = LocalizedStringField(allow_none=True, missing=None)
    id = marshmallow.fields.String(allow_none=True, missing=None)
    name = LocalizedStringField(allow_none=True, missing=None)
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TextLineItem(**data)


class TextLineItemDraftSchema(marshmallow.Schema):
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    description = LocalizedStringField(allow_none=True, missing=None)
    name = LocalizedStringField(allow_none=True, missing=None)
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TextLineItemDraft(**data)


class ShoppingListAddLineItemActionSchema(ShoppingListUpdateActionSchema):
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    product_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="productId"
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListAddLineItemAction(**data)


class ShoppingListAddTextLineItemActionSchema(ShoppingListUpdateActionSchema):
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListAddTextLineItemAction(**data)


class ShoppingListChangeLineItemQuantityActionSchema(ShoppingListUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListChangeLineItemQuantityAction(**data)


class ShoppingListChangeLineItemsOrderActionSchema(ShoppingListUpdateActionSchema):
    line_item_order = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="lineItemOrder",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListChangeLineItemsOrderAction(**data)


class ShoppingListChangeNameActionSchema(ShoppingListUpdateActionSchema):
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListChangeNameAction(**data)


class ShoppingListChangeTextLineItemNameActionSchema(ShoppingListUpdateActionSchema):
    text_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="textLineItemId"
    )
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListChangeTextLineItemNameAction(**data)


class ShoppingListChangeTextLineItemQuantityActionSchema(
    ShoppingListUpdateActionSchema
):
    text_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="textLineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListChangeTextLineItemQuantityAction(**data)


class ShoppingListChangeTextLineItemsOrderActionSchema(ShoppingListUpdateActionSchema):
    text_line_item_order = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="textLineItemOrder",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListChangeTextLineItemsOrderAction(**data)


class ShoppingListRemoveLineItemActionSchema(ShoppingListUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListRemoveLineItemAction(**data)


class ShoppingListRemoveTextLineItemActionSchema(ShoppingListUpdateActionSchema):
    text_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="textLineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListRemoveTextLineItemAction(**data)


class ShoppingListSetAnonymousIdActionSchema(ShoppingListUpdateActionSchema):
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetAnonymousIdAction(**data)


class ShoppingListSetCustomFieldActionSchema(ShoppingListUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetCustomFieldAction(**data)


class ShoppingListSetCustomTypeActionSchema(ShoppingListUpdateActionSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetCustomTypeAction(**data)


class ShoppingListSetCustomerActionSchema(ShoppingListUpdateActionSchema):
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetCustomerAction(**data)


class ShoppingListSetDeleteDaysAfterLastModificationActionSchema(
    ShoppingListUpdateActionSchema
):
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetDeleteDaysAfterLastModificationAction(**data)


class ShoppingListSetDescriptionActionSchema(ShoppingListUpdateActionSchema):
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetDescriptionAction(**data)


class ShoppingListSetKeyActionSchema(ShoppingListUpdateActionSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetKeyAction(**data)


class ShoppingListSetLineItemCustomFieldActionSchema(ShoppingListUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetLineItemCustomFieldAction(**data)


class ShoppingListSetLineItemCustomTypeActionSchema(ShoppingListUpdateActionSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetLineItemCustomTypeAction(**data)


class ShoppingListSetSlugActionSchema(ShoppingListUpdateActionSchema):
    slug = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetSlugAction(**data)


class ShoppingListSetTextLineItemCustomFieldActionSchema(
    ShoppingListUpdateActionSchema
):
    text_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="textLineItemId"
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetTextLineItemCustomFieldAction(**data)


class ShoppingListSetTextLineItemCustomTypeActionSchema(ShoppingListUpdateActionSchema):
    text_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="textLineItemId"
    )
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetTextLineItemCustomTypeAction(**data)


class ShoppingListSetTextLineItemDescriptionActionSchema(
    ShoppingListUpdateActionSchema
):
    text_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="textLineItemId"
    )
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShoppingListSetTextLineItemDescriptionAction(**data)

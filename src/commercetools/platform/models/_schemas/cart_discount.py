# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..cart_discount import SelectionMode, StackingMode
from ..common import ReferenceTypeId
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)

# Fields


# Marshmallow Schemas
class CartDiscountSchema(BaseResourceSchema):
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
    name = LocalizedStringField(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "absolute": helpers.absmod(
                __name__, ".CartDiscountValueAbsoluteDraftSchema"
            ),
            "giftLineItem": helpers.absmod(
                __name__, ".CartDiscountValueGiftLineItemDraftSchema"
            ),
            "relative": helpers.absmod(
                __name__, ".CartDiscountValueRelativeDraftSchema"
            ),
        },
        missing=None,
    )
    cart_predicate = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="cartPredicate"
    )
    target = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "customLineItems": helpers.absmod(
                __name__, ".CartDiscountCustomLineItemsTargetSchema"
            ),
            "lineItems": helpers.absmod(__name__, ".CartDiscountLineItemsTargetSchema"),
            "shipping": helpers.absmod(
                __name__, ".CartDiscountShippingCostTargetSchema"
            ),
            "multiBuyCustomLineItems": helpers.absmod(
                __name__, ".MultiBuyCustomLineItemsTargetSchema"
            ),
            "multiBuyLineItems": helpers.absmod(
                __name__, ".MultiBuyLineItemsTargetSchema"
            ),
        },
        missing=None,
    )
    sort_order = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="sortOrder"
    )
    is_active = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isActive"
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )
    requires_discount_code = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="requiresDiscountCode"
    )
    references = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("typeId", "type_id"),
            discriminator_schemas={
                "cart-discount": helpers.absmod(
                    __name__, ".CartDiscountReferenceSchema"
                ),
                "cart": helpers.absmod(__name__, ".cart.CartReferenceSchema"),
                "category": helpers.absmod(
                    __name__, ".category.CategoryReferenceSchema"
                ),
                "channel": helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
                "key-value-document": helpers.absmod(
                    __name__, ".custom_object.CustomObjectReferenceSchema"
                ),
                "customer-group": helpers.absmod(
                    __name__, ".customer_group.CustomerGroupReferenceSchema"
                ),
                "customer": helpers.absmod(
                    __name__, ".customer.CustomerReferenceSchema"
                ),
                "discount-code": helpers.absmod(
                    __name__, ".discount_code.DiscountCodeReferenceSchema"
                ),
                "inventory-entry": helpers.absmod(
                    __name__, ".inventory.InventoryEntryReferenceSchema"
                ),
                "order-edit": helpers.absmod(
                    __name__, ".order_edit.OrderEditReferenceSchema"
                ),
                "order": helpers.absmod(__name__, ".order.OrderReferenceSchema"),
                "payment": helpers.absmod(__name__, ".payment.PaymentReferenceSchema"),
                "product-discount": helpers.absmod(
                    __name__, ".product_discount.ProductDiscountReferenceSchema"
                ),
                "product-type": helpers.absmod(
                    __name__, ".product_type.ProductTypeReferenceSchema"
                ),
                "product": helpers.absmod(__name__, ".product.ProductReferenceSchema"),
                "review": helpers.absmod(__name__, ".review.ReviewReferenceSchema"),
                "shipping-method": helpers.absmod(
                    __name__, ".shipping_method.ShippingMethodReferenceSchema"
                ),
                "shopping-list": helpers.absmod(
                    __name__, ".shopping_list.ShoppingListReferenceSchema"
                ),
                "state": helpers.absmod(__name__, ".state.StateReferenceSchema"),
                "store": helpers.absmod(__name__, ".store.StoreReferenceSchema"),
                "tax-category": helpers.absmod(
                    __name__, ".tax_category.TaxCategoryReferenceSchema"
                ),
                "type": helpers.absmod(__name__, ".type.TypeReferenceSchema"),
                "zone": helpers.absmod(__name__, ".zone.ZoneReferenceSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )
    stacking_mode = marshmallow_enum.EnumField(
        StackingMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="stackingMode",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CartDiscount(**data)


class CartDiscountDraftSchema(marshmallow.Schema):
    name = LocalizedStringField(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "absolute": helpers.absmod(
                __name__, ".CartDiscountValueAbsoluteDraftSchema"
            ),
            "giftLineItem": helpers.absmod(
                __name__, ".CartDiscountValueGiftLineItemDraftSchema"
            ),
            "relative": helpers.absmod(
                __name__, ".CartDiscountValueRelativeDraftSchema"
            ),
        },
        missing=None,
    )
    cart_predicate = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="cartPredicate"
    )
    target = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "customLineItems": helpers.absmod(
                __name__, ".CartDiscountCustomLineItemsTargetSchema"
            ),
            "lineItems": helpers.absmod(__name__, ".CartDiscountLineItemsTargetSchema"),
            "shipping": helpers.absmod(
                __name__, ".CartDiscountShippingCostTargetSchema"
            ),
            "multiBuyCustomLineItems": helpers.absmod(
                __name__, ".MultiBuyCustomLineItemsTargetSchema"
            ),
            "multiBuyLineItems": helpers.absmod(
                __name__, ".MultiBuyLineItemsTargetSchema"
            ),
        },
        missing=None,
    )
    sort_order = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="sortOrder"
    )
    is_active = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isActive"
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )
    requires_discount_code = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="requiresDiscountCode"
    )
    stacking_mode = marshmallow_enum.EnumField(
        StackingMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="stackingMode",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CartDiscountDraft(**data)


class CartDiscountPagedQueryResponseSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CartDiscountSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CartDiscountPagedQueryResponse(**data)


class CartDiscountReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CartDiscountSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CartDiscountReference(**data)


class CartDiscountResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CartDiscountResourceIdentifier(**data)


class CartDiscountTargetSchema(marshmallow.Schema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartDiscountTarget(**data)


class CartDiscountCustomLineItemsTargetSchema(CartDiscountTargetSchema):
    predicate = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartDiscountCustomLineItemsTarget(**data)


class CartDiscountLineItemsTargetSchema(CartDiscountTargetSchema):
    predicate = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartDiscountLineItemsTarget(**data)


class CartDiscountShippingCostTargetSchema(CartDiscountTargetSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartDiscountShippingCostTarget(**data)


class CartDiscountUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeCartPredicate": helpers.absmod(
                    __name__, ".CartDiscountChangeCartPredicateActionSchema"
                ),
                "changeIsActive": helpers.absmod(
                    __name__, ".CartDiscountChangeIsActiveActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".CartDiscountChangeNameActionSchema"
                ),
                "changeRequiresDiscountCode": helpers.absmod(
                    __name__, ".CartDiscountChangeRequiresDiscountCodeActionSchema"
                ),
                "changeSortOrder": helpers.absmod(
                    __name__, ".CartDiscountChangeSortOrderActionSchema"
                ),
                "changeStackingMode": helpers.absmod(
                    __name__, ".CartDiscountChangeStackingModeActionSchema"
                ),
                "changeTarget": helpers.absmod(
                    __name__, ".CartDiscountChangeTargetActionSchema"
                ),
                "changeValue": helpers.absmod(
                    __name__, ".CartDiscountChangeValueActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".CartDiscountSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".CartDiscountSetCustomTypeActionSchema"
                ),
                "setDescription": helpers.absmod(
                    __name__, ".CartDiscountSetDescriptionActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".CartDiscountSetKeyActionSchema"),
                "setValidFrom": helpers.absmod(
                    __name__, ".CartDiscountSetValidFromActionSchema"
                ),
                "setValidFromAndUntil": helpers.absmod(
                    __name__, ".CartDiscountSetValidFromAndUntilActionSchema"
                ),
                "setValidUntil": helpers.absmod(
                    __name__, ".CartDiscountSetValidUntilActionSchema"
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

        return models.CartDiscountUpdate(**data)


class CartDiscountUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountUpdateAction(**data)


class CartDiscountValueSchema(marshmallow.Schema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartDiscountValue(**data)


class CartDiscountValueAbsoluteSchema(CartDiscountValueSchema):
    money = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "centPrecision": helpers.absmod(
                    __name__, ".common.CentPrecisionMoneySchema"
                ),
                "highPrecision": helpers.absmod(
                    __name__, ".common.HighPrecisionMoneySchema"
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
        del data["type"]
        return models.CartDiscountValueAbsolute(**data)


class CartDiscountValueDraftSchema(marshmallow.Schema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartDiscountValueDraft(**data)


class CartDiscountValueAbsoluteDraftSchema(CartDiscountValueDraftSchema):
    money = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartDiscountValueAbsoluteDraft(**data)


class CartDiscountValueGiftLineItemSchema(CartDiscountValueSchema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="supplyChannel",
    )
    distribution_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="distributionChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartDiscountValueGiftLineItem(**data)


class CartDiscountValueGiftLineItemDraftSchema(CartDiscountValueDraftSchema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="supplyChannel",
    )
    distribution_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="distributionChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartDiscountValueGiftLineItemDraft(**data)


class CartDiscountValueRelativeSchema(CartDiscountValueSchema):
    permyriad = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartDiscountValueRelative(**data)


class CartDiscountValueRelativeDraftSchema(CartDiscountValueDraftSchema):
    permyriad = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartDiscountValueRelativeDraft(**data)


class MultiBuyCustomLineItemsTargetSchema(CartDiscountTargetSchema):
    predicate = marshmallow.fields.String(allow_none=True, missing=None)
    trigger_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="triggerQuantity"
    )
    discounted_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="discountedQuantity"
    )
    max_occurrence = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxOccurrence"
    )
    selection_mode = marshmallow_enum.EnumField(
        SelectionMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="selectionMode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.MultiBuyCustomLineItemsTarget(**data)


class MultiBuyLineItemsTargetSchema(CartDiscountTargetSchema):
    predicate = marshmallow.fields.String(allow_none=True, missing=None)
    trigger_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="triggerQuantity"
    )
    discounted_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="discountedQuantity"
    )
    max_occurrence = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxOccurrence"
    )
    selection_mode = marshmallow_enum.EnumField(
        SelectionMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="selectionMode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.MultiBuyLineItemsTarget(**data)


class CartDiscountChangeCartPredicateActionSchema(CartDiscountUpdateActionSchema):
    cart_predicate = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="cartPredicate"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountChangeCartPredicateAction(**data)


class CartDiscountChangeIsActiveActionSchema(CartDiscountUpdateActionSchema):
    is_active = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isActive"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountChangeIsActiveAction(**data)


class CartDiscountChangeNameActionSchema(CartDiscountUpdateActionSchema):
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountChangeNameAction(**data)


class CartDiscountChangeRequiresDiscountCodeActionSchema(
    CartDiscountUpdateActionSchema
):
    requires_discount_code = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="requiresDiscountCode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountChangeRequiresDiscountCodeAction(**data)


class CartDiscountChangeSortOrderActionSchema(CartDiscountUpdateActionSchema):
    sort_order = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="sortOrder"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountChangeSortOrderAction(**data)


class CartDiscountChangeStackingModeActionSchema(CartDiscountUpdateActionSchema):
    stacking_mode = marshmallow_enum.EnumField(
        StackingMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="stackingMode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountChangeStackingModeAction(**data)


class CartDiscountChangeTargetActionSchema(CartDiscountUpdateActionSchema):
    target = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "customLineItems": helpers.absmod(
                __name__, ".CartDiscountCustomLineItemsTargetSchema"
            ),
            "lineItems": helpers.absmod(__name__, ".CartDiscountLineItemsTargetSchema"),
            "shipping": helpers.absmod(
                __name__, ".CartDiscountShippingCostTargetSchema"
            ),
            "multiBuyCustomLineItems": helpers.absmod(
                __name__, ".MultiBuyCustomLineItemsTargetSchema"
            ),
            "multiBuyLineItems": helpers.absmod(
                __name__, ".MultiBuyLineItemsTargetSchema"
            ),
        },
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountChangeTargetAction(**data)


class CartDiscountChangeValueActionSchema(CartDiscountUpdateActionSchema):
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "absolute": helpers.absmod(
                __name__, ".CartDiscountValueAbsoluteDraftSchema"
            ),
            "giftLineItem": helpers.absmod(
                __name__, ".CartDiscountValueGiftLineItemDraftSchema"
            ),
            "relative": helpers.absmod(
                __name__, ".CartDiscountValueRelativeDraftSchema"
            ),
        },
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountChangeValueAction(**data)


class CartDiscountSetCustomFieldActionSchema(CartDiscountUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountSetCustomFieldAction(**data)


class CartDiscountSetCustomTypeActionSchema(CartDiscountUpdateActionSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountSetCustomTypeAction(**data)


class CartDiscountSetDescriptionActionSchema(CartDiscountUpdateActionSchema):
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountSetDescriptionAction(**data)


class CartDiscountSetKeyActionSchema(CartDiscountUpdateActionSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountSetKeyAction(**data)


class CartDiscountSetValidFromActionSchema(CartDiscountUpdateActionSchema):
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountSetValidFromAction(**data)


class CartDiscountSetValidFromAndUntilActionSchema(CartDiscountUpdateActionSchema):
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountSetValidFromAndUntilAction(**data)


class CartDiscountSetValidUntilActionSchema(CartDiscountUpdateActionSchema):
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CartDiscountSetValidUntilAction(**data)

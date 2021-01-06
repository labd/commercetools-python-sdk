# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..cart import DiscountCodeState, ProductPublishScope
from ..order import OrderState, PaymentState, ReturnShipmentState, ShipmentState
from ..payment import TransactionState
from .common import BaseResourceSchema, LocalizedStringField

# Fields


# Marshmallow Schemas
class MessageSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="createdBy",
    )
    sequence_number = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="sequenceNumber"
    )
    resource = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("typeId", "type_id"),
        discriminator_schemas={
            "cart-discount": helpers.absmod(
                __name__, ".cart_discount.CartDiscountReferenceSchema"
            ),
            "cart": helpers.absmod(__name__, ".cart.CartReferenceSchema"),
            "category": helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
            "channel": helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
            "key-value-document": helpers.absmod(
                __name__, ".custom_object.CustomObjectReferenceSchema"
            ),
            "customer-group": helpers.absmod(
                __name__, ".customer_group.CustomerGroupReferenceSchema"
            ),
            "customer": helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
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
        missing=None,
    )
    resource_version = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="resourceVersion"
    )
    type = marshmallow.fields.String(allow_none=True, missing=None)
    resource_user_provided_identifiers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".UserProvidedIdentifiersSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="resourceUserProvidedIdentifiers",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.Message(**data)


class CategoryCreatedMessageSchema(MessageSchema):
    category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".category.CategorySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CategoryCreatedMessage(**data)


class CategorySlugChangedMessageSchema(MessageSchema):
    slug = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CategorySlugChangedMessage(**data)


class CustomLineItemStateTransitionMessageSchema(MessageSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    transition_date = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="transitionDate"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    from_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="fromState",
    )
    to_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="toState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomLineItemStateTransitionMessage(**data)


class CustomerAddressAddedMessageSchema(MessageSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerAddressAddedMessage(**data)


class CustomerAddressChangedMessageSchema(MessageSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerAddressChangedMessage(**data)


class CustomerAddressRemovedMessageSchema(MessageSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerAddressRemovedMessage(**data)


class CustomerCompanyNameSetMessageSchema(MessageSchema):
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerCompanyNameSetMessage(**data)


class CustomerCreatedMessageSchema(MessageSchema):
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerCreatedMessage(**data)


class CustomerDateOfBirthSetMessageSchema(MessageSchema):
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerDateOfBirthSetMessage(**data)


class CustomerEmailChangedMessageSchema(MessageSchema):
    email = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerEmailChangedMessage(**data)


class CustomerEmailVerifiedMessageSchema(MessageSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerEmailVerifiedMessage(**data)


class CustomerGroupSetMessageSchema(MessageSchema):
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerGroupSetMessage(**data)


class DeliveryAddedMessageSchema(MessageSchema):
    delivery = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliverySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DeliveryAddedMessage(**data)


class DeliveryAddressSetMessageSchema(MessageSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    old_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldAddress",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DeliveryAddressSetMessage(**data)


class DeliveryItemsUpdatedMessageSchema(MessageSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    old_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="oldItems",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DeliveryItemsUpdatedMessage(**data)


class DeliveryRemovedMessageSchema(MessageSchema):
    delivery = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliverySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DeliveryRemovedMessage(**data)


class InventoryEntryCreatedMessageSchema(MessageSchema):
    inventory_entry = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".inventory.InventoryEntrySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="inventoryEntry",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.InventoryEntryCreatedMessage(**data)


class InventoryEntryDeletedMessageSchema(MessageSchema):
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="supplyChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.InventoryEntryDeletedMessage(**data)


class InventoryEntryQuantitySetMessageSchema(MessageSchema):
    old_quantity_on_stock = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="oldQuantityOnStock"
    )
    new_quantity_on_stock = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="newQuantityOnStock"
    )
    old_available_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="oldAvailableQuantity"
    )
    new_available_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="newAvailableQuantity"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.InventoryEntryQuantitySetMessage(**data)


class LineItemStateTransitionMessageSchema(MessageSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    transition_date = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="transitionDate"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    from_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="fromState",
    )
    to_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="toState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.LineItemStateTransitionMessage(**data)


class MessageConfigurationSchema(helpers.BaseSchema):
    enabled = marshmallow.fields.Boolean(allow_none=True, missing=None)
    delete_days_after_creation = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="deleteDaysAfterCreation",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MessageConfiguration(**data)


class MessageConfigurationDraftSchema(helpers.BaseSchema):
    enabled = marshmallow.fields.Boolean(allow_none=True, missing=None)
    delete_days_after_creation = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterCreation"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MessageConfigurationDraft(**data)


class MessagePagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "CategoryCreated": helpers.absmod(
                    __name__, ".CategoryCreatedMessageSchema"
                ),
                "CategorySlugChanged": helpers.absmod(
                    __name__, ".CategorySlugChangedMessageSchema"
                ),
                "CustomLineItemStateTransition": helpers.absmod(
                    __name__, ".CustomLineItemStateTransitionMessageSchema"
                ),
                "CustomerAddressAdded": helpers.absmod(
                    __name__, ".CustomerAddressAddedMessageSchema"
                ),
                "CustomerAddressChanged": helpers.absmod(
                    __name__, ".CustomerAddressChangedMessageSchema"
                ),
                "CustomerAddressRemoved": helpers.absmod(
                    __name__, ".CustomerAddressRemovedMessageSchema"
                ),
                "CustomerCompanyNameSet": helpers.absmod(
                    __name__, ".CustomerCompanyNameSetMessageSchema"
                ),
                "CustomerCreated": helpers.absmod(
                    __name__, ".CustomerCreatedMessageSchema"
                ),
                "CustomerDateOfBirthSet": helpers.absmod(
                    __name__, ".CustomerDateOfBirthSetMessageSchema"
                ),
                "CustomerEmailChanged": helpers.absmod(
                    __name__, ".CustomerEmailChangedMessageSchema"
                ),
                "CustomerEmailVerified": helpers.absmod(
                    __name__, ".CustomerEmailVerifiedMessageSchema"
                ),
                "CustomerGroupSet": helpers.absmod(
                    __name__, ".CustomerGroupSetMessageSchema"
                ),
                "DeliveryAdded": helpers.absmod(
                    __name__, ".DeliveryAddedMessageSchema"
                ),
                "DeliveryAddressSet": helpers.absmod(
                    __name__, ".DeliveryAddressSetMessageSchema"
                ),
                "DeliveryItemsUpdated": helpers.absmod(
                    __name__, ".DeliveryItemsUpdatedMessageSchema"
                ),
                "DeliveryRemoved": helpers.absmod(
                    __name__, ".DeliveryRemovedMessageSchema"
                ),
                "InventoryEntryCreated": helpers.absmod(
                    __name__, ".InventoryEntryCreatedMessageSchema"
                ),
                "InventoryEntryDeleted": helpers.absmod(
                    __name__, ".InventoryEntryDeletedMessageSchema"
                ),
                "InventoryEntryQuantitySet": helpers.absmod(
                    __name__, ".InventoryEntryQuantitySetMessageSchema"
                ),
                "LineItemStateTransition": helpers.absmod(
                    __name__, ".LineItemStateTransitionMessageSchema"
                ),
                "OrderBillingAddressSet": helpers.absmod(
                    __name__, ".OrderBillingAddressSetMessageSchema"
                ),
                "OrderCreated": helpers.absmod(__name__, ".OrderCreatedMessageSchema"),
                "OrderCustomLineItemDiscountSet": helpers.absmod(
                    __name__, ".OrderCustomLineItemDiscountSetMessageSchema"
                ),
                "OrderCustomerEmailSet": helpers.absmod(
                    __name__, ".OrderCustomerEmailSetMessageSchema"
                ),
                "OrderCustomerGroupSet": helpers.absmod(
                    __name__, ".OrderCustomerGroupSetMessageSchema"
                ),
                "OrderCustomerSet": helpers.absmod(
                    __name__, ".OrderCustomerSetMessageSchema"
                ),
                "OrderDeleted": helpers.absmod(__name__, ".OrderDeletedMessageSchema"),
                "OrderDiscountCodeAdded": helpers.absmod(
                    __name__, ".OrderDiscountCodeAddedMessageSchema"
                ),
                "OrderDiscountCodeRemoved": helpers.absmod(
                    __name__, ".OrderDiscountCodeRemovedMessageSchema"
                ),
                "OrderDiscountCodeStateSet": helpers.absmod(
                    __name__, ".OrderDiscountCodeStateSetMessageSchema"
                ),
                "OrderEditApplied": helpers.absmod(
                    __name__, ".OrderEditAppliedMessageSchema"
                ),
                "OrderImported": helpers.absmod(
                    __name__, ".OrderImportedMessageSchema"
                ),
                "OrderLineItemAdded": helpers.absmod(
                    __name__, ".OrderLineItemAddedMessageSchema"
                ),
                "OrderLineItemDiscountSet": helpers.absmod(
                    __name__, ".OrderLineItemDiscountSetMessageSchema"
                ),
                "OrderPaymentStateChanged": helpers.absmod(
                    __name__, ".OrderPaymentStateChangedMessageSchema"
                ),
                "ReturnInfoAdded": helpers.absmod(
                    __name__, ".OrderReturnInfoAddedMessageSchema"
                ),
                "OrderReturnShipmentStateChanged": helpers.absmod(
                    __name__, ".OrderReturnShipmentStateChangedMessageSchema"
                ),
                "OrderShipmentStateChanged": helpers.absmod(
                    __name__, ".OrderShipmentStateChangedMessageSchema"
                ),
                "OrderShippingAddressSet": helpers.absmod(
                    __name__, ".OrderShippingAddressSetMessageSchema"
                ),
                "OrderShippingInfoSet": helpers.absmod(
                    __name__, ".OrderShippingInfoSetMessageSchema"
                ),
                "OrderShippingRateInputSet": helpers.absmod(
                    __name__, ".OrderShippingRateInputSetMessageSchema"
                ),
                "OrderStateChanged": helpers.absmod(
                    __name__, ".OrderStateChangedMessageSchema"
                ),
                "OrderStateTransition": helpers.absmod(
                    __name__, ".OrderStateTransitionMessageSchema"
                ),
                "OrderStoreSet": helpers.absmod(
                    __name__, ".OrderStoreSetMessageSchema"
                ),
                "ParcelAddedToDelivery": helpers.absmod(
                    __name__, ".ParcelAddedToDeliveryMessageSchema"
                ),
                "ParcelItemsUpdated": helpers.absmod(
                    __name__, ".ParcelItemsUpdatedMessageSchema"
                ),
                "ParcelMeasurementsUpdated": helpers.absmod(
                    __name__, ".ParcelMeasurementsUpdatedMessageSchema"
                ),
                "ParcelRemovedFromDelivery": helpers.absmod(
                    __name__, ".ParcelRemovedFromDeliveryMessageSchema"
                ),
                "ParcelTrackingDataUpdated": helpers.absmod(
                    __name__, ".ParcelTrackingDataUpdatedMessageSchema"
                ),
                "PaymentCreated": helpers.absmod(
                    __name__, ".PaymentCreatedMessageSchema"
                ),
                "PaymentInteractionAdded": helpers.absmod(
                    __name__, ".PaymentInteractionAddedMessageSchema"
                ),
                "PaymentStatusInterfaceCodeSet": helpers.absmod(
                    __name__, ".PaymentStatusInterfaceCodeSetMessageSchema"
                ),
                "PaymentStatusStateTransition": helpers.absmod(
                    __name__, ".PaymentStatusStateTransitionMessageSchema"
                ),
                "PaymentTransactionAdded": helpers.absmod(
                    __name__, ".PaymentTransactionAddedMessageSchema"
                ),
                "PaymentTransactionStateChanged": helpers.absmod(
                    __name__, ".PaymentTransactionStateChangedMessageSchema"
                ),
                "ProductAddedToCategory": helpers.absmod(
                    __name__, ".ProductAddedToCategoryMessageSchema"
                ),
                "ProductCreated": helpers.absmod(
                    __name__, ".ProductCreatedMessageSchema"
                ),
                "ProductDeleted": helpers.absmod(
                    __name__, ".ProductDeletedMessageSchema"
                ),
                "ProductImageAdded": helpers.absmod(
                    __name__, ".ProductImageAddedMessageSchema"
                ),
                "ProductPriceDiscountsSet": helpers.absmod(
                    __name__, ".ProductPriceDiscountsSetMessageSchema"
                ),
                "ProductPriceExternalDiscountSet": helpers.absmod(
                    __name__, ".ProductPriceExternalDiscountSetMessageSchema"
                ),
                "ProductPublished": helpers.absmod(
                    __name__, ".ProductPublishedMessageSchema"
                ),
                "ProductRemovedFromCategory": helpers.absmod(
                    __name__, ".ProductRemovedFromCategoryMessageSchema"
                ),
                "ProductRevertedStagedChanges": helpers.absmod(
                    __name__, ".ProductRevertedStagedChangesMessageSchema"
                ),
                "ProductSlugChanged": helpers.absmod(
                    __name__, ".ProductSlugChangedMessageSchema"
                ),
                "ProductStateTransition": helpers.absmod(
                    __name__, ".ProductStateTransitionMessageSchema"
                ),
                "ProductUnpublished": helpers.absmod(
                    __name__, ".ProductUnpublishedMessageSchema"
                ),
                "ProductVariantAdded": helpers.absmod(
                    __name__, ".ProductVariantAddedMessageSchema"
                ),
                "ProductVariantDeleted": helpers.absmod(
                    __name__, ".ProductVariantDeletedMessageSchema"
                ),
                "ReviewCreated": helpers.absmod(
                    __name__, ".ReviewCreatedMessageSchema"
                ),
                "ReviewRatingSet": helpers.absmod(
                    __name__, ".ReviewRatingSetMessageSchema"
                ),
                "ReviewStateTransition": helpers.absmod(
                    __name__, ".ReviewStateTransitionMessageSchema"
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

        return models.MessagePagedQueryResponse(**data)


class OrderBillingAddressSetMessageSchema(MessageSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    old_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldAddress",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderBillingAddressSetMessage(**data)


class OrderCreatedMessageSchema(MessageSchema):
    order = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.OrderSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderCreatedMessage(**data)


class OrderCustomLineItemDiscountSetMessageSchema(MessageSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    discounted_price_per_quantity = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".cart.DiscountedLineItemPriceForQuantitySchema"
        ),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountedPricePerQuantity",
    )
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.TaxedItemPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxedPrice",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderCustomLineItemDiscountSetMessage(**data)


class OrderCustomerEmailSetMessageSchema(MessageSchema):
    email = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    old_email = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldEmail",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderCustomerEmailSetMessage(**data)


class OrderCustomerGroupSetMessageSchema(MessageSchema):
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customerGroup",
    )
    old_customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldCustomerGroup",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderCustomerGroupSetMessage(**data)


class OrderCustomerSetMessageSchema(MessageSchema):
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customerGroup",
    )
    old_customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldCustomer",
    )
    old_customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldCustomerGroup",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderCustomerSetMessage(**data)


class OrderDeletedMessageSchema(MessageSchema):
    order = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.OrderSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderDeletedMessage(**data)


class OrderDiscountCodeAddedMessageSchema(MessageSchema):
    discount_code = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".discount_code.DiscountCodeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountCode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderDiscountCodeAddedMessage(**data)


class OrderDiscountCodeRemovedMessageSchema(MessageSchema):
    discount_code = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".discount_code.DiscountCodeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountCode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderDiscountCodeRemovedMessage(**data)


class OrderDiscountCodeStateSetMessageSchema(MessageSchema):
    discount_code = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".discount_code.DiscountCodeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountCode",
    )
    state = marshmallow_enum.EnumField(
        DiscountCodeState, by_value=True, allow_none=True, missing=None
    )
    old_state = marshmallow_enum.EnumField(
        DiscountCodeState,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderDiscountCodeStateSetMessage(**data)


class OrderEditAppliedMessageSchema(MessageSchema):
    edit = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order_edit.OrderEditReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    result = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order_edit.OrderEditAppliedSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderEditAppliedMessage(**data)


class OrderImportedMessageSchema(MessageSchema):
    order = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.OrderSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderImportedMessage(**data)


class OrderLineItemAddedMessageSchema(MessageSchema):
    line_item = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.LineItemSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lineItem",
    )
    added_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="addedQuantity"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderLineItemAddedMessage(**data)


class OrderLineItemDiscountSetMessageSchema(MessageSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    discounted_price_per_quantity = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".cart.DiscountedLineItemPriceForQuantitySchema"
        ),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountedPricePerQuantity",
    )
    total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="totalPrice",
    )
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.TaxedItemPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxedPrice",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderLineItemDiscountSetMessage(**data)


class OrderPaymentStateChangedMessageSchema(MessageSchema):
    payment_state = marshmallow_enum.EnumField(
        PaymentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="paymentState",
    )
    old_payment_state = marshmallow_enum.EnumField(
        PaymentState,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldPaymentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderPaymentStateChangedMessage(**data)


class OrderReturnInfoAddedMessageSchema(MessageSchema):
    return_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ReturnInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="returnInfo",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderReturnInfoAddedMessage(**data)


class OrderReturnShipmentStateChangedMessageSchema(MessageSchema):
    return_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="returnItemId"
    )
    return_shipment_state = marshmallow_enum.EnumField(
        ReturnShipmentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="returnShipmentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderReturnShipmentStateChangedMessage(**data)


class OrderShipmentStateChangedMessageSchema(MessageSchema):
    shipment_state = marshmallow_enum.EnumField(
        ShipmentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="shipmentState",
    )
    old_shipment_state = marshmallow_enum.EnumField(
        ShipmentState,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldShipmentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderShipmentStateChangedMessage(**data)


class OrderShippingAddressSetMessageSchema(MessageSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    old_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldAddress",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderShippingAddressSetMessage(**data)


class OrderShippingInfoSetMessageSchema(MessageSchema):
    shipping_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ShippingInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingInfo",
    )
    old_shipping_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ShippingInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldShippingInfo",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderShippingInfoSetMessage(**data)


class OrderShippingRateInputSetMessageSchema(MessageSchema):
    shipping_rate_input = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Classification": helpers.absmod(
                __name__, ".cart.ClassificationShippingRateInputSchema"
            ),
            "Score": helpers.absmod(__name__, ".cart.ScoreShippingRateInputSchema"),
        },
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingRateInput",
    )
    old_shipping_rate_input = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Classification": helpers.absmod(
                __name__, ".cart.ClassificationShippingRateInputSchema"
            ),
            "Score": helpers.absmod(__name__, ".cart.ScoreShippingRateInputSchema"),
        },
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldShippingRateInput",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderShippingRateInputSetMessage(**data)


class OrderStateChangedMessageSchema(MessageSchema):
    order_state = marshmallow_enum.EnumField(
        OrderState, by_value=True, allow_none=True, missing=None, data_key="orderState"
    )
    old_order_state = marshmallow_enum.EnumField(
        OrderState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="oldOrderState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderStateChangedMessage(**data)


class OrderStateTransitionMessageSchema(MessageSchema):
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    force = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderStateTransitionMessage(**data)


class OrderStoreSetMessageSchema(MessageSchema):
    store = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderStoreSetMessage(**data)


class ParcelAddedToDeliveryMessageSchema(MessageSchema):
    delivery = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliverySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    parcel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ParcelSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ParcelAddedToDeliveryMessage(**data)


class ParcelItemsUpdatedMessageSchema(MessageSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    delivery_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="deliveryId",
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    old_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="oldItems",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ParcelItemsUpdatedMessage(**data)


class ParcelMeasurementsUpdatedMessageSchema(MessageSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    measurements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ParcelMeasurementsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ParcelMeasurementsUpdatedMessage(**data)


class ParcelRemovedFromDeliveryMessageSchema(MessageSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    parcel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ParcelSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ParcelRemovedFromDeliveryMessage(**data)


class ParcelTrackingDataUpdatedMessageSchema(MessageSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    tracking_data = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.TrackingDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="trackingData",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ParcelTrackingDataUpdatedMessage(**data)


class PaymentCreatedMessageSchema(MessageSchema):
    payment = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.PaymentSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PaymentCreatedMessage(**data)


class PaymentInteractionAddedMessageSchema(MessageSchema):
    interaction = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PaymentInteractionAddedMessage(**data)


class PaymentStatusInterfaceCodeSetMessageSchema(MessageSchema):
    payment_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="paymentId"
    )
    interface_code = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interfaceCode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PaymentStatusInterfaceCodeSetMessage(**data)


class PaymentStatusStateTransitionMessageSchema(MessageSchema):
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    force = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PaymentStatusStateTransitionMessage(**data)


class PaymentTransactionAddedMessageSchema(MessageSchema):
    transaction = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.TransactionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PaymentTransactionAddedMessage(**data)


class PaymentTransactionStateChangedMessageSchema(MessageSchema):
    transaction_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="transactionId"
    )
    state = marshmallow_enum.EnumField(
        TransactionState, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PaymentTransactionStateChangedMessage(**data)


class ProductAddedToCategoryMessageSchema(MessageSchema):
    category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductAddedToCategoryMessage(**data)


class ProductCreatedMessageSchema(MessageSchema):
    product_projection = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductProjectionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productProjection",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductCreatedMessage(**data)


class ProductDeletedMessageSchema(MessageSchema):
    removed_image_urls = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="removedImageUrls",
    )
    current_projection = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductProjectionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="currentProjection",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductDeletedMessage(**data)


class ProductImageAddedMessageSchema(MessageSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    image = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ImageSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductImageAddedMessage(**data)


class ProductPriceDiscountsSetMessageSchema(MessageSchema):
    updated_prices = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductPriceDiscountsSetUpdatedPriceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="updatedPrices",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductPriceDiscountsSetMessage(**data)


class ProductPriceDiscountsSetUpdatedPriceSchema(helpers.BaseSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    variant_key = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantKey",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    price_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="priceId"
    )
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.DiscountedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductPriceDiscountsSetUpdatedPrice(**data)


class ProductPriceExternalDiscountSetMessageSchema(MessageSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    variant_key = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantKey",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    price_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="priceId"
    )
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.DiscountedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductPriceExternalDiscountSetMessage(**data)


class ProductPublishedMessageSchema(MessageSchema):
    removed_image_urls = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="removedImageUrls",
    )
    product_projection = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductProjectionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productProjection",
    )
    scope = marshmallow_enum.EnumField(
        ProductPublishScope, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductPublishedMessage(**data)


class ProductRemovedFromCategoryMessageSchema(MessageSchema):
    category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductRemovedFromCategoryMessage(**data)


class ProductRevertedStagedChangesMessageSchema(MessageSchema):
    removed_image_urls = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="removedImageUrls",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductRevertedStagedChangesMessage(**data)


class ProductSlugChangedMessageSchema(MessageSchema):
    slug = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductSlugChangedMessage(**data)


class ProductStateTransitionMessageSchema(MessageSchema):
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    force = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductStateTransitionMessage(**data)


class ProductUnpublishedMessageSchema(MessageSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductUnpublishedMessage(**data)


class ProductVariantAddedMessageSchema(MessageSchema):
    variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductVariantSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductVariantAddedMessage(**data)


class ProductVariantDeletedMessageSchema(MessageSchema):
    variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductVariantSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    removed_image_urls = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="removedImageUrls",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductVariantDeletedMessage(**data)


class ReviewCreatedMessageSchema(MessageSchema):
    review = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".review.ReviewSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ReviewCreatedMessage(**data)


class ReviewRatingSetMessageSchema(MessageSchema):
    old_rating = marshmallow.fields.Float(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldRating",
    )
    new_rating = marshmallow.fields.Float(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="newRating",
    )
    included_in_statistics = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="includedInStatistics"
    )
    target = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("typeId", "type_id"),
        discriminator_schemas={
            "cart-discount": helpers.absmod(
                __name__, ".cart_discount.CartDiscountReferenceSchema"
            ),
            "cart": helpers.absmod(__name__, ".cart.CartReferenceSchema"),
            "category": helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
            "channel": helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
            "key-value-document": helpers.absmod(
                __name__, ".custom_object.CustomObjectReferenceSchema"
            ),
            "customer-group": helpers.absmod(
                __name__, ".customer_group.CustomerGroupReferenceSchema"
            ),
            "customer": helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
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
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ReviewRatingSetMessage(**data)


class ReviewStateTransitionMessageSchema(MessageSchema):
    old_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="oldState",
    )
    new_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="newState",
    )
    old_included_in_statistics = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="oldIncludedInStatistics"
    )
    new_included_in_statistics = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="newIncludedInStatistics"
    )
    target = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("typeId", "type_id"),
        discriminator_schemas={
            "cart-discount": helpers.absmod(
                __name__, ".cart_discount.CartDiscountReferenceSchema"
            ),
            "cart": helpers.absmod(__name__, ".cart.CartReferenceSchema"),
            "category": helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
            "channel": helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
            "key-value-document": helpers.absmod(
                __name__, ".custom_object.CustomObjectReferenceSchema"
            ),
            "customer-group": helpers.absmod(
                __name__, ".customer_group.CustomerGroupReferenceSchema"
            ),
            "customer": helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
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
        missing=None,
    )
    force = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ReviewStateTransitionMessage(**data)


class UserProvidedIdentifiersSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    external_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalId",
    )
    order_number = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="orderNumber",
    )
    customer_number = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customerNumber",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    slug = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.UserProvidedIdentifiers(**data)


class MessagePayloadSchema(helpers.BaseSchema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.MessagePayload(**data)


class CategoryCreatedMessagePayloadSchema(MessagePayloadSchema):
    category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".category.CategorySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CategoryCreatedMessagePayload(**data)


class CategorySlugChangedMessagePayloadSchema(MessagePayloadSchema):
    slug = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CategorySlugChangedMessagePayload(**data)


class CustomLineItemStateTransitionMessagePayloadSchema(MessagePayloadSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    transition_date = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="transitionDate"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    from_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="fromState",
    )
    to_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="toState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomLineItemStateTransitionMessagePayload(**data)


class CustomerAddressAddedMessagePayloadSchema(MessagePayloadSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerAddressAddedMessagePayload(**data)


class CustomerAddressChangedMessagePayloadSchema(MessagePayloadSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerAddressChangedMessagePayload(**data)


class CustomerAddressRemovedMessagePayloadSchema(MessagePayloadSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerAddressRemovedMessagePayload(**data)


class CustomerCompanyNameSetMessagePayloadSchema(MessagePayloadSchema):
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerCompanyNameSetMessagePayload(**data)


class CustomerCreatedMessagePayloadSchema(MessagePayloadSchema):
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerCreatedMessagePayload(**data)


class CustomerDateOfBirthSetMessagePayloadSchema(MessagePayloadSchema):
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerDateOfBirthSetMessagePayload(**data)


class CustomerEmailChangedMessagePayloadSchema(MessagePayloadSchema):
    email = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerEmailChangedMessagePayload(**data)


class CustomerEmailVerifiedMessagePayloadSchema(MessagePayloadSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerEmailVerifiedMessagePayload(**data)


class CustomerGroupSetMessagePayloadSchema(MessagePayloadSchema):
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomerGroupSetMessagePayload(**data)


class DeliveryAddedMessagePayloadSchema(MessagePayloadSchema):
    delivery = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliverySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DeliveryAddedMessagePayload(**data)


class DeliveryAddressSetMessagePayloadSchema(MessagePayloadSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    old_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldAddress",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DeliveryAddressSetMessagePayload(**data)


class DeliveryItemsUpdatedMessagePayloadSchema(MessagePayloadSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    old_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="oldItems",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DeliveryItemsUpdatedMessagePayload(**data)


class DeliveryRemovedMessagePayloadSchema(MessagePayloadSchema):
    delivery = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliverySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DeliveryRemovedMessagePayload(**data)


class InventoryEntryCreatedMessagePayloadSchema(MessagePayloadSchema):
    inventory_entry = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".inventory.InventoryEntrySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="inventoryEntry",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.InventoryEntryCreatedMessagePayload(**data)


class InventoryEntryDeletedMessagePayloadSchema(MessagePayloadSchema):
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    supply_channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="supplyChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.InventoryEntryDeletedMessagePayload(**data)


class InventoryEntryQuantitySetMessagePayloadSchema(MessagePayloadSchema):
    old_quantity_on_stock = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="oldQuantityOnStock"
    )
    new_quantity_on_stock = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="newQuantityOnStock"
    )
    old_available_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="oldAvailableQuantity"
    )
    new_available_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="newAvailableQuantity"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.InventoryEntryQuantitySetMessagePayload(**data)


class LineItemStateTransitionMessagePayloadSchema(MessagePayloadSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    transition_date = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="transitionDate"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    from_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="fromState",
    )
    to_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="toState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.LineItemStateTransitionMessagePayload(**data)


class OrderBillingAddressSetMessagePayloadSchema(MessagePayloadSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    old_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldAddress",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderBillingAddressSetMessagePayload(**data)


class OrderCreatedMessagePayloadSchema(MessagePayloadSchema):
    order = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.OrderSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderCreatedMessagePayload(**data)


class OrderCustomLineItemDiscountSetMessagePayloadSchema(MessagePayloadSchema):
    custom_line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customLineItemId"
    )
    discounted_price_per_quantity = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".cart.DiscountedLineItemPriceForQuantitySchema"
        ),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountedPricePerQuantity",
    )
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.TaxedItemPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxedPrice",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderCustomLineItemDiscountSetMessagePayload(**data)


class OrderCustomerEmailSetMessagePayloadSchema(MessagePayloadSchema):
    email = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    old_email = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldEmail",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderCustomerEmailSetMessagePayload(**data)


class OrderCustomerGroupSetMessagePayloadSchema(MessagePayloadSchema):
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customerGroup",
    )
    old_customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldCustomerGroup",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderCustomerGroupSetMessagePayload(**data)


class OrderCustomerSetMessagePayloadSchema(MessagePayloadSchema):
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customerGroup",
    )
    old_customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldCustomer",
    )
    old_customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldCustomerGroup",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderCustomerSetMessagePayload(**data)


class OrderDeletedMessagePayloadSchema(MessagePayloadSchema):
    order = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.OrderSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderDeletedMessagePayload(**data)


class OrderDiscountCodeAddedMessagePayloadSchema(MessagePayloadSchema):
    discount_code = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".discount_code.DiscountCodeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountCode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderDiscountCodeAddedMessagePayload(**data)


class OrderDiscountCodeRemovedMessagePayloadSchema(MessagePayloadSchema):
    discount_code = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".discount_code.DiscountCodeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountCode",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderDiscountCodeRemovedMessagePayload(**data)


class OrderDiscountCodeStateSetMessagePayloadSchema(MessagePayloadSchema):
    discount_code = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".discount_code.DiscountCodeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountCode",
    )
    state = marshmallow_enum.EnumField(
        DiscountCodeState, by_value=True, allow_none=True, missing=None
    )
    old_state = marshmallow_enum.EnumField(
        DiscountCodeState,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderDiscountCodeStateSetMessagePayload(**data)


class OrderEditAppliedMessagePayloadSchema(MessagePayloadSchema):
    edit = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order_edit.OrderEditReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    result = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order_edit.OrderEditAppliedSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderEditAppliedMessagePayload(**data)


class OrderImportedMessagePayloadSchema(MessagePayloadSchema):
    order = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.OrderSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderImportedMessagePayload(**data)


class OrderLineItemAddedMessagePayloadSchema(MessagePayloadSchema):
    line_item = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.LineItemSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lineItem",
    )
    added_quantity = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="addedQuantity"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderLineItemAddedMessagePayload(**data)


class OrderLineItemDiscountSetMessagePayloadSchema(MessagePayloadSchema):
    line_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lineItemId"
    )
    discounted_price_per_quantity = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".cart.DiscountedLineItemPriceForQuantitySchema"
        ),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="discountedPricePerQuantity",
    )
    total_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="totalPrice",
    )
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.TaxedItemPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxedPrice",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderLineItemDiscountSetMessagePayload(**data)


class OrderPaymentStateChangedMessagePayloadSchema(MessagePayloadSchema):
    payment_state = marshmallow_enum.EnumField(
        PaymentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="paymentState",
    )
    old_payment_state = marshmallow_enum.EnumField(
        PaymentState,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldPaymentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderPaymentStateChangedMessagePayload(**data)


class OrderReturnInfoAddedMessagePayloadSchema(MessagePayloadSchema):
    return_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ReturnInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="returnInfo",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderReturnInfoAddedMessagePayload(**data)


class OrderReturnShipmentStateChangedMessagePayloadSchema(MessagePayloadSchema):
    return_item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="returnItemId"
    )
    return_shipment_state = marshmallow_enum.EnumField(
        ReturnShipmentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="returnShipmentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderReturnShipmentStateChangedMessagePayload(**data)


class OrderShipmentStateChangedMessagePayloadSchema(MessagePayloadSchema):
    shipment_state = marshmallow_enum.EnumField(
        ShipmentState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="shipmentState",
    )
    old_shipment_state = marshmallow_enum.EnumField(
        ShipmentState,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldShipmentState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderShipmentStateChangedMessagePayload(**data)


class OrderShippingAddressSetMessagePayloadSchema(MessagePayloadSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    old_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldAddress",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderShippingAddressSetMessagePayload(**data)


class OrderShippingInfoSetMessagePayloadSchema(MessagePayloadSchema):
    shipping_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ShippingInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingInfo",
    )
    old_shipping_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ShippingInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldShippingInfo",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderShippingInfoSetMessagePayload(**data)


class OrderShippingRateInputSetMessagePayloadSchema(MessagePayloadSchema):
    shipping_rate_input = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Classification": helpers.absmod(
                __name__, ".cart.ClassificationShippingRateInputSchema"
            ),
            "Score": helpers.absmod(__name__, ".cart.ScoreShippingRateInputSchema"),
        },
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingRateInput",
    )
    old_shipping_rate_input = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Classification": helpers.absmod(
                __name__, ".cart.ClassificationShippingRateInputSchema"
            ),
            "Score": helpers.absmod(__name__, ".cart.ScoreShippingRateInputSchema"),
        },
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldShippingRateInput",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderShippingRateInputSetMessagePayload(**data)


class OrderStateChangedMessagePayloadSchema(MessagePayloadSchema):
    order_state = marshmallow_enum.EnumField(
        OrderState, by_value=True, allow_none=True, missing=None, data_key="orderState"
    )
    old_order_state = marshmallow_enum.EnumField(
        OrderState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="oldOrderState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderStateChangedMessagePayload(**data)


class OrderStateTransitionMessagePayloadSchema(MessagePayloadSchema):
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    force = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderStateTransitionMessagePayload(**data)


class OrderStoreSetMessagePayloadSchema(MessagePayloadSchema):
    store = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.OrderStoreSetMessagePayload(**data)


class ParcelAddedToDeliveryMessagePayloadSchema(MessagePayloadSchema):
    delivery = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliverySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    parcel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ParcelSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ParcelAddedToDeliveryMessagePayload(**data)


class ParcelItemsUpdatedMessagePayloadSchema(MessagePayloadSchema):
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    delivery_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="deliveryId",
    )
    items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    old_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.DeliveryItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="oldItems",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ParcelItemsUpdatedMessagePayload(**data)


class ParcelMeasurementsUpdatedMessagePayloadSchema(MessagePayloadSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    measurements = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ParcelMeasurementsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ParcelMeasurementsUpdatedMessagePayload(**data)


class ParcelRemovedFromDeliveryMessagePayloadSchema(MessagePayloadSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    parcel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.ParcelSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ParcelRemovedFromDeliveryMessagePayload(**data)


class ParcelTrackingDataUpdatedMessagePayloadSchema(MessagePayloadSchema):
    delivery_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="deliveryId"
    )
    parcel_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="parcelId"
    )
    tracking_data = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.TrackingDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="trackingData",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ParcelTrackingDataUpdatedMessagePayload(**data)


class PaymentCreatedMessagePayloadSchema(MessagePayloadSchema):
    payment = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.PaymentSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PaymentCreatedMessagePayload(**data)


class PaymentInteractionAddedMessagePayloadSchema(MessagePayloadSchema):
    interaction = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PaymentInteractionAddedMessagePayload(**data)


class PaymentStatusInterfaceCodeSetMessagePayloadSchema(MessagePayloadSchema):
    payment_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="paymentId"
    )
    interface_code = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="interfaceCode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PaymentStatusInterfaceCodeSetMessagePayload(**data)


class PaymentStatusStateTransitionMessagePayloadSchema(MessagePayloadSchema):
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    force = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PaymentStatusStateTransitionMessagePayload(**data)


class PaymentTransactionAddedMessagePayloadSchema(MessagePayloadSchema):
    transaction = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".payment.TransactionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PaymentTransactionAddedMessagePayload(**data)


class PaymentTransactionStateChangedMessagePayloadSchema(MessagePayloadSchema):
    transaction_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="transactionId"
    )
    state = marshmallow_enum.EnumField(
        TransactionState, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PaymentTransactionStateChangedMessagePayload(**data)


class ProductAddedToCategoryMessagePayloadSchema(MessagePayloadSchema):
    category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductAddedToCategoryMessagePayload(**data)


class ProductCreatedMessagePayloadSchema(MessagePayloadSchema):
    product_projection = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductProjectionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productProjection",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductCreatedMessagePayload(**data)


class ProductDeletedMessagePayloadSchema(MessagePayloadSchema):
    removed_image_urls = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="removedImageUrls",
    )
    current_projection = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductProjectionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="currentProjection",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductDeletedMessagePayload(**data)


class ProductImageAddedMessagePayloadSchema(MessagePayloadSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    image = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ImageSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductImageAddedMessagePayload(**data)


class ProductPriceDiscountsSetMessagePayloadSchema(MessagePayloadSchema):
    updated_prices = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductPriceDiscountsSetUpdatedPriceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="updatedPrices",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductPriceDiscountsSetMessagePayload(**data)


class ProductPriceExternalDiscountSetMessagePayloadSchema(MessagePayloadSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    variant_key = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantKey",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    price_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="priceId"
    )
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.DiscountedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductPriceExternalDiscountSetMessagePayload(**data)


class ProductPublishedMessagePayloadSchema(MessagePayloadSchema):
    removed_image_urls = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="removedImageUrls",
    )
    product_projection = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductProjectionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productProjection",
    )
    scope = marshmallow_enum.EnumField(
        ProductPublishScope, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductPublishedMessagePayload(**data)


class ProductRemovedFromCategoryMessagePayloadSchema(MessagePayloadSchema):
    category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductRemovedFromCategoryMessagePayload(**data)


class ProductRevertedStagedChangesMessagePayloadSchema(MessagePayloadSchema):
    removed_image_urls = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="removedImageUrls",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductRevertedStagedChangesMessagePayload(**data)


class ProductSlugChangedMessagePayloadSchema(MessagePayloadSchema):
    slug = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductSlugChangedMessagePayload(**data)


class ProductStateTransitionMessagePayloadSchema(MessagePayloadSchema):
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    force = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductStateTransitionMessagePayload(**data)


class ProductUnpublishedMessagePayloadSchema(MessagePayloadSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductUnpublishedMessagePayload(**data)


class ProductVariantAddedMessagePayloadSchema(MessagePayloadSchema):
    variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductVariantSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductVariantAddedMessagePayload(**data)


class ProductVariantDeletedMessagePayloadSchema(MessagePayloadSchema):
    variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductVariantSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    removed_image_urls = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="removedImageUrls",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductVariantDeletedMessagePayload(**data)


class ReviewCreatedMessagePayloadSchema(MessagePayloadSchema):
    review = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".review.ReviewSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ReviewCreatedMessagePayload(**data)


class ReviewRatingSetMessagePayloadSchema(MessagePayloadSchema):
    old_rating = marshmallow.fields.Float(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="oldRating",
    )
    new_rating = marshmallow.fields.Float(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="newRating",
    )
    included_in_statistics = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="includedInStatistics"
    )
    target = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("typeId", "type_id"),
        discriminator_schemas={
            "cart-discount": helpers.absmod(
                __name__, ".cart_discount.CartDiscountReferenceSchema"
            ),
            "cart": helpers.absmod(__name__, ".cart.CartReferenceSchema"),
            "category": helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
            "channel": helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
            "key-value-document": helpers.absmod(
                __name__, ".custom_object.CustomObjectReferenceSchema"
            ),
            "customer-group": helpers.absmod(
                __name__, ".customer_group.CustomerGroupReferenceSchema"
            ),
            "customer": helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
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
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ReviewRatingSetMessagePayload(**data)


class ReviewStateTransitionMessagePayloadSchema(MessagePayloadSchema):
    old_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="oldState",
    )
    new_state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="newState",
    )
    old_included_in_statistics = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="oldIncludedInStatistics"
    )
    new_included_in_statistics = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="newIncludedInStatistics"
    )
    target = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("typeId", "type_id"),
        discriminator_schemas={
            "cart-discount": helpers.absmod(
                __name__, ".cart_discount.CartDiscountReferenceSchema"
            ),
            "cart": helpers.absmod(__name__, ".cart.CartReferenceSchema"),
            "category": helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
            "channel": helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
            "key-value-document": helpers.absmod(
                __name__, ".custom_object.CustomObjectReferenceSchema"
            ),
            "customer-group": helpers.absmod(
                __name__, ".customer_group.CustomerGroupReferenceSchema"
            ),
            "customer": helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
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
        missing=None,
    )
    force = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ReviewStateTransitionMessagePayload(**data)

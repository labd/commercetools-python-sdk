# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..extension import ExtensionAction, ExtensionResourceTypeId
from .common import BaseResourceSchema

# Fields


# Marshmallow Schemas
class ExtensionSchema(BaseResourceSchema):
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
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    destination = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "AWSLambda": helpers.absmod(
                __name__, ".ExtensionAWSLambdaDestinationSchema"
            ),
            "HTTP": helpers.absmod(__name__, ".ExtensionHttpDestinationSchema"),
        },
        missing=None,
    )
    triggers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExtensionTriggerSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    timeout_in_ms = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="timeoutInMs",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Extension(**data)


class ExtensionDestinationSchema(helpers.BaseSchema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ExtensionDestination(**data)


class ExtensionAWSLambdaDestinationSchema(ExtensionDestinationSchema):
    arn = marshmallow.fields.String(allow_none=True, missing=None)
    access_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="accessKey"
    )
    access_secret = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="accessSecret"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ExtensionAWSLambdaDestination(**data)


class ExtensionDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    destination = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "AWSLambda": helpers.absmod(
                __name__, ".ExtensionAWSLambdaDestinationSchema"
            ),
            "HTTP": helpers.absmod(__name__, ".ExtensionHttpDestinationSchema"),
        },
        missing=None,
    )
    triggers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExtensionTriggerSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    timeout_in_ms = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="timeoutInMs",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ExtensionDraft(**data)


class ExtensionHttpDestinationSchema(ExtensionDestinationSchema):
    url = marshmallow.fields.String(allow_none=True, missing=None)
    authentication = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "AuthorizationHeader": helpers.absmod(
                __name__, ".ExtensionAuthorizationHeaderAuthenticationSchema"
            ),
            "AzureFunctions": helpers.absmod(
                __name__, ".ExtensionAzureFunctionsAuthenticationSchema"
            ),
        },
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ExtensionHttpDestination(**data)


class ExtensionHttpDestinationAuthenticationSchema(helpers.BaseSchema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ExtensionHttpDestinationAuthentication(**data)


class ExtensionAuthorizationHeaderAuthenticationSchema(
    ExtensionHttpDestinationAuthenticationSchema
):
    header_value = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="headerValue"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ExtensionAuthorizationHeaderAuthentication(**data)


class ExtensionAzureFunctionsAuthenticationSchema(
    ExtensionHttpDestinationAuthenticationSchema
):
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ExtensionAzureFunctionsAuthentication(**data)


class ExtensionInputSchema(helpers.BaseSchema):
    action = marshmallow_enum.EnumField(
        ExtensionAction, by_value=True, allow_none=True, missing=None
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

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ExtensionInput(**data)


class ExtensionPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExtensionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ExtensionPagedQueryResponse(**data)


class ExtensionTriggerSchema(helpers.BaseSchema):
    resource_type_id = marshmallow_enum.EnumField(
        ExtensionResourceTypeId,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="resourceTypeId",
    )
    actions = marshmallow.fields.List(
        marshmallow_enum.EnumField(ExtensionAction, by_value=True, allow_none=True),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ExtensionTrigger(**data)


class ExtensionUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeDestination": helpers.absmod(
                    __name__, ".ExtensionChangeDestinationActionSchema"
                ),
                "changeTriggers": helpers.absmod(
                    __name__, ".ExtensionChangeTriggersActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".ExtensionSetKeyActionSchema"),
                "setTimeoutInMs": helpers.absmod(
                    __name__, ".ExtensionSetTimeoutInMsActionSchema"
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

        return models.ExtensionUpdate(**data)


class ExtensionUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ExtensionUpdateAction(**data)


class ExtensionChangeDestinationActionSchema(ExtensionUpdateActionSchema):
    destination = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "AWSLambda": helpers.absmod(
                __name__, ".ExtensionAWSLambdaDestinationSchema"
            ),
            "HTTP": helpers.absmod(__name__, ".ExtensionHttpDestinationSchema"),
        },
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ExtensionChangeDestinationAction(**data)


class ExtensionChangeTriggersActionSchema(ExtensionUpdateActionSchema):
    triggers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExtensionTriggerSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ExtensionChangeTriggersAction(**data)


class ExtensionSetKeyActionSchema(ExtensionUpdateActionSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ExtensionSetKeyAction(**data)


class ExtensionSetTimeoutInMsActionSchema(ExtensionUpdateActionSchema):
    timeout_in_ms = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="timeoutInMs",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ExtensionSetTimeoutInMsAction(**data)

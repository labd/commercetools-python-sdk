# DO NOT EDIT! This file is automatically generated
import marshmallow
import marshmallow_enum

from commercetools import helpers, types
from commercetools.schemas._common import BaseResourceSchema

__all__ = [
    "ExtensionAWSLambdaDestinationSchema",
    "ExtensionAuthorizationHeaderAuthenticationSchema",
    "ExtensionAzureFunctionsAuthenticationSchema",
    "ExtensionChangeDestinationActionSchema",
    "ExtensionChangeTriggersActionSchema",
    "ExtensionDestinationSchema",
    "ExtensionDraftSchema",
    "ExtensionHttpDestinationAuthenticationSchema",
    "ExtensionHttpDestinationSchema",
    "ExtensionInputSchema",
    "ExtensionPagedQueryResponseSchema",
    "ExtensionSchema",
    "ExtensionSetKeyActionSchema",
    "ExtensionSetTimeoutInMsActionSchema",
    "ExtensionTriggerSchema",
    "ExtensionUpdateActionSchema",
    "ExtensionUpdateSchema",
]


class ExtensionDestinationSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionDestination`."""

    type = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.ExtensionDestination(**data)


class ExtensionDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionDraft`."""

    key = marshmallow.fields.String(allow_none=True, missing=None)
    destination = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "AWSLambda": "commercetools.schemas._extension.ExtensionAWSLambdaDestinationSchema",
            "HTTP": "commercetools.schemas._extension.ExtensionHttpDestinationSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    triggers = marshmallow.fields.Nested(
        nested="commercetools.schemas._extension.ExtensionTriggerSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )
    timeout_in_ms = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="timeoutInMs"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ExtensionDraft(**data)


class ExtensionHttpDestinationAuthenticationSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionHttpDestinationAuthentication`."""

    type = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.ExtensionHttpDestinationAuthentication(**data)


class ExtensionInputSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionInput`."""

    action = marshmallow_enum.EnumField(types.ExtensionAction, by_value=True)
    resource = helpers.Discriminator(
        discriminator_field=("typeId", "type_id"),
        discriminator_schemas={
            "cart-discount": "commercetools.schemas._cart_discount.CartDiscountReferenceSchema",
            "cart": "commercetools.schemas._cart.CartReferenceSchema",
            "category": "commercetools.schemas._category.CategoryReferenceSchema",
            "channel": "commercetools.schemas._channel.ChannelReferenceSchema",
            "key-value-document": "commercetools.schemas._custom_object.CustomObjectReferenceSchema",
            "customer-group": "commercetools.schemas._customer_group.CustomerGroupReferenceSchema",
            "customer": "commercetools.schemas._customer.CustomerReferenceSchema",
            "discount-code": "commercetools.schemas._discount_code.DiscountCodeReferenceSchema",
            "inventory-entry": "commercetools.schemas._inventory.InventoryEntryReferenceSchema",
            "order-edit": "commercetools.schemas._order_edit.OrderEditReferenceSchema",
            "order": "commercetools.schemas._order.OrderReferenceSchema",
            "payment": "commercetools.schemas._payment.PaymentReferenceSchema",
            "product-discount": "commercetools.schemas._product_discount.ProductDiscountReferenceSchema",
            "product-type": "commercetools.schemas._product_type.ProductTypeReferenceSchema",
            "product": "commercetools.schemas._product.ProductReferenceSchema",
            "review": "commercetools.schemas._review.ReviewReferenceSchema",
            "shipping-method": "commercetools.schemas._shipping_method.ShippingMethodReferenceSchema",
            "shopping-list": "commercetools.schemas._shopping_list.ShoppingListReferenceSchema",
            "state": "commercetools.schemas._state.StateReferenceSchema",
            "store": "commercetools.schemas._store.StoreReferenceSchema",
            "tax-category": "commercetools.schemas._tax_category.TaxCategoryReferenceSchema",
            "type": "commercetools.schemas._type.TypeReferenceSchema",
            "zone": "commercetools.schemas._zone.ZoneReferenceSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ExtensionInput(**data)


class ExtensionPagedQueryResponseSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionPagedQueryResponse`."""

    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = marshmallow.fields.Nested(
        nested="commercetools.schemas._extension.ExtensionSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ExtensionPagedQueryResponse(**data)


class ExtensionSchema(BaseResourceSchema):
    """Marshmallow schema for :class:`commercetools.types.Extension`."""

    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True)
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, data_key="lastModifiedAt"
    )
    last_modified_by = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.LastModifiedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.CreatedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)
    destination = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "AWSLambda": "commercetools.schemas._extension.ExtensionAWSLambdaDestinationSchema",
            "HTTP": "commercetools.schemas._extension.ExtensionHttpDestinationSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    triggers = marshmallow.fields.Nested(
        nested="commercetools.schemas._extension.ExtensionTriggerSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )
    timeout_in_ms = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="timeoutInMs"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Extension(**data)


class ExtensionTriggerSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionTrigger`."""

    resource_type_id = marshmallow_enum.EnumField(
        types.ExtensionResourceTypeId, by_value=True, data_key="resourceTypeId"
    )
    actions = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.ExtensionAction, by_value=True)
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ExtensionTrigger(**data)


class ExtensionUpdateActionSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionUpdateAction`."""

    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ExtensionUpdateAction(**data)


class ExtensionUpdateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionUpdate`."""

    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeDestination": "commercetools.schemas._extension.ExtensionChangeDestinationActionSchema",
                "changeTriggers": "commercetools.schemas._extension.ExtensionChangeTriggersActionSchema",
                "setKey": "commercetools.schemas._extension.ExtensionSetKeyActionSchema",
                "setTimeoutInMs": "commercetools.schemas._extension.ExtensionSetTimeoutInMsActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ExtensionUpdate(**data)


class ExtensionAWSLambdaDestinationSchema(ExtensionDestinationSchema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionAWSLambdaDestination`."""

    arn = marshmallow.fields.String(allow_none=True)
    access_key = marshmallow.fields.String(allow_none=True, data_key="accessKey")
    access_secret = marshmallow.fields.String(allow_none=True, data_key="accessSecret")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.ExtensionAWSLambdaDestination(**data)


class ExtensionAuthorizationHeaderAuthenticationSchema(
    ExtensionHttpDestinationAuthenticationSchema
):
    """Marshmallow schema for :class:`commercetools.types.ExtensionAuthorizationHeaderAuthentication`."""

    header_value = marshmallow.fields.String(allow_none=True, data_key="headerValue")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.ExtensionAuthorizationHeaderAuthentication(**data)


class ExtensionAzureFunctionsAuthenticationSchema(
    ExtensionHttpDestinationAuthenticationSchema
):
    """Marshmallow schema for :class:`commercetools.types.ExtensionAzureFunctionsAuthentication`."""

    key = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.ExtensionAzureFunctionsAuthentication(**data)


class ExtensionChangeDestinationActionSchema(ExtensionUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionChangeDestinationAction`."""

    destination = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "AWSLambda": "commercetools.schemas._extension.ExtensionAWSLambdaDestinationSchema",
            "HTTP": "commercetools.schemas._extension.ExtensionHttpDestinationSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ExtensionChangeDestinationAction(**data)


class ExtensionChangeTriggersActionSchema(ExtensionUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionChangeTriggersAction`."""

    triggers = marshmallow.fields.Nested(
        nested="commercetools.schemas._extension.ExtensionTriggerSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ExtensionChangeTriggersAction(**data)


class ExtensionHttpDestinationSchema(ExtensionDestinationSchema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionHttpDestination`."""

    url = marshmallow.fields.String(allow_none=True)
    authentication = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "AuthorizationHeader": "commercetools.schemas._extension.ExtensionAuthorizationHeaderAuthenticationSchema",
            "AzureFunctions": "commercetools.schemas._extension.ExtensionAzureFunctionsAuthenticationSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.ExtensionHttpDestination(**data)


class ExtensionSetKeyActionSchema(ExtensionUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionSetKeyAction`."""

    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ExtensionSetKeyAction(**data)


class ExtensionSetTimeoutInMsActionSchema(ExtensionUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ExtensionSetTimeoutInMsAction`."""

    timeout_in_ms = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="timeoutInMs"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ExtensionSetTimeoutInMsAction(**data)

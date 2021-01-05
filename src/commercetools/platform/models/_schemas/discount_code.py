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
class DiscountCodeSchema(BaseResourceSchema):
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
    description = LocalizedStringField(allow_none=True, missing=None)
    code = marshmallow.fields.String(allow_none=True, missing=None)
    cart_discounts = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart_discount.CartDiscountReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="cartDiscounts",
    )
    cart_predicate = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="cartPredicate"
    )
    is_active = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isActive"
    )
    references = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("typeId", "type_id"),
            discriminator_schemas={
                "cart-discount": helpers.absmod(
                    __name__, ".cart_discount.CartDiscountReferenceSchema"
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
                    __name__, ".DiscountCodeReferenceSchema"
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
    max_applications = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxApplications"
    )
    max_applications_per_customer = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxApplicationsPerCustomer"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    groups = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )
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

        return models.DiscountCode(**data)


class DiscountCodeDraftSchema(marshmallow.Schema):
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    code = marshmallow.fields.String(allow_none=True, missing=None)
    cart_discounts = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".cart_discount.CartDiscountResourceIdentifierSchema"
        ),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="cartDiscounts",
    )
    cart_predicate = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="cartPredicate"
    )
    is_active = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isActive"
    )
    max_applications = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxApplications"
    )
    max_applications_per_customer = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxApplicationsPerCustomer"
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    groups = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )
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

        return models.DiscountCodeDraft(**data)


class DiscountCodePagedQueryResponseSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountCodeSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DiscountCodePagedQueryResponse(**data)


class DiscountCodeReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountCodeSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.DiscountCodeReference(**data)


class DiscountCodeResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.DiscountCodeResourceIdentifier(**data)


class DiscountCodeUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeCartDiscounts": helpers.absmod(
                    __name__, ".DiscountCodeChangeCartDiscountsActionSchema"
                ),
                "changeGroups": helpers.absmod(
                    __name__, ".DiscountCodeChangeGroupsActionSchema"
                ),
                "changeIsActive": helpers.absmod(
                    __name__, ".DiscountCodeChangeIsActiveActionSchema"
                ),
                "setCartPredicate": helpers.absmod(
                    __name__, ".DiscountCodeSetCartPredicateActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".DiscountCodeSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".DiscountCodeSetCustomTypeActionSchema"
                ),
                "setDescription": helpers.absmod(
                    __name__, ".DiscountCodeSetDescriptionActionSchema"
                ),
                "setMaxApplications": helpers.absmod(
                    __name__, ".DiscountCodeSetMaxApplicationsActionSchema"
                ),
                "setMaxApplicationsPerCustomer": helpers.absmod(
                    __name__, ".DiscountCodeSetMaxApplicationsPerCustomerActionSchema"
                ),
                "setName": helpers.absmod(__name__, ".DiscountCodeSetNameActionSchema"),
                "setValidFrom": helpers.absmod(
                    __name__, ".DiscountCodeSetValidFromActionSchema"
                ),
                "setValidFromAndUntil": helpers.absmod(
                    __name__, ".DiscountCodeSetValidFromAndUntilActionSchema"
                ),
                "setValidUntil": helpers.absmod(
                    __name__, ".DiscountCodeSetValidUntilActionSchema"
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

        return models.DiscountCodeUpdate(**data)


class DiscountCodeUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.DiscountCodeUpdateAction(**data)


class DiscountCodeChangeCartDiscountsActionSchema(DiscountCodeUpdateActionSchema):
    cart_discounts = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".cart_discount.CartDiscountResourceIdentifierSchema"
        ),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="cartDiscounts",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.DiscountCodeChangeCartDiscountsAction(**data)


class DiscountCodeChangeGroupsActionSchema(DiscountCodeUpdateActionSchema):
    groups = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.DiscountCodeChangeGroupsAction(**data)


class DiscountCodeChangeIsActiveActionSchema(DiscountCodeUpdateActionSchema):
    is_active = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isActive"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.DiscountCodeChangeIsActiveAction(**data)


class DiscountCodeSetCartPredicateActionSchema(DiscountCodeUpdateActionSchema):
    cart_predicate = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="cartPredicate"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.DiscountCodeSetCartPredicateAction(**data)


class DiscountCodeSetCustomFieldActionSchema(DiscountCodeUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.DiscountCodeSetCustomFieldAction(**data)


class DiscountCodeSetCustomTypeActionSchema(DiscountCodeUpdateActionSchema):
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
        return models.DiscountCodeSetCustomTypeAction(**data)


class DiscountCodeSetDescriptionActionSchema(DiscountCodeUpdateActionSchema):
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.DiscountCodeSetDescriptionAction(**data)


class DiscountCodeSetMaxApplicationsActionSchema(DiscountCodeUpdateActionSchema):
    max_applications = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxApplications"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.DiscountCodeSetMaxApplicationsAction(**data)


class DiscountCodeSetMaxApplicationsPerCustomerActionSchema(
    DiscountCodeUpdateActionSchema
):
    max_applications_per_customer = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxApplicationsPerCustomer"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.DiscountCodeSetMaxApplicationsPerCustomerAction(**data)


class DiscountCodeSetNameActionSchema(DiscountCodeUpdateActionSchema):
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.DiscountCodeSetNameAction(**data)


class DiscountCodeSetValidFromActionSchema(DiscountCodeUpdateActionSchema):
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.DiscountCodeSetValidFromAction(**data)


class DiscountCodeSetValidFromAndUntilActionSchema(DiscountCodeUpdateActionSchema):
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
        return models.DiscountCodeSetValidFromAndUntilAction(**data)


class DiscountCodeSetValidUntilActionSchema(DiscountCodeUpdateActionSchema):
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.DiscountCodeSetValidUntilAction(**data)

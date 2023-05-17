# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
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

# Fields


# Marshmallow Schemas
class ProductDiscountSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="createdBy",
    )
    name = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        load_default=None,
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "absolute": helpers.absmod(__name__, ".ProductDiscountValueAbsoluteSchema"),
            "external": helpers.absmod(__name__, ".ProductDiscountValueExternalSchema"),
            "relative": helpers.absmod(__name__, ".ProductDiscountValueRelativeSchema"),
        },
        load_default=None,
    )
    predicate = marshmallow.fields.String(allow_none=True, load_default=None)
    sort_order = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="sortOrder"
    )
    is_active = marshmallow.fields.Boolean(
        allow_none=True, load_default=None, data_key="isActive"
    )
    references = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("typeId", "type_id"),
            discriminator_schemas={
                "associate-role": helpers.absmod(
                    __name__, ".associate_role.AssociateRoleReferenceSchema"
                ),
                "attribute-group": helpers.absmod(
                    __name__, ".attribute_group.AttributeGroupReferenceSchema"
                ),
                "business-unit": helpers.absmod(
                    __name__, ".business_unit.BusinessUnitReferenceSchema"
                ),
                "cart-discount": helpers.absmod(
                    __name__, ".cart_discount.CartDiscountReferenceSchema"
                ),
                "cart": helpers.absmod(__name__, ".cart.CartReferenceSchema"),
                "direct-discount": helpers.absmod(
                    __name__, ".cart.DirectDiscountReferenceSchema"
                ),
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
                    __name__, ".ProductDiscountReferenceSchema"
                ),
                "product-selection": helpers.absmod(
                    __name__, ".product_selection.ProductSelectionReferenceSchema"
                ),
                "product-type": helpers.absmod(
                    __name__, ".product_type.ProductTypeReferenceSchema"
                ),
                "product": helpers.absmod(__name__, ".product.ProductReferenceSchema"),
                "quote-request": helpers.absmod(
                    __name__, ".quote_request.QuoteRequestReferenceSchema"
                ),
                "quote": helpers.absmod(__name__, ".quote.QuoteReferenceSchema"),
                "review": helpers.absmod(__name__, ".review.ReviewReferenceSchema"),
                "shipping-method": helpers.absmod(
                    __name__, ".shipping_method.ShippingMethodReferenceSchema"
                ),
                "shopping-list": helpers.absmod(
                    __name__, ".shopping_list.ShoppingListReferenceSchema"
                ),
                "staged-quote": helpers.absmod(
                    __name__, ".staged_quote.StagedQuoteReferenceSchema"
                ),
                "standalone-price": helpers.absmod(
                    __name__, ".standalone_price.StandalonePriceReferenceSchema"
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
        load_default=None,
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validFrom",
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validUntil",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return models.ProductDiscount(**data)


class ProductDiscountDraftSchema(helpers.BaseSchema):
    name = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        load_default=None,
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "absolute": helpers.absmod(
                __name__, ".ProductDiscountValueAbsoluteDraftSchema"
            ),
            "external": helpers.absmod(
                __name__, ".ProductDiscountValueExternalDraftSchema"
            ),
            "relative": helpers.absmod(
                __name__, ".ProductDiscountValueRelativeDraftSchema"
            ),
        },
        load_default=None,
    )
    predicate = marshmallow.fields.String(allow_none=True, load_default=None)
    sort_order = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="sortOrder"
    )
    is_active = marshmallow.fields.Boolean(
        allow_none=True, load_default=None, data_key="isActive"
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validFrom",
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validUntil",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return models.ProductDiscountDraft(**data)


class ProductDiscountMatchQuerySchema(helpers.BaseSchema):
    product_id = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="productId"
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, load_default=None, data_key="variantId"
    )
    staged = marshmallow.fields.Boolean(allow_none=True, load_default=None)
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.QueryPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return models.ProductDiscountMatchQuery(**data)


class ProductDiscountPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, load_default=None)
    offset = marshmallow.fields.Integer(allow_none=True, load_default=None)
    count = marshmallow.fields.Integer(allow_none=True, load_default=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductDiscountSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return models.ProductDiscountPagedQueryResponse(**data)


class ProductDiscountReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductDiscountSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductDiscountReference(**data)


class ProductDiscountResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductDiscountResourceIdentifier(**data)


class ProductDiscountUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, load_default=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeIsActive": helpers.absmod(
                    __name__, ".ProductDiscountChangeIsActiveActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".ProductDiscountChangeNameActionSchema"
                ),
                "changePredicate": helpers.absmod(
                    __name__, ".ProductDiscountChangePredicateActionSchema"
                ),
                "changeSortOrder": helpers.absmod(
                    __name__, ".ProductDiscountChangeSortOrderActionSchema"
                ),
                "changeValue": helpers.absmod(
                    __name__, ".ProductDiscountChangeValueActionSchema"
                ),
                "setDescription": helpers.absmod(
                    __name__, ".ProductDiscountSetDescriptionActionSchema"
                ),
                "setKey": helpers.absmod(
                    __name__, ".ProductDiscountSetKeyActionSchema"
                ),
                "setValidFrom": helpers.absmod(
                    __name__, ".ProductDiscountSetValidFromActionSchema"
                ),
                "setValidFromAndUntil": helpers.absmod(
                    __name__, ".ProductDiscountSetValidFromAndUntilActionSchema"
                ),
                "setValidUntil": helpers.absmod(
                    __name__, ".ProductDiscountSetValidUntilActionSchema"
                ),
            },
        ),
        allow_none=True,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return models.ProductDiscountUpdate(**data)


class ProductDiscountUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductDiscountUpdateAction(**data)


class ProductDiscountValueSchema(helpers.BaseSchema):
    type = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductDiscountValue(**data)


class ProductDiscountValueAbsoluteSchema(ProductDiscountValueSchema):
    money = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CentPrecisionMoneySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductDiscountValueAbsolute(**data)


class ProductDiscountValueDraftSchema(helpers.BaseSchema):
    type = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductDiscountValueDraft(**data)


class ProductDiscountValueAbsoluteDraftSchema(ProductDiscountValueDraftSchema):
    money = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductDiscountValueAbsoluteDraft(**data)


class ProductDiscountValueExternalSchema(ProductDiscountValueSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductDiscountValueExternal(**data)


class ProductDiscountValueExternalDraftSchema(ProductDiscountValueDraftSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductDiscountValueExternalDraft(**data)


class ProductDiscountValueRelativeSchema(ProductDiscountValueSchema):
    permyriad = marshmallow.fields.Integer(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductDiscountValueRelative(**data)


class ProductDiscountValueRelativeDraftSchema(ProductDiscountValueDraftSchema):
    permyriad = marshmallow.fields.Integer(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductDiscountValueRelativeDraft(**data)


class ProductDiscountChangeIsActiveActionSchema(ProductDiscountUpdateActionSchema):
    is_active = marshmallow.fields.Boolean(
        allow_none=True, load_default=None, data_key="isActive"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductDiscountChangeIsActiveAction(**data)


class ProductDiscountChangeNameActionSchema(ProductDiscountUpdateActionSchema):
    name = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductDiscountChangeNameAction(**data)


class ProductDiscountChangePredicateActionSchema(ProductDiscountUpdateActionSchema):
    predicate = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductDiscountChangePredicateAction(**data)


class ProductDiscountChangeSortOrderActionSchema(ProductDiscountUpdateActionSchema):
    sort_order = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="sortOrder"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductDiscountChangeSortOrderAction(**data)


class ProductDiscountChangeValueActionSchema(ProductDiscountUpdateActionSchema):
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "absolute": helpers.absmod(
                __name__, ".ProductDiscountValueAbsoluteDraftSchema"
            ),
            "external": helpers.absmod(
                __name__, ".ProductDiscountValueExternalDraftSchema"
            ),
            "relative": helpers.absmod(
                __name__, ".ProductDiscountValueRelativeDraftSchema"
            ),
        },
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductDiscountChangeValueAction(**data)


class ProductDiscountSetDescriptionActionSchema(ProductDiscountUpdateActionSchema):
    description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductDiscountSetDescriptionAction(**data)


class ProductDiscountSetKeyActionSchema(ProductDiscountUpdateActionSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductDiscountSetKeyAction(**data)


class ProductDiscountSetValidFromActionSchema(ProductDiscountUpdateActionSchema):
    valid_from = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validFrom",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductDiscountSetValidFromAction(**data)


class ProductDiscountSetValidFromAndUntilActionSchema(
    ProductDiscountUpdateActionSchema
):
    valid_from = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validFrom",
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validUntil",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductDiscountSetValidFromAndUntilAction(**data)


class ProductDiscountSetValidUntilActionSchema(ProductDiscountUpdateActionSchema):
    valid_until = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validUntil",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductDiscountSetValidUntilAction(**data)

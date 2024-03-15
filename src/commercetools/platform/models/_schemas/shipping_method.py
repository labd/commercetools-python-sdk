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
from ..shipping_method import ShippingRateTierType
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class PriceFunctionSchema(helpers.BaseSchema):
    currency_code = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="currencyCode"
    )
    function = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PriceFunction(**data)


class ShippingMethodSchema(BaseResourceSchema):
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
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    name = marshmallow.fields.String(allow_none=True, load_default=None)
    localized_name = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="localizedName",
    )
    description = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    localized_description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="localizedDescription",
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".tax_category.TaxCategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="taxCategory",
    )
    zone_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ZoneRateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="zoneRates",
    )
    is_default = marshmallow.fields.Boolean(
        allow_none=True, load_default=None, data_key="isDefault"
    )
    predicate = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingMethod(**data)


class ShippingMethodDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    name = marshmallow.fields.String(allow_none=True, load_default=None)
    localized_name = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="localizedName",
    )
    description = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    localized_description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="localizedDescription",
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="taxCategory",
    )
    zone_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ZoneRateDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="zoneRates",
    )
    is_default = marshmallow.fields.Boolean(
        allow_none=True, load_default=None, data_key="isDefault"
    )
    predicate = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingMethodDraft(**data)


class ShippingMethodPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    count = marshmallow.fields.Integer(allow_none=True, load_default=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    offset = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingMethodSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingMethodPagedQueryResponse(**data)


class ShippingMethodReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingMethodSchema"),
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
        return models.ShippingMethodReference(**data)


class ShippingMethodResourceIdentifierSchema(ResourceIdentifierSchema):

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ShippingMethodResourceIdentifier(**data)


class ShippingMethodUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, load_default=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addShippingRate": helpers.absmod(
                    __name__, ".ShippingMethodAddShippingRateActionSchema"
                ),
                "addZone": helpers.absmod(
                    __name__, ".ShippingMethodAddZoneActionSchema"
                ),
                "changeIsDefault": helpers.absmod(
                    __name__, ".ShippingMethodChangeIsDefaultActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".ShippingMethodChangeNameActionSchema"
                ),
                "changeTaxCategory": helpers.absmod(
                    __name__, ".ShippingMethodChangeTaxCategoryActionSchema"
                ),
                "removeShippingRate": helpers.absmod(
                    __name__, ".ShippingMethodRemoveShippingRateActionSchema"
                ),
                "removeZone": helpers.absmod(
                    __name__, ".ShippingMethodRemoveZoneActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".ShippingMethodSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".ShippingMethodSetCustomTypeActionSchema"
                ),
                "setDescription": helpers.absmod(
                    __name__, ".ShippingMethodSetDescriptionActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".ShippingMethodSetKeyActionSchema"),
                "setLocalizedDescription": helpers.absmod(
                    __name__, ".ShippingMethodSetLocalizedDescriptionActionSchema"
                ),
                "setLocalizedName": helpers.absmod(
                    __name__, ".ShippingMethodSetLocalizedNameActionSchema"
                ),
                "setPredicate": helpers.absmod(
                    __name__, ".ShippingMethodSetPredicateActionSchema"
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

        return models.ShippingMethodUpdate(**data)


class ShippingMethodUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodUpdateAction(**data)


class ShippingRateSchema(helpers.BaseSchema):
    price = helpers.Discriminator(
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
        load_default=None,
    )
    free_above = helpers.Discriminator(
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
        metadata={"omit_empty": True},
        load_default=None,
        data_key="freeAbove",
    )
    is_matching = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="isMatching",
    )
    tiers = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "CartClassification": helpers.absmod(
                    __name__, ".CartClassificationTierSchema"
                ),
                "CartScore": helpers.absmod(__name__, ".CartScoreTierSchema"),
                "CartValue": helpers.absmod(__name__, ".CartValueTierSchema"),
            },
        ),
        allow_none=True,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingRate(**data)


class ShippingRateDraftSchema(helpers.BaseSchema):
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    free_above = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="freeAbove",
    )
    tiers = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "CartClassification": helpers.absmod(
                    __name__, ".CartClassificationTierSchema"
                ),
                "CartScore": helpers.absmod(__name__, ".CartScoreTierSchema"),
                "CartValue": helpers.absmod(__name__, ".CartValueTierSchema"),
            },
        ),
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingRateDraft(**data)


class ShippingRatePriceTierSchema(helpers.BaseSchema):
    type = marshmallow_enum.EnumField(
        ShippingRateTierType, by_value=True, allow_none=True, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ShippingRatePriceTier(**data)


class CartClassificationTierSchema(ShippingRatePriceTierSchema):
    value = marshmallow.fields.String(allow_none=True, load_default=None)
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    is_matching = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="isMatching",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartClassificationTier(**data)


class CartScoreTierSchema(ShippingRatePriceTierSchema):
    score = marshmallow.fields.Integer(allow_none=True, load_default=None)
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    price_function = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PriceFunctionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="priceFunction",
    )
    is_matching = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="isMatching",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartScoreTier(**data)


class CartValueTierSchema(ShippingRatePriceTierSchema):
    minimum_cent_amount = marshmallow.fields.Integer(
        allow_none=True, load_default=None, data_key="minimumCentAmount"
    )
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    is_matching = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="isMatching",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartValueTier(**data)


class ZoneRateSchema(helpers.BaseSchema):
    zone = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".zone.ZoneReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    shipping_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingRateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="shippingRates",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ZoneRate(**data)


class ZoneRateDraftSchema(helpers.BaseSchema):
    zone = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".zone.ZoneResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    shipping_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingRateDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="shippingRates",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ZoneRateDraft(**data)


class ShippingMethodAddShippingRateActionSchema(ShippingMethodUpdateActionSchema):
    zone = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".zone.ZoneResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    shipping_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="shippingRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodAddShippingRateAction(**data)


class ShippingMethodAddZoneActionSchema(ShippingMethodUpdateActionSchema):
    zone = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".zone.ZoneResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodAddZoneAction(**data)


class ShippingMethodChangeIsDefaultActionSchema(ShippingMethodUpdateActionSchema):
    is_default = marshmallow.fields.Boolean(
        allow_none=True, load_default=None, data_key="isDefault"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodChangeIsDefaultAction(**data)


class ShippingMethodChangeNameActionSchema(ShippingMethodUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodChangeNameAction(**data)


class ShippingMethodChangeTaxCategoryActionSchema(ShippingMethodUpdateActionSchema):
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="taxCategory",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodChangeTaxCategoryAction(**data)


class ShippingMethodRemoveShippingRateActionSchema(ShippingMethodUpdateActionSchema):
    zone = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".zone.ZoneResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    shipping_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="shippingRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodRemoveShippingRateAction(**data)


class ShippingMethodRemoveZoneActionSchema(ShippingMethodUpdateActionSchema):
    zone = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".zone.ZoneResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodRemoveZoneAction(**data)


class ShippingMethodSetCustomFieldActionSchema(ShippingMethodUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, load_default=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodSetCustomFieldAction(**data)


class ShippingMethodSetCustomTypeActionSchema(ShippingMethodUpdateActionSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    fields = FieldContainerField(
        allow_none=True,
        values=marshmallow.fields.Raw(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodSetCustomTypeAction(**data)


class ShippingMethodSetDescriptionActionSchema(ShippingMethodUpdateActionSchema):
    description = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodSetDescriptionAction(**data)


class ShippingMethodSetKeyActionSchema(ShippingMethodUpdateActionSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodSetKeyAction(**data)


class ShippingMethodSetLocalizedDescriptionActionSchema(
    ShippingMethodUpdateActionSchema
):
    localized_description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="localizedDescription",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodSetLocalizedDescriptionAction(**data)


class ShippingMethodSetLocalizedNameActionSchema(ShippingMethodUpdateActionSchema):
    localized_name = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
        data_key="localizedName",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodSetLocalizedNameAction(**data)


class ShippingMethodSetPredicateActionSchema(ShippingMethodUpdateActionSchema):
    predicate = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodSetPredicateAction(**data)

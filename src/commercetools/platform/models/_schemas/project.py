# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..shipping_method import ShippingRateTierType

# Fields


# Marshmallow Schemas
class CartsConfigurationSchema(marshmallow.Schema):
    country_tax_rate_fallback_enabled = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="countryTaxRateFallbackEnabled"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CartsConfiguration(**data)


class ExternalOAuthSchema(marshmallow.Schema):
    url = marshmallow.fields.String(allow_none=True, missing=None)
    authorization_header = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="authorizationHeader"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ExternalOAuth(**data)


class ProjectSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    name = marshmallow.fields.String(allow_none=True, missing=None)
    countries = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )
    currencies = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )
    languages = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )
    created_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="createdAt"
    )
    trial_until = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="trialUntil"
    )
    messages = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".message.MessageConfigurationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    shipping_rate_input_type = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "CartClassification": helpers.absmod(
                __name__, ".CartClassificationTypeSchema"
            ),
            "CartScore": helpers.absmod(__name__, ".CartScoreTypeSchema"),
            "CartValue": helpers.absmod(__name__, ".CartValueTypeSchema"),
        },
        missing=None,
        data_key="shippingRateInputType",
    )
    external_o_auth = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalOAuthSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalOAuth",
    )
    carts = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CartsConfigurationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Project(**data)


class ProjectUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeCountries": helpers.absmod(
                    __name__, ".ProjectChangeCountriesActionSchema"
                ),
                "changeCountryTaxRateFallbackEnabled": helpers.absmod(
                    __name__, ".ProjectChangeCountryTaxRateFallbackEnabledActionSchema"
                ),
                "changeCurrencies": helpers.absmod(
                    __name__, ".ProjectChangeCurrenciesActionSchema"
                ),
                "changeLanguages": helpers.absmod(
                    __name__, ".ProjectChangeLanguagesActionSchema"
                ),
                "changeMessagesConfiguration": helpers.absmod(
                    __name__, ".ProjectChangeMessagesConfigurationActionSchema"
                ),
                "changeMessagesEnabled": helpers.absmod(
                    __name__, ".ProjectChangeMessagesEnabledActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".ProjectChangeNameActionSchema"
                ),
                "setExternalOAuth": helpers.absmod(
                    __name__, ".ProjectSetExternalOAuthActionSchema"
                ),
                "setShippingRateInputType": helpers.absmod(
                    __name__, ".ProjectSetShippingRateInputTypeActionSchema"
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

        return models.ProjectUpdate(**data)


class ProjectUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectUpdateAction(**data)


class ShippingRateInputTypeSchema(marshmallow.Schema):
    type = marshmallow_enum.EnumField(
        ShippingRateTierType, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ShippingRateInputType(**data)


class CartClassificationTypeSchema(ShippingRateInputTypeSchema):
    values = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldLocalizedEnumValueSchema"),
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
        return models.CartClassificationType(**data)


class CartScoreTypeSchema(ShippingRateInputTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartScoreType(**data)


class CartValueTypeSchema(ShippingRateInputTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartValueType(**data)


class ProjectChangeCountriesActionSchema(ProjectUpdateActionSchema):
    countries = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeCountriesAction(**data)


class ProjectChangeCountryTaxRateFallbackEnabledActionSchema(ProjectUpdateActionSchema):
    country_tax_rate_fallback_enabled = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="countryTaxRateFallbackEnabled"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeCountryTaxRateFallbackEnabledAction(**data)


class ProjectChangeCurrenciesActionSchema(ProjectUpdateActionSchema):
    currencies = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeCurrenciesAction(**data)


class ProjectChangeLanguagesActionSchema(ProjectUpdateActionSchema):
    languages = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeLanguagesAction(**data)


class ProjectChangeMessagesConfigurationActionSchema(ProjectUpdateActionSchema):
    messages_configuration = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".message.MessageConfigurationDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="messagesConfiguration",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeMessagesConfigurationAction(**data)


class ProjectChangeMessagesEnabledActionSchema(ProjectUpdateActionSchema):
    messages_enabled = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="messagesEnabled"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeMessagesEnabledAction(**data)


class ProjectChangeNameActionSchema(ProjectUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeNameAction(**data)


class ProjectSetExternalOAuthActionSchema(ProjectUpdateActionSchema):
    external_o_auth = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalOAuthSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="externalOAuth",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectSetExternalOAuthAction(**data)


class ProjectSetShippingRateInputTypeActionSchema(ProjectUpdateActionSchema):
    shipping_rate_input_type = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "CartClassification": helpers.absmod(
                __name__, ".CartClassificationTypeSchema"
            ),
            "CartScore": helpers.absmod(__name__, ".CartScoreTypeSchema"),
            "CartValue": helpers.absmod(__name__, ".CartValueTypeSchema"),
        },
        missing=None,
        data_key="shippingRateInputType",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectSetShippingRateInputTypeAction(**data)

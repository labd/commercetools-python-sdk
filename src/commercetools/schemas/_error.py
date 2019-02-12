# DO NOT EDIT! This file is automatically generated

import marshmallow
import marshmallow_enum

from commercetools import helpers, types

__all__ = [
    "AccessDeniedErrorSchema",
    "ConcurrentModificationErrorSchema",
    "DiscountCodeNonApplicableErrorSchema",
    "DuplicateAttributeValueErrorSchema",
    "DuplicateAttributeValuesErrorSchema",
    "DuplicateFieldErrorSchema",
    "DuplicatePriceScopeErrorSchema",
    "DuplicateVariantValuesErrorSchema",
    "ErrorObjectSchema",
    "ErrorResponseSchema",
    "InsufficientScopeErrorSchema",
    "InvalidCredentialsErrorSchema",
    "InvalidCurrentPasswordErrorSchema",
    "InvalidFieldErrorSchema",
    "InvalidInputErrorSchema",
    "InvalidItemShippingDetailsErrorSchema",
    "InvalidJsonInputErrorSchema",
    "InvalidOperationErrorSchema",
    "InvalidSubjectErrorSchema",
    "InvalidTokenErrorSchema",
    "MissingTaxRateForCountryErrorSchema",
    "NoMatchingProductDiscountFoundErrorSchema",
    "OutOfStockErrorSchema",
    "PriceChangedErrorSchema",
    "ReferenceExistsErrorSchema",
    "RequiredFieldErrorSchema",
    "ResourceNotFoundErrorSchema",
    "ShippingMethodDoesNotMatchCartErrorSchema",
    "VariantValuesSchema",
]


class ErrorObjectSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ErrorObject`."
    code = marshmallow.fields.String(allow_none=True)
    message = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.ErrorObject(**data)


class ErrorResponseSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ErrorResponse`."
    status_code = marshmallow.fields.Integer(allow_none=True, data_key="statusCode")
    message = marshmallow.fields.String(allow_none=True)
    error = marshmallow.fields.String(allow_none=True, missing=None)
    error_description = marshmallow.fields.String(allow_none=True, missing=None)
    errors = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("code", "code"),
            discriminator_schemas={
                "access_denied": "commercetools.schemas._error.AccessDeniedErrorSchema",
                "ConcurrentModification": "commercetools.schemas._error.ConcurrentModificationErrorSchema",
                "DiscountCodeNonApplicable": "commercetools.schemas._error.DiscountCodeNonApplicableErrorSchema",
                "DuplicateAttributeValue": "commercetools.schemas._error.DuplicateAttributeValueErrorSchema",
                "DuplicateAttributeValues": "commercetools.schemas._error.DuplicateAttributeValuesErrorSchema",
                "DuplicateField": "commercetools.schemas._error.DuplicateFieldErrorSchema",
                "DuplicatePriceScope": "commercetools.schemas._error.DuplicatePriceScopeErrorSchema",
                "DuplicateVariantValues": "commercetools.schemas._error.DuplicateVariantValuesErrorSchema",
                "insufficient_scope": "commercetools.schemas._error.InsufficientScopeErrorSchema",
                "InvalidCredentials": "commercetools.schemas._error.InvalidCredentialsErrorSchema",
                "InvalidCurrentPassword": "commercetools.schemas._error.InvalidCurrentPasswordErrorSchema",
                "InvalidField": "commercetools.schemas._error.InvalidFieldErrorSchema",
                "InvalidInput": "commercetools.schemas._error.InvalidInputErrorSchema",
                "InvalidItemShippingDetails": "commercetools.schemas._error.InvalidItemShippingDetailsErrorSchema",
                "InvalidJsonInput": "commercetools.schemas._error.InvalidJsonInputErrorSchema",
                "InvalidOperation": "commercetools.schemas._error.InvalidOperationErrorSchema",
                "InvalidSubject": "commercetools.schemas._error.InvalidSubjectErrorSchema",
                "invalid_token": "commercetools.schemas._error.InvalidTokenErrorSchema",
                "MissingTaxRateForCountry": "commercetools.schemas._error.MissingTaxRateForCountryErrorSchema",
                "NoMatchingProductDiscountFound": "commercetools.schemas._error.NoMatchingProductDiscountFoundErrorSchema",
                "OutOfStock": "commercetools.schemas._error.OutOfStockErrorSchema",
                "PriceChanged": "commercetools.schemas._error.PriceChangedErrorSchema",
                "ReferenceExists": "commercetools.schemas._error.ReferenceExistsErrorSchema",
                "RequiredField": "commercetools.schemas._error.RequiredFieldErrorSchema",
                "ResourceNotFound": "commercetools.schemas._error.ResourceNotFoundErrorSchema",
                "ShippingMethodDoesNotMatchCart": "commercetools.schemas._error.ShippingMethodDoesNotMatchCartErrorSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.ErrorResponse(**data)


class VariantValuesSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.VariantValues`."
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    prices = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.PriceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )
    attributes = marshmallow.fields.Nested(
        nested="commercetools.schemas._product.AttributeSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.VariantValues(**data)


class AccessDeniedErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.AccessDeniedError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.AccessDeniedError(**data)


class ConcurrentModificationErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.ConcurrentModificationError`."
    current_version = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="currentVersion"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.ConcurrentModificationError(**data)


class DiscountCodeNonApplicableErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeNonApplicableError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.DiscountCodeNonApplicableError(**data)


class DuplicateAttributeValueErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.DuplicateAttributeValueError`."
    attribute = marshmallow.fields.Nested(
        nested="commercetools.schemas._product.AttributeSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.DuplicateAttributeValueError(**data)


class DuplicateAttributeValuesErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.DuplicateAttributeValuesError`."
    attributes = marshmallow.fields.Nested(
        nested="commercetools.schemas._product.AttributeSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.DuplicateAttributeValuesError(**data)


class DuplicateFieldErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.DuplicateFieldError`."
    field = marshmallow.fields.String(allow_none=True, missing=None)
    duplicate_value = marshmallow.fields.Raw(
        allow_none=True, missing=None, data_key="duplicateValue"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.DuplicateFieldError(**data)


class DuplicatePriceScopeErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.DuplicatePriceScopeError`."
    conflicting_prices = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.PriceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        data_key="conflictingPrices",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.DuplicatePriceScopeError(**data)


class DuplicateVariantValuesErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.DuplicateVariantValuesError`."
    variant_values = marshmallow.fields.Nested(
        nested="commercetools.schemas._error.VariantValuesSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="variantValues",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.DuplicateVariantValuesError(**data)


class InsufficientScopeErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.InsufficientScopeError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.InsufficientScopeError(**data)


class InvalidCredentialsErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.InvalidCredentialsError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.InvalidCredentialsError(**data)


class InvalidCurrentPasswordErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.InvalidCurrentPasswordError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.InvalidCurrentPasswordError(**data)


class InvalidFieldErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.InvalidFieldError`."
    field = marshmallow.fields.String(allow_none=True)
    invalid_value = marshmallow.fields.Raw(allow_none=True, data_key="invalidValue")
    allowed_values = marshmallow.fields.List(
        marshmallow.fields.Nested(
            nested="commercetools.schemas.None.anySchema",
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
        missing=None,
        data_key="allowedValues",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.InvalidFieldError(**data)


class InvalidInputErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.InvalidInputError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.InvalidInputError(**data)


class InvalidItemShippingDetailsErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.InvalidItemShippingDetailsError`."
    subject = marshmallow.fields.String(allow_none=True)
    item_id = marshmallow.fields.String(allow_none=True, data_key="itemId")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.InvalidItemShippingDetailsError(**data)


class InvalidJsonInputErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.InvalidJsonInputError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.InvalidJsonInputError(**data)


class InvalidOperationErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.InvalidOperationError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.InvalidOperationError(**data)


class InvalidSubjectErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.InvalidSubjectError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.InvalidSubjectError(**data)


class InvalidTokenErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.InvalidTokenError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.InvalidTokenError(**data)


class MissingTaxRateForCountryErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.MissingTaxRateForCountryError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.MissingTaxRateForCountryError(**data)


class NoMatchingProductDiscountFoundErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.NoMatchingProductDiscountFoundError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.NoMatchingProductDiscountFoundError(**data)


class OutOfStockErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.OutOfStockError`."
    line_items = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), data_key="lineItems"
    )
    skus = marshmallow.fields.List(marshmallow.fields.String(allow_none=True))

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.OutOfStockError(**data)


class PriceChangedErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.PriceChangedError`."
    line_items = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), data_key="lineItems"
    )
    shipping = marshmallow.fields.Bool(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.PriceChangedError(**data)


class ReferenceExistsErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.ReferenceExistsError`."
    referenced_by = marshmallow_enum.EnumField(
        types.ReferenceTypeId, by_value=True, missing=None, data_key="referencedBy"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.ReferenceExistsError(**data)


class RequiredFieldErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.RequiredFieldError`."
    field = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.RequiredFieldError(**data)


class ResourceNotFoundErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.ResourceNotFoundError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.ResourceNotFoundError(**data)


class ShippingMethodDoesNotMatchCartErrorSchema(ErrorObjectSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodDoesNotMatchCartError`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["code"]
        return types.ShippingMethodDoesNotMatchCartError(**data)

# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..channel import ChannelRoleEnum
from ..common import ReferenceTypeId
from .common import LocalizedStringField

# Fields


# Marshmallow Schemas
class ErrorByExtensionSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ErrorByExtension(**data)


class ErrorObjectSchema(helpers.BaseSchema):
    code = marshmallow.fields.String(allow_none=True, missing=None)
    message = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ErrorObject(**data)


class AccessDeniedErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.AccessDeniedError(**data)


class AnonymousIdAlreadyInUseErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.AnonymousIdAlreadyInUseError(**data)


class AttributeDefinitionAlreadyExistsErrorSchema(ErrorObjectSchema):
    conflicting_product_type_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="conflictingProductTypeId"
    )
    conflicting_product_type_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="conflictingProductTypeName"
    )
    conflicting_attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="conflictingAttributeName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.AttributeDefinitionAlreadyExistsError(**data)


class AttributeDefinitionTypeConflictErrorSchema(ErrorObjectSchema):
    conflicting_product_type_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="conflictingProductTypeId"
    )
    conflicting_product_type_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="conflictingProductTypeName"
    )
    conflicting_attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="conflictingAttributeName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.AttributeDefinitionTypeConflictError(**data)


class AttributeNameDoesNotExistErrorSchema(ErrorObjectSchema):
    invalid_attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="invalidAttributeName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.AttributeNameDoesNotExistError(**data)


class ConcurrentModificationErrorSchema(ErrorObjectSchema):
    current_version = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="currentVersion",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ConcurrentModificationError(**data)


class DiscountCodeNonApplicableErrorSchema(ErrorObjectSchema):
    discount_code = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="discountCode",
    )
    reason = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    dicount_code_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="dicountCodeId",
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="validFrom",
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="validUntil",
    )
    validity_check_time = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="validityCheckTime",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.DiscountCodeNonApplicableError(**data)


class DuplicateAttributeValueErrorSchema(ErrorObjectSchema):
    attribute = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.AttributeSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.DuplicateAttributeValueError(**data)


class DuplicateAttributeValuesErrorSchema(ErrorObjectSchema):
    attributes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.AttributeSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.DuplicateAttributeValuesError(**data)


class DuplicateEnumValuesErrorSchema(ErrorObjectSchema):
    duplicates = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.DuplicateEnumValuesError(**data)


class DuplicateFieldErrorSchema(ErrorObjectSchema):
    field = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    duplicate_value = marshmallow.fields.Raw(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="duplicateValue",
    )
    conflicting_resource = helpers.Discriminator(
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
        data_key="conflictingResource",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.DuplicateFieldError(**data)


class DuplicateFieldWithConflictingResourceErrorSchema(ErrorObjectSchema):
    field = marshmallow.fields.String(allow_none=True, missing=None)
    duplicate_value = marshmallow.fields.Raw(
        allow_none=True, missing=None, data_key="duplicateValue"
    )
    conflicting_resource = helpers.Discriminator(
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
        data_key="conflictingResource",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.DuplicateFieldWithConflictingResourceError(**data)


class DuplicatePriceScopeErrorSchema(ErrorObjectSchema):
    conflicting_prices = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="conflictingPrices",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.DuplicatePriceScopeError(**data)


class DuplicateVariantValuesErrorSchema(ErrorObjectSchema):
    variant_values = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".VariantValuesSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="variantValues",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.DuplicateVariantValuesError(**data)


class EditPreviewFailedErrorSchema(ErrorObjectSchema):
    result = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order_edit.OrderEditPreviewFailureSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.EditPreviewFailedError(**data)


class EnumKeyAlreadyExistsErrorSchema(ErrorObjectSchema):
    conflicting_enum_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="conflictingEnumKey"
    )
    conflicting_attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="conflictingAttributeName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.EnumKeyAlreadyExistsError(**data)


class EnumKeyDoesNotExistErrorSchema(ErrorObjectSchema):
    conflicting_enum_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="conflictingEnumKey"
    )
    conflicting_attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="conflictingAttributeName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.EnumKeyDoesNotExistError(**data)


class EnumValueIsUsedErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.EnumValueIsUsedError(**data)


class EnumValuesMustMatchErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.EnumValuesMustMatchError(**data)


class ErrorResponseSchema(helpers.BaseSchema):
    status_code = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="statusCode"
    )
    message = marshmallow.fields.String(allow_none=True, missing=None)
    error = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    error_description = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    errors = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("code", "code"),
            discriminator_schemas={
                "access_denied": helpers.absmod(__name__, ".AccessDeniedErrorSchema"),
                "AnonymousIdAlreadyInUse": helpers.absmod(
                    __name__, ".AnonymousIdAlreadyInUseErrorSchema"
                ),
                "AttributeDefinitionAlreadyExists": helpers.absmod(
                    __name__, ".AttributeDefinitionAlreadyExistsErrorSchema"
                ),
                "AttributeDefinitionTypeConflict": helpers.absmod(
                    __name__, ".AttributeDefinitionTypeConflictErrorSchema"
                ),
                "AttributeNameDoesNotExist": helpers.absmod(
                    __name__, ".AttributeNameDoesNotExistErrorSchema"
                ),
                "ConcurrentModification": helpers.absmod(
                    __name__, ".ConcurrentModificationErrorSchema"
                ),
                "DiscountCodeNonApplicable": helpers.absmod(
                    __name__, ".DiscountCodeNonApplicableErrorSchema"
                ),
                "DuplicateAttributeValue": helpers.absmod(
                    __name__, ".DuplicateAttributeValueErrorSchema"
                ),
                "DuplicateAttributeValues": helpers.absmod(
                    __name__, ".DuplicateAttributeValuesErrorSchema"
                ),
                "DuplicateEnumValues": helpers.absmod(
                    __name__, ".DuplicateEnumValuesErrorSchema"
                ),
                "DuplicateField": helpers.absmod(
                    __name__, ".DuplicateFieldErrorSchema"
                ),
                "DuplicateFieldWithConflictingResource": helpers.absmod(
                    __name__, ".DuplicateFieldWithConflictingResourceErrorSchema"
                ),
                "DuplicatePriceScope": helpers.absmod(
                    __name__, ".DuplicatePriceScopeErrorSchema"
                ),
                "DuplicateVariantValues": helpers.absmod(
                    __name__, ".DuplicateVariantValuesErrorSchema"
                ),
                "EditPreviewFailed": helpers.absmod(
                    __name__, ".EditPreviewFailedErrorSchema"
                ),
                "EnumKeyAlreadyExists": helpers.absmod(
                    __name__, ".EnumKeyAlreadyExistsErrorSchema"
                ),
                "EnumKeyDoesNotExist": helpers.absmod(
                    __name__, ".EnumKeyDoesNotExistErrorSchema"
                ),
                "EnumValueIsUsed": helpers.absmod(
                    __name__, ".EnumValueIsUsedErrorSchema"
                ),
                "EnumValuesMustMatch": helpers.absmod(
                    __name__, ".EnumValuesMustMatchErrorSchema"
                ),
                "ExtensionBadResponse": helpers.absmod(
                    __name__, ".ExtensionBadResponseErrorSchema"
                ),
                "ExtensionNoResponse": helpers.absmod(
                    __name__, ".ExtensionNoResponseErrorSchema"
                ),
                "ExtensionUpdateActionsFailed": helpers.absmod(
                    __name__, ".ExtensionUpdateActionsFailedErrorSchema"
                ),
                "ExternalOAuthFailed": helpers.absmod(
                    __name__, ".ExternalOAuthFailedErrorSchema"
                ),
                "FeatureRemoved": helpers.absmod(
                    __name__, ".FeatureRemovedErrorSchema"
                ),
                "General": helpers.absmod(__name__, ".GeneralErrorSchema"),
                "insufficient_scope": helpers.absmod(
                    __name__, ".InsufficientScopeErrorSchema"
                ),
                "InternalConstraintViolated": helpers.absmod(
                    __name__, ".InternalConstraintViolatedErrorSchema"
                ),
                "InvalidCredentials": helpers.absmod(
                    __name__, ".InvalidCredentialsErrorSchema"
                ),
                "InvalidCurrentPassword": helpers.absmod(
                    __name__, ".InvalidCurrentPasswordErrorSchema"
                ),
                "InvalidField": helpers.absmod(__name__, ".InvalidFieldErrorSchema"),
                "InvalidInput": helpers.absmod(__name__, ".InvalidInputErrorSchema"),
                "InvalidItemShippingDetails": helpers.absmod(
                    __name__, ".InvalidItemShippingDetailsErrorSchema"
                ),
                "InvalidJsonInput": helpers.absmod(
                    __name__, ".InvalidJsonInputErrorSchema"
                ),
                "InvalidOperation": helpers.absmod(
                    __name__, ".InvalidOperationErrorSchema"
                ),
                "InvalidSubject": helpers.absmod(
                    __name__, ".InvalidSubjectErrorSchema"
                ),
                "invalid_token": helpers.absmod(__name__, ".InvalidTokenErrorSchema"),
                "LanguageUsedInStores": helpers.absmod(
                    __name__, ".LanguageUsedInStoresErrorSchema"
                ),
                "MatchingPriceNotFound": helpers.absmod(
                    __name__, ".MatchingPriceNotFoundErrorSchema"
                ),
                "MaxResourceLimitExceeded": helpers.absmod(
                    __name__, ".MaxResourceLimitExceededErrorSchema"
                ),
                "MissingRoleOnChannel": helpers.absmod(
                    __name__, ".MissingRoleOnChannelErrorSchema"
                ),
                "MissingTaxRateForCountry": helpers.absmod(
                    __name__, ".MissingTaxRateForCountryErrorSchema"
                ),
                "NoMatchingProductDiscountFound": helpers.absmod(
                    __name__, ".NoMatchingProductDiscountFoundErrorSchema"
                ),
                "NotEnabled": helpers.absmod(__name__, ".NotEnabledErrorSchema"),
                "ObjectNotFound": helpers.absmod(
                    __name__, ".ObjectNotFoundErrorSchema"
                ),
                "OutOfStock": helpers.absmod(__name__, ".OutOfStockErrorSchema"),
                "OverCapacity": helpers.absmod(__name__, ".OverCapacityErrorSchema"),
                "PendingOperation": helpers.absmod(
                    __name__, ".PendingOperationErrorSchema"
                ),
                "PriceChanged": helpers.absmod(__name__, ".PriceChangedErrorSchema"),
                "ProjectNotConfiguredForLanguages": helpers.absmod(
                    __name__, ".ProjectNotConfiguredForLanguagesErrorSchema"
                ),
                "QueryComplexityLimitExceeded": helpers.absmod(
                    __name__, ".QueryComplexityLimitExceededErrorSchema"
                ),
                "QueryTimedOut": helpers.absmod(__name__, ".QueryTimedOutErrorSchema"),
                "ReferenceExists": helpers.absmod(
                    __name__, ".ReferenceExistsErrorSchema"
                ),
                "ReferencedResourceNotFound": helpers.absmod(
                    __name__, ".ReferencedResourceNotFoundErrorSchema"
                ),
                "RequiredField": helpers.absmod(__name__, ".RequiredFieldErrorSchema"),
                "ResourceNotFound": helpers.absmod(
                    __name__, ".ResourceNotFoundErrorSchema"
                ),
                "ResourceSizeLimitExceeded": helpers.absmod(
                    __name__, ".ResourceSizeLimitExceededErrorSchema"
                ),
                "SearchExecutionFailure": helpers.absmod(
                    __name__, ".SearchExecutionFailureErrorSchema"
                ),
                "SearchFacetPathNotFound": helpers.absmod(
                    __name__, ".SearchFacetPathNotFoundErrorSchema"
                ),
                "SemanticError": helpers.absmod(__name__, ".SemanticErrorErrorSchema"),
                "ShippingMethodDoesNotMatchCart": helpers.absmod(
                    __name__, ".ShippingMethodDoesNotMatchCartErrorSchema"
                ),
                "SyntaxError": helpers.absmod(__name__, ".SyntaxErrorErrorSchema"),
                "WeakPassword": helpers.absmod(__name__, ".WeakPasswordErrorSchema"),
            },
        ),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ErrorResponse(**data)


class ExtensionBadResponseErrorSchema(ErrorObjectSchema):
    localized_message = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="localizedMessage",
    )
    extension_extra_info = marshmallow.fields.Raw(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="extensionExtraInfo",
    )
    error_by_extension = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ErrorByExtensionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="errorByExtension",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ExtensionBadResponseError(**data)


class ExtensionNoResponseErrorSchema(ErrorObjectSchema):
    extension_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="extensionId"
    )
    extension_key = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="extensionKey",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ExtensionNoResponseError(**data)


class ExtensionUpdateActionsFailedErrorSchema(ErrorObjectSchema):
    localized_message = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="localizedMessage",
    )
    extension_extra_info = marshmallow.fields.Raw(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="extensionExtraInfo",
    )
    error_by_extension = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ErrorByExtensionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="errorByExtension",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ExtensionUpdateActionsFailedError(**data)


class ExternalOAuthFailedErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ExternalOAuthFailedError(**data)


class FeatureRemovedErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.FeatureRemovedError(**data)


class GeneralErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.GeneralError(**data)


class InsufficientScopeErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InsufficientScopeError(**data)


class InternalConstraintViolatedErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InternalConstraintViolatedError(**data)


class InvalidCredentialsErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidCredentialsError(**data)


class InvalidCurrentPasswordErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidCurrentPasswordError(**data)


class InvalidFieldErrorSchema(ErrorObjectSchema):
    field = marshmallow.fields.String(allow_none=True, missing=None)
    invalid_value = marshmallow.fields.Raw(
        allow_none=True, missing=None, data_key="invalidValue"
    )
    allowed_values = marshmallow.fields.List(
        marshmallow.fields.Raw(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="allowedValues",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidFieldError(**data)


class InvalidInputErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidInputError(**data)


class InvalidItemShippingDetailsErrorSchema(ErrorObjectSchema):
    subject = marshmallow.fields.String(allow_none=True, missing=None)
    item_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="itemId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidItemShippingDetailsError(**data)


class InvalidJsonInputErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidJsonInputError(**data)


class InvalidOperationErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidOperationError(**data)


class InvalidSubjectErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidSubjectError(**data)


class InvalidTokenErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidTokenError(**data)


class LanguageUsedInStoresErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.LanguageUsedInStoresError(**data)


class MatchingPriceNotFoundErrorSchema(ErrorObjectSchema):
    product_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="productId"
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    currency = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    country = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.MatchingPriceNotFoundError(**data)


class MaxResourceLimitExceededErrorSchema(ErrorObjectSchema):
    exceeded_resource = marshmallow_enum.EnumField(
        ReferenceTypeId,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="exceededResource",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.MaxResourceLimitExceededError(**data)


class MissingRoleOnChannelErrorSchema(ErrorObjectSchema):
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    missing_role = marshmallow_enum.EnumField(
        ChannelRoleEnum,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="missingRole",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.MissingRoleOnChannelError(**data)


class MissingTaxRateForCountryErrorSchema(ErrorObjectSchema):
    tax_category_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="taxCategoryId"
    )
    country = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    state = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.MissingTaxRateForCountryError(**data)


class NoMatchingProductDiscountFoundErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.NoMatchingProductDiscountFoundError(**data)


class NotEnabledErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.NotEnabledError(**data)


class ObjectNotFoundErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ObjectNotFoundError(**data)


class OutOfStockErrorSchema(ErrorObjectSchema):
    line_items = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="lineItems",
    )
    skus = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.OutOfStockError(**data)


class OverCapacityErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.OverCapacityError(**data)


class PendingOperationErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.PendingOperationError(**data)


class PriceChangedErrorSchema(ErrorObjectSchema):
    line_items = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="lineItems",
    )
    shipping = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.PriceChangedError(**data)


class ProjectNotConfiguredForLanguagesErrorSchema(ErrorObjectSchema):
    languages = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ProjectNotConfiguredForLanguagesError(**data)


class QueryComplexityLimitExceededErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.QueryComplexityLimitExceededError(**data)


class QueryTimedOutErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.QueryTimedOutError(**data)


class ReferenceExistsErrorSchema(ErrorObjectSchema):
    referenced_by = marshmallow_enum.EnumField(
        ReferenceTypeId,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="referencedBy",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ReferenceExistsError(**data)


class ReferencedResourceNotFoundErrorSchema(ErrorObjectSchema):
    type_id = marshmallow_enum.EnumField(
        ReferenceTypeId, by_value=True, allow_none=True, missing=None, data_key="typeId"
    )
    id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ReferencedResourceNotFoundError(**data)


class RequiredFieldErrorSchema(ErrorObjectSchema):
    field = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.RequiredFieldError(**data)


class ResourceNotFoundErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ResourceNotFoundError(**data)


class ResourceSizeLimitExceededErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ResourceSizeLimitExceededError(**data)


class SearchExecutionFailureErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.SearchExecutionFailureError(**data)


class SearchFacetPathNotFoundErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.SearchFacetPathNotFoundError(**data)


class SemanticErrorErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.SemanticErrorError(**data)


class ShippingMethodDoesNotMatchCartErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ShippingMethodDoesNotMatchCartError(**data)


class SyntaxErrorErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.SyntaxErrorError(**data)


class VariantValuesSchema(helpers.BaseSchema):
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    prices = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    attributes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.AttributeSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.VariantValues(**data)


class WeakPasswordErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.WeakPasswordError(**data)

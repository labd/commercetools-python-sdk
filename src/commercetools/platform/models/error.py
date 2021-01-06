# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .channel import ChannelRoleEnum
from .common import ReferenceTypeId

if typing.TYPE_CHECKING:
    from .channel import ChannelReference, ChannelResourceIdentifier, ChannelRoleEnum
    from .common import LocalizedString, Price, PriceDraft, Reference, ReferenceTypeId
    from .customer_group import CustomerGroupReference
    from .order_edit import OrderEditPreviewFailure
    from .product import Attribute

__all__ = [
    "AccessDeniedError",
    "AnonymousIdAlreadyInUseError",
    "AttributeDefinitionAlreadyExistsError",
    "AttributeDefinitionTypeConflictError",
    "AttributeNameDoesNotExistError",
    "ConcurrentModificationError",
    "DiscountCodeNonApplicableError",
    "DuplicateAttributeValueError",
    "DuplicateAttributeValuesError",
    "DuplicateEnumValuesError",
    "DuplicateFieldError",
    "DuplicateFieldWithConflictingResourceError",
    "DuplicatePriceScopeError",
    "DuplicateVariantValuesError",
    "EditPreviewFailedError",
    "EnumKeyAlreadyExistsError",
    "EnumKeyDoesNotExistError",
    "EnumValueIsUsedError",
    "EnumValuesMustMatchError",
    "ErrorByExtension",
    "ErrorObject",
    "ErrorResponse",
    "ExtensionBadResponseError",
    "ExtensionNoResponseError",
    "ExtensionUpdateActionsFailedError",
    "ExternalOAuthFailedError",
    "FeatureRemovedError",
    "GeneralError",
    "InsufficientScopeError",
    "InternalConstraintViolatedError",
    "InvalidCredentialsError",
    "InvalidCurrentPasswordError",
    "InvalidFieldError",
    "InvalidInputError",
    "InvalidItemShippingDetailsError",
    "InvalidJsonInputError",
    "InvalidOperationError",
    "InvalidSubjectError",
    "InvalidTokenError",
    "LanguageUsedInStoresError",
    "MatchingPriceNotFoundError",
    "MaxResourceLimitExceededError",
    "MissingRoleOnChannelError",
    "MissingTaxRateForCountryError",
    "NoMatchingProductDiscountFoundError",
    "NotEnabledError",
    "ObjectNotFoundError",
    "OutOfStockError",
    "OverCapacityError",
    "PendingOperationError",
    "PriceChangedError",
    "ProjectNotConfiguredForLanguagesError",
    "QueryComplexityLimitExceededError",
    "QueryTimedOutError",
    "ReferenceExistsError",
    "ReferencedResourceNotFoundError",
    "RequiredFieldError",
    "ResourceNotFoundError",
    "ResourceSizeLimitExceededError",
    "SearchExecutionFailureError",
    "SearchFacetPathNotFoundError",
    "SemanticErrorError",
    "ShippingMethodDoesNotMatchCartError",
    "SyntaxErrorError",
    "VariantValues",
    "WeakPasswordError",
]


class ErrorByExtension(_BaseType):
    id: str
    key: typing.Optional[str]

    def __init__(self, *, id: str, key: typing.Optional[str] = None):
        self.id = id
        self.key = key
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ErrorByExtension":
        from ._schemas.error import ErrorByExtensionSchema

        return ErrorByExtensionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ErrorByExtensionSchema

        return ErrorByExtensionSchema().dump(self)


class ErrorObject(_BaseType):
    code: str
    message: str

    def __init__(self, *, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ErrorObject":
        if data["code"] == "access_denied":
            from ._schemas.error import AccessDeniedErrorSchema

            return AccessDeniedErrorSchema().load(data)
        if data["code"] == "AnonymousIdAlreadyInUse":
            from ._schemas.error import AnonymousIdAlreadyInUseErrorSchema

            return AnonymousIdAlreadyInUseErrorSchema().load(data)
        if data["code"] == "AttributeDefinitionAlreadyExists":
            from ._schemas.error import AttributeDefinitionAlreadyExistsErrorSchema

            return AttributeDefinitionAlreadyExistsErrorSchema().load(data)
        if data["code"] == "AttributeDefinitionTypeConflict":
            from ._schemas.error import AttributeDefinitionTypeConflictErrorSchema

            return AttributeDefinitionTypeConflictErrorSchema().load(data)
        if data["code"] == "AttributeNameDoesNotExist":
            from ._schemas.error import AttributeNameDoesNotExistErrorSchema

            return AttributeNameDoesNotExistErrorSchema().load(data)
        if data["code"] == "ConcurrentModification":
            from ._schemas.error import ConcurrentModificationErrorSchema

            return ConcurrentModificationErrorSchema().load(data)
        if data["code"] == "DiscountCodeNonApplicable":
            from ._schemas.error import DiscountCodeNonApplicableErrorSchema

            return DiscountCodeNonApplicableErrorSchema().load(data)
        if data["code"] == "DuplicateAttributeValue":
            from ._schemas.error import DuplicateAttributeValueErrorSchema

            return DuplicateAttributeValueErrorSchema().load(data)
        if data["code"] == "DuplicateAttributeValues":
            from ._schemas.error import DuplicateAttributeValuesErrorSchema

            return DuplicateAttributeValuesErrorSchema().load(data)
        if data["code"] == "DuplicateEnumValues":
            from ._schemas.error import DuplicateEnumValuesErrorSchema

            return DuplicateEnumValuesErrorSchema().load(data)
        if data["code"] == "DuplicateField":
            from ._schemas.error import DuplicateFieldErrorSchema

            return DuplicateFieldErrorSchema().load(data)
        if data["code"] == "DuplicateFieldWithConflictingResource":
            from ._schemas.error import DuplicateFieldWithConflictingResourceErrorSchema

            return DuplicateFieldWithConflictingResourceErrorSchema().load(data)
        if data["code"] == "DuplicatePriceScope":
            from ._schemas.error import DuplicatePriceScopeErrorSchema

            return DuplicatePriceScopeErrorSchema().load(data)
        if data["code"] == "DuplicateVariantValues":
            from ._schemas.error import DuplicateVariantValuesErrorSchema

            return DuplicateVariantValuesErrorSchema().load(data)
        if data["code"] == "EditPreviewFailed":
            from ._schemas.error import EditPreviewFailedErrorSchema

            return EditPreviewFailedErrorSchema().load(data)
        if data["code"] == "EnumKeyAlreadyExists":
            from ._schemas.error import EnumKeyAlreadyExistsErrorSchema

            return EnumKeyAlreadyExistsErrorSchema().load(data)
        if data["code"] == "EnumKeyDoesNotExist":
            from ._schemas.error import EnumKeyDoesNotExistErrorSchema

            return EnumKeyDoesNotExistErrorSchema().load(data)
        if data["code"] == "EnumValueIsUsed":
            from ._schemas.error import EnumValueIsUsedErrorSchema

            return EnumValueIsUsedErrorSchema().load(data)
        if data["code"] == "EnumValuesMustMatch":
            from ._schemas.error import EnumValuesMustMatchErrorSchema

            return EnumValuesMustMatchErrorSchema().load(data)
        if data["code"] == "ExtensionBadResponse":
            from ._schemas.error import ExtensionBadResponseErrorSchema

            return ExtensionBadResponseErrorSchema().load(data)
        if data["code"] == "ExtensionNoResponse":
            from ._schemas.error import ExtensionNoResponseErrorSchema

            return ExtensionNoResponseErrorSchema().load(data)
        if data["code"] == "ExtensionUpdateActionsFailed":
            from ._schemas.error import ExtensionUpdateActionsFailedErrorSchema

            return ExtensionUpdateActionsFailedErrorSchema().load(data)
        if data["code"] == "ExternalOAuthFailed":
            from ._schemas.error import ExternalOAuthFailedErrorSchema

            return ExternalOAuthFailedErrorSchema().load(data)
        if data["code"] == "FeatureRemoved":
            from ._schemas.error import FeatureRemovedErrorSchema

            return FeatureRemovedErrorSchema().load(data)
        if data["code"] == "General":
            from ._schemas.error import GeneralErrorSchema

            return GeneralErrorSchema().load(data)
        if data["code"] == "insufficient_scope":
            from ._schemas.error import InsufficientScopeErrorSchema

            return InsufficientScopeErrorSchema().load(data)
        if data["code"] == "InternalConstraintViolated":
            from ._schemas.error import InternalConstraintViolatedErrorSchema

            return InternalConstraintViolatedErrorSchema().load(data)
        if data["code"] == "InvalidCredentials":
            from ._schemas.error import InvalidCredentialsErrorSchema

            return InvalidCredentialsErrorSchema().load(data)
        if data["code"] == "InvalidCurrentPassword":
            from ._schemas.error import InvalidCurrentPasswordErrorSchema

            return InvalidCurrentPasswordErrorSchema().load(data)
        if data["code"] == "InvalidField":
            from ._schemas.error import InvalidFieldErrorSchema

            return InvalidFieldErrorSchema().load(data)
        if data["code"] == "InvalidInput":
            from ._schemas.error import InvalidInputErrorSchema

            return InvalidInputErrorSchema().load(data)
        if data["code"] == "InvalidItemShippingDetails":
            from ._schemas.error import InvalidItemShippingDetailsErrorSchema

            return InvalidItemShippingDetailsErrorSchema().load(data)
        if data["code"] == "InvalidJsonInput":
            from ._schemas.error import InvalidJsonInputErrorSchema

            return InvalidJsonInputErrorSchema().load(data)
        if data["code"] == "InvalidOperation":
            from ._schemas.error import InvalidOperationErrorSchema

            return InvalidOperationErrorSchema().load(data)
        if data["code"] == "InvalidSubject":
            from ._schemas.error import InvalidSubjectErrorSchema

            return InvalidSubjectErrorSchema().load(data)
        if data["code"] == "invalid_token":
            from ._schemas.error import InvalidTokenErrorSchema

            return InvalidTokenErrorSchema().load(data)
        if data["code"] == "LanguageUsedInStores":
            from ._schemas.error import LanguageUsedInStoresErrorSchema

            return LanguageUsedInStoresErrorSchema().load(data)
        if data["code"] == "MatchingPriceNotFound":
            from ._schemas.error import MatchingPriceNotFoundErrorSchema

            return MatchingPriceNotFoundErrorSchema().load(data)
        if data["code"] == "MaxResourceLimitExceeded":
            from ._schemas.error import MaxResourceLimitExceededErrorSchema

            return MaxResourceLimitExceededErrorSchema().load(data)
        if data["code"] == "MissingRoleOnChannel":
            from ._schemas.error import MissingRoleOnChannelErrorSchema

            return MissingRoleOnChannelErrorSchema().load(data)
        if data["code"] == "MissingTaxRateForCountry":
            from ._schemas.error import MissingTaxRateForCountryErrorSchema

            return MissingTaxRateForCountryErrorSchema().load(data)
        if data["code"] == "NoMatchingProductDiscountFound":
            from ._schemas.error import NoMatchingProductDiscountFoundErrorSchema

            return NoMatchingProductDiscountFoundErrorSchema().load(data)
        if data["code"] == "NotEnabled":
            from ._schemas.error import NotEnabledErrorSchema

            return NotEnabledErrorSchema().load(data)
        if data["code"] == "ObjectNotFound":
            from ._schemas.error import ObjectNotFoundErrorSchema

            return ObjectNotFoundErrorSchema().load(data)
        if data["code"] == "OutOfStock":
            from ._schemas.error import OutOfStockErrorSchema

            return OutOfStockErrorSchema().load(data)
        if data["code"] == "OverCapacity":
            from ._schemas.error import OverCapacityErrorSchema

            return OverCapacityErrorSchema().load(data)
        if data["code"] == "PendingOperation":
            from ._schemas.error import PendingOperationErrorSchema

            return PendingOperationErrorSchema().load(data)
        if data["code"] == "PriceChanged":
            from ._schemas.error import PriceChangedErrorSchema

            return PriceChangedErrorSchema().load(data)
        if data["code"] == "ProjectNotConfiguredForLanguages":
            from ._schemas.error import ProjectNotConfiguredForLanguagesErrorSchema

            return ProjectNotConfiguredForLanguagesErrorSchema().load(data)
        if data["code"] == "QueryComplexityLimitExceeded":
            from ._schemas.error import QueryComplexityLimitExceededErrorSchema

            return QueryComplexityLimitExceededErrorSchema().load(data)
        if data["code"] == "QueryTimedOut":
            from ._schemas.error import QueryTimedOutErrorSchema

            return QueryTimedOutErrorSchema().load(data)
        if data["code"] == "ReferenceExists":
            from ._schemas.error import ReferenceExistsErrorSchema

            return ReferenceExistsErrorSchema().load(data)
        if data["code"] == "ReferencedResourceNotFound":
            from ._schemas.error import ReferencedResourceNotFoundErrorSchema

            return ReferencedResourceNotFoundErrorSchema().load(data)
        if data["code"] == "RequiredField":
            from ._schemas.error import RequiredFieldErrorSchema

            return RequiredFieldErrorSchema().load(data)
        if data["code"] == "ResourceNotFound":
            from ._schemas.error import ResourceNotFoundErrorSchema

            return ResourceNotFoundErrorSchema().load(data)
        if data["code"] == "ResourceSizeLimitExceeded":
            from ._schemas.error import ResourceSizeLimitExceededErrorSchema

            return ResourceSizeLimitExceededErrorSchema().load(data)
        if data["code"] == "SearchExecutionFailure":
            from ._schemas.error import SearchExecutionFailureErrorSchema

            return SearchExecutionFailureErrorSchema().load(data)
        if data["code"] == "SearchFacetPathNotFound":
            from ._schemas.error import SearchFacetPathNotFoundErrorSchema

            return SearchFacetPathNotFoundErrorSchema().load(data)
        if data["code"] == "SemanticError":
            from ._schemas.error import SemanticErrorErrorSchema

            return SemanticErrorErrorSchema().load(data)
        if data["code"] == "ShippingMethodDoesNotMatchCart":
            from ._schemas.error import ShippingMethodDoesNotMatchCartErrorSchema

            return ShippingMethodDoesNotMatchCartErrorSchema().load(data)
        if data["code"] == "SyntaxError":
            from ._schemas.error import SyntaxErrorErrorSchema

            return SyntaxErrorErrorSchema().load(data)
        if data["code"] == "WeakPassword":
            from ._schemas.error import WeakPasswordErrorSchema

            return WeakPasswordErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ErrorObjectSchema

        return ErrorObjectSchema().dump(self)


class AccessDeniedError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="access_denied")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AccessDeniedError":
        from ._schemas.error import AccessDeniedErrorSchema

        return AccessDeniedErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import AccessDeniedErrorSchema

        return AccessDeniedErrorSchema().dump(self)


class AnonymousIdAlreadyInUseError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="AnonymousIdAlreadyInUse")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AnonymousIdAlreadyInUseError":
        from ._schemas.error import AnonymousIdAlreadyInUseErrorSchema

        return AnonymousIdAlreadyInUseErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import AnonymousIdAlreadyInUseErrorSchema

        return AnonymousIdAlreadyInUseErrorSchema().dump(self)


class AttributeDefinitionAlreadyExistsError(ErrorObject):
    conflicting_product_type_id: str
    conflicting_product_type_name: str
    conflicting_attribute_name: str

    def __init__(
        self,
        *,
        message: str,
        conflicting_product_type_id: str,
        conflicting_product_type_name: str,
        conflicting_attribute_name: str
    ):
        self.conflicting_product_type_id = conflicting_product_type_id
        self.conflicting_product_type_name = conflicting_product_type_name
        self.conflicting_attribute_name = conflicting_attribute_name
        super().__init__(message=message, code="AttributeDefinitionAlreadyExists")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeDefinitionAlreadyExistsError":
        from ._schemas.error import AttributeDefinitionAlreadyExistsErrorSchema

        return AttributeDefinitionAlreadyExistsErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import AttributeDefinitionAlreadyExistsErrorSchema

        return AttributeDefinitionAlreadyExistsErrorSchema().dump(self)


class AttributeDefinitionTypeConflictError(ErrorObject):
    conflicting_product_type_id: str
    conflicting_product_type_name: str
    conflicting_attribute_name: str

    def __init__(
        self,
        *,
        message: str,
        conflicting_product_type_id: str,
        conflicting_product_type_name: str,
        conflicting_attribute_name: str
    ):
        self.conflicting_product_type_id = conflicting_product_type_id
        self.conflicting_product_type_name = conflicting_product_type_name
        self.conflicting_attribute_name = conflicting_attribute_name
        super().__init__(message=message, code="AttributeDefinitionTypeConflict")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeDefinitionTypeConflictError":
        from ._schemas.error import AttributeDefinitionTypeConflictErrorSchema

        return AttributeDefinitionTypeConflictErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import AttributeDefinitionTypeConflictErrorSchema

        return AttributeDefinitionTypeConflictErrorSchema().dump(self)


class AttributeNameDoesNotExistError(ErrorObject):
    invalid_attribute_name: str

    def __init__(self, *, message: str, invalid_attribute_name: str):
        self.invalid_attribute_name = invalid_attribute_name
        super().__init__(message=message, code="AttributeNameDoesNotExist")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeNameDoesNotExistError":
        from ._schemas.error import AttributeNameDoesNotExistErrorSchema

        return AttributeNameDoesNotExistErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import AttributeNameDoesNotExistErrorSchema

        return AttributeNameDoesNotExistErrorSchema().dump(self)


class ConcurrentModificationError(ErrorObject):
    current_version: typing.Optional[int]

    def __init__(self, *, message: str, current_version: typing.Optional[int] = None):
        self.current_version = current_version
        super().__init__(message=message, code="ConcurrentModification")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ConcurrentModificationError":
        from ._schemas.error import ConcurrentModificationErrorSchema

        return ConcurrentModificationErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ConcurrentModificationErrorSchema

        return ConcurrentModificationErrorSchema().dump(self)


class DiscountCodeNonApplicableError(ErrorObject):
    discount_code: typing.Optional[str]
    reason: typing.Optional[str]
    dicount_code_id: typing.Optional[str]
    valid_from: typing.Optional[datetime.datetime]
    valid_until: typing.Optional[datetime.datetime]
    validity_check_time: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        message: str,
        discount_code: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        dicount_code_id: typing.Optional[str] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        validity_check_time: typing.Optional[datetime.datetime] = None
    ):
        self.discount_code = discount_code
        self.reason = reason
        self.dicount_code_id = dicount_code_id
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.validity_check_time = validity_check_time
        super().__init__(message=message, code="DiscountCodeNonApplicable")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeNonApplicableError":
        from ._schemas.error import DiscountCodeNonApplicableErrorSchema

        return DiscountCodeNonApplicableErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import DiscountCodeNonApplicableErrorSchema

        return DiscountCodeNonApplicableErrorSchema().dump(self)


class DuplicateAttributeValueError(ErrorObject):
    attribute: "Attribute"

    def __init__(self, *, message: str, attribute: "Attribute"):
        self.attribute = attribute
        super().__init__(message=message, code="DuplicateAttributeValue")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DuplicateAttributeValueError":
        from ._schemas.error import DuplicateAttributeValueErrorSchema

        return DuplicateAttributeValueErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import DuplicateAttributeValueErrorSchema

        return DuplicateAttributeValueErrorSchema().dump(self)


class DuplicateAttributeValuesError(ErrorObject):
    attributes: typing.List["Attribute"]

    def __init__(self, *, message: str, attributes: typing.List["Attribute"]):
        self.attributes = attributes
        super().__init__(message=message, code="DuplicateAttributeValues")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DuplicateAttributeValuesError":
        from ._schemas.error import DuplicateAttributeValuesErrorSchema

        return DuplicateAttributeValuesErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import DuplicateAttributeValuesErrorSchema

        return DuplicateAttributeValuesErrorSchema().dump(self)


class DuplicateEnumValuesError(ErrorObject):
    duplicates: typing.List["str"]

    def __init__(self, *, message: str, duplicates: typing.List["str"]):
        self.duplicates = duplicates
        super().__init__(message=message, code="DuplicateEnumValues")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DuplicateEnumValuesError":
        from ._schemas.error import DuplicateEnumValuesErrorSchema

        return DuplicateEnumValuesErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import DuplicateEnumValuesErrorSchema

        return DuplicateEnumValuesErrorSchema().dump(self)


class DuplicateFieldError(ErrorObject):
    field: typing.Optional[str]
    duplicate_value: typing.Optional[typing.Any]
    conflicting_resource: typing.Optional["Reference"]

    def __init__(
        self,
        *,
        message: str,
        field: typing.Optional[str] = None,
        duplicate_value: typing.Optional[typing.Any] = None,
        conflicting_resource: typing.Optional["Reference"] = None
    ):
        self.field = field
        self.duplicate_value = duplicate_value
        self.conflicting_resource = conflicting_resource
        super().__init__(message=message, code="DuplicateField")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DuplicateFieldError":
        from ._schemas.error import DuplicateFieldErrorSchema

        return DuplicateFieldErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import DuplicateFieldErrorSchema

        return DuplicateFieldErrorSchema().dump(self)


class DuplicateFieldWithConflictingResourceError(ErrorObject):
    field: str
    duplicate_value: typing.Any
    conflicting_resource: "Reference"

    def __init__(
        self,
        *,
        message: str,
        field: str,
        duplicate_value: typing.Any,
        conflicting_resource: "Reference"
    ):
        self.field = field
        self.duplicate_value = duplicate_value
        self.conflicting_resource = conflicting_resource
        super().__init__(message=message, code="DuplicateFieldWithConflictingResource")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DuplicateFieldWithConflictingResourceError":
        from ._schemas.error import DuplicateFieldWithConflictingResourceErrorSchema

        return DuplicateFieldWithConflictingResourceErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import DuplicateFieldWithConflictingResourceErrorSchema

        return DuplicateFieldWithConflictingResourceErrorSchema().dump(self)


class DuplicatePriceScopeError(ErrorObject):
    conflicting_prices: typing.List["Price"]

    def __init__(self, *, message: str, conflicting_prices: typing.List["Price"]):
        self.conflicting_prices = conflicting_prices
        super().__init__(message=message, code="DuplicatePriceScope")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DuplicatePriceScopeError":
        from ._schemas.error import DuplicatePriceScopeErrorSchema

        return DuplicatePriceScopeErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import DuplicatePriceScopeErrorSchema

        return DuplicatePriceScopeErrorSchema().dump(self)


class DuplicateVariantValuesError(ErrorObject):
    variant_values: "VariantValues"

    def __init__(self, *, message: str, variant_values: "VariantValues"):
        self.variant_values = variant_values
        super().__init__(message=message, code="DuplicateVariantValues")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DuplicateVariantValuesError":
        from ._schemas.error import DuplicateVariantValuesErrorSchema

        return DuplicateVariantValuesErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import DuplicateVariantValuesErrorSchema

        return DuplicateVariantValuesErrorSchema().dump(self)


class EditPreviewFailedError(ErrorObject):
    result: "OrderEditPreviewFailure"

    def __init__(self, *, message: str, result: "OrderEditPreviewFailure"):
        self.result = result
        super().__init__(message=message, code="EditPreviewFailed")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "EditPreviewFailedError":
        from ._schemas.error import EditPreviewFailedErrorSchema

        return EditPreviewFailedErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import EditPreviewFailedErrorSchema

        return EditPreviewFailedErrorSchema().dump(self)


class EnumKeyAlreadyExistsError(ErrorObject):
    conflicting_enum_key: str
    conflicting_attribute_name: str

    def __init__(
        self,
        *,
        message: str,
        conflicting_enum_key: str,
        conflicting_attribute_name: str
    ):
        self.conflicting_enum_key = conflicting_enum_key
        self.conflicting_attribute_name = conflicting_attribute_name
        super().__init__(message=message, code="EnumKeyAlreadyExists")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "EnumKeyAlreadyExistsError":
        from ._schemas.error import EnumKeyAlreadyExistsErrorSchema

        return EnumKeyAlreadyExistsErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import EnumKeyAlreadyExistsErrorSchema

        return EnumKeyAlreadyExistsErrorSchema().dump(self)


class EnumKeyDoesNotExistError(ErrorObject):
    conflicting_enum_key: str
    conflicting_attribute_name: str

    def __init__(
        self,
        *,
        message: str,
        conflicting_enum_key: str,
        conflicting_attribute_name: str
    ):
        self.conflicting_enum_key = conflicting_enum_key
        self.conflicting_attribute_name = conflicting_attribute_name
        super().__init__(message=message, code="EnumKeyDoesNotExist")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "EnumKeyDoesNotExistError":
        from ._schemas.error import EnumKeyDoesNotExistErrorSchema

        return EnumKeyDoesNotExistErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import EnumKeyDoesNotExistErrorSchema

        return EnumKeyDoesNotExistErrorSchema().dump(self)


class EnumValueIsUsedError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="EnumValueIsUsed")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "EnumValueIsUsedError":
        from ._schemas.error import EnumValueIsUsedErrorSchema

        return EnumValueIsUsedErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import EnumValueIsUsedErrorSchema

        return EnumValueIsUsedErrorSchema().dump(self)


class EnumValuesMustMatchError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="EnumValuesMustMatch")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "EnumValuesMustMatchError":
        from ._schemas.error import EnumValuesMustMatchErrorSchema

        return EnumValuesMustMatchErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import EnumValuesMustMatchErrorSchema

        return EnumValuesMustMatchErrorSchema().dump(self)


class ErrorResponse(_BaseType):
    status_code: int
    message: str
    error: typing.Optional[str]
    error_description: typing.Optional[str]
    errors: typing.Optional[typing.List["ErrorObject"]]

    def __init__(
        self,
        *,
        status_code: int,
        message: str,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        errors: typing.Optional[typing.List["ErrorObject"]] = None
    ):
        self.status_code = status_code
        self.message = message
        self.error = error
        self.error_description = error_description
        self.errors = errors
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ErrorResponse":
        from ._schemas.error import ErrorResponseSchema

        return ErrorResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ErrorResponseSchema

        return ErrorResponseSchema().dump(self)


class ExtensionBadResponseError(ErrorObject):
    localized_message: typing.Optional["LocalizedString"]
    extension_extra_info: typing.Optional[object]
    error_by_extension: "ErrorByExtension"

    def __init__(
        self,
        *,
        message: str,
        localized_message: typing.Optional["LocalizedString"] = None,
        extension_extra_info: typing.Optional[object] = None,
        error_by_extension: "ErrorByExtension"
    ):
        self.localized_message = localized_message
        self.extension_extra_info = extension_extra_info
        self.error_by_extension = error_by_extension
        super().__init__(message=message, code="ExtensionBadResponse")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExtensionBadResponseError":
        from ._schemas.error import ExtensionBadResponseErrorSchema

        return ExtensionBadResponseErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ExtensionBadResponseErrorSchema

        return ExtensionBadResponseErrorSchema().dump(self)


class ExtensionNoResponseError(ErrorObject):
    extension_id: str
    extension_key: typing.Optional[str]

    def __init__(
        self,
        *,
        message: str,
        extension_id: str,
        extension_key: typing.Optional[str] = None
    ):
        self.extension_id = extension_id
        self.extension_key = extension_key
        super().__init__(message=message, code="ExtensionNoResponse")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExtensionNoResponseError":
        from ._schemas.error import ExtensionNoResponseErrorSchema

        return ExtensionNoResponseErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ExtensionNoResponseErrorSchema

        return ExtensionNoResponseErrorSchema().dump(self)


class ExtensionUpdateActionsFailedError(ErrorObject):
    localized_message: typing.Optional["LocalizedString"]
    extension_extra_info: typing.Optional[object]
    error_by_extension: "ErrorByExtension"

    def __init__(
        self,
        *,
        message: str,
        localized_message: typing.Optional["LocalizedString"] = None,
        extension_extra_info: typing.Optional[object] = None,
        error_by_extension: "ErrorByExtension"
    ):
        self.localized_message = localized_message
        self.extension_extra_info = extension_extra_info
        self.error_by_extension = error_by_extension
        super().__init__(message=message, code="ExtensionUpdateActionsFailed")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExtensionUpdateActionsFailedError":
        from ._schemas.error import ExtensionUpdateActionsFailedErrorSchema

        return ExtensionUpdateActionsFailedErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ExtensionUpdateActionsFailedErrorSchema

        return ExtensionUpdateActionsFailedErrorSchema().dump(self)


class ExternalOAuthFailedError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="ExternalOAuthFailed")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExternalOAuthFailedError":
        from ._schemas.error import ExternalOAuthFailedErrorSchema

        return ExternalOAuthFailedErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ExternalOAuthFailedErrorSchema

        return ExternalOAuthFailedErrorSchema().dump(self)


class FeatureRemovedError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="FeatureRemoved")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "FeatureRemovedError":
        from ._schemas.error import FeatureRemovedErrorSchema

        return FeatureRemovedErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import FeatureRemovedErrorSchema

        return FeatureRemovedErrorSchema().dump(self)


class GeneralError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="General")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "GeneralError":
        from ._schemas.error import GeneralErrorSchema

        return GeneralErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import GeneralErrorSchema

        return GeneralErrorSchema().dump(self)


class InsufficientScopeError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="insufficient_scope")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InsufficientScopeError":
        from ._schemas.error import InsufficientScopeErrorSchema

        return InsufficientScopeErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import InsufficientScopeErrorSchema

        return InsufficientScopeErrorSchema().dump(self)


class InternalConstraintViolatedError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="InternalConstraintViolated")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InternalConstraintViolatedError":
        from ._schemas.error import InternalConstraintViolatedErrorSchema

        return InternalConstraintViolatedErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import InternalConstraintViolatedErrorSchema

        return InternalConstraintViolatedErrorSchema().dump(self)


class InvalidCredentialsError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="InvalidCredentials")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InvalidCredentialsError":
        from ._schemas.error import InvalidCredentialsErrorSchema

        return InvalidCredentialsErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import InvalidCredentialsErrorSchema

        return InvalidCredentialsErrorSchema().dump(self)


class InvalidCurrentPasswordError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="InvalidCurrentPassword")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InvalidCurrentPasswordError":
        from ._schemas.error import InvalidCurrentPasswordErrorSchema

        return InvalidCurrentPasswordErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import InvalidCurrentPasswordErrorSchema

        return InvalidCurrentPasswordErrorSchema().dump(self)


class InvalidFieldError(ErrorObject):
    field: str
    invalid_value: typing.Any
    allowed_values: typing.Optional[typing.List["typing.Any"]]

    def __init__(
        self,
        *,
        message: str,
        field: str,
        invalid_value: typing.Any,
        allowed_values: typing.Optional[typing.List["typing.Any"]] = None
    ):
        self.field = field
        self.invalid_value = invalid_value
        self.allowed_values = allowed_values
        super().__init__(message=message, code="InvalidField")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidFieldError":
        from ._schemas.error import InvalidFieldErrorSchema

        return InvalidFieldErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import InvalidFieldErrorSchema

        return InvalidFieldErrorSchema().dump(self)


class InvalidInputError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="InvalidInput")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidInputError":
        from ._schemas.error import InvalidInputErrorSchema

        return InvalidInputErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import InvalidInputErrorSchema

        return InvalidInputErrorSchema().dump(self)


class InvalidItemShippingDetailsError(ErrorObject):
    subject: str
    item_id: str

    def __init__(self, *, message: str, subject: str, item_id: str):
        self.subject = subject
        self.item_id = item_id
        super().__init__(message=message, code="InvalidItemShippingDetails")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InvalidItemShippingDetailsError":
        from ._schemas.error import InvalidItemShippingDetailsErrorSchema

        return InvalidItemShippingDetailsErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import InvalidItemShippingDetailsErrorSchema

        return InvalidItemShippingDetailsErrorSchema().dump(self)


class InvalidJsonInputError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="InvalidJsonInput")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidJsonInputError":
        from ._schemas.error import InvalidJsonInputErrorSchema

        return InvalidJsonInputErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import InvalidJsonInputErrorSchema

        return InvalidJsonInputErrorSchema().dump(self)


class InvalidOperationError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="InvalidOperation")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidOperationError":
        from ._schemas.error import InvalidOperationErrorSchema

        return InvalidOperationErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import InvalidOperationErrorSchema

        return InvalidOperationErrorSchema().dump(self)


class InvalidSubjectError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="InvalidSubject")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidSubjectError":
        from ._schemas.error import InvalidSubjectErrorSchema

        return InvalidSubjectErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import InvalidSubjectErrorSchema

        return InvalidSubjectErrorSchema().dump(self)


class InvalidTokenError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="invalid_token")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidTokenError":
        from ._schemas.error import InvalidTokenErrorSchema

        return InvalidTokenErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import InvalidTokenErrorSchema

        return InvalidTokenErrorSchema().dump(self)


class LanguageUsedInStoresError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="LanguageUsedInStores")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "LanguageUsedInStoresError":
        from ._schemas.error import LanguageUsedInStoresErrorSchema

        return LanguageUsedInStoresErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import LanguageUsedInStoresErrorSchema

        return LanguageUsedInStoresErrorSchema().dump(self)


class MatchingPriceNotFoundError(ErrorObject):
    product_id: str
    variant_id: int
    currency: typing.Optional[str]
    country: typing.Optional[str]
    customer_group: typing.Optional["CustomerGroupReference"]
    channel: typing.Optional["ChannelReference"]

    def __init__(
        self,
        *,
        message: str,
        product_id: str,
        variant_id: int,
        currency: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        channel: typing.Optional["ChannelReference"] = None
    ):
        self.product_id = product_id
        self.variant_id = variant_id
        self.currency = currency
        self.country = country
        self.customer_group = customer_group
        self.channel = channel
        super().__init__(message=message, code="MatchingPriceNotFound")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MatchingPriceNotFoundError":
        from ._schemas.error import MatchingPriceNotFoundErrorSchema

        return MatchingPriceNotFoundErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import MatchingPriceNotFoundErrorSchema

        return MatchingPriceNotFoundErrorSchema().dump(self)


class MaxResourceLimitExceededError(ErrorObject):
    exceeded_resource: "ReferenceTypeId"

    def __init__(self, *, message: str, exceeded_resource: "ReferenceTypeId"):
        self.exceeded_resource = exceeded_resource
        super().__init__(message=message, code="MaxResourceLimitExceeded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MaxResourceLimitExceededError":
        from ._schemas.error import MaxResourceLimitExceededErrorSchema

        return MaxResourceLimitExceededErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import MaxResourceLimitExceededErrorSchema

        return MaxResourceLimitExceededErrorSchema().dump(self)


class MissingRoleOnChannelError(ErrorObject):
    channel: typing.Optional["ChannelResourceIdentifier"]
    missing_role: "ChannelRoleEnum"

    def __init__(
        self,
        *,
        message: str,
        channel: typing.Optional["ChannelResourceIdentifier"] = None,
        missing_role: "ChannelRoleEnum"
    ):
        self.channel = channel
        self.missing_role = missing_role
        super().__init__(message=message, code="MissingRoleOnChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingRoleOnChannelError":
        from ._schemas.error import MissingRoleOnChannelErrorSchema

        return MissingRoleOnChannelErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import MissingRoleOnChannelErrorSchema

        return MissingRoleOnChannelErrorSchema().dump(self)


class MissingTaxRateForCountryError(ErrorObject):
    tax_category_id: str
    country: typing.Optional[str]
    state: typing.Optional[str]

    def __init__(
        self,
        *,
        message: str,
        tax_category_id: str,
        country: typing.Optional[str] = None,
        state: typing.Optional[str] = None
    ):
        self.tax_category_id = tax_category_id
        self.country = country
        self.state = state
        super().__init__(message=message, code="MissingTaxRateForCountry")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingTaxRateForCountryError":
        from ._schemas.error import MissingTaxRateForCountryErrorSchema

        return MissingTaxRateForCountryErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import MissingTaxRateForCountryErrorSchema

        return MissingTaxRateForCountryErrorSchema().dump(self)


class NoMatchingProductDiscountFoundError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="NoMatchingProductDiscountFound")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "NoMatchingProductDiscountFoundError":
        from ._schemas.error import NoMatchingProductDiscountFoundErrorSchema

        return NoMatchingProductDiscountFoundErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import NoMatchingProductDiscountFoundErrorSchema

        return NoMatchingProductDiscountFoundErrorSchema().dump(self)


class NotEnabledError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="NotEnabled")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "NotEnabledError":
        from ._schemas.error import NotEnabledErrorSchema

        return NotEnabledErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import NotEnabledErrorSchema

        return NotEnabledErrorSchema().dump(self)


class ObjectNotFoundError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="ObjectNotFound")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ObjectNotFoundError":
        from ._schemas.error import ObjectNotFoundErrorSchema

        return ObjectNotFoundErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ObjectNotFoundErrorSchema

        return ObjectNotFoundErrorSchema().dump(self)


class OutOfStockError(ErrorObject):
    line_items: typing.List["str"]
    skus: typing.List["str"]

    def __init__(
        self, *, message: str, line_items: typing.List["str"], skus: typing.List["str"]
    ):
        self.line_items = line_items
        self.skus = skus
        super().__init__(message=message, code="OutOfStock")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OutOfStockError":
        from ._schemas.error import OutOfStockErrorSchema

        return OutOfStockErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import OutOfStockErrorSchema

        return OutOfStockErrorSchema().dump(self)


class OverCapacityError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="OverCapacity")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OverCapacityError":
        from ._schemas.error import OverCapacityErrorSchema

        return OverCapacityErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import OverCapacityErrorSchema

        return OverCapacityErrorSchema().dump(self)


class PendingOperationError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="PendingOperation")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PendingOperationError":
        from ._schemas.error import PendingOperationErrorSchema

        return PendingOperationErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import PendingOperationErrorSchema

        return PendingOperationErrorSchema().dump(self)


class PriceChangedError(ErrorObject):
    line_items: typing.List["str"]
    shipping: bool

    def __init__(self, *, message: str, line_items: typing.List["str"], shipping: bool):
        self.line_items = line_items
        self.shipping = shipping
        super().__init__(message=message, code="PriceChanged")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceChangedError":
        from ._schemas.error import PriceChangedErrorSchema

        return PriceChangedErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import PriceChangedErrorSchema

        return PriceChangedErrorSchema().dump(self)


class ProjectNotConfiguredForLanguagesError(ErrorObject):
    languages: typing.Optional[typing.List["str"]]

    def __init__(
        self, *, message: str, languages: typing.Optional[typing.List["str"]] = None
    ):
        self.languages = languages
        super().__init__(message=message, code="ProjectNotConfiguredForLanguages")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectNotConfiguredForLanguagesError":
        from ._schemas.error import ProjectNotConfiguredForLanguagesErrorSchema

        return ProjectNotConfiguredForLanguagesErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ProjectNotConfiguredForLanguagesErrorSchema

        return ProjectNotConfiguredForLanguagesErrorSchema().dump(self)


class QueryComplexityLimitExceededError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="QueryComplexityLimitExceeded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QueryComplexityLimitExceededError":
        from ._schemas.error import QueryComplexityLimitExceededErrorSchema

        return QueryComplexityLimitExceededErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import QueryComplexityLimitExceededErrorSchema

        return QueryComplexityLimitExceededErrorSchema().dump(self)


class QueryTimedOutError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="QueryTimedOut")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "QueryTimedOutError":
        from ._schemas.error import QueryTimedOutErrorSchema

        return QueryTimedOutErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import QueryTimedOutErrorSchema

        return QueryTimedOutErrorSchema().dump(self)


class ReferenceExistsError(ErrorObject):
    referenced_by: typing.Optional["ReferenceTypeId"]

    def __init__(
        self, *, message: str, referenced_by: typing.Optional["ReferenceTypeId"] = None
    ):
        self.referenced_by = referenced_by
        super().__init__(message=message, code="ReferenceExists")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReferenceExistsError":
        from ._schemas.error import ReferenceExistsErrorSchema

        return ReferenceExistsErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ReferenceExistsErrorSchema

        return ReferenceExistsErrorSchema().dump(self)


class ReferencedResourceNotFoundError(ErrorObject):
    type_id: "ReferenceTypeId"
    id: typing.Optional[str]
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        message: str,
        type_id: "ReferenceTypeId",
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ):
        self.type_id = type_id
        self.id = id
        self.key = key
        super().__init__(message=message, code="ReferencedResourceNotFound")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReferencedResourceNotFoundError":
        from ._schemas.error import ReferencedResourceNotFoundErrorSchema

        return ReferencedResourceNotFoundErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ReferencedResourceNotFoundErrorSchema

        return ReferencedResourceNotFoundErrorSchema().dump(self)


class RequiredFieldError(ErrorObject):
    field: str

    def __init__(self, *, message: str, field: str):
        self.field = field
        super().__init__(message=message, code="RequiredField")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "RequiredFieldError":
        from ._schemas.error import RequiredFieldErrorSchema

        return RequiredFieldErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import RequiredFieldErrorSchema

        return RequiredFieldErrorSchema().dump(self)


class ResourceNotFoundError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="ResourceNotFound")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ResourceNotFoundError":
        from ._schemas.error import ResourceNotFoundErrorSchema

        return ResourceNotFoundErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ResourceNotFoundErrorSchema

        return ResourceNotFoundErrorSchema().dump(self)


class ResourceSizeLimitExceededError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="ResourceSizeLimitExceeded")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ResourceSizeLimitExceededError":
        from ._schemas.error import ResourceSizeLimitExceededErrorSchema

        return ResourceSizeLimitExceededErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ResourceSizeLimitExceededErrorSchema

        return ResourceSizeLimitExceededErrorSchema().dump(self)


class SearchExecutionFailureError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="SearchExecutionFailure")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchExecutionFailureError":
        from ._schemas.error import SearchExecutionFailureErrorSchema

        return SearchExecutionFailureErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import SearchExecutionFailureErrorSchema

        return SearchExecutionFailureErrorSchema().dump(self)


class SearchFacetPathNotFoundError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="SearchFacetPathNotFound")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchFacetPathNotFoundError":
        from ._schemas.error import SearchFacetPathNotFoundErrorSchema

        return SearchFacetPathNotFoundErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import SearchFacetPathNotFoundErrorSchema

        return SearchFacetPathNotFoundErrorSchema().dump(self)


class SemanticErrorError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="SemanticError")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SemanticErrorError":
        from ._schemas.error import SemanticErrorErrorSchema

        return SemanticErrorErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import SemanticErrorErrorSchema

        return SemanticErrorErrorSchema().dump(self)


class ShippingMethodDoesNotMatchCartError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="ShippingMethodDoesNotMatchCart")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodDoesNotMatchCartError":
        from ._schemas.error import ShippingMethodDoesNotMatchCartErrorSchema

        return ShippingMethodDoesNotMatchCartErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import ShippingMethodDoesNotMatchCartErrorSchema

        return ShippingMethodDoesNotMatchCartErrorSchema().dump(self)


class SyntaxErrorError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="SyntaxError")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SyntaxErrorError":
        from ._schemas.error import SyntaxErrorErrorSchema

        return SyntaxErrorErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import SyntaxErrorErrorSchema

        return SyntaxErrorErrorSchema().dump(self)


class VariantValues(_BaseType):
    sku: typing.Optional[str]
    prices: typing.List["PriceDraft"]
    attributes: typing.List["Attribute"]

    def __init__(
        self,
        *,
        sku: typing.Optional[str] = None,
        prices: typing.List["PriceDraft"],
        attributes: typing.List["Attribute"]
    ):
        self.sku = sku
        self.prices = prices
        self.attributes = attributes
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "VariantValues":
        from ._schemas.error import VariantValuesSchema

        return VariantValuesSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import VariantValuesSchema

        return VariantValuesSchema().dump(self)


class WeakPasswordError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="WeakPassword")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "WeakPasswordError":
        from ._schemas.error import WeakPasswordErrorSchema

        return WeakPasswordErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.error import WeakPasswordErrorSchema

        return WeakPasswordErrorSchema().dump(self)

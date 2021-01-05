# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ProcessingState

if typing.TYPE_CHECKING:
    from .common import ProcessingState
    from .prices import PriceImport
    from .productvariants import Attribute


class ErrorResponse(_BaseType):
    """The response in case of an error."""

    #: The http status code of the response.
    status_code: "int"
    #: Describes the error.
    message: "str"
    #: This property is only used for OAuth2 errors.
    #: Contains the error code.
    error: typing.Optional["str"]
    #: This property is only used for OAuth2 errors.
    #: Additional information to assist the client developer in
    #: understanding the error.
    error_description: typing.Optional["str"]
    #: The errors that caused this error response.
    errors: typing.Optional[typing.List["ErrorObject"]]

    def __init__(
        self,
        *,
        status_code: "int",
        message: "str",
        error: typing.Optional["str"] = None,
        error_description: typing.Optional["str"] = None,
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
        from ._schemas.errors import ErrorResponseSchema

        return ErrorResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ErrorResponseSchema

        return ErrorResponseSchema().dump(self)


class ErrorObject(_BaseType):
    """An error."""

    code: "str"
    #: The error's description.
    message: "str"

    def __init__(self, *, code: "str", message: "str"):
        self.code = code
        self.message = message
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ErrorObject":
        from ._schemas.errors import ErrorObjectSchema

        return ErrorObjectSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ErrorObjectSchema

        return ErrorObjectSchema().dump(self)


class AccessDeniedError(ErrorObject):
    def __init__(self, *, message: "str"):

        super().__init__(message=message, code="access_denied")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AccessDeniedError":
        from ._schemas.errors import AccessDeniedErrorSchema

        return AccessDeniedErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import AccessDeniedErrorSchema

        return AccessDeniedErrorSchema().dump(self)


class InvalidScopeError(ErrorObject):
    """The requested scope is invalid, unknown, malformed, or exceeds the scope granted by the resource owner."""

    def __init__(self, *, message: "str"):

        super().__init__(message=message, code="invalid_scope")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidScopeError":
        from ._schemas.errors import InvalidScopeErrorSchema

        return InvalidScopeErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidScopeErrorSchema

        return InvalidScopeErrorSchema().dump(self)


class InvalidOperation(ErrorObject):
    """The resources involved in the request are not in a valid state for the operation.
    The client application should validate the constraints described in the error message before sending the request.

    """

    def __init__(self, *, message: "str"):

        super().__init__(message=message, code="InvalidOperation")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidOperation":
        from ._schemas.errors import InvalidOperationSchema

        return InvalidOperationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidOperationSchema

        return InvalidOperationSchema().dump(self)


class DuplicateAttributeValueError(ErrorObject):
    """The Unique AttributeConstraint was violated."""

    #: The conflicting attribute.
    attribute: "Attribute"

    def __init__(self, *, message: "str", attribute: "Attribute"):
        self.attribute = attribute
        super().__init__(message=message, code="DuplicateAttributeValue")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DuplicateAttributeValueError":
        from ._schemas.errors import DuplicateAttributeValueErrorSchema

        return DuplicateAttributeValueErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import DuplicateAttributeValueErrorSchema

        return DuplicateAttributeValueErrorSchema().dump(self)


class DuplicateAttributeValuesError(ErrorObject):
    """The CombinationUnique AttributeConstraint was violated."""

    attributes: typing.List["Attribute"]

    def __init__(self, *, message: "str", attributes: typing.List["Attribute"]):
        self.attributes = attributes
        super().__init__(message=message, code="DuplicateAttributeValues")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DuplicateAttributeValuesError":
        from ._schemas.errors import DuplicateAttributeValuesErrorSchema

        return DuplicateAttributeValuesErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import DuplicateAttributeValuesErrorSchema

        return DuplicateAttributeValuesErrorSchema().dump(self)


class DuplicateFieldError(ErrorObject):
    """A value for a field conflicts with an existing duplicate value."""

    #: The name of the field.
    field: typing.Optional["str"]
    #: The offending duplicate value.
    duplicate_value: typing.Optional["any"]

    def __init__(
        self,
        *,
        message: "str",
        field: typing.Optional["str"] = None,
        duplicate_value: typing.Optional["any"] = None
    ):
        self.field = field
        self.duplicate_value = duplicate_value
        super().__init__(message=message, code="DuplicateField")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DuplicateFieldError":
        from ._schemas.errors import DuplicateFieldErrorSchema

        return DuplicateFieldErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import DuplicateFieldErrorSchema

        return DuplicateFieldErrorSchema().dump(self)


class DuplicateVariantValuesError(ErrorObject):
    """A given combination of variant values conflicts with an existing one.
    Every product variant must have a distinct combination of SKU, prices, and custom attribute values.

    """

    #: The offending variant values.
    variant_values: "VariantValues"

    def __init__(self, *, message: "str", variant_values: "VariantValues"):
        self.variant_values = variant_values
        super().__init__(message=message, code="DuplicateVariantValues")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DuplicateVariantValuesError":
        from ._schemas.errors import DuplicateVariantValuesErrorSchema

        return DuplicateVariantValuesErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import DuplicateVariantValuesErrorSchema

        return DuplicateVariantValuesErrorSchema().dump(self)


class VariantValues(_BaseType):
    sku: typing.Optional["str"]
    prices: typing.List["PriceImport"]
    attributes: typing.List["Attribute"]

    def __init__(
        self,
        *,
        sku: typing.Optional["str"] = None,
        prices: typing.List["PriceImport"],
        attributes: typing.List["Attribute"]
    ):
        self.sku = sku
        self.prices = prices
        self.attributes = attributes
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "VariantValues":
        from ._schemas.errors import VariantValuesSchema

        return VariantValuesSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import VariantValuesSchema

        return VariantValuesSchema().dump(self)


class InsufficientScopeError(ErrorObject):
    def __init__(self, *, message: "str"):

        super().__init__(message=message, code="insufficient_scope")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InsufficientScopeError":
        from ._schemas.errors import InsufficientScopeErrorSchema

        return InsufficientScopeErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InsufficientScopeErrorSchema

        return InsufficientScopeErrorSchema().dump(self)


class InvalidCredentialsError(ErrorObject):
    def __init__(self, *, message: "str"):

        super().__init__(message=message, code="InvalidCredentials")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InvalidCredentialsError":
        from ._schemas.errors import InvalidCredentialsErrorSchema

        return InvalidCredentialsErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidCredentialsErrorSchema

        return InvalidCredentialsErrorSchema().dump(self)


class InvalidTokenError(ErrorObject):
    def __init__(self, *, message: "str"):

        super().__init__(message=message, code="invalid_token")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidTokenError":
        from ._schemas.errors import InvalidTokenErrorSchema

        return InvalidTokenErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidTokenErrorSchema

        return InvalidTokenErrorSchema().dump(self)


class InvalidFieldError(ErrorObject):
    """A field has an invalid value."""

    #: The name of the field.
    field: "str"
    #: The invalid value.
    invalid_value: "any"
    #: A fixed set of allowed values for the field, if any.
    allowed_values: typing.Optional[typing.List["any"]]

    def __init__(
        self,
        *,
        message: "str",
        field: "str",
        invalid_value: "any",
        allowed_values: typing.Optional[typing.List["any"]] = None
    ):
        self.field = field
        self.invalid_value = invalid_value
        self.allowed_values = allowed_values
        super().__init__(message=message, code="InvalidField")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidFieldError":
        from ._schemas.errors import InvalidFieldErrorSchema

        return InvalidFieldErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidFieldErrorSchema

        return InvalidFieldErrorSchema().dump(self)


class InvalidJsonInput(ErrorObject):
    """Invalid JSON input has been sent to the service. Either the JSON is syntactically not correct, or the JSON does not
    conform to the expected shape (e.g. is missing a required field). The client application should validate the input
    according to the constraints described in the error message before sending the request.

    """

    def __init__(self, *, message: "str"):

        super().__init__(message=message, code="InvalidJsonInput")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidJsonInput":
        from ._schemas.errors import InvalidJsonInputSchema

        return InvalidJsonInputSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidJsonInputSchema

        return InvalidJsonInputSchema().dump(self)


class InvalidInput(ErrorObject):
    """Invalid input has been sent to the service. The client application should validate the input according to the
    constraints described in the error message before sending the request.

    """

    def __init__(self, *, message: "str"):

        super().__init__(message=message, code="InvalidInput")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidInput":
        from ._schemas.errors import InvalidInputSchema

        return InvalidInputSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidInputSchema

        return InvalidInputSchema().dump(self)


class ResourceNotFoundError(ErrorObject):
    resource: typing.Optional["any"]

    def __init__(self, *, message: "str", resource: typing.Optional["any"] = None):
        self.resource = resource
        super().__init__(message=message, code="ResourceNotFound")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ResourceNotFoundError":
        from ._schemas.errors import ResourceNotFoundErrorSchema

        return ResourceNotFoundErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ResourceNotFoundErrorSchema

        return ResourceNotFoundErrorSchema().dump(self)


class ResourceCreationError(ErrorObject):
    resource: typing.Optional["any"]

    def __init__(self, *, message: "str", resource: typing.Optional["any"] = None):
        self.resource = resource
        super().__init__(message=message, code="ResourceCreation")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ResourceCreationError":
        from ._schemas.errors import ResourceCreationErrorSchema

        return ResourceCreationErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ResourceCreationErrorSchema

        return ResourceCreationErrorSchema().dump(self)


class ResourceUpdateError(ErrorObject):
    resource: typing.Optional["any"]

    def __init__(self, *, message: "str", resource: typing.Optional["any"] = None):
        self.resource = resource
        super().__init__(message=message, code="ResourceUpdate")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ResourceUpdateError":
        from ._schemas.errors import ResourceUpdateErrorSchema

        return ResourceUpdateErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ResourceUpdateErrorSchema

        return ResourceUpdateErrorSchema().dump(self)


class ResourceDeletionError(ErrorObject):
    resource: typing.Optional["any"]

    def __init__(self, *, message: "str", resource: typing.Optional["any"] = None):
        self.resource = resource
        super().__init__(message=message, code="ResourceDeletion")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ResourceDeletionError":
        from ._schemas.errors import ResourceDeletionErrorSchema

        return ResourceDeletionErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ResourceDeletionErrorSchema

        return ResourceDeletionErrorSchema().dump(self)


class RequiredFieldError(ErrorObject):
    """A required field is missing a value."""

    #: The name of the field.
    field: "str"

    def __init__(self, *, message: "str", field: "str"):
        self.field = field
        super().__init__(message=message, code="RequiredField")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "RequiredFieldError":
        from ._schemas.errors import RequiredFieldErrorSchema

        return RequiredFieldErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import RequiredFieldErrorSchema

        return RequiredFieldErrorSchema().dump(self)


class InvalidStateTransitionError(ErrorObject):
    #: This enumeration describes the processing state of an import operation.
    current_state: "ProcessingState"
    #: This enumeration describes the processing state of an import operation.
    new_state: "ProcessingState"

    def __init__(
        self,
        *,
        message: "str",
        current_state: "ProcessingState",
        new_state: "ProcessingState"
    ):
        self.current_state = current_state
        self.new_state = new_state
        super().__init__(message=message, code="InvalidTransition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InvalidStateTransitionError":
        from ._schemas.errors import InvalidStateTransitionErrorSchema

        return InvalidStateTransitionErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidStateTransitionErrorSchema

        return InvalidStateTransitionErrorSchema().dump(self)


class ConcurrentModificationError(ErrorObject):
    """The request conflicts with the current state of the involved resource(s). Typically, the request attempts to modify a resource
    that is out of date, i.e. that has been modified by another client since the last time it was retrieved.
    The client application should resolve the conflict (with or without involving the end-user) before retrying the request

    """

    #: The version specified in the failed request.
    specified_version: typing.Optional["int"]
    #: The current version of the resource.
    current_version: "int"
    #: The conflicted resource.
    conflicted_resource: typing.Optional["any"]

    def __init__(
        self,
        *,
        message: "str",
        specified_version: typing.Optional["int"] = None,
        current_version: "int",
        conflicted_resource: typing.Optional["any"] = None
    ):
        self.specified_version = specified_version
        self.current_version = current_version
        self.conflicted_resource = conflicted_resource
        super().__init__(message=message, code="ConcurrentModification")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ConcurrentModificationError":
        from ._schemas.errors import ConcurrentModificationErrorSchema

        return ConcurrentModificationErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ConcurrentModificationErrorSchema

        return ConcurrentModificationErrorSchema().dump(self)


class ContentionError(ErrorObject):
    def __init__(self, *, message: "str"):

        super().__init__(message=message, code="Contention")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ContentionError":
        from ._schemas.errors import ContentionErrorSchema

        return ContentionErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ContentionErrorSchema

        return ContentionErrorSchema().dump(self)


class GenericError(ErrorObject):
    def __init__(self, *, message: "str"):

        super().__init__(message=message, code="Generic")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "GenericError":
        from ._schemas.errors import GenericErrorSchema

        return GenericErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import GenericErrorSchema

        return GenericErrorSchema().dump(self)

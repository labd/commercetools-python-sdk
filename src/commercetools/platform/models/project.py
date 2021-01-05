# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .shipping_method import ShippingRateTierType

if typing.TYPE_CHECKING:
    from .message import MessageConfiguration, MessageConfigurationDraft
    from .shipping_method import ShippingRateTierType
    from .type import CustomFieldLocalizedEnumValue


class CartsConfiguration(_BaseType):
    #: if country - no state tax rate fallback should be used when a shipping address state is not explicitly covered in the rates lists of all tax categories of a cart line items. Default value 'false'
    country_tax_rate_fallback_enabled: typing.Optional["bool"]

    def __init__(
        self, *, country_tax_rate_fallback_enabled: typing.Optional["bool"] = None
    ):
        self.country_tax_rate_fallback_enabled = country_tax_rate_fallback_enabled
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartsConfiguration":
        from ._schemas.project import CartsConfigurationSchema

        return CartsConfigurationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import CartsConfigurationSchema

        return CartsConfigurationSchema().dump(self)


class ExternalOAuth(_BaseType):
    url: "str"
    authorization_header: "str"

    def __init__(self, *, url: "str", authorization_header: "str"):
        self.url = url
        self.authorization_header = authorization_header
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ExternalOAuth":
        from ._schemas.project import ExternalOAuthSchema

        return ExternalOAuthSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ExternalOAuthSchema

        return ExternalOAuthSchema().dump(self)


class Project(_BaseType):
    #: The current version of the project.
    version: "int"
    #: The unique key of the project.
    key: "str"
    #: The name of the project.
    name: "str"
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    countries: typing.List["str"]
    #: A three-digit currency code as per [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).
    currencies: typing.List["str"]
    languages: typing.List["str"]
    created_at: "datetime.datetime"
    #: The time is in the format Year-Month `YYYY-MM`.
    trial_until: typing.Optional["str"]
    messages: "MessageConfiguration"
    shipping_rate_input_type: typing.Optional["ShippingRateInputType"]
    external_o_auth: typing.Optional["ExternalOAuth"]
    carts: "CartsConfiguration"

    def __init__(
        self,
        *,
        version: "int",
        key: "str",
        name: "str",
        countries: typing.List["str"],
        currencies: typing.List["str"],
        languages: typing.List["str"],
        created_at: "datetime.datetime",
        trial_until: typing.Optional["str"] = None,
        messages: "MessageConfiguration",
        shipping_rate_input_type: typing.Optional["ShippingRateInputType"] = None,
        external_o_auth: typing.Optional["ExternalOAuth"] = None,
        carts: "CartsConfiguration"
    ):
        self.version = version
        self.key = key
        self.name = name
        self.countries = countries
        self.currencies = currencies
        self.languages = languages
        self.created_at = created_at
        self.trial_until = trial_until
        self.messages = messages
        self.shipping_rate_input_type = shipping_rate_input_type
        self.external_o_auth = external_o_auth
        self.carts = carts
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Project":
        from ._schemas.project import ProjectSchema

        return ProjectSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectSchema

        return ProjectSchema().dump(self)


class ProjectUpdate(_BaseType):
    version: "int"
    actions: typing.List["ProjectUpdateAction"]

    def __init__(self, *, version: "int", actions: typing.List["ProjectUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProjectUpdate":
        from ._schemas.project import ProjectUpdateSchema

        return ProjectUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectUpdateSchema

        return ProjectUpdateSchema().dump(self)


class ProjectUpdateAction(_BaseType):
    action: "str"

    def __init__(self, *, action: "str"):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProjectUpdateAction":
        from ._schemas.project import ProjectUpdateActionSchema

        return ProjectUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectUpdateActionSchema

        return ProjectUpdateActionSchema().dump(self)


class ShippingRateInputType(_BaseType):
    type: "ShippingRateTierType"

    def __init__(self, *, type: "ShippingRateTierType"):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShippingRateInputType":
        from ._schemas.project import ShippingRateInputTypeSchema

        return ShippingRateInputTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ShippingRateInputTypeSchema

        return ShippingRateInputTypeSchema().dump(self)


class CartClassificationType(ShippingRateInputType):
    values: typing.List["CustomFieldLocalizedEnumValue"]

    def __init__(self, *, values: typing.List["CustomFieldLocalizedEnumValue"]):
        self.values = values
        super().__init__(type=ShippingRateTierType.CART_CLASSIFICATION)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartClassificationType":
        from ._schemas.project import CartClassificationTypeSchema

        return CartClassificationTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import CartClassificationTypeSchema

        return CartClassificationTypeSchema().dump(self)


class CartScoreType(ShippingRateInputType):
    def __init__(self):

        super().__init__(type=ShippingRateTierType.CART_SCORE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartScoreType":
        from ._schemas.project import CartScoreTypeSchema

        return CartScoreTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import CartScoreTypeSchema

        return CartScoreTypeSchema().dump(self)


class CartValueType(ShippingRateInputType):
    def __init__(self):

        super().__init__(type=ShippingRateTierType.CART_VALUE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartValueType":
        from ._schemas.project import CartValueTypeSchema

        return CartValueTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import CartValueTypeSchema

        return CartValueTypeSchema().dump(self)


class ProjectChangeCountriesAction(ProjectUpdateAction):
    #: A two-digit country code as per country code.
    countries: typing.List["str"]

    def __init__(self, *, countries: typing.List["str"]):
        self.countries = countries
        super().__init__(action="changeCountries")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeCountriesAction":
        from ._schemas.project import ProjectChangeCountriesActionSchema

        return ProjectChangeCountriesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeCountriesActionSchema

        return ProjectChangeCountriesActionSchema().dump(self)


class ProjectChangeCountryTaxRateFallbackEnabledAction(ProjectUpdateAction):
    #: default value is `false`
    country_tax_rate_fallback_enabled: "bool"

    def __init__(self, *, country_tax_rate_fallback_enabled: "bool"):
        self.country_tax_rate_fallback_enabled = country_tax_rate_fallback_enabled
        super().__init__(action="changeCountryTaxRateFallbackEnabled")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeCountryTaxRateFallbackEnabledAction":
        from ._schemas.project import (
            ProjectChangeCountryTaxRateFallbackEnabledActionSchema,
        )

        return ProjectChangeCountryTaxRateFallbackEnabledActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import (
            ProjectChangeCountryTaxRateFallbackEnabledActionSchema,
        )

        return ProjectChangeCountryTaxRateFallbackEnabledActionSchema().dump(self)


class ProjectChangeCurrenciesAction(ProjectUpdateAction):
    #: A three-digit currency code as per currency code.
    currencies: typing.List["str"]

    def __init__(self, *, currencies: typing.List["str"]):
        self.currencies = currencies
        super().__init__(action="changeCurrencies")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeCurrenciesAction":
        from ._schemas.project import ProjectChangeCurrenciesActionSchema

        return ProjectChangeCurrenciesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeCurrenciesActionSchema

        return ProjectChangeCurrenciesActionSchema().dump(self)


class ProjectChangeLanguagesAction(ProjectUpdateAction):
    #:  .
    languages: typing.List["str"]

    def __init__(self, *, languages: typing.List["str"]):
        self.languages = languages
        super().__init__(action="changeLanguages")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeLanguagesAction":
        from ._schemas.project import ProjectChangeLanguagesActionSchema

        return ProjectChangeLanguagesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeLanguagesActionSchema

        return ProjectChangeLanguagesActionSchema().dump(self)


class ProjectChangeMessagesConfigurationAction(ProjectUpdateAction):
    messages_configuration: "MessageConfigurationDraft"

    def __init__(self, *, messages_configuration: "MessageConfigurationDraft"):
        self.messages_configuration = messages_configuration
        super().__init__(action="changeMessagesConfiguration")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeMessagesConfigurationAction":
        from ._schemas.project import ProjectChangeMessagesConfigurationActionSchema

        return ProjectChangeMessagesConfigurationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeMessagesConfigurationActionSchema

        return ProjectChangeMessagesConfigurationActionSchema().dump(self)


class ProjectChangeMessagesEnabledAction(ProjectUpdateAction):
    messages_enabled: "bool"

    def __init__(self, *, messages_enabled: "bool"):
        self.messages_enabled = messages_enabled
        super().__init__(action="changeMessagesEnabled")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeMessagesEnabledAction":
        from ._schemas.project import ProjectChangeMessagesEnabledActionSchema

        return ProjectChangeMessagesEnabledActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeMessagesEnabledActionSchema

        return ProjectChangeMessagesEnabledActionSchema().dump(self)


class ProjectChangeNameAction(ProjectUpdateAction):
    name: "str"

    def __init__(self, *, name: "str"):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeNameAction":
        from ._schemas.project import ProjectChangeNameActionSchema

        return ProjectChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeNameActionSchema

        return ProjectChangeNameActionSchema().dump(self)


class ProjectSetExternalOAuthAction(ProjectUpdateAction):
    #: If you do not provide the `externalOAuth` field or provide a value
    #: of `null`, the update action unsets the External OAuth provider.
    external_o_auth: typing.Optional["ExternalOAuth"]

    def __init__(self, *, external_o_auth: typing.Optional["ExternalOAuth"] = None):
        self.external_o_auth = external_o_auth
        super().__init__(action="setExternalOAuth")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectSetExternalOAuthAction":
        from ._schemas.project import ProjectSetExternalOAuthActionSchema

        return ProjectSetExternalOAuthActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectSetExternalOAuthActionSchema

        return ProjectSetExternalOAuthActionSchema().dump(self)


class ProjectSetShippingRateInputTypeAction(ProjectUpdateAction):
    #: If not set, removes existing shippingRateInputType.
    shipping_rate_input_type: typing.Optional["ShippingRateInputType"]

    def __init__(
        self,
        *,
        shipping_rate_input_type: typing.Optional["ShippingRateInputType"] = None
    ):
        self.shipping_rate_input_type = shipping_rate_input_type
        super().__init__(action="setShippingRateInputType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectSetShippingRateInputTypeAction":
        from ._schemas.project import ProjectSetShippingRateInputTypeActionSchema

        return ProjectSetShippingRateInputTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectSetShippingRateInputTypeActionSchema

        return ProjectSetShippingRateInputTypeActionSchema().dump(self)

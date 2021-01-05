# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import (
        CreatedBy,
        LastModifiedBy,
        LocalizedString,
        Money,
        ReferenceTypeId,
        TypedMoney,
    )
    from .tax_category import TaxCategoryReference, TaxCategoryResourceIdentifier
    from .zone import ZoneReference, ZoneResourceIdentifier

__all__ = [
    "CartClassificationTier",
    "CartScoreTier",
    "CartValueTier",
    "PriceFunction",
    "ShippingMethod",
    "ShippingMethodAddShippingRateAction",
    "ShippingMethodAddZoneAction",
    "ShippingMethodChangeIsDefaultAction",
    "ShippingMethodChangeNameAction",
    "ShippingMethodChangeTaxCategoryAction",
    "ShippingMethodDraft",
    "ShippingMethodPagedQueryResponse",
    "ShippingMethodReference",
    "ShippingMethodRemoveShippingRateAction",
    "ShippingMethodRemoveZoneAction",
    "ShippingMethodResourceIdentifier",
    "ShippingMethodSetDescriptionAction",
    "ShippingMethodSetKeyAction",
    "ShippingMethodSetLocalizedDescriptionAction",
    "ShippingMethodSetPredicateAction",
    "ShippingMethodUpdate",
    "ShippingMethodUpdateAction",
    "ShippingRate",
    "ShippingRateDraft",
    "ShippingRatePriceTier",
    "ShippingRateTierType",
    "ZoneRate",
    "ZoneRateDraft",
]


class PriceFunction(_BaseType):
    #: The currency code compliant to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).
    currency_code: str
    function: str

    def __init__(self, *, currency_code: str, function: str):
        self.currency_code = currency_code
        self.function = function
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceFunction":
        from ._schemas.shipping_method import PriceFunctionSchema

        return PriceFunctionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import PriceFunctionSchema

        return PriceFunctionSchema().dump(self)


class ShippingMethod(BaseResource):
    last_modified_by: typing.Optional["LastModifiedBy"]
    created_by: typing.Optional["CreatedBy"]
    #: User-specific unique identifier for the shipping method.
    key: typing.Optional[str]
    name: str
    description: typing.Optional[str]
    localized_description: typing.Optional["LocalizedString"]
    tax_category: "TaxCategoryReference"
    zone_rates: typing.List["ZoneRate"]
    #: One shipping method in a project can be default.
    is_default: bool
    #: A Cart predicate which can be used to more precisely select a shipping method for a cart.
    predicate: typing.Optional[str]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional[str] = None,
        name: str,
        description: typing.Optional[str] = None,
        localized_description: typing.Optional["LocalizedString"] = None,
        tax_category: "TaxCategoryReference",
        zone_rates: typing.List["ZoneRate"],
        is_default: bool,
        predicate: typing.Optional[str] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.description = description
        self.localized_description = localized_description
        self.tax_category = tax_category
        self.zone_rates = zone_rates
        self.is_default = is_default
        self.predicate = predicate
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShippingMethod":
        from ._schemas.shipping_method import ShippingMethodSchema

        return ShippingMethodSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodSchema

        return ShippingMethodSchema().dump(self)


class ShippingMethodDraft(_BaseType):
    key: typing.Optional[str]
    name: str
    description: typing.Optional[str]
    localized_description: typing.Optional["LocalizedString"]
    tax_category: "TaxCategoryResourceIdentifier"
    zone_rates: typing.List["ZoneRateDraft"]
    #: If `true` the shipping method will be the default one in a project.
    is_default: bool
    #: A Cart predicate which can be used to more precisely select a shipping method for a cart.
    predicate: typing.Optional[str]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        name: str,
        description: typing.Optional[str] = None,
        localized_description: typing.Optional["LocalizedString"] = None,
        tax_category: "TaxCategoryResourceIdentifier",
        zone_rates: typing.List["ZoneRateDraft"],
        is_default: bool,
        predicate: typing.Optional[str] = None
    ):
        self.key = key
        self.name = name
        self.description = description
        self.localized_description = localized_description
        self.tax_category = tax_category
        self.zone_rates = zone_rates
        self.is_default = is_default
        self.predicate = predicate
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShippingMethodDraft":
        from ._schemas.shipping_method import ShippingMethodDraftSchema

        return ShippingMethodDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodDraftSchema

        return ShippingMethodDraftSchema().dump(self)


class ShippingMethodPagedQueryResponse(_BaseType):
    limit: typing.Optional[int]
    count: int
    total: typing.Optional[int]
    offset: typing.Optional[int]
    results: typing.List["ShippingMethod"]

    def __init__(
        self,
        *,
        limit: typing.Optional[int] = None,
        count: int,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.List["ShippingMethod"]
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodPagedQueryResponse":
        from ._schemas.shipping_method import ShippingMethodPagedQueryResponseSchema

        return ShippingMethodPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodPagedQueryResponseSchema

        return ShippingMethodPagedQueryResponseSchema().dump(self)


class ShippingMethodReference(Reference):
    obj: typing.Optional["ShippingMethod"]

    def __init__(self, *, id: str, obj: typing.Optional["ShippingMethod"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.SHIPPING_METHOD)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodReference":
        from ._schemas.shipping_method import ShippingMethodReferenceSchema

        return ShippingMethodReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodReferenceSchema

        return ShippingMethodReferenceSchema().dump(self)


class ShippingMethodResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.SHIPPING_METHOD)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodResourceIdentifier":
        from ._schemas.shipping_method import ShippingMethodResourceIdentifierSchema

        return ShippingMethodResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodResourceIdentifierSchema

        return ShippingMethodResourceIdentifierSchema().dump(self)


class ShippingMethodUpdate(_BaseType):
    version: int
    actions: typing.List["ShippingMethodUpdateAction"]

    def __init__(
        self, *, version: int, actions: typing.List["ShippingMethodUpdateAction"]
    ):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShippingMethodUpdate":
        from ._schemas.shipping_method import ShippingMethodUpdateSchema

        return ShippingMethodUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodUpdateSchema

        return ShippingMethodUpdateSchema().dump(self)


class ShippingMethodUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodUpdateAction":
        if data["action"] == "addShippingRate":
            from ._schemas.shipping_method import (
                ShippingMethodAddShippingRateActionSchema,
            )

            return ShippingMethodAddShippingRateActionSchema().load(data)
        if data["action"] == "addZone":
            from ._schemas.shipping_method import ShippingMethodAddZoneActionSchema

            return ShippingMethodAddZoneActionSchema().load(data)
        if data["action"] == "changeIsDefault":
            from ._schemas.shipping_method import (
                ShippingMethodChangeIsDefaultActionSchema,
            )

            return ShippingMethodChangeIsDefaultActionSchema().load(data)
        if data["action"] == "changeName":
            from ._schemas.shipping_method import ShippingMethodChangeNameActionSchema

            return ShippingMethodChangeNameActionSchema().load(data)
        if data["action"] == "changeTaxCategory":
            from ._schemas.shipping_method import (
                ShippingMethodChangeTaxCategoryActionSchema,
            )

            return ShippingMethodChangeTaxCategoryActionSchema().load(data)
        if data["action"] == "removeShippingRate":
            from ._schemas.shipping_method import (
                ShippingMethodRemoveShippingRateActionSchema,
            )

            return ShippingMethodRemoveShippingRateActionSchema().load(data)
        if data["action"] == "removeZone":
            from ._schemas.shipping_method import ShippingMethodRemoveZoneActionSchema

            return ShippingMethodRemoveZoneActionSchema().load(data)
        if data["action"] == "setDescription":
            from ._schemas.shipping_method import (
                ShippingMethodSetDescriptionActionSchema,
            )

            return ShippingMethodSetDescriptionActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.shipping_method import ShippingMethodSetKeyActionSchema

            return ShippingMethodSetKeyActionSchema().load(data)
        if data["action"] == "setLocalizedDescription":
            from ._schemas.shipping_method import (
                ShippingMethodSetLocalizedDescriptionActionSchema,
            )

            return ShippingMethodSetLocalizedDescriptionActionSchema().load(data)
        if data["action"] == "setPredicate":
            from ._schemas.shipping_method import ShippingMethodSetPredicateActionSchema

            return ShippingMethodSetPredicateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodUpdateActionSchema

        return ShippingMethodUpdateActionSchema().dump(self)


class ShippingRate(_BaseType):
    price: "TypedMoney"
    #: The shipping is free if the order total (the sum of line item prices) exceeds the `freeAbove` value.
    #: Note: `freeAbove` applies before any Cart or Product discounts, and can cause discounts to apply in invalid scenarios.
    #: Use a Cart Discount to set the shipping price to 0 to avoid providing free shipping in invalid discount scenarios.
    free_above: typing.Optional["TypedMoney"]
    #: Only appears in response to requests for shipping methods by cart or location to mark this shipping rate as one that matches the cart or location.
    is_matching: typing.Optional[bool]
    #: A list of shipping rate price tiers.
    tiers: typing.List["ShippingRatePriceTier"]

    def __init__(
        self,
        *,
        price: "TypedMoney",
        free_above: typing.Optional["TypedMoney"] = None,
        is_matching: typing.Optional[bool] = None,
        tiers: typing.List["ShippingRatePriceTier"]
    ):
        self.price = price
        self.free_above = free_above
        self.is_matching = is_matching
        self.tiers = tiers
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShippingRate":
        from ._schemas.shipping_method import ShippingRateSchema

        return ShippingRateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingRateSchema

        return ShippingRateSchema().dump(self)


class ShippingRateDraft(_BaseType):
    price: "Money"
    #: The shipping is free if the order total (the sum of line item prices) exceeds the freeAbove value.
    #: Note: `freeAbove` applies before any Cart or Product discounts, and can cause discounts to apply in invalid scenarios.
    #: Use a Cart Discount to set the shipping price to 0 to avoid providing free shipping in invalid discount scenarios.
    free_above: typing.Optional["Money"]
    #: A list of shipping rate price tiers.
    tiers: typing.Optional[typing.List["ShippingRatePriceTier"]]

    def __init__(
        self,
        *,
        price: "Money",
        free_above: typing.Optional["Money"] = None,
        tiers: typing.Optional[typing.List["ShippingRatePriceTier"]] = None
    ):
        self.price = price
        self.free_above = free_above
        self.tiers = tiers
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShippingRateDraft":
        from ._schemas.shipping_method import ShippingRateDraftSchema

        return ShippingRateDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingRateDraftSchema

        return ShippingRateDraftSchema().dump(self)


class ShippingRatePriceTier(_BaseType):
    type: "ShippingRateTierType"

    def __init__(self, *, type: "ShippingRateTierType"):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShippingRatePriceTier":
        if data["type"] == "CartClassification":
            from ._schemas.shipping_method import CartClassificationTierSchema

            return CartClassificationTierSchema().load(data)
        if data["type"] == "CartScore":
            from ._schemas.shipping_method import CartScoreTierSchema

            return CartScoreTierSchema().load(data)
        if data["type"] == "CartValue":
            from ._schemas.shipping_method import CartValueTierSchema

            return CartValueTierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingRatePriceTierSchema

        return ShippingRatePriceTierSchema().dump(self)


class CartClassificationTier(ShippingRatePriceTier):
    value: str
    price: "Money"
    is_matching: typing.Optional[bool]

    def __init__(
        self, *, value: str, price: "Money", is_matching: typing.Optional[bool] = None
    ):
        self.value = value
        self.price = price
        self.is_matching = is_matching
        super().__init__(type=ShippingRateTierType.CART_CLASSIFICATION)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartClassificationTier":
        from ._schemas.shipping_method import CartClassificationTierSchema

        return CartClassificationTierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import CartClassificationTierSchema

        return CartClassificationTierSchema().dump(self)


class CartScoreTier(ShippingRatePriceTier):
    score: float
    price: typing.Optional["Money"]
    price_function: typing.Optional["PriceFunction"]
    is_matching: typing.Optional[bool]

    def __init__(
        self,
        *,
        score: float,
        price: typing.Optional["Money"] = None,
        price_function: typing.Optional["PriceFunction"] = None,
        is_matching: typing.Optional[bool] = None
    ):
        self.score = score
        self.price = price
        self.price_function = price_function
        self.is_matching = is_matching
        super().__init__(type=ShippingRateTierType.CART_SCORE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartScoreTier":
        from ._schemas.shipping_method import CartScoreTierSchema

        return CartScoreTierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import CartScoreTierSchema

        return CartScoreTierSchema().dump(self)


class CartValueTier(ShippingRatePriceTier):
    minimum_cent_amount: int
    price: "Money"
    is_matching: typing.Optional[bool]

    def __init__(
        self,
        *,
        minimum_cent_amount: int,
        price: "Money",
        is_matching: typing.Optional[bool] = None
    ):
        self.minimum_cent_amount = minimum_cent_amount
        self.price = price
        self.is_matching = is_matching
        super().__init__(type=ShippingRateTierType.CART_VALUE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartValueTier":
        from ._schemas.shipping_method import CartValueTierSchema

        return CartValueTierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import CartValueTierSchema

        return CartValueTierSchema().dump(self)


class ShippingRateTierType(enum.Enum):
    CART_VALUE = "CartValue"
    CART_CLASSIFICATION = "CartClassification"
    CART_SCORE = "CartScore"


class ZoneRate(_BaseType):
    zone: "ZoneReference"
    #: The array does not contain two shipping rates with the same currency.
    shipping_rates: typing.List["ShippingRate"]

    def __init__(
        self, *, zone: "ZoneReference", shipping_rates: typing.List["ShippingRate"]
    ):
        self.zone = zone
        self.shipping_rates = shipping_rates
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneRate":
        from ._schemas.shipping_method import ZoneRateSchema

        return ZoneRateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ZoneRateSchema

        return ZoneRateSchema().dump(self)


class ZoneRateDraft(_BaseType):
    zone: "ZoneResourceIdentifier"
    #: The array must not contain two shipping rates with the same currency.
    shipping_rates: typing.List["ShippingRateDraft"]

    def __init__(
        self,
        *,
        zone: "ZoneResourceIdentifier",
        shipping_rates: typing.List["ShippingRateDraft"]
    ):
        self.zone = zone
        self.shipping_rates = shipping_rates
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneRateDraft":
        from ._schemas.shipping_method import ZoneRateDraftSchema

        return ZoneRateDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ZoneRateDraftSchema

        return ZoneRateDraftSchema().dump(self)


class ShippingMethodAddShippingRateAction(ShippingMethodUpdateAction):
    zone: "ZoneResourceIdentifier"
    shipping_rate: "ShippingRateDraft"

    def __init__(
        self, *, zone: "ZoneResourceIdentifier", shipping_rate: "ShippingRateDraft"
    ):
        self.zone = zone
        self.shipping_rate = shipping_rate
        super().__init__(action="addShippingRate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodAddShippingRateAction":
        from ._schemas.shipping_method import ShippingMethodAddShippingRateActionSchema

        return ShippingMethodAddShippingRateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodAddShippingRateActionSchema

        return ShippingMethodAddShippingRateActionSchema().dump(self)


class ShippingMethodAddZoneAction(ShippingMethodUpdateAction):
    zone: "ZoneResourceIdentifier"

    def __init__(self, *, zone: "ZoneResourceIdentifier"):
        self.zone = zone
        super().__init__(action="addZone")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodAddZoneAction":
        from ._schemas.shipping_method import ShippingMethodAddZoneActionSchema

        return ShippingMethodAddZoneActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodAddZoneActionSchema

        return ShippingMethodAddZoneActionSchema().dump(self)


class ShippingMethodChangeIsDefaultAction(ShippingMethodUpdateAction):
    #: Only one ShippingMethod in a project can be default.
    is_default: bool

    def __init__(self, *, is_default: bool):
        self.is_default = is_default
        super().__init__(action="changeIsDefault")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodChangeIsDefaultAction":
        from ._schemas.shipping_method import ShippingMethodChangeIsDefaultActionSchema

        return ShippingMethodChangeIsDefaultActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodChangeIsDefaultActionSchema

        return ShippingMethodChangeIsDefaultActionSchema().dump(self)


class ShippingMethodChangeNameAction(ShippingMethodUpdateAction):
    name: str

    def __init__(self, *, name: str):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodChangeNameAction":
        from ._schemas.shipping_method import ShippingMethodChangeNameActionSchema

        return ShippingMethodChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodChangeNameActionSchema

        return ShippingMethodChangeNameActionSchema().dump(self)


class ShippingMethodChangeTaxCategoryAction(ShippingMethodUpdateAction):
    tax_category: "TaxCategoryResourceIdentifier"

    def __init__(self, *, tax_category: "TaxCategoryResourceIdentifier"):
        self.tax_category = tax_category
        super().__init__(action="changeTaxCategory")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodChangeTaxCategoryAction":
        from ._schemas.shipping_method import (
            ShippingMethodChangeTaxCategoryActionSchema,
        )

        return ShippingMethodChangeTaxCategoryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import (
            ShippingMethodChangeTaxCategoryActionSchema,
        )

        return ShippingMethodChangeTaxCategoryActionSchema().dump(self)


class ShippingMethodRemoveShippingRateAction(ShippingMethodUpdateAction):
    zone: "ZoneResourceIdentifier"
    shipping_rate: "ShippingRateDraft"

    def __init__(
        self, *, zone: "ZoneResourceIdentifier", shipping_rate: "ShippingRateDraft"
    ):
        self.zone = zone
        self.shipping_rate = shipping_rate
        super().__init__(action="removeShippingRate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodRemoveShippingRateAction":
        from ._schemas.shipping_method import (
            ShippingMethodRemoveShippingRateActionSchema,
        )

        return ShippingMethodRemoveShippingRateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import (
            ShippingMethodRemoveShippingRateActionSchema,
        )

        return ShippingMethodRemoveShippingRateActionSchema().dump(self)


class ShippingMethodRemoveZoneAction(ShippingMethodUpdateAction):
    zone: "ZoneResourceIdentifier"

    def __init__(self, *, zone: "ZoneResourceIdentifier"):
        self.zone = zone
        super().__init__(action="removeZone")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodRemoveZoneAction":
        from ._schemas.shipping_method import ShippingMethodRemoveZoneActionSchema

        return ShippingMethodRemoveZoneActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodRemoveZoneActionSchema

        return ShippingMethodRemoveZoneActionSchema().dump(self)


class ShippingMethodSetDescriptionAction(ShippingMethodUpdateAction):
    description: typing.Optional[str]

    def __init__(self, *, description: typing.Optional[str] = None):
        self.description = description
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodSetDescriptionAction":
        from ._schemas.shipping_method import ShippingMethodSetDescriptionActionSchema

        return ShippingMethodSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodSetDescriptionActionSchema

        return ShippingMethodSetDescriptionActionSchema().dump(self)


class ShippingMethodSetKeyAction(ShippingMethodUpdateAction):
    #: If `key` is absent or `null`, it is removed if it exists.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodSetKeyAction":
        from ._schemas.shipping_method import ShippingMethodSetKeyActionSchema

        return ShippingMethodSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodSetKeyActionSchema

        return ShippingMethodSetKeyActionSchema().dump(self)


class ShippingMethodSetLocalizedDescriptionAction(ShippingMethodUpdateAction):
    localized_description: typing.Optional[str]

    def __init__(self, *, localized_description: typing.Optional[str] = None):
        self.localized_description = localized_description
        super().__init__(action="setLocalizedDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodSetLocalizedDescriptionAction":
        from ._schemas.shipping_method import (
            ShippingMethodSetLocalizedDescriptionActionSchema,
        )

        return ShippingMethodSetLocalizedDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import (
            ShippingMethodSetLocalizedDescriptionActionSchema,
        )

        return ShippingMethodSetLocalizedDescriptionActionSchema().dump(self)


class ShippingMethodSetPredicateAction(ShippingMethodUpdateAction):
    #: A valid Cart predicate.
    #: If `predicate` is absent or `null`, it is removed if it exists.
    predicate: typing.Optional[str]

    def __init__(self, *, predicate: typing.Optional[str] = None):
        self.predicate = predicate
        super().__init__(action="setPredicate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodSetPredicateAction":
        from ._schemas.shipping_method import ShippingMethodSetPredicateActionSchema

        return ShippingMethodSetPredicateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shipping_method import ShippingMethodSetPredicateActionSchema

        return ShippingMethodSetPredicateActionSchema().dump(self)

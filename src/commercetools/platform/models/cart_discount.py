# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .channel import ChannelReference, ChannelResourceIdentifier
    from .common import (
        CreatedBy,
        LastModifiedBy,
        LocalizedString,
        Money,
        Reference,
        ReferenceTypeId,
        TypedMoney,
    )
    from .product import ProductReference, ProductResourceIdentifier
    from .type import CustomFields, TypeResourceIdentifier

__all__ = [
    "CartDiscount",
    "CartDiscountChangeCartPredicateAction",
    "CartDiscountChangeIsActiveAction",
    "CartDiscountChangeNameAction",
    "CartDiscountChangeRequiresDiscountCodeAction",
    "CartDiscountChangeSortOrderAction",
    "CartDiscountChangeStackingModeAction",
    "CartDiscountChangeTargetAction",
    "CartDiscountChangeValueAction",
    "CartDiscountCustomLineItemsTarget",
    "CartDiscountDraft",
    "CartDiscountLineItemsTarget",
    "CartDiscountPagedQueryResponse",
    "CartDiscountReference",
    "CartDiscountResourceIdentifier",
    "CartDiscountSetCustomFieldAction",
    "CartDiscountSetCustomTypeAction",
    "CartDiscountSetDescriptionAction",
    "CartDiscountSetKeyAction",
    "CartDiscountSetValidFromAction",
    "CartDiscountSetValidFromAndUntilAction",
    "CartDiscountSetValidUntilAction",
    "CartDiscountShippingCostTarget",
    "CartDiscountTarget",
    "CartDiscountUpdate",
    "CartDiscountUpdateAction",
    "CartDiscountValue",
    "CartDiscountValueAbsolute",
    "CartDiscountValueAbsoluteDraft",
    "CartDiscountValueDraft",
    "CartDiscountValueGiftLineItem",
    "CartDiscountValueGiftLineItemDraft",
    "CartDiscountValueRelative",
    "CartDiscountValueRelativeDraft",
    "MultiBuyCustomLineItemsTarget",
    "MultiBuyLineItemsTarget",
    "SelectionMode",
    "StackingMode",
]


class CartDiscount(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    name: "LocalizedString"
    #: User-specific unique identifier for a cart discount.
    #: Must be unique across a project.
    key: typing.Optional[str]
    description: typing.Optional["LocalizedString"]
    value: "CartDiscountValueDraft"
    #: A valid Cart predicate.
    cart_predicate: str
    #: Empty when the `value` has type `giftLineItem`, otherwise a CartDiscountTarget is set.
    target: typing.Optional["CartDiscountTarget"]
    #: The string must contain a number between 0 and 1.
    #: All matching cart discounts are applied to a cart in the order defined by this field.
    #: A discount with greater sort order is prioritized higher than a discount with lower sort order.
    #: The sort order is unambiguous among all cart discounts.
    sort_order: str
    #: Only active discount can be applied to the cart.
    is_active: bool
    valid_from: typing.Optional[datetime.datetime]
    valid_until: typing.Optional[datetime.datetime]
    #: States whether the discount can only be used in a connection with a DiscountCode.
    requires_discount_code: bool
    #: The platform will generate this array from the predicate.
    #: It contains the references of all the resources that are addressed in the predicate.
    references: typing.List["Reference"]
    #: Specifies whether the application of this discount causes the following discounts to be ignored.
    #: Defaults to Stacking.
    stacking_mode: "StackingMode"
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        name: "LocalizedString",
        key: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None,
        value: "CartDiscountValueDraft",
        cart_predicate: str,
        target: typing.Optional["CartDiscountTarget"] = None,
        sort_order: str,
        is_active: bool,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        requires_discount_code: bool,
        references: typing.List["Reference"],
        stacking_mode: "StackingMode",
        custom: typing.Optional["CustomFields"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.name = name
        self.key = key
        self.description = description
        self.value = value
        self.cart_predicate = cart_predicate
        self.target = target
        self.sort_order = sort_order
        self.is_active = is_active
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.requires_discount_code = requires_discount_code
        self.references = references
        self.stacking_mode = stacking_mode
        self.custom = custom
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartDiscount":
        from ._schemas.cart_discount import CartDiscountSchema

        return CartDiscountSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountSchema

        return CartDiscountSchema().dump(self)


class CartDiscountDraft(_BaseType):
    name: "LocalizedString"
    #: User-specific unique identifier for a cart discount.
    #: Must be unique across a project.
    #: The field can be reset using the Set Key UpdateAction.
    key: typing.Optional[str]
    description: typing.Optional["LocalizedString"]
    value: "CartDiscountValueDraft"
    #: A valid Cart predicate.
    cart_predicate: str
    #: Must not be set when the `value` has type `giftLineItem`, otherwise a CartDiscountTarget must be set.
    target: typing.Optional["CartDiscountTarget"]
    #: The string must contain a number between 0 and 1.
    #: A discount with greater sort order is prioritized higher than a discount with lower sort order.
    #: The sort order must be unambiguous among all cart discounts.
    sort_order: str
    #: Only active discount can be applied to the cart.
    #: Defaults to `true`.
    is_active: typing.Optional[bool]
    valid_from: typing.Optional[datetime.datetime]
    valid_until: typing.Optional[datetime.datetime]
    #: States whether the discount can only be used in a connection with a DiscountCode.
    #: Defaults to `false`.
    requires_discount_code: bool
    #: Specifies whether the application of this discount causes the following discounts to be ignored.
    #: Defaults to Stacking.
    stacking_mode: typing.Optional["StackingMode"]
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        name: "LocalizedString",
        key: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None,
        value: "CartDiscountValueDraft",
        cart_predicate: str,
        target: typing.Optional["CartDiscountTarget"] = None,
        sort_order: str,
        is_active: typing.Optional[bool] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        requires_discount_code: bool,
        stacking_mode: typing.Optional["StackingMode"] = None,
        custom: typing.Optional["CustomFields"] = None
    ):
        self.name = name
        self.key = key
        self.description = description
        self.value = value
        self.cart_predicate = cart_predicate
        self.target = target
        self.sort_order = sort_order
        self.is_active = is_active
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.requires_discount_code = requires_discount_code
        self.stacking_mode = stacking_mode
        self.custom = custom
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartDiscountDraft":
        from ._schemas.cart_discount import CartDiscountDraftSchema

        return CartDiscountDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountDraftSchema

        return CartDiscountDraftSchema().dump(self)


class CartDiscountPagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["CartDiscount"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["CartDiscount"]
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
    ) -> "CartDiscountPagedQueryResponse":
        from ._schemas.cart_discount import CartDiscountPagedQueryResponseSchema

        return CartDiscountPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountPagedQueryResponseSchema

        return CartDiscountPagedQueryResponseSchema().dump(self)


class CartDiscountReference(Reference):
    obj: typing.Optional["CartDiscount"]

    def __init__(self, *, id: str, obj: typing.Optional["CartDiscount"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.CART_DISCOUNT)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartDiscountReference":
        from ._schemas.cart_discount import CartDiscountReferenceSchema

        return CartDiscountReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountReferenceSchema

        return CartDiscountReferenceSchema().dump(self)


class CartDiscountResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.CART_DISCOUNT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountResourceIdentifier":
        from ._schemas.cart_discount import CartDiscountResourceIdentifierSchema

        return CartDiscountResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountResourceIdentifierSchema

        return CartDiscountResourceIdentifierSchema().dump(self)


class CartDiscountTarget(_BaseType):
    type: str

    def __init__(self, *, type: str):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartDiscountTarget":
        if data["type"] == "customLineItems":
            from ._schemas.cart_discount import CartDiscountCustomLineItemsTargetSchema

            return CartDiscountCustomLineItemsTargetSchema().load(data)
        if data["type"] == "lineItems":
            from ._schemas.cart_discount import CartDiscountLineItemsTargetSchema

            return CartDiscountLineItemsTargetSchema().load(data)
        if data["type"] == "shipping":
            from ._schemas.cart_discount import CartDiscountShippingCostTargetSchema

            return CartDiscountShippingCostTargetSchema().load(data)
        if data["type"] == "multiBuyCustomLineItems":
            from ._schemas.cart_discount import MultiBuyCustomLineItemsTargetSchema

            return MultiBuyCustomLineItemsTargetSchema().load(data)
        if data["type"] == "multiBuyLineItems":
            from ._schemas.cart_discount import MultiBuyLineItemsTargetSchema

            return MultiBuyLineItemsTargetSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountTargetSchema

        return CartDiscountTargetSchema().dump(self)


class CartDiscountCustomLineItemsTarget(CartDiscountTarget):
    predicate: str

    def __init__(self, *, predicate: str):
        self.predicate = predicate
        super().__init__(type="customLineItems")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountCustomLineItemsTarget":
        from ._schemas.cart_discount import CartDiscountCustomLineItemsTargetSchema

        return CartDiscountCustomLineItemsTargetSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountCustomLineItemsTargetSchema

        return CartDiscountCustomLineItemsTargetSchema().dump(self)


class CartDiscountLineItemsTarget(CartDiscountTarget):
    predicate: str

    def __init__(self, *, predicate: str):
        self.predicate = predicate
        super().__init__(type="lineItems")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountLineItemsTarget":
        from ._schemas.cart_discount import CartDiscountLineItemsTargetSchema

        return CartDiscountLineItemsTargetSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountLineItemsTargetSchema

        return CartDiscountLineItemsTargetSchema().dump(self)


class CartDiscountShippingCostTarget(CartDiscountTarget):
    def __init__(self):

        super().__init__(type="shipping")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountShippingCostTarget":
        from ._schemas.cart_discount import CartDiscountShippingCostTargetSchema

        return CartDiscountShippingCostTargetSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountShippingCostTargetSchema

        return CartDiscountShippingCostTargetSchema().dump(self)


class CartDiscountUpdate(_BaseType):
    version: int
    actions: typing.List["CartDiscountUpdateAction"]

    def __init__(
        self, *, version: int, actions: typing.List["CartDiscountUpdateAction"]
    ):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartDiscountUpdate":
        from ._schemas.cart_discount import CartDiscountUpdateSchema

        return CartDiscountUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountUpdateSchema

        return CartDiscountUpdateSchema().dump(self)


class CartDiscountUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountUpdateAction":
        if data["action"] == "changeCartPredicate":
            from ._schemas.cart_discount import (
                CartDiscountChangeCartPredicateActionSchema,
            )

            return CartDiscountChangeCartPredicateActionSchema().load(data)
        if data["action"] == "changeIsActive":
            from ._schemas.cart_discount import CartDiscountChangeIsActiveActionSchema

            return CartDiscountChangeIsActiveActionSchema().load(data)
        if data["action"] == "changeName":
            from ._schemas.cart_discount import CartDiscountChangeNameActionSchema

            return CartDiscountChangeNameActionSchema().load(data)
        if data["action"] == "changeRequiresDiscountCode":
            from ._schemas.cart_discount import (
                CartDiscountChangeRequiresDiscountCodeActionSchema,
            )

            return CartDiscountChangeRequiresDiscountCodeActionSchema().load(data)
        if data["action"] == "changeSortOrder":
            from ._schemas.cart_discount import CartDiscountChangeSortOrderActionSchema

            return CartDiscountChangeSortOrderActionSchema().load(data)
        if data["action"] == "changeStackingMode":
            from ._schemas.cart_discount import (
                CartDiscountChangeStackingModeActionSchema,
            )

            return CartDiscountChangeStackingModeActionSchema().load(data)
        if data["action"] == "changeTarget":
            from ._schemas.cart_discount import CartDiscountChangeTargetActionSchema

            return CartDiscountChangeTargetActionSchema().load(data)
        if data["action"] == "changeValue":
            from ._schemas.cart_discount import CartDiscountChangeValueActionSchema

            return CartDiscountChangeValueActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.cart_discount import CartDiscountSetCustomFieldActionSchema

            return CartDiscountSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.cart_discount import CartDiscountSetCustomTypeActionSchema

            return CartDiscountSetCustomTypeActionSchema().load(data)
        if data["action"] == "setDescription":
            from ._schemas.cart_discount import CartDiscountSetDescriptionActionSchema

            return CartDiscountSetDescriptionActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.cart_discount import CartDiscountSetKeyActionSchema

            return CartDiscountSetKeyActionSchema().load(data)
        if data["action"] == "setValidFrom":
            from ._schemas.cart_discount import CartDiscountSetValidFromActionSchema

            return CartDiscountSetValidFromActionSchema().load(data)
        if data["action"] == "setValidFromAndUntil":
            from ._schemas.cart_discount import (
                CartDiscountSetValidFromAndUntilActionSchema,
            )

            return CartDiscountSetValidFromAndUntilActionSchema().load(data)
        if data["action"] == "setValidUntil":
            from ._schemas.cart_discount import CartDiscountSetValidUntilActionSchema

            return CartDiscountSetValidUntilActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountUpdateActionSchema

        return CartDiscountUpdateActionSchema().dump(self)


class CartDiscountValue(_BaseType):
    type: str

    def __init__(self, *, type: str):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartDiscountValue":
        if data["type"] == "absolute":
            from ._schemas.cart_discount import CartDiscountValueAbsoluteSchema

            return CartDiscountValueAbsoluteSchema().load(data)
        if data["type"] == "giftLineItem":
            from ._schemas.cart_discount import CartDiscountValueGiftLineItemSchema

            return CartDiscountValueGiftLineItemSchema().load(data)
        if data["type"] == "relative":
            from ._schemas.cart_discount import CartDiscountValueRelativeSchema

            return CartDiscountValueRelativeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountValueSchema

        return CartDiscountValueSchema().dump(self)


class CartDiscountValueAbsolute(CartDiscountValue):
    money: typing.List["TypedMoney"]

    def __init__(self, *, money: typing.List["TypedMoney"]):
        self.money = money
        super().__init__(type="absolute")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountValueAbsolute":
        from ._schemas.cart_discount import CartDiscountValueAbsoluteSchema

        return CartDiscountValueAbsoluteSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountValueAbsoluteSchema

        return CartDiscountValueAbsoluteSchema().dump(self)


class CartDiscountValueDraft(_BaseType):
    type: str

    def __init__(self, *, type: str):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountValueDraft":
        if data["type"] == "absolute":
            from ._schemas.cart_discount import CartDiscountValueAbsoluteDraftSchema

            return CartDiscountValueAbsoluteDraftSchema().load(data)
        if data["type"] == "giftLineItem":
            from ._schemas.cart_discount import CartDiscountValueGiftLineItemDraftSchema

            return CartDiscountValueGiftLineItemDraftSchema().load(data)
        if data["type"] == "relative":
            from ._schemas.cart_discount import CartDiscountValueRelativeDraftSchema

            return CartDiscountValueRelativeDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountValueDraftSchema

        return CartDiscountValueDraftSchema().dump(self)


class CartDiscountValueAbsoluteDraft(CartDiscountValueDraft):
    money: typing.List["Money"]

    def __init__(self, *, money: typing.List["Money"]):
        self.money = money
        super().__init__(type="absolute")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountValueAbsoluteDraft":
        from ._schemas.cart_discount import CartDiscountValueAbsoluteDraftSchema

        return CartDiscountValueAbsoluteDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountValueAbsoluteDraftSchema

        return CartDiscountValueAbsoluteDraftSchema().dump(self)


class CartDiscountValueGiftLineItem(CartDiscountValue):
    product: "ProductReference"
    variant_id: int
    #: The channel must have the role `InventorySupply`
    supply_channel: typing.Optional["ChannelReference"]
    #: The channel must have the role `ProductDistribution`
    distribution_channel: typing.Optional["ChannelReference"]

    def __init__(
        self,
        *,
        product: "ProductReference",
        variant_id: int,
        supply_channel: typing.Optional["ChannelReference"] = None,
        distribution_channel: typing.Optional["ChannelReference"] = None
    ):
        self.product = product
        self.variant_id = variant_id
        self.supply_channel = supply_channel
        self.distribution_channel = distribution_channel
        super().__init__(type="giftLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountValueGiftLineItem":
        from ._schemas.cart_discount import CartDiscountValueGiftLineItemSchema

        return CartDiscountValueGiftLineItemSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountValueGiftLineItemSchema

        return CartDiscountValueGiftLineItemSchema().dump(self)


class CartDiscountValueGiftLineItemDraft(CartDiscountValueDraft):
    product: "ProductResourceIdentifier"
    variant_id: int
    #: The channel must have the role `InventorySupply`
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    #: The channel must have the role `ProductDistribution`
    distribution_channel: typing.Optional["ChannelResourceIdentifier"]

    def __init__(
        self,
        *,
        product: "ProductResourceIdentifier",
        variant_id: int,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        distribution_channel: typing.Optional["ChannelResourceIdentifier"] = None
    ):
        self.product = product
        self.variant_id = variant_id
        self.supply_channel = supply_channel
        self.distribution_channel = distribution_channel
        super().__init__(type="giftLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountValueGiftLineItemDraft":
        from ._schemas.cart_discount import CartDiscountValueGiftLineItemDraftSchema

        return CartDiscountValueGiftLineItemDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountValueGiftLineItemDraftSchema

        return CartDiscountValueGiftLineItemDraftSchema().dump(self)


class CartDiscountValueRelative(CartDiscountValue):
    permyriad: int

    def __init__(self, *, permyriad: int):
        self.permyriad = permyriad
        super().__init__(type="relative")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountValueRelative":
        from ._schemas.cart_discount import CartDiscountValueRelativeSchema

        return CartDiscountValueRelativeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountValueRelativeSchema

        return CartDiscountValueRelativeSchema().dump(self)


class CartDiscountValueRelativeDraft(CartDiscountValueDraft):
    permyriad: int

    def __init__(self, *, permyriad: int):
        self.permyriad = permyriad
        super().__init__(type="relative")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountValueRelativeDraft":
        from ._schemas.cart_discount import CartDiscountValueRelativeDraftSchema

        return CartDiscountValueRelativeDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountValueRelativeDraftSchema

        return CartDiscountValueRelativeDraftSchema().dump(self)


class MultiBuyCustomLineItemsTarget(CartDiscountTarget):
    #: A valid custom line item target predicate. The discount will be applied to custom line items that are
    #: matched by the predicate.
    predicate: str
    #: Quantity of line items that need to be present in order to trigger an application of this discount.
    trigger_quantity: int
    #: Quantity of line items that are discounted per application of this discount.
    discounted_quantity: int
    #: Maximum number of applications of this discount.
    max_occurrence: typing.Optional[int]
    selection_mode: "SelectionMode"

    def __init__(
        self,
        *,
        predicate: str,
        trigger_quantity: int,
        discounted_quantity: int,
        max_occurrence: typing.Optional[int] = None,
        selection_mode: "SelectionMode"
    ):
        self.predicate = predicate
        self.trigger_quantity = trigger_quantity
        self.discounted_quantity = discounted_quantity
        self.max_occurrence = max_occurrence
        self.selection_mode = selection_mode
        super().__init__(type="multiBuyCustomLineItems")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MultiBuyCustomLineItemsTarget":
        from ._schemas.cart_discount import MultiBuyCustomLineItemsTargetSchema

        return MultiBuyCustomLineItemsTargetSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import MultiBuyCustomLineItemsTargetSchema

        return MultiBuyCustomLineItemsTargetSchema().dump(self)


class MultiBuyLineItemsTarget(CartDiscountTarget):
    #: A valid line item target predicate. The discount will be applied to line items that are matched by the predicate.
    predicate: str
    #: Quantity of line items that need to be present in order to trigger an application of this discount.
    trigger_quantity: int
    #: Quantity of line items that are discounted per application of this discount.
    discounted_quantity: int
    #: Maximum number of applications of this discount.
    max_occurrence: typing.Optional[int]
    selection_mode: "SelectionMode"

    def __init__(
        self,
        *,
        predicate: str,
        trigger_quantity: int,
        discounted_quantity: int,
        max_occurrence: typing.Optional[int] = None,
        selection_mode: "SelectionMode"
    ):
        self.predicate = predicate
        self.trigger_quantity = trigger_quantity
        self.discounted_quantity = discounted_quantity
        self.max_occurrence = max_occurrence
        self.selection_mode = selection_mode
        super().__init__(type="multiBuyLineItems")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MultiBuyLineItemsTarget":
        from ._schemas.cart_discount import MultiBuyLineItemsTargetSchema

        return MultiBuyLineItemsTargetSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import MultiBuyLineItemsTargetSchema

        return MultiBuyLineItemsTargetSchema().dump(self)


class SelectionMode(enum.Enum):
    CHEAPEST = "Cheapest"
    MOST_EXPENSIVE = "MostExpensive"


class StackingMode(enum.Enum):
    STACKING = "Stacking"
    STOP_AFTER_THIS_DISCOUNT = "StopAfterThisDiscount"


class CartDiscountChangeCartPredicateAction(CartDiscountUpdateAction):
    #: A valid Cart predicate.
    cart_predicate: str

    def __init__(self, *, cart_predicate: str):
        self.cart_predicate = cart_predicate
        super().__init__(action="changeCartPredicate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountChangeCartPredicateAction":
        from ._schemas.cart_discount import CartDiscountChangeCartPredicateActionSchema

        return CartDiscountChangeCartPredicateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountChangeCartPredicateActionSchema

        return CartDiscountChangeCartPredicateActionSchema().dump(self)


class CartDiscountChangeIsActiveAction(CartDiscountUpdateAction):
    is_active: bool

    def __init__(self, *, is_active: bool):
        self.is_active = is_active
        super().__init__(action="changeIsActive")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountChangeIsActiveAction":
        from ._schemas.cart_discount import CartDiscountChangeIsActiveActionSchema

        return CartDiscountChangeIsActiveActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountChangeIsActiveActionSchema

        return CartDiscountChangeIsActiveActionSchema().dump(self)


class CartDiscountChangeNameAction(CartDiscountUpdateAction):
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString"):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountChangeNameAction":
        from ._schemas.cart_discount import CartDiscountChangeNameActionSchema

        return CartDiscountChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountChangeNameActionSchema

        return CartDiscountChangeNameActionSchema().dump(self)


class CartDiscountChangeRequiresDiscountCodeAction(CartDiscountUpdateAction):
    requires_discount_code: bool

    def __init__(self, *, requires_discount_code: bool):
        self.requires_discount_code = requires_discount_code
        super().__init__(action="changeRequiresDiscountCode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountChangeRequiresDiscountCodeAction":
        from ._schemas.cart_discount import (
            CartDiscountChangeRequiresDiscountCodeActionSchema,
        )

        return CartDiscountChangeRequiresDiscountCodeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import (
            CartDiscountChangeRequiresDiscountCodeActionSchema,
        )

        return CartDiscountChangeRequiresDiscountCodeActionSchema().dump(self)


class CartDiscountChangeSortOrderAction(CartDiscountUpdateAction):
    #: The string must contain a number between 0 and 1.
    #: A discount with greater sortOrder is prioritized higher than a discount with lower sortOrder.
    sort_order: str

    def __init__(self, *, sort_order: str):
        self.sort_order = sort_order
        super().__init__(action="changeSortOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountChangeSortOrderAction":
        from ._schemas.cart_discount import CartDiscountChangeSortOrderActionSchema

        return CartDiscountChangeSortOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountChangeSortOrderActionSchema

        return CartDiscountChangeSortOrderActionSchema().dump(self)


class CartDiscountChangeStackingModeAction(CartDiscountUpdateAction):
    stacking_mode: "StackingMode"

    def __init__(self, *, stacking_mode: "StackingMode"):
        self.stacking_mode = stacking_mode
        super().__init__(action="changeStackingMode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountChangeStackingModeAction":
        from ._schemas.cart_discount import CartDiscountChangeStackingModeActionSchema

        return CartDiscountChangeStackingModeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountChangeStackingModeActionSchema

        return CartDiscountChangeStackingModeActionSchema().dump(self)


class CartDiscountChangeTargetAction(CartDiscountUpdateAction):
    target: "CartDiscountTarget"

    def __init__(self, *, target: "CartDiscountTarget"):
        self.target = target
        super().__init__(action="changeTarget")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountChangeTargetAction":
        from ._schemas.cart_discount import CartDiscountChangeTargetActionSchema

        return CartDiscountChangeTargetActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountChangeTargetActionSchema

        return CartDiscountChangeTargetActionSchema().dump(self)


class CartDiscountChangeValueAction(CartDiscountUpdateAction):
    value: "CartDiscountValueDraft"

    def __init__(self, *, value: "CartDiscountValueDraft"):
        self.value = value
        super().__init__(action="changeValue")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountChangeValueAction":
        from ._schemas.cart_discount import CartDiscountChangeValueActionSchema

        return CartDiscountChangeValueActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountChangeValueActionSchema

        return CartDiscountChangeValueActionSchema().dump(self)


class CartDiscountSetCustomFieldAction(CartDiscountUpdateAction):
    name: str
    #: If `value` is absent or `null`, this field will be removed if it exists.
    #: Trying to remove a field that does not exist will fail with an `InvalidOperation` error.
    #: If `value` is provided, set the `value` of the field defined by the `name`.
    #: The FieldDefinition determines the format for the `value` to be provided.
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountSetCustomFieldAction":
        from ._schemas.cart_discount import CartDiscountSetCustomFieldActionSchema

        return CartDiscountSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountSetCustomFieldActionSchema

        return CartDiscountSetCustomFieldActionSchema().dump(self)


class CartDiscountSetCustomTypeAction(CartDiscountUpdateAction):
    #: If absent, the custom type and any existing CustomFields are removed.
    type: typing.Optional["TypeResourceIdentifier"]
    #: A valid JSON object, based on the FieldDefinitions of the Type.
    #: Sets the custom fields to this value.
    fields: typing.Optional[object]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional[object] = None
    ):
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountSetCustomTypeAction":
        from ._schemas.cart_discount import CartDiscountSetCustomTypeActionSchema

        return CartDiscountSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountSetCustomTypeActionSchema

        return CartDiscountSetCustomTypeActionSchema().dump(self)


class CartDiscountSetDescriptionAction(CartDiscountUpdateAction):
    #: If the `description` parameter is not included, the field will be emptied.
    description: typing.Optional["LocalizedString"]

    def __init__(self, *, description: typing.Optional["LocalizedString"] = None):
        self.description = description
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountSetDescriptionAction":
        from ._schemas.cart_discount import CartDiscountSetDescriptionActionSchema

        return CartDiscountSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountSetDescriptionActionSchema

        return CartDiscountSetDescriptionActionSchema().dump(self)


class CartDiscountSetKeyAction(CartDiscountUpdateAction):
    #: If `key` is absent or `null`, this field will be removed if it exists.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountSetKeyAction":
        from ._schemas.cart_discount import CartDiscountSetKeyActionSchema

        return CartDiscountSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountSetKeyActionSchema

        return CartDiscountSetKeyActionSchema().dump(self)


class CartDiscountSetValidFromAction(CartDiscountUpdateAction):
    #: If absent, the field with the value is removed in case a value was set before.
    valid_from: typing.Optional[datetime.datetime]

    def __init__(self, *, valid_from: typing.Optional[datetime.datetime] = None):
        self.valid_from = valid_from
        super().__init__(action="setValidFrom")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountSetValidFromAction":
        from ._schemas.cart_discount import CartDiscountSetValidFromActionSchema

        return CartDiscountSetValidFromActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountSetValidFromActionSchema

        return CartDiscountSetValidFromActionSchema().dump(self)


class CartDiscountSetValidFromAndUntilAction(CartDiscountUpdateAction):
    #: If absent, the field with the value is removed in case a value was set before.
    valid_from: typing.Optional[datetime.datetime]
    #: If absent, the field with the value is removed in case a value was set before.
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None
    ):
        self.valid_from = valid_from
        self.valid_until = valid_until
        super().__init__(action="setValidFromAndUntil")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountSetValidFromAndUntilAction":
        from ._schemas.cart_discount import CartDiscountSetValidFromAndUntilActionSchema

        return CartDiscountSetValidFromAndUntilActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountSetValidFromAndUntilActionSchema

        return CartDiscountSetValidFromAndUntilActionSchema().dump(self)


class CartDiscountSetValidUntilAction(CartDiscountUpdateAction):
    #: If absent, the field with the value is removed in case a value was set before.
    valid_until: typing.Optional[datetime.datetime]

    def __init__(self, *, valid_until: typing.Optional[datetime.datetime] = None):
        self.valid_until = valid_until
        super().__init__(action="setValidUntil")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountSetValidUntilAction":
        from ._schemas.cart_discount import CartDiscountSetValidUntilActionSchema

        return CartDiscountSetValidUntilActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.cart_discount import CartDiscountSetValidUntilActionSchema

        return CartDiscountSetValidUntilActionSchema().dump(self)

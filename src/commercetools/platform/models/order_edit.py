# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .cart import CartOrigin, InventoryMode, RoundingMode, TaxCalculationMode, TaxMode
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier
from .order import (
    Order,
    OrderState,
    PaymentState,
    ReturnPaymentState,
    ReturnShipmentState,
    ShipmentState,
    StagedOrderUpdateAction,
)

if typing.TYPE_CHECKING:
    from .cart import (
        CartOrigin,
        CartReference,
        CustomLineItem,
        DiscountCodeInfo,
        ExternalLineItemTotalPrice,
        ExternalTaxAmountDraft,
        ExternalTaxRateDraft,
        InventoryMode,
        ItemShippingDetailsDraft,
        LineItem,
        RoundingMode,
        ShippingInfo,
        ShippingRateInput,
        ShippingRateInputDraft,
        TaxCalculationMode,
        TaxedPrice,
        TaxMode,
        TaxPortionDraft,
    )
    from .cart_discount import CartDiscountReference
    from .channel import ChannelResourceIdentifier
    from .common import (
        Address,
        CreatedBy,
        LastModifiedBy,
        LocalizedString,
        Money,
        ReferenceTypeId,
        TypedMoney,
    )
    from .customer_group import CustomerGroupReference, CustomerGroupResourceIdentifier
    from .discount_code import DiscountCodeReference
    from .error import ErrorObject
    from .message import MessagePayload
    from .order import (
        DeliveryItem,
        ItemState,
        OrderReference,
        OrderState,
        ParcelDraft,
        ParcelMeasurements,
        PaymentInfo,
        PaymentState,
        ReturnInfo,
        ReturnItemDraft,
        ReturnPaymentState,
        ReturnShipmentState,
        ShipmentState,
        StagedOrderUpdateAction,
        SyncInfo,
        TrackingData,
    )
    from .payment import PaymentResourceIdentifier
    from .shipping_method import ShippingMethodResourceIdentifier, ShippingRateDraft
    from .shopping_list import ShoppingListResourceIdentifier
    from .state import StateReference, StateResourceIdentifier
    from .store import StoreKeyReference
    from .tax_category import TaxCategoryResourceIdentifier
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "OrderEdit",
    "OrderEditAddStagedActionAction",
    "OrderEditApplied",
    "OrderEditApply",
    "OrderEditDraft",
    "OrderEditNotProcessed",
    "OrderEditPagedQueryResponse",
    "OrderEditPreviewFailure",
    "OrderEditPreviewSuccess",
    "OrderEditReference",
    "OrderEditResourceIdentifier",
    "OrderEditResult",
    "OrderEditSetCommentAction",
    "OrderEditSetCustomFieldAction",
    "OrderEditSetCustomTypeAction",
    "OrderEditSetKeyAction",
    "OrderEditSetStagedActionsAction",
    "OrderEditUpdate",
    "OrderEditUpdateAction",
    "OrderExcerpt",
    "StagedOrder",
    "StagedOrderAddCustomLineItemAction",
    "StagedOrderAddDeliveryAction",
    "StagedOrderAddDiscountCodeAction",
    "StagedOrderAddItemShippingAddressAction",
    "StagedOrderAddLineItemAction",
    "StagedOrderAddParcelToDeliveryAction",
    "StagedOrderAddPaymentAction",
    "StagedOrderAddReturnInfoAction",
    "StagedOrderAddShoppingListAction",
    "StagedOrderChangeCustomLineItemMoneyAction",
    "StagedOrderChangeCustomLineItemQuantityAction",
    "StagedOrderChangeLineItemQuantityAction",
    "StagedOrderChangeOrderStateAction",
    "StagedOrderChangePaymentStateAction",
    "StagedOrderChangeShipmentStateAction",
    "StagedOrderChangeTaxCalculationModeAction",
    "StagedOrderChangeTaxModeAction",
    "StagedOrderChangeTaxRoundingModeAction",
    "StagedOrderImportCustomLineItemStateAction",
    "StagedOrderImportLineItemStateAction",
    "StagedOrderRemoveCustomLineItemAction",
    "StagedOrderRemoveDeliveryAction",
    "StagedOrderRemoveDiscountCodeAction",
    "StagedOrderRemoveItemShippingAddressAction",
    "StagedOrderRemoveLineItemAction",
    "StagedOrderRemoveParcelFromDeliveryAction",
    "StagedOrderRemovePaymentAction",
    "StagedOrderSetBillingAddressAction",
    "StagedOrderSetCountryAction",
    "StagedOrderSetCustomFieldAction",
    "StagedOrderSetCustomLineItemCustomFieldAction",
    "StagedOrderSetCustomLineItemCustomTypeAction",
    "StagedOrderSetCustomLineItemShippingDetailsAction",
    "StagedOrderSetCustomLineItemTaxAmountAction",
    "StagedOrderSetCustomLineItemTaxRateAction",
    "StagedOrderSetCustomShippingMethodAction",
    "StagedOrderSetCustomTypeAction",
    "StagedOrderSetCustomerEmailAction",
    "StagedOrderSetCustomerGroupAction",
    "StagedOrderSetCustomerIdAction",
    "StagedOrderSetDeliveryAddressAction",
    "StagedOrderSetDeliveryItemsAction",
    "StagedOrderSetLineItemCustomFieldAction",
    "StagedOrderSetLineItemCustomTypeAction",
    "StagedOrderSetLineItemDistributionChannelAction",
    "StagedOrderSetLineItemPriceAction",
    "StagedOrderSetLineItemShippingDetailsAction",
    "StagedOrderSetLineItemTaxAmountAction",
    "StagedOrderSetLineItemTaxRateAction",
    "StagedOrderSetLineItemTotalPriceAction",
    "StagedOrderSetLocaleAction",
    "StagedOrderSetOrderNumberAction",
    "StagedOrderSetOrderTotalTaxAction",
    "StagedOrderSetParcelItemsAction",
    "StagedOrderSetParcelMeasurementsAction",
    "StagedOrderSetParcelTrackingDataAction",
    "StagedOrderSetReturnPaymentStateAction",
    "StagedOrderSetReturnShipmentStateAction",
    "StagedOrderSetShippingAddressAction",
    "StagedOrderSetShippingAddressAndCustomShippingMethodAction",
    "StagedOrderSetShippingAddressAndShippingMethodAction",
    "StagedOrderSetShippingMethodAction",
    "StagedOrderSetShippingMethodTaxAmountAction",
    "StagedOrderSetShippingMethodTaxRateAction",
    "StagedOrderSetShippingRateInputAction",
    "StagedOrderTransitionCustomLineItemStateAction",
    "StagedOrderTransitionLineItemStateAction",
    "StagedOrderTransitionStateAction",
    "StagedOrderUpdateItemShippingAddressAction",
    "StagedOrderUpdateSyncInfoAction",
]


class OrderEdit(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    #: Unique identifier for this edit.
    key: typing.Optional[str]
    #: The order to be updated with this edit.
    resource: "OrderReference"
    #: The actions to apply to the Order.
    #: Cannot be updated after the edit has been applied.
    staged_actions: typing.List["StagedOrderUpdateAction"]
    custom: typing.Optional["CustomFields"]
    #: Contains a preview of the changes in case of unapplied edit.
    #: For applied edits, it contains the summary of the changes.
    result: "OrderEditResult"
    #: This field can be used to add textual information regarding the edit.
    comment: typing.Optional[str]

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
        resource: "OrderReference",
        staged_actions: typing.List["StagedOrderUpdateAction"],
        custom: typing.Optional["CustomFields"] = None,
        result: "OrderEditResult",
        comment: typing.Optional[str] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.resource = resource
        self.staged_actions = staged_actions
        self.custom = custom
        self.result = result
        self.comment = comment
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderEdit":
        from ._schemas.order_edit import OrderEditSchema

        return OrderEditSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditSchema

        return OrderEditSchema().dump(self)


class OrderEditApply(_BaseType):
    edit_version: int
    resource_version: int

    def __init__(self, *, edit_version: int, resource_version: int):
        self.edit_version = edit_version
        self.resource_version = resource_version
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderEditApply":
        from ._schemas.order_edit import OrderEditApplySchema

        return OrderEditApplySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditApplySchema

        return OrderEditApplySchema().dump(self)


class OrderEditDraft(_BaseType):
    #: Unique identifier for this edit.
    key: typing.Optional[str]
    #: The order to be updated with this edit.
    resource: "OrderReference"
    #: The actions to apply to `resource`.
    staged_actions: typing.Optional[typing.List["StagedOrderUpdateAction"]]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    #: This field can be used to add additional textual information regarding the edit.
    comment: typing.Optional[str]
    #: When set to `true` the edit is applied on the Order without persisting it.
    dry_run: typing.Optional[bool]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        resource: "OrderReference",
        staged_actions: typing.Optional[typing.List["StagedOrderUpdateAction"]] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        comment: typing.Optional[str] = None,
        dry_run: typing.Optional[bool] = None
    ):
        self.key = key
        self.resource = resource
        self.staged_actions = staged_actions
        self.custom = custom
        self.comment = comment
        self.dry_run = dry_run
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderEditDraft":
        from ._schemas.order_edit import OrderEditDraftSchema

        return OrderEditDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditDraftSchema

        return OrderEditDraftSchema().dump(self)


class OrderEditPagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["OrderEdit"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["OrderEdit"]
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
    ) -> "OrderEditPagedQueryResponse":
        from ._schemas.order_edit import OrderEditPagedQueryResponseSchema

        return OrderEditPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditPagedQueryResponseSchema

        return OrderEditPagedQueryResponseSchema().dump(self)


class OrderEditReference(Reference):
    obj: typing.Optional["OrderEdit"]

    def __init__(self, *, id: str, obj: typing.Optional["OrderEdit"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.ORDER_EDIT)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderEditReference":
        from ._schemas.order_edit import OrderEditReferenceSchema

        return OrderEditReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditReferenceSchema

        return OrderEditReferenceSchema().dump(self)


class OrderEditResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.ORDER_EDIT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderEditResourceIdentifier":
        from ._schemas.order_edit import OrderEditResourceIdentifierSchema

        return OrderEditResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditResourceIdentifierSchema

        return OrderEditResourceIdentifierSchema().dump(self)


class OrderEditResult(_BaseType):
    type: str

    def __init__(self, *, type: str):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderEditResult":
        if data["type"] == "Applied":
            from ._schemas.order_edit import OrderEditAppliedSchema

            return OrderEditAppliedSchema().load(data)
        if data["type"] == "NotProcessed":
            from ._schemas.order_edit import OrderEditNotProcessedSchema

            return OrderEditNotProcessedSchema().load(data)
        if data["type"] == "PreviewFailure":
            from ._schemas.order_edit import OrderEditPreviewFailureSchema

            return OrderEditPreviewFailureSchema().load(data)
        if data["type"] == "PreviewSuccess":
            from ._schemas.order_edit import OrderEditPreviewSuccessSchema

            return OrderEditPreviewSuccessSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditResultSchema

        return OrderEditResultSchema().dump(self)


class OrderEditApplied(OrderEditResult):
    applied_at: datetime.datetime
    excerpt_before_edit: "OrderExcerpt"
    excerpt_after_edit: "OrderExcerpt"

    def __init__(
        self,
        *,
        applied_at: datetime.datetime,
        excerpt_before_edit: "OrderExcerpt",
        excerpt_after_edit: "OrderExcerpt"
    ):
        self.applied_at = applied_at
        self.excerpt_before_edit = excerpt_before_edit
        self.excerpt_after_edit = excerpt_after_edit
        super().__init__(type="Applied")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderEditApplied":
        from ._schemas.order_edit import OrderEditAppliedSchema

        return OrderEditAppliedSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditAppliedSchema

        return OrderEditAppliedSchema().dump(self)


class OrderEditNotProcessed(OrderEditResult):
    def __init__(self):

        super().__init__(type="NotProcessed")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderEditNotProcessed":
        from ._schemas.order_edit import OrderEditNotProcessedSchema

        return OrderEditNotProcessedSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditNotProcessedSchema

        return OrderEditNotProcessedSchema().dump(self)


class OrderEditPreviewFailure(OrderEditResult):
    errors: typing.List["ErrorObject"]

    def __init__(self, *, errors: typing.List["ErrorObject"]):
        self.errors = errors
        super().__init__(type="PreviewFailure")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderEditPreviewFailure":
        from ._schemas.order_edit import OrderEditPreviewFailureSchema

        return OrderEditPreviewFailureSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditPreviewFailureSchema

        return OrderEditPreviewFailureSchema().dump(self)


class OrderEditPreviewSuccess(OrderEditResult):
    preview: "StagedOrder"
    message_payloads: typing.List["MessagePayload"]

    def __init__(
        self, *, preview: "StagedOrder", message_payloads: typing.List["MessagePayload"]
    ):
        self.preview = preview
        self.message_payloads = message_payloads
        super().__init__(type="PreviewSuccess")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderEditPreviewSuccess":
        from ._schemas.order_edit import OrderEditPreviewSuccessSchema

        return OrderEditPreviewSuccessSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditPreviewSuccessSchema

        return OrderEditPreviewSuccessSchema().dump(self)


class OrderEditUpdate(_BaseType):
    version: int
    actions: typing.List["OrderEditUpdateAction"]
    dry_run: typing.Optional[bool]

    def __init__(
        self,
        *,
        version: int,
        actions: typing.List["OrderEditUpdateAction"],
        dry_run: typing.Optional[bool] = None
    ):
        self.version = version
        self.actions = actions
        self.dry_run = dry_run
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderEditUpdate":
        from ._schemas.order_edit import OrderEditUpdateSchema

        return OrderEditUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditUpdateSchema

        return OrderEditUpdateSchema().dump(self)


class OrderEditUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderEditUpdateAction":
        if data["action"] == "addStagedAction":
            from ._schemas.order_edit import OrderEditAddStagedActionActionSchema

            return OrderEditAddStagedActionActionSchema().load(data)
        if data["action"] == "setComment":
            from ._schemas.order_edit import OrderEditSetCommentActionSchema

            return OrderEditSetCommentActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.order_edit import OrderEditSetCustomFieldActionSchema

            return OrderEditSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.order_edit import OrderEditSetCustomTypeActionSchema

            return OrderEditSetCustomTypeActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.order_edit import OrderEditSetKeyActionSchema

            return OrderEditSetKeyActionSchema().load(data)
        if data["action"] == "setStagedActions":
            from ._schemas.order_edit import OrderEditSetStagedActionsActionSchema

            return OrderEditSetStagedActionsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditUpdateActionSchema

        return OrderEditUpdateActionSchema().dump(self)


class OrderExcerpt(_BaseType):
    total_price: "TypedMoney"
    taxed_price: typing.Optional["TaxedPrice"]
    version: int

    def __init__(
        self,
        *,
        total_price: "TypedMoney",
        taxed_price: typing.Optional["TaxedPrice"] = None,
        version: int
    ):
        self.total_price = total_price
        self.taxed_price = taxed_price
        self.version = version
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderExcerpt":
        from ._schemas.order_edit import OrderExcerptSchema

        return OrderExcerptSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderExcerptSchema

        return OrderExcerptSchema().dump(self)


class StagedOrder(Order):
    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        completed_at: typing.Optional[datetime.datetime] = None,
        order_number: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        customer_email: typing.Optional[str] = None,
        anonymous_id: typing.Optional[str] = None,
        store: typing.Optional["StoreKeyReference"] = None,
        line_items: typing.List["LineItem"],
        custom_line_items: typing.List["CustomLineItem"],
        total_price: "TypedMoney",
        taxed_price: typing.Optional["TaxedPrice"] = None,
        shipping_address: typing.Optional["Address"] = None,
        billing_address: typing.Optional["Address"] = None,
        tax_mode: typing.Optional["TaxMode"] = None,
        tax_rounding_mode: typing.Optional["RoundingMode"] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        country: typing.Optional[str] = None,
        order_state: "OrderState",
        state: typing.Optional["StateReference"] = None,
        shipment_state: typing.Optional["ShipmentState"] = None,
        payment_state: typing.Optional["PaymentState"] = None,
        shipping_info: typing.Optional["ShippingInfo"] = None,
        sync_info: typing.List["SyncInfo"],
        return_info: typing.Optional[typing.List["ReturnInfo"]] = None,
        discount_codes: typing.Optional[typing.List["DiscountCodeInfo"]] = None,
        last_message_sequence_number: int,
        cart: typing.Optional["CartReference"] = None,
        custom: typing.Optional["CustomFields"] = None,
        payment_info: typing.Optional["PaymentInfo"] = None,
        locale: typing.Optional[str] = None,
        inventory_mode: typing.Optional["InventoryMode"] = None,
        origin: "CartOrigin",
        tax_calculation_mode: typing.Optional["TaxCalculationMode"] = None,
        shipping_rate_input: typing.Optional["ShippingRateInput"] = None,
        item_shipping_addresses: typing.Optional[typing.List["Address"]] = None,
        refused_gifts: typing.List["CartDiscountReference"]
    ):

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
            completed_at=completed_at,
            order_number=order_number,
            customer_id=customer_id,
            customer_email=customer_email,
            anonymous_id=anonymous_id,
            store=store,
            line_items=line_items,
            custom_line_items=custom_line_items,
            total_price=total_price,
            taxed_price=taxed_price,
            shipping_address=shipping_address,
            billing_address=billing_address,
            tax_mode=tax_mode,
            tax_rounding_mode=tax_rounding_mode,
            customer_group=customer_group,
            country=country,
            order_state=order_state,
            state=state,
            shipment_state=shipment_state,
            payment_state=payment_state,
            shipping_info=shipping_info,
            sync_info=sync_info,
            return_info=return_info,
            discount_codes=discount_codes,
            last_message_sequence_number=last_message_sequence_number,
            cart=cart,
            custom=custom,
            payment_info=payment_info,
            locale=locale,
            inventory_mode=inventory_mode,
            origin=origin,
            tax_calculation_mode=tax_calculation_mode,
            shipping_rate_input=shipping_rate_input,
            item_shipping_addresses=item_shipping_addresses,
            refused_gifts=refused_gifts,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StagedOrder":
        from ._schemas.order_edit import StagedOrderSchema

        return StagedOrderSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSchema

        return StagedOrderSchema().dump(self)


class OrderEditAddStagedActionAction(OrderEditUpdateAction):
    staged_action: "StagedOrderUpdateAction"

    def __init__(self, *, staged_action: "StagedOrderUpdateAction"):
        self.staged_action = staged_action
        super().__init__(action="addStagedAction")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderEditAddStagedActionAction":
        from ._schemas.order_edit import OrderEditAddStagedActionActionSchema

        return OrderEditAddStagedActionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditAddStagedActionActionSchema

        return OrderEditAddStagedActionActionSchema().dump(self)


class OrderEditSetCommentAction(OrderEditUpdateAction):
    comment: typing.Optional[str]

    def __init__(self, *, comment: typing.Optional[str] = None):
        self.comment = comment
        super().__init__(action="setComment")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderEditSetCommentAction":
        from ._schemas.order_edit import OrderEditSetCommentActionSchema

        return OrderEditSetCommentActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditSetCommentActionSchema

        return OrderEditSetCommentActionSchema().dump(self)


class OrderEditSetCustomFieldAction(OrderEditUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderEditSetCustomFieldAction":
        from ._schemas.order_edit import OrderEditSetCustomFieldActionSchema

        return OrderEditSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditSetCustomFieldActionSchema

        return OrderEditSetCustomFieldActionSchema().dump(self)


class OrderEditSetCustomTypeAction(OrderEditUpdateAction):
    #: If set, the custom type is set to this new value.
    #: If absent, the custom type and any existing custom fields are removed.
    type: typing.Optional["TypeResourceIdentifier"]
    #: If set, the custom fields are set to this new value.
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
    ) -> "OrderEditSetCustomTypeAction":
        from ._schemas.order_edit import OrderEditSetCustomTypeActionSchema

        return OrderEditSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditSetCustomTypeActionSchema

        return OrderEditSetCustomTypeActionSchema().dump(self)


class OrderEditSetKeyAction(OrderEditUpdateAction):
    #: If `key` is absent or `null`, this field will be removed if it exists.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderEditSetKeyAction":
        from ._schemas.order_edit import OrderEditSetKeyActionSchema

        return OrderEditSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditSetKeyActionSchema

        return OrderEditSetKeyActionSchema().dump(self)


class OrderEditSetStagedActionsAction(OrderEditUpdateAction):
    #: The actions to edit the `resource`.
    staged_actions: typing.List["StagedOrderUpdateAction"]

    def __init__(self, *, staged_actions: typing.List["StagedOrderUpdateAction"]):
        self.staged_actions = staged_actions
        super().__init__(action="setStagedActions")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderEditSetStagedActionsAction":
        from ._schemas.order_edit import OrderEditSetStagedActionsActionSchema

        return OrderEditSetStagedActionsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import OrderEditSetStagedActionsActionSchema

        return OrderEditSetStagedActionsActionSchema().dump(self)


class StagedOrderAddCustomLineItemAction(StagedOrderUpdateAction):
    money: "Money"
    name: "LocalizedString"
    quantity: typing.Optional[float]
    slug: str
    tax_category: typing.Optional["TaxCategoryResourceIdentifier"]
    custom: typing.Optional["CustomFieldsDraft"]
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self,
        *,
        money: "Money",
        name: "LocalizedString",
        quantity: typing.Optional[float] = None,
        slug: str,
        tax_category: typing.Optional["TaxCategoryResourceIdentifier"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.money = money
        self.name = name
        self.quantity = quantity
        self.slug = slug
        self.tax_category = tax_category
        self.custom = custom
        self.external_tax_rate = external_tax_rate
        super().__init__(action="addCustomLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderAddCustomLineItemAction":
        from ._schemas.order_edit import StagedOrderAddCustomLineItemActionSchema

        return StagedOrderAddCustomLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderAddCustomLineItemActionSchema

        return StagedOrderAddCustomLineItemActionSchema().dump(self)


class StagedOrderAddDeliveryAction(StagedOrderUpdateAction):
    items: typing.Optional[typing.List["DeliveryItem"]]
    address: typing.Optional["Address"]
    parcels: typing.Optional[typing.List["ParcelDraft"]]

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List["DeliveryItem"]] = None,
        address: typing.Optional["Address"] = None,
        parcels: typing.Optional[typing.List["ParcelDraft"]] = None
    ):
        self.items = items
        self.address = address
        self.parcels = parcels
        super().__init__(action="addDelivery")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderAddDeliveryAction":
        from ._schemas.order_edit import StagedOrderAddDeliveryActionSchema

        return StagedOrderAddDeliveryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderAddDeliveryActionSchema

        return StagedOrderAddDeliveryActionSchema().dump(self)


class StagedOrderAddDiscountCodeAction(StagedOrderUpdateAction):
    code: str

    def __init__(self, *, code: str):
        self.code = code
        super().__init__(action="addDiscountCode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderAddDiscountCodeAction":
        from ._schemas.order_edit import StagedOrderAddDiscountCodeActionSchema

        return StagedOrderAddDiscountCodeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderAddDiscountCodeActionSchema

        return StagedOrderAddDiscountCodeActionSchema().dump(self)


class StagedOrderAddItemShippingAddressAction(StagedOrderUpdateAction):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(action="addItemShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderAddItemShippingAddressAction":
        from ._schemas.order_edit import StagedOrderAddItemShippingAddressActionSchema

        return StagedOrderAddItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderAddItemShippingAddressActionSchema

        return StagedOrderAddItemShippingAddressActionSchema().dump(self)


class StagedOrderAddLineItemAction(StagedOrderUpdateAction):
    custom: typing.Optional["CustomFieldsDraft"]
    distribution_channel: typing.Optional["ChannelResourceIdentifier"]
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]
    product_id: typing.Optional[str]
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    quantity: typing.Optional[float]
    added_at: typing.Optional[datetime.datetime]
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    external_price: typing.Optional["Money"]
    external_total_price: typing.Optional["ExternalLineItemTotalPrice"]
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        distribution_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None,
        product_id: typing.Optional[str] = None,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        quantity: typing.Optional[float] = None,
        added_at: typing.Optional[datetime.datetime] = None,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        external_price: typing.Optional["Money"] = None,
        external_total_price: typing.Optional["ExternalLineItemTotalPrice"] = None,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.custom = custom
        self.distribution_channel = distribution_channel
        self.external_tax_rate = external_tax_rate
        self.product_id = product_id
        self.variant_id = variant_id
        self.sku = sku
        self.quantity = quantity
        self.added_at = added_at
        self.supply_channel = supply_channel
        self.external_price = external_price
        self.external_total_price = external_total_price
        self.shipping_details = shipping_details
        super().__init__(action="addLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderAddLineItemAction":
        from ._schemas.order_edit import StagedOrderAddLineItemActionSchema

        return StagedOrderAddLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderAddLineItemActionSchema

        return StagedOrderAddLineItemActionSchema().dump(self)


class StagedOrderAddParcelToDeliveryAction(StagedOrderUpdateAction):
    delivery_id: str
    measurements: typing.Optional["ParcelMeasurements"]
    tracking_data: typing.Optional["TrackingData"]
    items: typing.Optional[typing.List["DeliveryItem"]]

    def __init__(
        self,
        *,
        delivery_id: str,
        measurements: typing.Optional["ParcelMeasurements"] = None,
        tracking_data: typing.Optional["TrackingData"] = None,
        items: typing.Optional[typing.List["DeliveryItem"]] = None
    ):
        self.delivery_id = delivery_id
        self.measurements = measurements
        self.tracking_data = tracking_data
        self.items = items
        super().__init__(action="addParcelToDelivery")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderAddParcelToDeliveryAction":
        from ._schemas.order_edit import StagedOrderAddParcelToDeliveryActionSchema

        return StagedOrderAddParcelToDeliveryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderAddParcelToDeliveryActionSchema

        return StagedOrderAddParcelToDeliveryActionSchema().dump(self)


class StagedOrderAddPaymentAction(StagedOrderUpdateAction):
    payment: "PaymentResourceIdentifier"

    def __init__(self, *, payment: "PaymentResourceIdentifier"):
        self.payment = payment
        super().__init__(action="addPayment")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderAddPaymentAction":
        from ._schemas.order_edit import StagedOrderAddPaymentActionSchema

        return StagedOrderAddPaymentActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderAddPaymentActionSchema

        return StagedOrderAddPaymentActionSchema().dump(self)


class StagedOrderAddReturnInfoAction(StagedOrderUpdateAction):
    return_tracking_id: typing.Optional[str]
    items: typing.List["ReturnItemDraft"]
    return_date: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        return_tracking_id: typing.Optional[str] = None,
        items: typing.List["ReturnItemDraft"],
        return_date: typing.Optional[datetime.datetime] = None
    ):
        self.return_tracking_id = return_tracking_id
        self.items = items
        self.return_date = return_date
        super().__init__(action="addReturnInfo")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderAddReturnInfoAction":
        from ._schemas.order_edit import StagedOrderAddReturnInfoActionSchema

        return StagedOrderAddReturnInfoActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderAddReturnInfoActionSchema

        return StagedOrderAddReturnInfoActionSchema().dump(self)


class StagedOrderAddShoppingListAction(StagedOrderUpdateAction):
    shopping_list: "ShoppingListResourceIdentifier"
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    distribution_channel: typing.Optional["ChannelResourceIdentifier"]

    def __init__(
        self,
        *,
        shopping_list: "ShoppingListResourceIdentifier",
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        distribution_channel: typing.Optional["ChannelResourceIdentifier"] = None
    ):
        self.shopping_list = shopping_list
        self.supply_channel = supply_channel
        self.distribution_channel = distribution_channel
        super().__init__(action="addShoppingList")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderAddShoppingListAction":
        from ._schemas.order_edit import StagedOrderAddShoppingListActionSchema

        return StagedOrderAddShoppingListActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderAddShoppingListActionSchema

        return StagedOrderAddShoppingListActionSchema().dump(self)


class StagedOrderChangeCustomLineItemMoneyAction(StagedOrderUpdateAction):
    custom_line_item_id: str
    money: "Money"

    def __init__(self, *, custom_line_item_id: str, money: "Money"):
        self.custom_line_item_id = custom_line_item_id
        self.money = money
        super().__init__(action="changeCustomLineItemMoney")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderChangeCustomLineItemMoneyAction":
        from ._schemas.order_edit import (
            StagedOrderChangeCustomLineItemMoneyActionSchema,
        )

        return StagedOrderChangeCustomLineItemMoneyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderChangeCustomLineItemMoneyActionSchema,
        )

        return StagedOrderChangeCustomLineItemMoneyActionSchema().dump(self)


class StagedOrderChangeCustomLineItemQuantityAction(StagedOrderUpdateAction):
    custom_line_item_id: str
    quantity: float

    def __init__(self, *, custom_line_item_id: str, quantity: float):
        self.custom_line_item_id = custom_line_item_id
        self.quantity = quantity
        super().__init__(action="changeCustomLineItemQuantity")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderChangeCustomLineItemQuantityAction":
        from ._schemas.order_edit import (
            StagedOrderChangeCustomLineItemQuantityActionSchema,
        )

        return StagedOrderChangeCustomLineItemQuantityActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderChangeCustomLineItemQuantityActionSchema,
        )

        return StagedOrderChangeCustomLineItemQuantityActionSchema().dump(self)


class StagedOrderChangeLineItemQuantityAction(StagedOrderUpdateAction):
    line_item_id: str
    quantity: float
    external_price: typing.Optional["Money"]
    external_total_price: typing.Optional["ExternalLineItemTotalPrice"]

    def __init__(
        self,
        *,
        line_item_id: str,
        quantity: float,
        external_price: typing.Optional["Money"] = None,
        external_total_price: typing.Optional["ExternalLineItemTotalPrice"] = None
    ):
        self.line_item_id = line_item_id
        self.quantity = quantity
        self.external_price = external_price
        self.external_total_price = external_total_price
        super().__init__(action="changeLineItemQuantity")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderChangeLineItemQuantityAction":
        from ._schemas.order_edit import StagedOrderChangeLineItemQuantityActionSchema

        return StagedOrderChangeLineItemQuantityActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderChangeLineItemQuantityActionSchema

        return StagedOrderChangeLineItemQuantityActionSchema().dump(self)


class StagedOrderChangeOrderStateAction(StagedOrderUpdateAction):
    order_state: "OrderState"

    def __init__(self, *, order_state: "OrderState"):
        self.order_state = order_state
        super().__init__(action="changeOrderState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderChangeOrderStateAction":
        from ._schemas.order_edit import StagedOrderChangeOrderStateActionSchema

        return StagedOrderChangeOrderStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderChangeOrderStateActionSchema

        return StagedOrderChangeOrderStateActionSchema().dump(self)


class StagedOrderChangePaymentStateAction(StagedOrderUpdateAction):
    payment_state: typing.Optional["PaymentState"]

    def __init__(self, *, payment_state: typing.Optional["PaymentState"] = None):
        self.payment_state = payment_state
        super().__init__(action="changePaymentState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderChangePaymentStateAction":
        from ._schemas.order_edit import StagedOrderChangePaymentStateActionSchema

        return StagedOrderChangePaymentStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderChangePaymentStateActionSchema

        return StagedOrderChangePaymentStateActionSchema().dump(self)


class StagedOrderChangeShipmentStateAction(StagedOrderUpdateAction):
    shipment_state: typing.Optional["ShipmentState"]

    def __init__(self, *, shipment_state: typing.Optional["ShipmentState"] = None):
        self.shipment_state = shipment_state
        super().__init__(action="changeShipmentState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderChangeShipmentStateAction":
        from ._schemas.order_edit import StagedOrderChangeShipmentStateActionSchema

        return StagedOrderChangeShipmentStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderChangeShipmentStateActionSchema

        return StagedOrderChangeShipmentStateActionSchema().dump(self)


class StagedOrderChangeTaxCalculationModeAction(StagedOrderUpdateAction):
    tax_calculation_mode: "TaxCalculationMode"

    def __init__(self, *, tax_calculation_mode: "TaxCalculationMode"):
        self.tax_calculation_mode = tax_calculation_mode
        super().__init__(action="changeTaxCalculationMode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderChangeTaxCalculationModeAction":
        from ._schemas.order_edit import StagedOrderChangeTaxCalculationModeActionSchema

        return StagedOrderChangeTaxCalculationModeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderChangeTaxCalculationModeActionSchema

        return StagedOrderChangeTaxCalculationModeActionSchema().dump(self)


class StagedOrderChangeTaxModeAction(StagedOrderUpdateAction):
    tax_mode: "TaxMode"

    def __init__(self, *, tax_mode: "TaxMode"):
        self.tax_mode = tax_mode
        super().__init__(action="changeTaxMode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderChangeTaxModeAction":
        from ._schemas.order_edit import StagedOrderChangeTaxModeActionSchema

        return StagedOrderChangeTaxModeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderChangeTaxModeActionSchema

        return StagedOrderChangeTaxModeActionSchema().dump(self)


class StagedOrderChangeTaxRoundingModeAction(StagedOrderUpdateAction):
    tax_rounding_mode: "RoundingMode"

    def __init__(self, *, tax_rounding_mode: "RoundingMode"):
        self.tax_rounding_mode = tax_rounding_mode
        super().__init__(action="changeTaxRoundingMode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderChangeTaxRoundingModeAction":
        from ._schemas.order_edit import StagedOrderChangeTaxRoundingModeActionSchema

        return StagedOrderChangeTaxRoundingModeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderChangeTaxRoundingModeActionSchema

        return StagedOrderChangeTaxRoundingModeActionSchema().dump(self)


class StagedOrderImportCustomLineItemStateAction(StagedOrderUpdateAction):
    custom_line_item_id: str
    state: typing.List["ItemState"]

    def __init__(self, *, custom_line_item_id: str, state: typing.List["ItemState"]):
        self.custom_line_item_id = custom_line_item_id
        self.state = state
        super().__init__(action="importCustomLineItemState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderImportCustomLineItemStateAction":
        from ._schemas.order_edit import (
            StagedOrderImportCustomLineItemStateActionSchema,
        )

        return StagedOrderImportCustomLineItemStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderImportCustomLineItemStateActionSchema,
        )

        return StagedOrderImportCustomLineItemStateActionSchema().dump(self)


class StagedOrderImportLineItemStateAction(StagedOrderUpdateAction):
    line_item_id: str
    state: typing.List["ItemState"]

    def __init__(self, *, line_item_id: str, state: typing.List["ItemState"]):
        self.line_item_id = line_item_id
        self.state = state
        super().__init__(action="importLineItemState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderImportLineItemStateAction":
        from ._schemas.order_edit import StagedOrderImportLineItemStateActionSchema

        return StagedOrderImportLineItemStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderImportLineItemStateActionSchema

        return StagedOrderImportLineItemStateActionSchema().dump(self)


class StagedOrderRemoveCustomLineItemAction(StagedOrderUpdateAction):
    custom_line_item_id: str

    def __init__(self, *, custom_line_item_id: str):
        self.custom_line_item_id = custom_line_item_id
        super().__init__(action="removeCustomLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderRemoveCustomLineItemAction":
        from ._schemas.order_edit import StagedOrderRemoveCustomLineItemActionSchema

        return StagedOrderRemoveCustomLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderRemoveCustomLineItemActionSchema

        return StagedOrderRemoveCustomLineItemActionSchema().dump(self)


class StagedOrderRemoveDeliveryAction(StagedOrderUpdateAction):
    delivery_id: str

    def __init__(self, *, delivery_id: str):
        self.delivery_id = delivery_id
        super().__init__(action="removeDelivery")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderRemoveDeliveryAction":
        from ._schemas.order_edit import StagedOrderRemoveDeliveryActionSchema

        return StagedOrderRemoveDeliveryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderRemoveDeliveryActionSchema

        return StagedOrderRemoveDeliveryActionSchema().dump(self)


class StagedOrderRemoveDiscountCodeAction(StagedOrderUpdateAction):
    discount_code: "DiscountCodeReference"

    def __init__(self, *, discount_code: "DiscountCodeReference"):
        self.discount_code = discount_code
        super().__init__(action="removeDiscountCode")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderRemoveDiscountCodeAction":
        from ._schemas.order_edit import StagedOrderRemoveDiscountCodeActionSchema

        return StagedOrderRemoveDiscountCodeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderRemoveDiscountCodeActionSchema

        return StagedOrderRemoveDiscountCodeActionSchema().dump(self)


class StagedOrderRemoveItemShippingAddressAction(StagedOrderUpdateAction):
    address_key: str

    def __init__(self, *, address_key: str):
        self.address_key = address_key
        super().__init__(action="removeItemShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderRemoveItemShippingAddressAction":
        from ._schemas.order_edit import (
            StagedOrderRemoveItemShippingAddressActionSchema,
        )

        return StagedOrderRemoveItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderRemoveItemShippingAddressActionSchema,
        )

        return StagedOrderRemoveItemShippingAddressActionSchema().dump(self)


class StagedOrderRemoveLineItemAction(StagedOrderUpdateAction):
    line_item_id: str
    quantity: typing.Optional[float]
    external_price: typing.Optional["Money"]
    external_total_price: typing.Optional["ExternalLineItemTotalPrice"]
    shipping_details_to_remove: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        line_item_id: str,
        quantity: typing.Optional[float] = None,
        external_price: typing.Optional["Money"] = None,
        external_total_price: typing.Optional["ExternalLineItemTotalPrice"] = None,
        shipping_details_to_remove: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.line_item_id = line_item_id
        self.quantity = quantity
        self.external_price = external_price
        self.external_total_price = external_total_price
        self.shipping_details_to_remove = shipping_details_to_remove
        super().__init__(action="removeLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderRemoveLineItemAction":
        from ._schemas.order_edit import StagedOrderRemoveLineItemActionSchema

        return StagedOrderRemoveLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderRemoveLineItemActionSchema

        return StagedOrderRemoveLineItemActionSchema().dump(self)


class StagedOrderRemoveParcelFromDeliveryAction(StagedOrderUpdateAction):
    parcel_id: str

    def __init__(self, *, parcel_id: str):
        self.parcel_id = parcel_id
        super().__init__(action="removeParcelFromDelivery")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderRemoveParcelFromDeliveryAction":
        from ._schemas.order_edit import StagedOrderRemoveParcelFromDeliveryActionSchema

        return StagedOrderRemoveParcelFromDeliveryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderRemoveParcelFromDeliveryActionSchema

        return StagedOrderRemoveParcelFromDeliveryActionSchema().dump(self)


class StagedOrderRemovePaymentAction(StagedOrderUpdateAction):
    payment: "PaymentResourceIdentifier"

    def __init__(self, *, payment: "PaymentResourceIdentifier"):
        self.payment = payment
        super().__init__(action="removePayment")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderRemovePaymentAction":
        from ._schemas.order_edit import StagedOrderRemovePaymentActionSchema

        return StagedOrderRemovePaymentActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderRemovePaymentActionSchema

        return StagedOrderRemovePaymentActionSchema().dump(self)


class StagedOrderSetBillingAddressAction(StagedOrderUpdateAction):
    address: typing.Optional["Address"]

    def __init__(self, *, address: typing.Optional["Address"] = None):
        self.address = address
        super().__init__(action="setBillingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetBillingAddressAction":
        from ._schemas.order_edit import StagedOrderSetBillingAddressActionSchema

        return StagedOrderSetBillingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetBillingAddressActionSchema

        return StagedOrderSetBillingAddressActionSchema().dump(self)


class StagedOrderSetCountryAction(StagedOrderUpdateAction):
    country: typing.Optional[str]

    def __init__(self, *, country: typing.Optional[str] = None):
        self.country = country
        super().__init__(action="setCountry")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetCountryAction":
        from ._schemas.order_edit import StagedOrderSetCountryActionSchema

        return StagedOrderSetCountryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetCountryActionSchema

        return StagedOrderSetCountryActionSchema().dump(self)


class StagedOrderSetCustomFieldAction(StagedOrderUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetCustomFieldAction":
        from ._schemas.order_edit import StagedOrderSetCustomFieldActionSchema

        return StagedOrderSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetCustomFieldActionSchema

        return StagedOrderSetCustomFieldActionSchema().dump(self)


class StagedOrderSetCustomLineItemCustomFieldAction(StagedOrderUpdateAction):
    custom_line_item_id: str
    name: str
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        custom_line_item_id: str,
        name: str,
        value: typing.Optional[typing.Any] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.name = name
        self.value = value
        super().__init__(action="setCustomLineItemCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetCustomLineItemCustomFieldAction":
        from ._schemas.order_edit import (
            StagedOrderSetCustomLineItemCustomFieldActionSchema,
        )

        return StagedOrderSetCustomLineItemCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderSetCustomLineItemCustomFieldActionSchema,
        )

        return StagedOrderSetCustomLineItemCustomFieldActionSchema().dump(self)


class StagedOrderSetCustomLineItemCustomTypeAction(StagedOrderUpdateAction):
    custom_line_item_id: str
    type: typing.Optional["TypeResourceIdentifier"]
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        custom_line_item_id: str,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomLineItemCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetCustomLineItemCustomTypeAction":
        from ._schemas.order_edit import (
            StagedOrderSetCustomLineItemCustomTypeActionSchema,
        )

        return StagedOrderSetCustomLineItemCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderSetCustomLineItemCustomTypeActionSchema,
        )

        return StagedOrderSetCustomLineItemCustomTypeActionSchema().dump(self)


class StagedOrderSetCustomLineItemShippingDetailsAction(StagedOrderUpdateAction):
    custom_line_item_id: str
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        custom_line_item_id: str,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.shipping_details = shipping_details
        super().__init__(action="setCustomLineItemShippingDetails")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetCustomLineItemShippingDetailsAction":
        from ._schemas.order_edit import (
            StagedOrderSetCustomLineItemShippingDetailsActionSchema,
        )

        return StagedOrderSetCustomLineItemShippingDetailsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderSetCustomLineItemShippingDetailsActionSchema,
        )

        return StagedOrderSetCustomLineItemShippingDetailsActionSchema().dump(self)


class StagedOrderSetCustomLineItemTaxAmountAction(StagedOrderUpdateAction):
    custom_line_item_id: str
    external_tax_amount: typing.Optional["ExternalTaxAmountDraft"]

    def __init__(
        self,
        *,
        custom_line_item_id: str,
        external_tax_amount: typing.Optional["ExternalTaxAmountDraft"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.external_tax_amount = external_tax_amount
        super().__init__(action="setCustomLineItemTaxAmount")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetCustomLineItemTaxAmountAction":
        from ._schemas.order_edit import (
            StagedOrderSetCustomLineItemTaxAmountActionSchema,
        )

        return StagedOrderSetCustomLineItemTaxAmountActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderSetCustomLineItemTaxAmountActionSchema,
        )

        return StagedOrderSetCustomLineItemTaxAmountActionSchema().dump(self)


class StagedOrderSetCustomLineItemTaxRateAction(StagedOrderUpdateAction):
    custom_line_item_id: str
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self,
        *,
        custom_line_item_id: str,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.external_tax_rate = external_tax_rate
        super().__init__(action="setCustomLineItemTaxRate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetCustomLineItemTaxRateAction":
        from ._schemas.order_edit import StagedOrderSetCustomLineItemTaxRateActionSchema

        return StagedOrderSetCustomLineItemTaxRateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetCustomLineItemTaxRateActionSchema

        return StagedOrderSetCustomLineItemTaxRateActionSchema().dump(self)


class StagedOrderSetCustomShippingMethodAction(StagedOrderUpdateAction):
    shipping_method_name: str
    shipping_rate: "ShippingRateDraft"
    tax_category: typing.Optional["TaxCategoryResourceIdentifier"]
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self,
        *,
        shipping_method_name: str,
        shipping_rate: "ShippingRateDraft",
        tax_category: typing.Optional["TaxCategoryResourceIdentifier"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.shipping_method_name = shipping_method_name
        self.shipping_rate = shipping_rate
        self.tax_category = tax_category
        self.external_tax_rate = external_tax_rate
        super().__init__(action="setCustomShippingMethod")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetCustomShippingMethodAction":
        from ._schemas.order_edit import StagedOrderSetCustomShippingMethodActionSchema

        return StagedOrderSetCustomShippingMethodActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetCustomShippingMethodActionSchema

        return StagedOrderSetCustomShippingMethodActionSchema().dump(self)


class StagedOrderSetCustomTypeAction(StagedOrderUpdateAction):
    type: typing.Optional["TypeResourceIdentifier"]
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetCustomTypeAction":
        from ._schemas.order_edit import StagedOrderSetCustomTypeActionSchema

        return StagedOrderSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetCustomTypeActionSchema

        return StagedOrderSetCustomTypeActionSchema().dump(self)


class StagedOrderSetCustomerEmailAction(StagedOrderUpdateAction):
    email: typing.Optional[str]

    def __init__(self, *, email: typing.Optional[str] = None):
        self.email = email
        super().__init__(action="setCustomerEmail")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetCustomerEmailAction":
        from ._schemas.order_edit import StagedOrderSetCustomerEmailActionSchema

        return StagedOrderSetCustomerEmailActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetCustomerEmailActionSchema

        return StagedOrderSetCustomerEmailActionSchema().dump(self)


class StagedOrderSetCustomerGroupAction(StagedOrderUpdateAction):
    customer_group: typing.Optional["CustomerGroupResourceIdentifier"]

    def __init__(
        self,
        *,
        customer_group: typing.Optional["CustomerGroupResourceIdentifier"] = None
    ):
        self.customer_group = customer_group
        super().__init__(action="setCustomerGroup")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetCustomerGroupAction":
        from ._schemas.order_edit import StagedOrderSetCustomerGroupActionSchema

        return StagedOrderSetCustomerGroupActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetCustomerGroupActionSchema

        return StagedOrderSetCustomerGroupActionSchema().dump(self)


class StagedOrderSetCustomerIdAction(StagedOrderUpdateAction):
    customer_id: typing.Optional[str]

    def __init__(self, *, customer_id: typing.Optional[str] = None):
        self.customer_id = customer_id
        super().__init__(action="setCustomerId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetCustomerIdAction":
        from ._schemas.order_edit import StagedOrderSetCustomerIdActionSchema

        return StagedOrderSetCustomerIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetCustomerIdActionSchema

        return StagedOrderSetCustomerIdActionSchema().dump(self)


class StagedOrderSetDeliveryAddressAction(StagedOrderUpdateAction):
    delivery_id: str
    address: typing.Optional["Address"]

    def __init__(self, *, delivery_id: str, address: typing.Optional["Address"] = None):
        self.delivery_id = delivery_id
        self.address = address
        super().__init__(action="setDeliveryAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetDeliveryAddressAction":
        from ._schemas.order_edit import StagedOrderSetDeliveryAddressActionSchema

        return StagedOrderSetDeliveryAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetDeliveryAddressActionSchema

        return StagedOrderSetDeliveryAddressActionSchema().dump(self)


class StagedOrderSetDeliveryItemsAction(StagedOrderUpdateAction):
    delivery_id: str
    items: typing.List["DeliveryItem"]

    def __init__(self, *, delivery_id: str, items: typing.List["DeliveryItem"]):
        self.delivery_id = delivery_id
        self.items = items
        super().__init__(action="setDeliveryItems")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetDeliveryItemsAction":
        from ._schemas.order_edit import StagedOrderSetDeliveryItemsActionSchema

        return StagedOrderSetDeliveryItemsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetDeliveryItemsActionSchema

        return StagedOrderSetDeliveryItemsActionSchema().dump(self)


class StagedOrderSetLineItemCustomFieldAction(StagedOrderUpdateAction):
    line_item_id: str
    name: str
    value: typing.Optional[typing.Any]

    def __init__(
        self, *, line_item_id: str, name: str, value: typing.Optional[typing.Any] = None
    ):
        self.line_item_id = line_item_id
        self.name = name
        self.value = value
        super().__init__(action="setLineItemCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetLineItemCustomFieldAction":
        from ._schemas.order_edit import StagedOrderSetLineItemCustomFieldActionSchema

        return StagedOrderSetLineItemCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetLineItemCustomFieldActionSchema

        return StagedOrderSetLineItemCustomFieldActionSchema().dump(self)


class StagedOrderSetLineItemCustomTypeAction(StagedOrderUpdateAction):
    line_item_id: str
    type: typing.Optional["TypeResourceIdentifier"]
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        line_item_id: str,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.line_item_id = line_item_id
        self.type = type
        self.fields = fields
        super().__init__(action="setLineItemCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetLineItemCustomTypeAction":
        from ._schemas.order_edit import StagedOrderSetLineItemCustomTypeActionSchema

        return StagedOrderSetLineItemCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetLineItemCustomTypeActionSchema

        return StagedOrderSetLineItemCustomTypeActionSchema().dump(self)


class StagedOrderSetLineItemDistributionChannelAction(StagedOrderUpdateAction):
    line_item_id: str
    distribution_channel: typing.Optional["ChannelResourceIdentifier"]

    def __init__(
        self,
        *,
        line_item_id: str,
        distribution_channel: typing.Optional["ChannelResourceIdentifier"] = None
    ):
        self.line_item_id = line_item_id
        self.distribution_channel = distribution_channel
        super().__init__(action="setLineItemDistributionChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetLineItemDistributionChannelAction":
        from ._schemas.order_edit import (
            StagedOrderSetLineItemDistributionChannelActionSchema,
        )

        return StagedOrderSetLineItemDistributionChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderSetLineItemDistributionChannelActionSchema,
        )

        return StagedOrderSetLineItemDistributionChannelActionSchema().dump(self)


class StagedOrderSetLineItemPriceAction(StagedOrderUpdateAction):
    line_item_id: str
    external_price: typing.Optional["Money"]

    def __init__(
        self, *, line_item_id: str, external_price: typing.Optional["Money"] = None
    ):
        self.line_item_id = line_item_id
        self.external_price = external_price
        super().__init__(action="setLineItemPrice")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetLineItemPriceAction":
        from ._schemas.order_edit import StagedOrderSetLineItemPriceActionSchema

        return StagedOrderSetLineItemPriceActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetLineItemPriceActionSchema

        return StagedOrderSetLineItemPriceActionSchema().dump(self)


class StagedOrderSetLineItemShippingDetailsAction(StagedOrderUpdateAction):
    line_item_id: str
    shipping_details: typing.Optional["ItemShippingDetailsDraft"]

    def __init__(
        self,
        *,
        line_item_id: str,
        shipping_details: typing.Optional["ItemShippingDetailsDraft"] = None
    ):
        self.line_item_id = line_item_id
        self.shipping_details = shipping_details
        super().__init__(action="setLineItemShippingDetails")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetLineItemShippingDetailsAction":
        from ._schemas.order_edit import (
            StagedOrderSetLineItemShippingDetailsActionSchema,
        )

        return StagedOrderSetLineItemShippingDetailsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderSetLineItemShippingDetailsActionSchema,
        )

        return StagedOrderSetLineItemShippingDetailsActionSchema().dump(self)


class StagedOrderSetLineItemTaxAmountAction(StagedOrderUpdateAction):
    line_item_id: str
    external_tax_amount: typing.Optional["ExternalTaxAmountDraft"]

    def __init__(
        self,
        *,
        line_item_id: str,
        external_tax_amount: typing.Optional["ExternalTaxAmountDraft"] = None
    ):
        self.line_item_id = line_item_id
        self.external_tax_amount = external_tax_amount
        super().__init__(action="setLineItemTaxAmount")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetLineItemTaxAmountAction":
        from ._schemas.order_edit import StagedOrderSetLineItemTaxAmountActionSchema

        return StagedOrderSetLineItemTaxAmountActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetLineItemTaxAmountActionSchema

        return StagedOrderSetLineItemTaxAmountActionSchema().dump(self)


class StagedOrderSetLineItemTaxRateAction(StagedOrderUpdateAction):
    line_item_id: str
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self,
        *,
        line_item_id: str,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.line_item_id = line_item_id
        self.external_tax_rate = external_tax_rate
        super().__init__(action="setLineItemTaxRate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetLineItemTaxRateAction":
        from ._schemas.order_edit import StagedOrderSetLineItemTaxRateActionSchema

        return StagedOrderSetLineItemTaxRateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetLineItemTaxRateActionSchema

        return StagedOrderSetLineItemTaxRateActionSchema().dump(self)


class StagedOrderSetLineItemTotalPriceAction(StagedOrderUpdateAction):
    line_item_id: str
    external_total_price: typing.Optional["ExternalLineItemTotalPrice"]

    def __init__(
        self,
        *,
        line_item_id: str,
        external_total_price: typing.Optional["ExternalLineItemTotalPrice"] = None
    ):
        self.line_item_id = line_item_id
        self.external_total_price = external_total_price
        super().__init__(action="setLineItemTotalPrice")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetLineItemTotalPriceAction":
        from ._schemas.order_edit import StagedOrderSetLineItemTotalPriceActionSchema

        return StagedOrderSetLineItemTotalPriceActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetLineItemTotalPriceActionSchema

        return StagedOrderSetLineItemTotalPriceActionSchema().dump(self)


class StagedOrderSetLocaleAction(StagedOrderUpdateAction):
    locale: typing.Optional[str]

    def __init__(self, *, locale: typing.Optional[str] = None):
        self.locale = locale
        super().__init__(action="setLocale")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetLocaleAction":
        from ._schemas.order_edit import StagedOrderSetLocaleActionSchema

        return StagedOrderSetLocaleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetLocaleActionSchema

        return StagedOrderSetLocaleActionSchema().dump(self)


class StagedOrderSetOrderNumberAction(StagedOrderUpdateAction):
    order_number: typing.Optional[str]

    def __init__(self, *, order_number: typing.Optional[str] = None):
        self.order_number = order_number
        super().__init__(action="setOrderNumber")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetOrderNumberAction":
        from ._schemas.order_edit import StagedOrderSetOrderNumberActionSchema

        return StagedOrderSetOrderNumberActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetOrderNumberActionSchema

        return StagedOrderSetOrderNumberActionSchema().dump(self)


class StagedOrderSetOrderTotalTaxAction(StagedOrderUpdateAction):
    external_total_gross: "Money"
    external_tax_portions: typing.Optional[typing.List["TaxPortionDraft"]]

    def __init__(
        self,
        *,
        external_total_gross: "Money",
        external_tax_portions: typing.Optional[typing.List["TaxPortionDraft"]] = None
    ):
        self.external_total_gross = external_total_gross
        self.external_tax_portions = external_tax_portions
        super().__init__(action="setOrderTotalTax")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetOrderTotalTaxAction":
        from ._schemas.order_edit import StagedOrderSetOrderTotalTaxActionSchema

        return StagedOrderSetOrderTotalTaxActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetOrderTotalTaxActionSchema

        return StagedOrderSetOrderTotalTaxActionSchema().dump(self)


class StagedOrderSetParcelItemsAction(StagedOrderUpdateAction):
    parcel_id: str
    items: typing.List["DeliveryItem"]

    def __init__(self, *, parcel_id: str, items: typing.List["DeliveryItem"]):
        self.parcel_id = parcel_id
        self.items = items
        super().__init__(action="setParcelItems")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetParcelItemsAction":
        from ._schemas.order_edit import StagedOrderSetParcelItemsActionSchema

        return StagedOrderSetParcelItemsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetParcelItemsActionSchema

        return StagedOrderSetParcelItemsActionSchema().dump(self)


class StagedOrderSetParcelMeasurementsAction(StagedOrderUpdateAction):
    parcel_id: str
    measurements: typing.Optional["ParcelMeasurements"]

    def __init__(
        self,
        *,
        parcel_id: str,
        measurements: typing.Optional["ParcelMeasurements"] = None
    ):
        self.parcel_id = parcel_id
        self.measurements = measurements
        super().__init__(action="setParcelMeasurements")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetParcelMeasurementsAction":
        from ._schemas.order_edit import StagedOrderSetParcelMeasurementsActionSchema

        return StagedOrderSetParcelMeasurementsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetParcelMeasurementsActionSchema

        return StagedOrderSetParcelMeasurementsActionSchema().dump(self)


class StagedOrderSetParcelTrackingDataAction(StagedOrderUpdateAction):
    parcel_id: str
    tracking_data: typing.Optional["TrackingData"]

    def __init__(
        self, *, parcel_id: str, tracking_data: typing.Optional["TrackingData"] = None
    ):
        self.parcel_id = parcel_id
        self.tracking_data = tracking_data
        super().__init__(action="setParcelTrackingData")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetParcelTrackingDataAction":
        from ._schemas.order_edit import StagedOrderSetParcelTrackingDataActionSchema

        return StagedOrderSetParcelTrackingDataActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetParcelTrackingDataActionSchema

        return StagedOrderSetParcelTrackingDataActionSchema().dump(self)


class StagedOrderSetReturnPaymentStateAction(StagedOrderUpdateAction):
    return_item_id: str
    payment_state: "ReturnPaymentState"

    def __init__(self, *, return_item_id: str, payment_state: "ReturnPaymentState"):
        self.return_item_id = return_item_id
        self.payment_state = payment_state
        super().__init__(action="setReturnPaymentState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetReturnPaymentStateAction":
        from ._schemas.order_edit import StagedOrderSetReturnPaymentStateActionSchema

        return StagedOrderSetReturnPaymentStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetReturnPaymentStateActionSchema

        return StagedOrderSetReturnPaymentStateActionSchema().dump(self)


class StagedOrderSetReturnShipmentStateAction(StagedOrderUpdateAction):
    return_item_id: str
    shipment_state: "ReturnShipmentState"

    def __init__(self, *, return_item_id: str, shipment_state: "ReturnShipmentState"):
        self.return_item_id = return_item_id
        self.shipment_state = shipment_state
        super().__init__(action="setReturnShipmentState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetReturnShipmentStateAction":
        from ._schemas.order_edit import StagedOrderSetReturnShipmentStateActionSchema

        return StagedOrderSetReturnShipmentStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetReturnShipmentStateActionSchema

        return StagedOrderSetReturnShipmentStateActionSchema().dump(self)


class StagedOrderSetShippingAddressAction(StagedOrderUpdateAction):
    address: typing.Optional["Address"]

    def __init__(self, *, address: typing.Optional["Address"] = None):
        self.address = address
        super().__init__(action="setShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetShippingAddressAction":
        from ._schemas.order_edit import StagedOrderSetShippingAddressActionSchema

        return StagedOrderSetShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetShippingAddressActionSchema

        return StagedOrderSetShippingAddressActionSchema().dump(self)


class StagedOrderSetShippingAddressAndCustomShippingMethodAction(
    StagedOrderUpdateAction
):
    address: "Address"
    shipping_method_name: str
    shipping_rate: "ShippingRateDraft"
    tax_category: typing.Optional["TaxCategoryResourceIdentifier"]
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self,
        *,
        address: "Address",
        shipping_method_name: str,
        shipping_rate: "ShippingRateDraft",
        tax_category: typing.Optional["TaxCategoryResourceIdentifier"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.address = address
        self.shipping_method_name = shipping_method_name
        self.shipping_rate = shipping_rate
        self.tax_category = tax_category
        self.external_tax_rate = external_tax_rate
        super().__init__(action="setShippingAddressAndCustomShippingMethod")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetShippingAddressAndCustomShippingMethodAction":
        from ._schemas.order_edit import (
            StagedOrderSetShippingAddressAndCustomShippingMethodActionSchema,
        )

        return StagedOrderSetShippingAddressAndCustomShippingMethodActionSchema().load(
            data
        )

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderSetShippingAddressAndCustomShippingMethodActionSchema,
        )

        return StagedOrderSetShippingAddressAndCustomShippingMethodActionSchema().dump(
            self
        )


class StagedOrderSetShippingAddressAndShippingMethodAction(StagedOrderUpdateAction):
    address: "Address"
    shipping_method: typing.Optional["ShippingMethodResourceIdentifier"]
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self,
        *,
        address: "Address",
        shipping_method: typing.Optional["ShippingMethodResourceIdentifier"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.address = address
        self.shipping_method = shipping_method
        self.external_tax_rate = external_tax_rate
        super().__init__(action="setShippingAddressAndShippingMethod")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetShippingAddressAndShippingMethodAction":
        from ._schemas.order_edit import (
            StagedOrderSetShippingAddressAndShippingMethodActionSchema,
        )

        return StagedOrderSetShippingAddressAndShippingMethodActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderSetShippingAddressAndShippingMethodActionSchema,
        )

        return StagedOrderSetShippingAddressAndShippingMethodActionSchema().dump(self)


class StagedOrderSetShippingMethodAction(StagedOrderUpdateAction):
    shipping_method: typing.Optional["ShippingMethodResourceIdentifier"]
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self,
        *,
        shipping_method: typing.Optional["ShippingMethodResourceIdentifier"] = None,
        external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.shipping_method = shipping_method
        self.external_tax_rate = external_tax_rate
        super().__init__(action="setShippingMethod")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetShippingMethodAction":
        from ._schemas.order_edit import StagedOrderSetShippingMethodActionSchema

        return StagedOrderSetShippingMethodActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetShippingMethodActionSchema

        return StagedOrderSetShippingMethodActionSchema().dump(self)


class StagedOrderSetShippingMethodTaxAmountAction(StagedOrderUpdateAction):
    external_tax_amount: typing.Optional["ExternalTaxAmountDraft"]

    def __init__(
        self, *, external_tax_amount: typing.Optional["ExternalTaxAmountDraft"] = None
    ):
        self.external_tax_amount = external_tax_amount
        super().__init__(action="setShippingMethodTaxAmount")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetShippingMethodTaxAmountAction":
        from ._schemas.order_edit import (
            StagedOrderSetShippingMethodTaxAmountActionSchema,
        )

        return StagedOrderSetShippingMethodTaxAmountActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderSetShippingMethodTaxAmountActionSchema,
        )

        return StagedOrderSetShippingMethodTaxAmountActionSchema().dump(self)


class StagedOrderSetShippingMethodTaxRateAction(StagedOrderUpdateAction):
    external_tax_rate: typing.Optional["ExternalTaxRateDraft"]

    def __init__(
        self, *, external_tax_rate: typing.Optional["ExternalTaxRateDraft"] = None
    ):
        self.external_tax_rate = external_tax_rate
        super().__init__(action="setShippingMethodTaxRate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetShippingMethodTaxRateAction":
        from ._schemas.order_edit import StagedOrderSetShippingMethodTaxRateActionSchema

        return StagedOrderSetShippingMethodTaxRateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetShippingMethodTaxRateActionSchema

        return StagedOrderSetShippingMethodTaxRateActionSchema().dump(self)


class StagedOrderSetShippingRateInputAction(StagedOrderUpdateAction):
    shipping_rate_input: typing.Optional["ShippingRateInputDraft"]

    def __init__(
        self, *, shipping_rate_input: typing.Optional["ShippingRateInputDraft"] = None
    ):
        self.shipping_rate_input = shipping_rate_input
        super().__init__(action="setShippingRateInput")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderSetShippingRateInputAction":
        from ._schemas.order_edit import StagedOrderSetShippingRateInputActionSchema

        return StagedOrderSetShippingRateInputActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderSetShippingRateInputActionSchema

        return StagedOrderSetShippingRateInputActionSchema().dump(self)


class StagedOrderTransitionCustomLineItemStateAction(StagedOrderUpdateAction):
    custom_line_item_id: str
    quantity: int
    from_state: "StateResourceIdentifier"
    to_state: "StateResourceIdentifier"
    actual_transition_date: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        custom_line_item_id: str,
        quantity: int,
        from_state: "StateResourceIdentifier",
        to_state: "StateResourceIdentifier",
        actual_transition_date: typing.Optional[datetime.datetime] = None
    ):
        self.custom_line_item_id = custom_line_item_id
        self.quantity = quantity
        self.from_state = from_state
        self.to_state = to_state
        self.actual_transition_date = actual_transition_date
        super().__init__(action="transitionCustomLineItemState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderTransitionCustomLineItemStateAction":
        from ._schemas.order_edit import (
            StagedOrderTransitionCustomLineItemStateActionSchema,
        )

        return StagedOrderTransitionCustomLineItemStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderTransitionCustomLineItemStateActionSchema,
        )

        return StagedOrderTransitionCustomLineItemStateActionSchema().dump(self)


class StagedOrderTransitionLineItemStateAction(StagedOrderUpdateAction):
    line_item_id: str
    quantity: int
    from_state: "StateResourceIdentifier"
    to_state: "StateResourceIdentifier"
    actual_transition_date: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        line_item_id: str,
        quantity: int,
        from_state: "StateResourceIdentifier",
        to_state: "StateResourceIdentifier",
        actual_transition_date: typing.Optional[datetime.datetime] = None
    ):
        self.line_item_id = line_item_id
        self.quantity = quantity
        self.from_state = from_state
        self.to_state = to_state
        self.actual_transition_date = actual_transition_date
        super().__init__(action="transitionLineItemState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderTransitionLineItemStateAction":
        from ._schemas.order_edit import StagedOrderTransitionLineItemStateActionSchema

        return StagedOrderTransitionLineItemStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderTransitionLineItemStateActionSchema

        return StagedOrderTransitionLineItemStateActionSchema().dump(self)


class StagedOrderTransitionStateAction(StagedOrderUpdateAction):
    state: "StateResourceIdentifier"
    force: typing.Optional[bool]

    def __init__(
        self, *, state: "StateResourceIdentifier", force: typing.Optional[bool] = None
    ):
        self.state = state
        self.force = force
        super().__init__(action="transitionState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderTransitionStateAction":
        from ._schemas.order_edit import StagedOrderTransitionStateActionSchema

        return StagedOrderTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderTransitionStateActionSchema

        return StagedOrderTransitionStateActionSchema().dump(self)


class StagedOrderUpdateItemShippingAddressAction(StagedOrderUpdateAction):
    address: "Address"

    def __init__(self, *, address: "Address"):
        self.address = address
        super().__init__(action="updateItemShippingAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderUpdateItemShippingAddressAction":
        from ._schemas.order_edit import (
            StagedOrderUpdateItemShippingAddressActionSchema,
        )

        return StagedOrderUpdateItemShippingAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import (
            StagedOrderUpdateItemShippingAddressActionSchema,
        )

        return StagedOrderUpdateItemShippingAddressActionSchema().dump(self)


class StagedOrderUpdateSyncInfoAction(StagedOrderUpdateAction):
    channel: "ChannelResourceIdentifier"
    external_id: typing.Optional[str]
    synced_at: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        channel: "ChannelResourceIdentifier",
        external_id: typing.Optional[str] = None,
        synced_at: typing.Optional[datetime.datetime] = None
    ):
        self.channel = channel
        self.external_id = external_id
        self.synced_at = synced_at
        super().__init__(action="updateSyncInfo")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedOrderUpdateSyncInfoAction":
        from ._schemas.order_edit import StagedOrderUpdateSyncInfoActionSchema

        return StagedOrderUpdateSyncInfoActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_edit import StagedOrderUpdateSyncInfoActionSchema

        return StagedOrderUpdateSyncInfoActionSchema().dump(self)

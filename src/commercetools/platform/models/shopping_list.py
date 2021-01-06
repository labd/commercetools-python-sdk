# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, LocalizedString, ReferenceTypeId
    from .customer import CustomerReference, CustomerResourceIdentifier
    from .product import ProductVariant
    from .product_type import ProductTypeReference
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "MyShoppingList",
    "ShoppingList",
    "ShoppingListAddLineItemAction",
    "ShoppingListAddTextLineItemAction",
    "ShoppingListChangeLineItemQuantityAction",
    "ShoppingListChangeLineItemsOrderAction",
    "ShoppingListChangeNameAction",
    "ShoppingListChangeTextLineItemNameAction",
    "ShoppingListChangeTextLineItemQuantityAction",
    "ShoppingListChangeTextLineItemsOrderAction",
    "ShoppingListDraft",
    "ShoppingListLineItem",
    "ShoppingListLineItemDraft",
    "ShoppingListPagedQueryResponse",
    "ShoppingListReference",
    "ShoppingListRemoveLineItemAction",
    "ShoppingListRemoveTextLineItemAction",
    "ShoppingListResourceIdentifier",
    "ShoppingListSetAnonymousIdAction",
    "ShoppingListSetCustomFieldAction",
    "ShoppingListSetCustomTypeAction",
    "ShoppingListSetCustomerAction",
    "ShoppingListSetDeleteDaysAfterLastModificationAction",
    "ShoppingListSetDescriptionAction",
    "ShoppingListSetKeyAction",
    "ShoppingListSetLineItemCustomFieldAction",
    "ShoppingListSetLineItemCustomTypeAction",
    "ShoppingListSetSlugAction",
    "ShoppingListSetTextLineItemCustomFieldAction",
    "ShoppingListSetTextLineItemCustomTypeAction",
    "ShoppingListSetTextLineItemDescriptionAction",
    "ShoppingListUpdate",
    "ShoppingListUpdateAction",
    "TextLineItem",
    "TextLineItemDraft",
]


class MyShoppingList(BaseResource):
    last_modified_by: typing.Optional["LastModifiedBy"]
    created_by: typing.Optional["CreatedBy"]
    custom: typing.Optional["CustomFields"]
    customer: typing.Optional["CustomerReference"]
    delete_days_after_last_modification: typing.Optional[int]
    description: typing.Optional["LocalizedString"]
    key: typing.Optional[str]
    line_items: typing.Optional[typing.List["ShoppingListLineItem"]]
    name: "LocalizedString"
    slug: typing.Optional["LocalizedString"]
    text_line_items: typing.Optional[typing.List["TextLineItem"]]
    anonymous_id: typing.Optional[str]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        custom: typing.Optional["CustomFields"] = None,
        customer: typing.Optional["CustomerReference"] = None,
        delete_days_after_last_modification: typing.Optional[int] = None,
        description: typing.Optional["LocalizedString"] = None,
        key: typing.Optional[str] = None,
        line_items: typing.Optional[typing.List["ShoppingListLineItem"]] = None,
        name: "LocalizedString",
        slug: typing.Optional["LocalizedString"] = None,
        text_line_items: typing.Optional[typing.List["TextLineItem"]] = None,
        anonymous_id: typing.Optional[str] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.custom = custom
        self.customer = customer
        self.delete_days_after_last_modification = delete_days_after_last_modification
        self.description = description
        self.key = key
        self.line_items = line_items
        self.name = name
        self.slug = slug
        self.text_line_items = text_line_items
        self.anonymous_id = anonymous_id
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MyShoppingList":
        from ._schemas.shopping_list import MyShoppingListSchema

        return MyShoppingListSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import MyShoppingListSchema

        return MyShoppingListSchema().dump(self)


class ShoppingList(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    custom: typing.Optional["CustomFields"]
    customer: typing.Optional["CustomerReference"]
    #: The shopping list will be deleted automatically if it hasn't been modified for the specified amount of days.
    delete_days_after_last_modification: typing.Optional[int]
    description: typing.Optional["LocalizedString"]
    #: User-specific unique identifier for the shopping list.
    key: typing.Optional[str]
    line_items: typing.Optional[typing.List["ShoppingListLineItem"]]
    name: "LocalizedString"
    #: Human-readable identifiers usually used as deep-link URL to the related shopping list.
    #: Each slug is unique across a project, but a shopping list can have the same slug for different languages.
    #: The slug must match the pattern [a-zA-Z0-9_-]{2,256}.
    slug: typing.Optional["LocalizedString"]
    text_line_items: typing.Optional[typing.List["TextLineItem"]]
    #: Identifies shopping lists belonging to an anonymous session (the customer has not signed up/in yet).
    anonymous_id: typing.Optional[str]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        custom: typing.Optional["CustomFields"] = None,
        customer: typing.Optional["CustomerReference"] = None,
        delete_days_after_last_modification: typing.Optional[int] = None,
        description: typing.Optional["LocalizedString"] = None,
        key: typing.Optional[str] = None,
        line_items: typing.Optional[typing.List["ShoppingListLineItem"]] = None,
        name: "LocalizedString",
        slug: typing.Optional["LocalizedString"] = None,
        text_line_items: typing.Optional[typing.List["TextLineItem"]] = None,
        anonymous_id: typing.Optional[str] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.custom = custom
        self.customer = customer
        self.delete_days_after_last_modification = delete_days_after_last_modification
        self.description = description
        self.key = key
        self.line_items = line_items
        self.name = name
        self.slug = slug
        self.text_line_items = text_line_items
        self.anonymous_id = anonymous_id
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShoppingList":
        from ._schemas.shopping_list import ShoppingListSchema

        return ShoppingListSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListSchema

        return ShoppingListSchema().dump(self)


class ShoppingListDraft(_BaseType):
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    customer: typing.Optional["CustomerResourceIdentifier"]
    #: The shopping list will be deleted automatically if it hasn't been modified for the specified amount of days.
    delete_days_after_last_modification: typing.Optional[int]
    description: typing.Optional["LocalizedString"]
    #: User-specific unique identifier for the shopping list.
    key: typing.Optional[str]
    line_items: typing.Optional[typing.List["ShoppingListLineItemDraft"]]
    name: "LocalizedString"
    #: Human-readable identifiers usually used as deep-link URL to the related shopping list.
    #: Each slug is unique across a project, but a shopping list can have the same slug for different languages.
    #: The slug must match the pattern [a-zA-Z0-9_-]{2,256}.
    slug: typing.Optional["LocalizedString"]
    text_line_items: typing.Optional[typing.List["TextLineItemDraft"]]
    #: Identifies shopping lists belonging to an anonymous session (the customer has not signed up/in yet).
    anonymous_id: typing.Optional[str]

    def __init__(
        self,
        *,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        customer: typing.Optional["CustomerResourceIdentifier"] = None,
        delete_days_after_last_modification: typing.Optional[int] = None,
        description: typing.Optional["LocalizedString"] = None,
        key: typing.Optional[str] = None,
        line_items: typing.Optional[typing.List["ShoppingListLineItemDraft"]] = None,
        name: "LocalizedString",
        slug: typing.Optional["LocalizedString"] = None,
        text_line_items: typing.Optional[typing.List["TextLineItemDraft"]] = None,
        anonymous_id: typing.Optional[str] = None
    ):
        self.custom = custom
        self.customer = customer
        self.delete_days_after_last_modification = delete_days_after_last_modification
        self.description = description
        self.key = key
        self.line_items = line_items
        self.name = name
        self.slug = slug
        self.text_line_items = text_line_items
        self.anonymous_id = anonymous_id
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShoppingListDraft":
        from ._schemas.shopping_list import ShoppingListDraftSchema

        return ShoppingListDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListDraftSchema

        return ShoppingListDraftSchema().dump(self)


class ShoppingListLineItem(_BaseType):
    added_at: datetime.datetime
    custom: typing.Optional["CustomFields"]
    deactivated_at: typing.Optional[datetime.datetime]
    id: str
    name: "LocalizedString"
    product_id: str
    product_slug: typing.Optional["LocalizedString"]
    product_type: "ProductTypeReference"
    quantity: int
    variant: typing.Optional["ProductVariant"]
    variant_id: typing.Optional[int]

    def __init__(
        self,
        *,
        added_at: datetime.datetime,
        custom: typing.Optional["CustomFields"] = None,
        deactivated_at: typing.Optional[datetime.datetime] = None,
        id: str,
        name: "LocalizedString",
        product_id: str,
        product_slug: typing.Optional["LocalizedString"] = None,
        product_type: "ProductTypeReference",
        quantity: int,
        variant: typing.Optional["ProductVariant"] = None,
        variant_id: typing.Optional[int] = None
    ):
        self.added_at = added_at
        self.custom = custom
        self.deactivated_at = deactivated_at
        self.id = id
        self.name = name
        self.product_id = product_id
        self.product_slug = product_slug
        self.product_type = product_type
        self.quantity = quantity
        self.variant = variant
        self.variant_id = variant_id
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShoppingListLineItem":
        from ._schemas.shopping_list import ShoppingListLineItemSchema

        return ShoppingListLineItemSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListLineItemSchema

        return ShoppingListLineItemSchema().dump(self)


class ShoppingListLineItemDraft(_BaseType):
    added_at: typing.Optional[datetime.datetime]
    custom: typing.Optional["CustomFieldsDraft"]
    sku: typing.Optional[str]
    product_id: typing.Optional[str]
    quantity: typing.Optional[int]
    variant_id: typing.Optional[int]

    def __init__(
        self,
        *,
        added_at: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        sku: typing.Optional[str] = None,
        product_id: typing.Optional[str] = None,
        quantity: typing.Optional[int] = None,
        variant_id: typing.Optional[int] = None
    ):
        self.added_at = added_at
        self.custom = custom
        self.sku = sku
        self.product_id = product_id
        self.quantity = quantity
        self.variant_id = variant_id
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListLineItemDraft":
        from ._schemas.shopping_list import ShoppingListLineItemDraftSchema

        return ShoppingListLineItemDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListLineItemDraftSchema

        return ShoppingListLineItemDraftSchema().dump(self)


class ShoppingListPagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["ShoppingList"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["ShoppingList"]
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
    ) -> "ShoppingListPagedQueryResponse":
        from ._schemas.shopping_list import ShoppingListPagedQueryResponseSchema

        return ShoppingListPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListPagedQueryResponseSchema

        return ShoppingListPagedQueryResponseSchema().dump(self)


class ShoppingListReference(Reference):
    obj: typing.Optional["ShoppingList"]

    def __init__(self, *, id: str, obj: typing.Optional["ShoppingList"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.SHOPPING_LIST)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShoppingListReference":
        from ._schemas.shopping_list import ShoppingListReferenceSchema

        return ShoppingListReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListReferenceSchema

        return ShoppingListReferenceSchema().dump(self)


class ShoppingListResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.SHOPPING_LIST)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListResourceIdentifier":
        from ._schemas.shopping_list import ShoppingListResourceIdentifierSchema

        return ShoppingListResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListResourceIdentifierSchema

        return ShoppingListResourceIdentifierSchema().dump(self)


class ShoppingListUpdate(_BaseType):
    version: int
    actions: typing.List["ShoppingListUpdateAction"]

    def __init__(
        self, *, version: int, actions: typing.List["ShoppingListUpdateAction"]
    ):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShoppingListUpdate":
        from ._schemas.shopping_list import ShoppingListUpdateSchema

        return ShoppingListUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListUpdateSchema

        return ShoppingListUpdateSchema().dump(self)


class ShoppingListUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListUpdateAction":
        if data["action"] == "addLineItem":
            from ._schemas.shopping_list import ShoppingListAddLineItemActionSchema

            return ShoppingListAddLineItemActionSchema().load(data)
        if data["action"] == "addTextLineItem":
            from ._schemas.shopping_list import ShoppingListAddTextLineItemActionSchema

            return ShoppingListAddTextLineItemActionSchema().load(data)
        if data["action"] == "changeLineItemQuantity":
            from ._schemas.shopping_list import (
                ShoppingListChangeLineItemQuantityActionSchema,
            )

            return ShoppingListChangeLineItemQuantityActionSchema().load(data)
        if data["action"] == "changeLineItemsOrder":
            from ._schemas.shopping_list import (
                ShoppingListChangeLineItemsOrderActionSchema,
            )

            return ShoppingListChangeLineItemsOrderActionSchema().load(data)
        if data["action"] == "changeName":
            from ._schemas.shopping_list import ShoppingListChangeNameActionSchema

            return ShoppingListChangeNameActionSchema().load(data)
        if data["action"] == "changeTextLineItemName":
            from ._schemas.shopping_list import (
                ShoppingListChangeTextLineItemNameActionSchema,
            )

            return ShoppingListChangeTextLineItemNameActionSchema().load(data)
        if data["action"] == "changeTextLineItemQuantity":
            from ._schemas.shopping_list import (
                ShoppingListChangeTextLineItemQuantityActionSchema,
            )

            return ShoppingListChangeTextLineItemQuantityActionSchema().load(data)
        if data["action"] == "changeTextLineItemsOrder":
            from ._schemas.shopping_list import (
                ShoppingListChangeTextLineItemsOrderActionSchema,
            )

            return ShoppingListChangeTextLineItemsOrderActionSchema().load(data)
        if data["action"] == "removeLineItem":
            from ._schemas.shopping_list import ShoppingListRemoveLineItemActionSchema

            return ShoppingListRemoveLineItemActionSchema().load(data)
        if data["action"] == "removeTextLineItem":
            from ._schemas.shopping_list import (
                ShoppingListRemoveTextLineItemActionSchema,
            )

            return ShoppingListRemoveTextLineItemActionSchema().load(data)
        if data["action"] == "setAnonymousId":
            from ._schemas.shopping_list import ShoppingListSetAnonymousIdActionSchema

            return ShoppingListSetAnonymousIdActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.shopping_list import ShoppingListSetCustomFieldActionSchema

            return ShoppingListSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.shopping_list import ShoppingListSetCustomTypeActionSchema

            return ShoppingListSetCustomTypeActionSchema().load(data)
        if data["action"] == "setCustomer":
            from ._schemas.shopping_list import ShoppingListSetCustomerActionSchema

            return ShoppingListSetCustomerActionSchema().load(data)
        if data["action"] == "setDeleteDaysAfterLastModification":
            from ._schemas.shopping_list import (
                ShoppingListSetDeleteDaysAfterLastModificationActionSchema,
            )

            return ShoppingListSetDeleteDaysAfterLastModificationActionSchema().load(
                data
            )
        if data["action"] == "setDescription":
            from ._schemas.shopping_list import ShoppingListSetDescriptionActionSchema

            return ShoppingListSetDescriptionActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.shopping_list import ShoppingListSetKeyActionSchema

            return ShoppingListSetKeyActionSchema().load(data)
        if data["action"] == "setLineItemCustomField":
            from ._schemas.shopping_list import (
                ShoppingListSetLineItemCustomFieldActionSchema,
            )

            return ShoppingListSetLineItemCustomFieldActionSchema().load(data)
        if data["action"] == "setLineItemCustomType":
            from ._schemas.shopping_list import (
                ShoppingListSetLineItemCustomTypeActionSchema,
            )

            return ShoppingListSetLineItemCustomTypeActionSchema().load(data)
        if data["action"] == "setSlug":
            from ._schemas.shopping_list import ShoppingListSetSlugActionSchema

            return ShoppingListSetSlugActionSchema().load(data)
        if data["action"] == "setTextLineItemCustomField":
            from ._schemas.shopping_list import (
                ShoppingListSetTextLineItemCustomFieldActionSchema,
            )

            return ShoppingListSetTextLineItemCustomFieldActionSchema().load(data)
        if data["action"] == "setTextLineItemCustomType":
            from ._schemas.shopping_list import (
                ShoppingListSetTextLineItemCustomTypeActionSchema,
            )

            return ShoppingListSetTextLineItemCustomTypeActionSchema().load(data)
        if data["action"] == "setTextLineItemDescription":
            from ._schemas.shopping_list import (
                ShoppingListSetTextLineItemDescriptionActionSchema,
            )

            return ShoppingListSetTextLineItemDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListUpdateActionSchema

        return ShoppingListUpdateActionSchema().dump(self)


class TextLineItem(_BaseType):
    #: When the text line item was added to the shopping list.
    added_at: datetime.datetime
    custom: typing.Optional["CustomFields"]
    description: typing.Optional["LocalizedString"]
    #: The unique ID of this TextLineItem.
    id: str
    name: "LocalizedString"
    quantity: int

    def __init__(
        self,
        *,
        added_at: datetime.datetime,
        custom: typing.Optional["CustomFields"] = None,
        description: typing.Optional["LocalizedString"] = None,
        id: str,
        name: "LocalizedString",
        quantity: int
    ):
        self.added_at = added_at
        self.custom = custom
        self.description = description
        self.id = id
        self.name = name
        self.quantity = quantity
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TextLineItem":
        from ._schemas.shopping_list import TextLineItemSchema

        return TextLineItemSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import TextLineItemSchema

        return TextLineItemSchema().dump(self)


class TextLineItemDraft(_BaseType):
    #: Defaults to the current date and time.
    added_at: typing.Optional[datetime.datetime]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    description: typing.Optional["LocalizedString"]
    name: "LocalizedString"
    #: Defaults to `1`.
    quantity: typing.Optional[int]

    def __init__(
        self,
        *,
        added_at: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        description: typing.Optional["LocalizedString"] = None,
        name: "LocalizedString",
        quantity: typing.Optional[int] = None
    ):
        self.added_at = added_at
        self.custom = custom
        self.description = description
        self.name = name
        self.quantity = quantity
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TextLineItemDraft":
        from ._schemas.shopping_list import TextLineItemDraftSchema

        return TextLineItemDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import TextLineItemDraftSchema

        return TextLineItemDraftSchema().dump(self)


class ShoppingListAddLineItemAction(ShoppingListUpdateAction):
    sku: typing.Optional[str]
    product_id: typing.Optional[str]
    variant_id: typing.Optional[int]
    quantity: typing.Optional[int]
    added_at: typing.Optional[datetime.datetime]
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        sku: typing.Optional[str] = None,
        product_id: typing.Optional[str] = None,
        variant_id: typing.Optional[int] = None,
        quantity: typing.Optional[int] = None,
        added_at: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.sku = sku
        self.product_id = product_id
        self.variant_id = variant_id
        self.quantity = quantity
        self.added_at = added_at
        self.custom = custom
        super().__init__(action="addLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListAddLineItemAction":
        from ._schemas.shopping_list import ShoppingListAddLineItemActionSchema

        return ShoppingListAddLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListAddLineItemActionSchema

        return ShoppingListAddLineItemActionSchema().dump(self)


class ShoppingListAddTextLineItemAction(ShoppingListUpdateAction):
    name: "LocalizedString"
    description: typing.Optional["LocalizedString"]
    quantity: typing.Optional[int]
    added_at: typing.Optional[datetime.datetime]
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        quantity: typing.Optional[int] = None,
        added_at: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.added_at = added_at
        self.custom = custom
        super().__init__(action="addTextLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListAddTextLineItemAction":
        from ._schemas.shopping_list import ShoppingListAddTextLineItemActionSchema

        return ShoppingListAddTextLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListAddTextLineItemActionSchema

        return ShoppingListAddTextLineItemActionSchema().dump(self)


class ShoppingListChangeLineItemQuantityAction(ShoppingListUpdateAction):
    line_item_id: str
    quantity: int

    def __init__(self, *, line_item_id: str, quantity: int):
        self.line_item_id = line_item_id
        self.quantity = quantity
        super().__init__(action="changeLineItemQuantity")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListChangeLineItemQuantityAction":
        from ._schemas.shopping_list import (
            ShoppingListChangeLineItemQuantityActionSchema,
        )

        return ShoppingListChangeLineItemQuantityActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import (
            ShoppingListChangeLineItemQuantityActionSchema,
        )

        return ShoppingListChangeLineItemQuantityActionSchema().dump(self)


class ShoppingListChangeLineItemsOrderAction(ShoppingListUpdateAction):
    line_item_order: typing.List["str"]

    def __init__(self, *, line_item_order: typing.List["str"]):
        self.line_item_order = line_item_order
        super().__init__(action="changeLineItemsOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListChangeLineItemsOrderAction":
        from ._schemas.shopping_list import ShoppingListChangeLineItemsOrderActionSchema

        return ShoppingListChangeLineItemsOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListChangeLineItemsOrderActionSchema

        return ShoppingListChangeLineItemsOrderActionSchema().dump(self)


class ShoppingListChangeNameAction(ShoppingListUpdateAction):
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString"):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListChangeNameAction":
        from ._schemas.shopping_list import ShoppingListChangeNameActionSchema

        return ShoppingListChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListChangeNameActionSchema

        return ShoppingListChangeNameActionSchema().dump(self)


class ShoppingListChangeTextLineItemNameAction(ShoppingListUpdateAction):
    text_line_item_id: str
    name: "LocalizedString"

    def __init__(self, *, text_line_item_id: str, name: "LocalizedString"):
        self.text_line_item_id = text_line_item_id
        self.name = name
        super().__init__(action="changeTextLineItemName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListChangeTextLineItemNameAction":
        from ._schemas.shopping_list import (
            ShoppingListChangeTextLineItemNameActionSchema,
        )

        return ShoppingListChangeTextLineItemNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import (
            ShoppingListChangeTextLineItemNameActionSchema,
        )

        return ShoppingListChangeTextLineItemNameActionSchema().dump(self)


class ShoppingListChangeTextLineItemQuantityAction(ShoppingListUpdateAction):
    text_line_item_id: str
    quantity: int

    def __init__(self, *, text_line_item_id: str, quantity: int):
        self.text_line_item_id = text_line_item_id
        self.quantity = quantity
        super().__init__(action="changeTextLineItemQuantity")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListChangeTextLineItemQuantityAction":
        from ._schemas.shopping_list import (
            ShoppingListChangeTextLineItemQuantityActionSchema,
        )

        return ShoppingListChangeTextLineItemQuantityActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import (
            ShoppingListChangeTextLineItemQuantityActionSchema,
        )

        return ShoppingListChangeTextLineItemQuantityActionSchema().dump(self)


class ShoppingListChangeTextLineItemsOrderAction(ShoppingListUpdateAction):
    text_line_item_order: typing.List["str"]

    def __init__(self, *, text_line_item_order: typing.List["str"]):
        self.text_line_item_order = text_line_item_order
        super().__init__(action="changeTextLineItemsOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListChangeTextLineItemsOrderAction":
        from ._schemas.shopping_list import (
            ShoppingListChangeTextLineItemsOrderActionSchema,
        )

        return ShoppingListChangeTextLineItemsOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import (
            ShoppingListChangeTextLineItemsOrderActionSchema,
        )

        return ShoppingListChangeTextLineItemsOrderActionSchema().dump(self)


class ShoppingListRemoveLineItemAction(ShoppingListUpdateAction):
    line_item_id: str
    quantity: typing.Optional[int]

    def __init__(self, *, line_item_id: str, quantity: typing.Optional[int] = None):
        self.line_item_id = line_item_id
        self.quantity = quantity
        super().__init__(action="removeLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListRemoveLineItemAction":
        from ._schemas.shopping_list import ShoppingListRemoveLineItemActionSchema

        return ShoppingListRemoveLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListRemoveLineItemActionSchema

        return ShoppingListRemoveLineItemActionSchema().dump(self)


class ShoppingListRemoveTextLineItemAction(ShoppingListUpdateAction):
    text_line_item_id: str
    quantity: typing.Optional[int]

    def __init__(
        self, *, text_line_item_id: str, quantity: typing.Optional[int] = None
    ):
        self.text_line_item_id = text_line_item_id
        self.quantity = quantity
        super().__init__(action="removeTextLineItem")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListRemoveTextLineItemAction":
        from ._schemas.shopping_list import ShoppingListRemoveTextLineItemActionSchema

        return ShoppingListRemoveTextLineItemActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListRemoveTextLineItemActionSchema

        return ShoppingListRemoveTextLineItemActionSchema().dump(self)


class ShoppingListSetAnonymousIdAction(ShoppingListUpdateAction):
    #: Anonymous ID of the anonymous customer that this shopping list belongs to.
    #: If this field is not set any existing `anonymousId` is removed.
    anonymous_id: typing.Optional[str]

    def __init__(self, *, anonymous_id: typing.Optional[str] = None):
        self.anonymous_id = anonymous_id
        super().__init__(action="setAnonymousId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListSetAnonymousIdAction":
        from ._schemas.shopping_list import ShoppingListSetAnonymousIdActionSchema

        return ShoppingListSetAnonymousIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListSetAnonymousIdActionSchema

        return ShoppingListSetAnonymousIdActionSchema().dump(self)


class ShoppingListSetCustomFieldAction(ShoppingListUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListSetCustomFieldAction":
        from ._schemas.shopping_list import ShoppingListSetCustomFieldActionSchema

        return ShoppingListSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListSetCustomFieldActionSchema

        return ShoppingListSetCustomFieldActionSchema().dump(self)


class ShoppingListSetCustomTypeAction(ShoppingListUpdateAction):
    #: If set, the custom type is set to this new value.
    #: If absent, the custom type and any existing custom fields are removed.
    type: typing.Optional["TypeResourceIdentifier"]
    #: If set, the custom fields are set to this new value.
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
    ) -> "ShoppingListSetCustomTypeAction":
        from ._schemas.shopping_list import ShoppingListSetCustomTypeActionSchema

        return ShoppingListSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListSetCustomTypeActionSchema

        return ShoppingListSetCustomTypeActionSchema().dump(self)


class ShoppingListSetCustomerAction(ShoppingListUpdateAction):
    customer: typing.Optional["CustomerResourceIdentifier"]

    def __init__(
        self, *, customer: typing.Optional["CustomerResourceIdentifier"] = None
    ):
        self.customer = customer
        super().__init__(action="setCustomer")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListSetCustomerAction":
        from ._schemas.shopping_list import ShoppingListSetCustomerActionSchema

        return ShoppingListSetCustomerActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListSetCustomerActionSchema

        return ShoppingListSetCustomerActionSchema().dump(self)


class ShoppingListSetDeleteDaysAfterLastModificationAction(ShoppingListUpdateAction):
    delete_days_after_last_modification: typing.Optional[int]

    def __init__(
        self, *, delete_days_after_last_modification: typing.Optional[int] = None
    ):
        self.delete_days_after_last_modification = delete_days_after_last_modification
        super().__init__(action="setDeleteDaysAfterLastModification")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListSetDeleteDaysAfterLastModificationAction":
        from ._schemas.shopping_list import (
            ShoppingListSetDeleteDaysAfterLastModificationActionSchema,
        )

        return ShoppingListSetDeleteDaysAfterLastModificationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import (
            ShoppingListSetDeleteDaysAfterLastModificationActionSchema,
        )

        return ShoppingListSetDeleteDaysAfterLastModificationActionSchema().dump(self)


class ShoppingListSetDescriptionAction(ShoppingListUpdateAction):
    description: typing.Optional["LocalizedString"]

    def __init__(self, *, description: typing.Optional["LocalizedString"] = None):
        self.description = description
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListSetDescriptionAction":
        from ._schemas.shopping_list import ShoppingListSetDescriptionActionSchema

        return ShoppingListSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListSetDescriptionActionSchema

        return ShoppingListSetDescriptionActionSchema().dump(self)


class ShoppingListSetKeyAction(ShoppingListUpdateAction):
    #: User-specific unique identifier for the shopping list.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListSetKeyAction":
        from ._schemas.shopping_list import ShoppingListSetKeyActionSchema

        return ShoppingListSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListSetKeyActionSchema

        return ShoppingListSetKeyActionSchema().dump(self)


class ShoppingListSetLineItemCustomFieldAction(ShoppingListUpdateAction):
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
    ) -> "ShoppingListSetLineItemCustomFieldAction":
        from ._schemas.shopping_list import (
            ShoppingListSetLineItemCustomFieldActionSchema,
        )

        return ShoppingListSetLineItemCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import (
            ShoppingListSetLineItemCustomFieldActionSchema,
        )

        return ShoppingListSetLineItemCustomFieldActionSchema().dump(self)


class ShoppingListSetLineItemCustomTypeAction(ShoppingListUpdateAction):
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
    ) -> "ShoppingListSetLineItemCustomTypeAction":
        from ._schemas.shopping_list import (
            ShoppingListSetLineItemCustomTypeActionSchema,
        )

        return ShoppingListSetLineItemCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import (
            ShoppingListSetLineItemCustomTypeActionSchema,
        )

        return ShoppingListSetLineItemCustomTypeActionSchema().dump(self)


class ShoppingListSetSlugAction(ShoppingListUpdateAction):
    slug: typing.Optional["LocalizedString"]

    def __init__(self, *, slug: typing.Optional["LocalizedString"] = None):
        self.slug = slug
        super().__init__(action="setSlug")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListSetSlugAction":
        from ._schemas.shopping_list import ShoppingListSetSlugActionSchema

        return ShoppingListSetSlugActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import ShoppingListSetSlugActionSchema

        return ShoppingListSetSlugActionSchema().dump(self)


class ShoppingListSetTextLineItemCustomFieldAction(ShoppingListUpdateAction):
    text_line_item_id: str
    name: str
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        text_line_item_id: str,
        name: str,
        value: typing.Optional[typing.Any] = None
    ):
        self.text_line_item_id = text_line_item_id
        self.name = name
        self.value = value
        super().__init__(action="setTextLineItemCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListSetTextLineItemCustomFieldAction":
        from ._schemas.shopping_list import (
            ShoppingListSetTextLineItemCustomFieldActionSchema,
        )

        return ShoppingListSetTextLineItemCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import (
            ShoppingListSetTextLineItemCustomFieldActionSchema,
        )

        return ShoppingListSetTextLineItemCustomFieldActionSchema().dump(self)


class ShoppingListSetTextLineItemCustomTypeAction(ShoppingListUpdateAction):
    text_line_item_id: str
    type: typing.Optional["TypeResourceIdentifier"]
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        text_line_item_id: str,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.text_line_item_id = text_line_item_id
        self.type = type
        self.fields = fields
        super().__init__(action="setTextLineItemCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListSetTextLineItemCustomTypeAction":
        from ._schemas.shopping_list import (
            ShoppingListSetTextLineItemCustomTypeActionSchema,
        )

        return ShoppingListSetTextLineItemCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import (
            ShoppingListSetTextLineItemCustomTypeActionSchema,
        )

        return ShoppingListSetTextLineItemCustomTypeActionSchema().dump(self)


class ShoppingListSetTextLineItemDescriptionAction(ShoppingListUpdateAction):
    text_line_item_id: str
    description: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        text_line_item_id: str,
        description: typing.Optional["LocalizedString"] = None
    ):
        self.text_line_item_id = text_line_item_id
        self.description = description
        super().__init__(action="setTextLineItemDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListSetTextLineItemDescriptionAction":
        from ._schemas.shopping_list import (
            ShoppingListSetTextLineItemDescriptionActionSchema,
        )

        return ShoppingListSetTextLineItemDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.shopping_list import (
            ShoppingListSetTextLineItemDescriptionActionSchema,
        )

        return ShoppingListSetTextLineItemDescriptionActionSchema().dump(self)

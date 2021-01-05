# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType


class LocalizedString(typing.Dict[str, str]):
    pass


class Money(_BaseType):
    cent_amount: "int"
    #: The currency code compliant to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).
    currency_code: "str"

    def __init__(self, *, cent_amount: "int", currency_code: "str"):
        self.cent_amount = cent_amount
        self.currency_code = currency_code
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Money":
        from ._schemas.common import MoneySchema

        return MoneySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import MoneySchema

        return MoneySchema().dump(self)


class ReferenceTypeId(enum.Enum):
    CART = "cart"
    CART_DISCOUNT = "cart-discount"
    CATEGORY = "category"
    CHANNEL = "channel"
    CUSTOMER = "customer"
    CUSTOMER_GROUP = "customer-group"
    DISCOUNT_CODE = "discount-code"
    KEY_VALUE_DOCUMENT = "key-value-document"
    PAYMENT = "payment"
    PRODUCT = "product"
    PRODUCT_TYPE = "product-type"
    PRODUCT_DISCOUNT = "product-discount"
    ORDER = "order"
    REVIEW = "review"
    SHOPPING_LIST = "shopping-list"
    SHIPPING_METHOD = "shipping-method"
    STATE = "state"
    STORE = "store"
    TAX_CATEGORY = "tax-category"
    TYPE = "type"
    ZONE = "zone"
    INVENTORY_ENTRY = "inventory-entry"
    ORDER_EDIT = "order-edit"


class Reference(_BaseType):
    type_id: "ReferenceTypeId"
    id: "str"

    def __init__(self, *, type_id: "ReferenceTypeId", id: "str"):
        self.type_id = type_id
        self.id = id
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Reference":
        from ._schemas.common import ReferenceSchema

        return ReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ReferenceSchema

        return ReferenceSchema().dump(self)


class CategoryReference(Reference):
    def __init__(self, *, id: "str"):

        super().__init__(id=id, type_id=ReferenceTypeId.CATEGORY)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CategoryReference":
        from ._schemas.common import CategoryReferenceSchema

        return CategoryReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CategoryReferenceSchema

        return CategoryReferenceSchema().dump(self)


class ProductReference(Reference):
    def __init__(self, *, id: "str"):

        super().__init__(id=id, type_id=ReferenceTypeId.PRODUCT)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductReference":
        from ._schemas.common import ProductReferenceSchema

        return ProductReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ProductReferenceSchema

        return ProductReferenceSchema().dump(self)


class ProductTypeReference(Reference):
    def __init__(self, *, id: "str"):

        super().__init__(id=id, type_id=ReferenceTypeId.PRODUCT_TYPE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductTypeReference":
        from ._schemas.common import ProductTypeReferenceSchema

        return ProductTypeReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ProductTypeReferenceSchema

        return ProductTypeReferenceSchema().dump(self)


class ProductVariant(_BaseType):
    """The product variant that contains the image."""

    #: The product that contains this variant.
    product: "ProductReference"
    #: The state of the product variant.
    staged: "bool"
    #: The id of the product variant.
    variant_id: "int"

    def __init__(
        self, *, product: "ProductReference", staged: "bool", variant_id: "int"
    ):
        self.product = product
        self.staged = staged
        self.variant_id = variant_id
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductVariant":
        from ._schemas.common import ProductVariantSchema

        return ProductVariantSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ProductVariantSchema

        return ProductVariantSchema().dump(self)


class TaskStatusEnum(enum.Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"


class TaskToken(_BaseType):
    """Represents a URL path to poll to get the results of an Asynchronous Request."""

    #: The ID for the task. Used to find the status of the task.
    task_id: "str"
    #: The URI path to poll for the status of the task.
    uri_path: "str"

    def __init__(self, *, task_id: "str", uri_path: "str"):
        self.task_id = task_id
        self.uri_path = uri_path
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaskToken":
        from ._schemas.common import TaskTokenSchema

        return TaskTokenSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import TaskTokenSchema

        return TaskTokenSchema().dump(self)

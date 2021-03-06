# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType

if typing.TYPE_CHECKING:
    from .customfields import Custom

__all__ = [
    "Address",
    "Asset",
    "AssetDimensions",
    "AssetSource",
    "CartDiscountKeyReference",
    "CategoryKeyReference",
    "ChannelKeyReference",
    "CustomerGroupKeyReference",
    "CustomerKeyReference",
    "DiscountedPrice",
    "EnumValue",
    "HighPrecisionMoney",
    "Image",
    "ImportResource",
    "ImportResourceType",
    "KeyReference",
    "LocalizedEnumValue",
    "LocalizedString",
    "Money",
    "MoneyType",
    "PriceKeyReference",
    "PriceTier",
    "ProcessingState",
    "ProductDiscountKeyReference",
    "ProductKeyReference",
    "ProductTypeKeyReference",
    "ProductVariantKeyReference",
    "ReferenceType",
    "ShippingMethodKeyReference",
    "StateKeyReference",
    "StoreKeyReference",
    "TaxCategoryKeyReference",
    "TypeKeyReference",
    "TypedMoney",
]


class Asset(_BaseType):
    #: User-defined identifier for the asset.
    #: Asset keys are unique inside their container (a product variant or a category).
    key: str
    sources: typing.List["AssetSource"]
    name: "LocalizedString"
    description: typing.Optional["LocalizedString"]
    tags: typing.Optional[typing.List["str"]]
    #: The representation to be sent to the server when creating a resource with custom fields.
    custom: typing.Optional["Custom"]

    def __init__(
        self,
        *,
        key: str,
        sources: typing.List["AssetSource"],
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        tags: typing.Optional[typing.List["str"]] = None,
        custom: typing.Optional["Custom"] = None
    ):
        self.key = key
        self.sources = sources
        self.name = name
        self.description = description
        self.tags = tags
        self.custom = custom
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Asset":
        from ._schemas.common import AssetSchema

        return AssetSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import AssetSchema

        return AssetSchema().dump(self)


class AssetDimensions(_BaseType):
    w: float
    h: float

    def __init__(self, *, w: float, h: float):
        self.w = w
        self.h = h
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AssetDimensions":
        from ._schemas.common import AssetDimensionsSchema

        return AssetDimensionsSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import AssetDimensionsSchema

        return AssetDimensionsSchema().dump(self)


class AssetSource(_BaseType):
    uri: str
    key: typing.Optional[str]
    dimensions: typing.Optional["AssetDimensions"]
    content_type: typing.Optional[str]

    def __init__(
        self,
        *,
        uri: str,
        key: typing.Optional[str] = None,
        dimensions: typing.Optional["AssetDimensions"] = None,
        content_type: typing.Optional[str] = None
    ):
        self.uri = uri
        self.key = key
        self.dimensions = dimensions
        self.content_type = content_type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AssetSource":
        from ._schemas.common import AssetSourceSchema

        return AssetSourceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import AssetSourceSchema

        return AssetSourceSchema().dump(self)


class Image(_BaseType):
    url: str
    dimensions: "AssetDimensions"
    label: typing.Optional[str]

    def __init__(
        self,
        *,
        url: str,
        dimensions: "AssetDimensions",
        label: typing.Optional[str] = None
    ):
        self.url = url
        self.dimensions = dimensions
        self.label = label
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Image":
        from ._schemas.common import ImageSchema

        return ImageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ImageSchema

        return ImageSchema().dump(self)


class EnumValue(_BaseType):
    key: str
    label: str

    def __init__(self, *, key: str, label: str):
        self.key = key
        self.label = label
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "EnumValue":
        from ._schemas.common import EnumValueSchema

        return EnumValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import EnumValueSchema

        return EnumValueSchema().dump(self)


class LocalizedEnumValue(_BaseType):
    key: str
    label: "LocalizedString"

    def __init__(self, *, key: str, label: "LocalizedString"):
        self.key = key
        self.label = label
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "LocalizedEnumValue":
        from ._schemas.common import LocalizedEnumValueSchema

        return LocalizedEnumValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import LocalizedEnumValueSchema

        return LocalizedEnumValueSchema().dump(self)


class LocalizedString(typing.Dict[str, str]):
    pass


class ImportResource(_BaseType):
    """A representation of the resource to import.
    Import resources are similar to commercetools draft types, but they only support key references.
    In general, import resources are more granular then the normal commercetools resource.
    They are optimized for incremental updates and therefore have a slightly different structure.

    """

    key: str

    def __init__(self, *, key: str):
        self.key = key
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImportResource":
        from ._schemas.common import ImportResourceSchema

        return ImportResourceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ImportResourceSchema

        return ImportResourceSchema().dump(self)


class KeyReference(_BaseType):
    """References a resource by its key."""

    key: str
    #: The type of the referenced resource.
    type_id: "ReferenceType"

    def __init__(self, *, key: str, type_id: "ReferenceType"):
        self.key = key
        self.type_id = type_id
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "KeyReference":
        if data["typeId"] == "cart-discount":
            from ._schemas.common import CartDiscountKeyReferenceSchema

            return CartDiscountKeyReferenceSchema().load(data)
        if data["typeId"] == "category":
            from ._schemas.common import CategoryKeyReferenceSchema

            return CategoryKeyReferenceSchema().load(data)
        if data["typeId"] == "channel":
            from ._schemas.common import ChannelKeyReferenceSchema

            return ChannelKeyReferenceSchema().load(data)
        if data["typeId"] == "customer":
            from ._schemas.common import CustomerKeyReferenceSchema

            return CustomerKeyReferenceSchema().load(data)
        if data["typeId"] == "customer-group":
            from ._schemas.common import CustomerGroupKeyReferenceSchema

            return CustomerGroupKeyReferenceSchema().load(data)
        if data["typeId"] == "price":
            from ._schemas.common import PriceKeyReferenceSchema

            return PriceKeyReferenceSchema().load(data)
        if data["typeId"] == "product":
            from ._schemas.common import ProductKeyReferenceSchema

            return ProductKeyReferenceSchema().load(data)
        if data["typeId"] == "product-discount":
            from ._schemas.common import ProductDiscountKeyReferenceSchema

            return ProductDiscountKeyReferenceSchema().load(data)
        if data["typeId"] == "product-type":
            from ._schemas.common import ProductTypeKeyReferenceSchema

            return ProductTypeKeyReferenceSchema().load(data)
        if data["typeId"] == "product-variant":
            from ._schemas.common import ProductVariantKeyReferenceSchema

            return ProductVariantKeyReferenceSchema().load(data)
        if data["typeId"] == "shipping-method":
            from ._schemas.common import ShippingMethodKeyReferenceSchema

            return ShippingMethodKeyReferenceSchema().load(data)
        if data["typeId"] == "state":
            from ._schemas.common import StateKeyReferenceSchema

            return StateKeyReferenceSchema().load(data)
        if data["typeId"] == "store":
            from ._schemas.common import StoreKeyReferenceSchema

            return StoreKeyReferenceSchema().load(data)
        if data["typeId"] == "tax-category":
            from ._schemas.common import TaxCategoryKeyReferenceSchema

            return TaxCategoryKeyReferenceSchema().load(data)
        if data["typeId"] == "type":
            from ._schemas.common import TypeKeyReferenceSchema

            return TypeKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import KeyReferenceSchema

        return KeyReferenceSchema().dump(self)


class CartDiscountKeyReference(KeyReference):
    """References a cart discount by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.CART_DISCOUNT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountKeyReference":
        from ._schemas.common import CartDiscountKeyReferenceSchema

        return CartDiscountKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CartDiscountKeyReferenceSchema

        return CartDiscountKeyReferenceSchema().dump(self)


class CategoryKeyReference(KeyReference):
    """References a category by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.CATEGORY)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CategoryKeyReference":
        from ._schemas.common import CategoryKeyReferenceSchema

        return CategoryKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CategoryKeyReferenceSchema

        return CategoryKeyReferenceSchema().dump(self)


class ChannelKeyReference(KeyReference):
    """References a channel by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.CHANNEL)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ChannelKeyReference":
        from ._schemas.common import ChannelKeyReferenceSchema

        return ChannelKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ChannelKeyReferenceSchema

        return ChannelKeyReferenceSchema().dump(self)


class CustomerKeyReference(KeyReference):
    """References a customer by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.CUSTOMER)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerKeyReference":
        from ._schemas.common import CustomerKeyReferenceSchema

        return CustomerKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CustomerKeyReferenceSchema

        return CustomerKeyReferenceSchema().dump(self)


class CustomerGroupKeyReference(KeyReference):
    """References a customer group by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.CUSTOMER_GROUP)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerGroupKeyReference":
        from ._schemas.common import CustomerGroupKeyReferenceSchema

        return CustomerGroupKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CustomerGroupKeyReferenceSchema

        return CustomerGroupKeyReferenceSchema().dump(self)


class PriceKeyReference(KeyReference):
    """References a price by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.PRICE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceKeyReference":
        from ._schemas.common import PriceKeyReferenceSchema

        return PriceKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import PriceKeyReferenceSchema

        return PriceKeyReferenceSchema().dump(self)


class ProductKeyReference(KeyReference):
    """References a product by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.PRODUCT)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductKeyReference":
        from ._schemas.common import ProductKeyReferenceSchema

        return ProductKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ProductKeyReferenceSchema

        return ProductKeyReferenceSchema().dump(self)


class ProductDiscountKeyReference(KeyReference):
    """References a product discount by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.PRODUCT_DISCOUNT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountKeyReference":
        from ._schemas.common import ProductDiscountKeyReferenceSchema

        return ProductDiscountKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ProductDiscountKeyReferenceSchema

        return ProductDiscountKeyReferenceSchema().dump(self)


class ProductTypeKeyReference(KeyReference):
    """References a product type by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.PRODUCT_TYPE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeKeyReference":
        from ._schemas.common import ProductTypeKeyReferenceSchema

        return ProductTypeKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ProductTypeKeyReferenceSchema

        return ProductTypeKeyReferenceSchema().dump(self)


class ProductVariantKeyReference(KeyReference):
    """References a product variant by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.PRODUCT_VARIANT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantKeyReference":
        from ._schemas.common import ProductVariantKeyReferenceSchema

        return ProductVariantKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ProductVariantKeyReferenceSchema

        return ProductVariantKeyReferenceSchema().dump(self)


class ShippingMethodKeyReference(KeyReference):
    """References a shipping method by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.SHIPPING_METHOD)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodKeyReference":
        from ._schemas.common import ShippingMethodKeyReferenceSchema

        return ShippingMethodKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ShippingMethodKeyReferenceSchema

        return ShippingMethodKeyReferenceSchema().dump(self)


class StateKeyReference(KeyReference):
    """References a state by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.STATE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateKeyReference":
        from ._schemas.common import StateKeyReferenceSchema

        return StateKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import StateKeyReferenceSchema

        return StateKeyReferenceSchema().dump(self)


class StoreKeyReference(KeyReference):
    """References a store by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.STORE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreKeyReference":
        from ._schemas.common import StoreKeyReferenceSchema

        return StoreKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import StoreKeyReferenceSchema

        return StoreKeyReferenceSchema().dump(self)


class TaxCategoryKeyReference(KeyReference):
    """References a tax category by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.TAX_CATEGORY)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TaxCategoryKeyReference":
        from ._schemas.common import TaxCategoryKeyReferenceSchema

        return TaxCategoryKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import TaxCategoryKeyReferenceSchema

        return TaxCategoryKeyReferenceSchema().dump(self)


class TypeKeyReference(KeyReference):
    """References a type by its key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.TYPE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypeKeyReference":
        from ._schemas.common import TypeKeyReferenceSchema

        return TypeKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import TypeKeyReferenceSchema

        return TypeKeyReferenceSchema().dump(self)


class MoneyType(enum.Enum):
    CENT_PRECISION = "centPrecision"
    HIGH_PRECISION = "highPrecision"


class TypedMoney(_BaseType):
    type: "MoneyType"
    fraction_digits: typing.Optional[int]
    cent_amount: int
    #: The currency code compliant to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).
    currency_code: str

    def __init__(
        self,
        *,
        type: "MoneyType",
        fraction_digits: typing.Optional[int] = None,
        cent_amount: int,
        currency_code: str
    ):
        self.type = type
        self.fraction_digits = fraction_digits
        self.cent_amount = cent_amount
        self.currency_code = currency_code
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypedMoney":
        if data["type"] == "highPrecision":
            from ._schemas.common import HighPrecisionMoneySchema

            return HighPrecisionMoneySchema().load(data)
        if data["type"] == "centPrecision":
            from ._schemas.common import MoneySchema

            return MoneySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import TypedMoneySchema

        return TypedMoneySchema().dump(self)


class HighPrecisionMoney(TypedMoney):
    precise_amount: int

    def __init__(
        self,
        *,
        fraction_digits: typing.Optional[int] = None,
        cent_amount: int,
        currency_code: str,
        precise_amount: int
    ):
        self.precise_amount = precise_amount
        super().__init__(
            fraction_digits=fraction_digits,
            cent_amount=cent_amount,
            currency_code=currency_code,
            type=MoneyType.HIGH_PRECISION,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "HighPrecisionMoney":
        from ._schemas.common import HighPrecisionMoneySchema

        return HighPrecisionMoneySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import HighPrecisionMoneySchema

        return HighPrecisionMoneySchema().dump(self)


class Money(TypedMoney):
    def __init__(
        self,
        *,
        fraction_digits: typing.Optional[int] = None,
        cent_amount: int,
        currency_code: str
    ):

        super().__init__(
            fraction_digits=fraction_digits,
            cent_amount=cent_amount,
            currency_code=currency_code,
            type=MoneyType.CENT_PRECISION,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Money":
        from ._schemas.common import MoneySchema

        return MoneySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import MoneySchema

        return MoneySchema().dump(self)


class DiscountedPrice(_BaseType):
    value: "TypedMoney"
    #: Reference to a ProductDiscount.
    discount: "ProductDiscountKeyReference"

    def __init__(self, *, value: "TypedMoney", discount: "ProductDiscountKeyReference"):
        self.value = value
        self.discount = discount
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DiscountedPrice":
        from ._schemas.common import DiscountedPriceSchema

        return DiscountedPriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import DiscountedPriceSchema

        return DiscountedPriceSchema().dump(self)


class PriceTier(_BaseType):
    """A price tier is selected instead of the default price when a certain quantity of the ProductVariant is added to a cart and ordered."""

    #: The minimum quantity this price tier is valid for.
    minimum_quantity: int
    #: The currency of a price tier is always the same as the currency of the base Price.
    value: "TypedMoney"

    def __init__(self, *, minimum_quantity: int, value: "TypedMoney"):
        self.minimum_quantity = minimum_quantity
        self.value = value
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceTier":
        from ._schemas.common import PriceTierSchema

        return PriceTierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import PriceTierSchema

        return PriceTierSchema().dump(self)


class ImportResourceType(enum.Enum):
    """The type of the import resource."""

    CATEGORY = "category"
    ORDER = "order"
    PRICE = "price"
    PRODUCT = "product"
    PRODUCT_DRAFT = "product-draft"
    PRODUCT_TYPE = "product-type"
    PRODUCT_VARIANT = "product-variant"
    PRODUCT_VARIANT_PATCH = "product-variant-patch"
    CUSTOMER = "customer"
    INVENTORY = "inventory"


class ReferenceType(enum.Enum):
    """The type of the referenced resource."""

    CART_DISCOUNT = "cart-discount"
    CATEGORY = "category"
    CHANNEL = "channel"
    CUSTOMER = "customer"
    CUSTOMER_GROUP = "customer-group"
    PRICE = "price"
    PRODUCT = "product"
    PRODUCT_DISCOUNT = "product-discount"
    PRODUCT_TYPE = "product-type"
    PRODUCT_VARIANT = "product-variant"
    SHIPPING_METHOD = "shipping-method"
    STATE = "state"
    STORE = "store"
    TAX_CATEGORY = "tax-category"
    TYPE = "type"


class ProcessingState(enum.Enum):
    """This enumeration describes the processing state of an import operation."""

    VALIDATION_FAILED = "ValidationFailed"
    UNRESOLVED = "Unresolved"
    WAIT_FOR_MASTER_VARIANT = "WaitForMasterVariant"
    IMPORTED = "Imported"
    DELETE = "Delete"
    DELETED = "Deleted"
    REJECTED = "Rejected"


class Address(_BaseType):
    id: typing.Optional[str]
    key: typing.Optional[str]
    title: typing.Optional[str]
    salutation: typing.Optional[str]
    first_name: typing.Optional[str]
    last_name: typing.Optional[str]
    street_name: typing.Optional[str]
    street_number: typing.Optional[str]
    additional_street_info: typing.Optional[str]
    postal_code: typing.Optional[str]
    city: typing.Optional[str]
    region: typing.Optional[str]
    state: typing.Optional[str]
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: str
    company: typing.Optional[str]
    department: typing.Optional[str]
    building: typing.Optional[str]
    apartment: typing.Optional[str]
    p_o_box: typing.Optional[str]
    phone: typing.Optional[str]
    mobile: typing.Optional[str]
    email: typing.Optional[str]
    fax: typing.Optional[str]
    additional_address_info: typing.Optional[str]
    external_id: typing.Optional[str]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        salutation: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        street_name: typing.Optional[str] = None,
        street_number: typing.Optional[str] = None,
        additional_street_info: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        country: str,
        company: typing.Optional[str] = None,
        department: typing.Optional[str] = None,
        building: typing.Optional[str] = None,
        apartment: typing.Optional[str] = None,
        p_o_box: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        mobile: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        fax: typing.Optional[str] = None,
        additional_address_info: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None
    ):
        self.id = id
        self.key = key
        self.title = title
        self.salutation = salutation
        self.first_name = first_name
        self.last_name = last_name
        self.street_name = street_name
        self.street_number = street_number
        self.additional_street_info = additional_street_info
        self.postal_code = postal_code
        self.city = city
        self.region = region
        self.state = state
        self.country = country
        self.company = company
        self.department = department
        self.building = building
        self.apartment = apartment
        self.p_o_box = p_o_box
        self.phone = phone
        self.mobile = mobile
        self.email = email
        self.fax = fax
        self.additional_address_info = additional_address_info
        self.external_id = external_id
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Address":
        from ._schemas.common import AddressSchema

        return AddressSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import AddressSchema

        return AddressSchema().dump(self)

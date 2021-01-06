# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType

if typing.TYPE_CHECKING:
    from .channel import ChannelReference, ChannelResourceIdentifier
    from .customer import CustomerReference
    from .customer_group import CustomerGroupReference, CustomerGroupResourceIdentifier
    from .product_discount import ProductDiscountReference
    from .type import CustomFields, CustomFieldsDraft

__all__ = [
    "Address",
    "Asset",
    "AssetDimensions",
    "AssetDraft",
    "AssetSource",
    "BaseResource",
    "CentPrecisionMoney",
    "CentPrecisionMoneyDraft",
    "ClientLogging",
    "CreatedBy",
    "DiscountedPrice",
    "GeoJson",
    "GeoJsonPoint",
    "HighPrecisionMoney",
    "HighPrecisionMoneyDraft",
    "Image",
    "ImageDimensions",
    "KeyReference",
    "LastModifiedBy",
    "LocalizedString",
    "Money",
    "MoneyType",
    "PagedQueryResponse",
    "Price",
    "PriceDraft",
    "PriceTier",
    "PriceTierDraft",
    "QueryPrice",
    "Reference",
    "ReferenceTypeId",
    "ResourceIdentifier",
    "ScopedPrice",
    "TypedMoney",
    "TypedMoneyDraft",
    "Update",
    "UpdateAction",
]


class PagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["BaseResource"]
    meta: typing.Optional[object]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["BaseResource"],
        meta: typing.Optional[object] = None
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        self.meta = meta
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PagedQueryResponse":
        from ._schemas.common import PagedQueryResponseSchema

        return PagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import PagedQueryResponseSchema

        return PagedQueryResponseSchema().dump(self)


class Update(_BaseType):
    version: int
    actions: typing.List["UpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["UpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Update":
        from ._schemas.common import UpdateSchema

        return UpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import UpdateSchema

        return UpdateSchema().dump(self)


class UpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "UpdateAction":
        from ._schemas.common import UpdateActionSchema

        return UpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import UpdateActionSchema

        return UpdateActionSchema().dump(self)


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


class Asset(_BaseType):
    id: str
    sources: typing.List["AssetSource"]
    name: "LocalizedString"
    description: typing.Optional["LocalizedString"]
    tags: typing.Optional[typing.List["str"]]
    custom: typing.Optional["CustomFields"]
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        id: str,
        sources: typing.List["AssetSource"],
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        tags: typing.Optional[typing.List["str"]] = None,
        custom: typing.Optional["CustomFields"] = None,
        key: typing.Optional[str] = None
    ):
        self.id = id
        self.sources = sources
        self.name = name
        self.description = description
        self.tags = tags
        self.custom = custom
        self.key = key
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Asset":
        from ._schemas.common import AssetSchema

        return AssetSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import AssetSchema

        return AssetSchema().dump(self)


class AssetDimensions(_BaseType):
    w: int
    h: int

    def __init__(self, *, w: int, h: int):
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


class AssetDraft(_BaseType):
    sources: typing.List["AssetSource"]
    name: "LocalizedString"
    description: typing.Optional["LocalizedString"]
    tags: typing.Optional[typing.List["str"]]
    custom: typing.Optional["CustomFieldsDraft"]
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        sources: typing.List["AssetSource"],
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        tags: typing.Optional[typing.List["str"]] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        key: typing.Optional[str] = None
    ):
        self.sources = sources
        self.name = name
        self.description = description
        self.tags = tags
        self.custom = custom
        self.key = key
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AssetDraft":
        from ._schemas.common import AssetDraftSchema

        return AssetDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import AssetDraftSchema

        return AssetDraftSchema().dump(self)


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


class BaseResource(_BaseType):
    id: str
    version: int
    created_at: datetime.datetime
    last_modified_at: datetime.datetime

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime
    ):
        self.id = id
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "BaseResource":
        from ._schemas.common import BaseResourceSchema

        return BaseResourceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import BaseResourceSchema

        return BaseResourceSchema().dump(self)


class ClientLogging(_BaseType):
    client_id: typing.Optional[str]
    external_user_id: typing.Optional[str]
    customer: typing.Optional["CustomerReference"]
    anonymous_id: typing.Optional[str]

    def __init__(
        self,
        *,
        client_id: typing.Optional[str] = None,
        external_user_id: typing.Optional[str] = None,
        customer: typing.Optional["CustomerReference"] = None,
        anonymous_id: typing.Optional[str] = None
    ):
        self.client_id = client_id
        self.external_user_id = external_user_id
        self.customer = customer
        self.anonymous_id = anonymous_id
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ClientLogging":
        from ._schemas.common import ClientLoggingSchema

        return ClientLoggingSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ClientLoggingSchema

        return ClientLoggingSchema().dump(self)


class CreatedBy(ClientLogging):
    def __init__(
        self,
        *,
        client_id: typing.Optional[str] = None,
        external_user_id: typing.Optional[str] = None,
        customer: typing.Optional["CustomerReference"] = None,
        anonymous_id: typing.Optional[str] = None
    ):

        super().__init__(
            client_id=client_id,
            external_user_id=external_user_id,
            customer=customer,
            anonymous_id=anonymous_id,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CreatedBy":
        from ._schemas.common import CreatedBySchema

        return CreatedBySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CreatedBySchema

        return CreatedBySchema().dump(self)


class DiscountedPrice(_BaseType):
    value: "Money"
    discount: "ProductDiscountReference"

    def __init__(self, *, value: "Money", discount: "ProductDiscountReference"):
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


class GeoJson(_BaseType):
    type: str

    def __init__(self, *, type: str):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "GeoJson":
        if data["type"] == "Point":
            from ._schemas.common import GeoJsonPointSchema

            return GeoJsonPointSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import GeoJsonSchema

        return GeoJsonSchema().dump(self)


class GeoJsonPoint(GeoJson):
    coordinates: typing.List["float"]

    def __init__(self, *, coordinates: typing.List["float"]):
        self.coordinates = coordinates
        super().__init__(type="Point")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "GeoJsonPoint":
        from ._schemas.common import GeoJsonPointSchema

        return GeoJsonPointSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import GeoJsonPointSchema

        return GeoJsonPointSchema().dump(self)


class Image(_BaseType):
    url: str
    dimensions: "ImageDimensions"
    label: typing.Optional[str]

    def __init__(
        self,
        *,
        url: str,
        dimensions: "ImageDimensions",
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


class ImageDimensions(_BaseType):
    w: int
    h: int

    def __init__(self, *, w: int, h: int):
        self.w = w
        self.h = h
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImageDimensions":
        from ._schemas.common import ImageDimensionsSchema

        return ImageDimensionsSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ImageDimensionsSchema

        return ImageDimensionsSchema().dump(self)


class KeyReference(_BaseType):
    type_id: "ReferenceTypeId"
    key: str

    def __init__(self, *, type_id: "ReferenceTypeId", key: str):
        self.type_id = type_id
        self.key = key
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "KeyReference":
        if data["typeId"] == "store":
            from ._schemas.store import StoreKeyReferenceSchema

            return StoreKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import KeyReferenceSchema

        return KeyReferenceSchema().dump(self)


class LastModifiedBy(ClientLogging):
    def __init__(
        self,
        *,
        client_id: typing.Optional[str] = None,
        external_user_id: typing.Optional[str] = None,
        customer: typing.Optional["CustomerReference"] = None,
        anonymous_id: typing.Optional[str] = None
    ):

        super().__init__(
            client_id=client_id,
            external_user_id=external_user_id,
            customer=customer,
            anonymous_id=anonymous_id,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "LastModifiedBy":
        from ._schemas.common import LastModifiedBySchema

        return LastModifiedBySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import LastModifiedBySchema

        return LastModifiedBySchema().dump(self)


class LocalizedString(typing.Dict[str, str]):
    pass


class Money(_BaseType):
    cent_amount: int
    #: The currency code compliant to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).
    currency_code: str

    def __init__(self, *, cent_amount: int, currency_code: str):
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


class MoneyType(enum.Enum):
    CENT_PRECISION = "centPrecision"
    HIGH_PRECISION = "highPrecision"


class Price(_BaseType):
    id: str
    value: "TypedMoney"
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: typing.Optional[str]
    customer_group: typing.Optional["CustomerGroupReference"]
    channel: typing.Optional["ChannelReference"]
    valid_from: typing.Optional[datetime.datetime]
    valid_until: typing.Optional[datetime.datetime]
    discounted: typing.Optional["DiscountedPrice"]
    custom: typing.Optional["CustomFields"]
    tiers: typing.Optional[typing.List["PriceTier"]]

    def __init__(
        self,
        *,
        id: str,
        value: "TypedMoney",
        country: typing.Optional[str] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        channel: typing.Optional["ChannelReference"] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        discounted: typing.Optional["DiscountedPrice"] = None,
        custom: typing.Optional["CustomFields"] = None,
        tiers: typing.Optional[typing.List["PriceTier"]] = None
    ):
        self.id = id
        self.value = value
        self.country = country
        self.customer_group = customer_group
        self.channel = channel
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.discounted = discounted
        self.custom = custom
        self.tiers = tiers
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Price":
        from ._schemas.common import PriceSchema

        return PriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import PriceSchema

        return PriceSchema().dump(self)


class PriceDraft(_BaseType):
    value: "Money"
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: typing.Optional[str]
    customer_group: typing.Optional["CustomerGroupResourceIdentifier"]
    channel: typing.Optional["ChannelResourceIdentifier"]
    valid_from: typing.Optional[datetime.datetime]
    valid_until: typing.Optional[datetime.datetime]
    custom: typing.Optional["CustomFieldsDraft"]
    tiers: typing.Optional[typing.List["PriceTierDraft"]]
    discounted: typing.Optional["DiscountedPrice"]

    def __init__(
        self,
        *,
        value: "Money",
        country: typing.Optional[str] = None,
        customer_group: typing.Optional["CustomerGroupResourceIdentifier"] = None,
        channel: typing.Optional["ChannelResourceIdentifier"] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        tiers: typing.Optional[typing.List["PriceTierDraft"]] = None,
        discounted: typing.Optional["DiscountedPrice"] = None
    ):
        self.value = value
        self.country = country
        self.customer_group = customer_group
        self.channel = channel
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.custom = custom
        self.tiers = tiers
        self.discounted = discounted
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceDraft":
        from ._schemas.common import PriceDraftSchema

        return PriceDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import PriceDraftSchema

        return PriceDraftSchema().dump(self)


class PriceTier(_BaseType):
    minimum_quantity: int
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


class PriceTierDraft(_BaseType):
    minimum_quantity: int
    value: "Money"

    def __init__(self, *, minimum_quantity: int, value: "Money"):
        self.minimum_quantity = minimum_quantity
        self.value = value
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceTierDraft":
        from ._schemas.common import PriceTierDraftSchema

        return PriceTierDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import PriceTierDraftSchema

        return PriceTierDraftSchema().dump(self)


class QueryPrice(_BaseType):
    id: str
    value: "Money"
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: typing.Optional[str]
    customer_group: typing.Optional["CustomerGroupReference"]
    channel: typing.Optional["ChannelReference"]
    valid_from: typing.Optional[datetime.datetime]
    valid_until: typing.Optional[datetime.datetime]
    discounted: typing.Optional["DiscountedPrice"]
    custom: typing.Optional["CustomFields"]
    tiers: typing.Optional[typing.List["PriceTierDraft"]]

    def __init__(
        self,
        *,
        id: str,
        value: "Money",
        country: typing.Optional[str] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        channel: typing.Optional["ChannelReference"] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        discounted: typing.Optional["DiscountedPrice"] = None,
        custom: typing.Optional["CustomFields"] = None,
        tiers: typing.Optional[typing.List["PriceTierDraft"]] = None
    ):
        self.id = id
        self.value = value
        self.country = country
        self.customer_group = customer_group
        self.channel = channel
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.discounted = discounted
        self.custom = custom
        self.tiers = tiers
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "QueryPrice":
        from ._schemas.common import QueryPriceSchema

        return QueryPriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import QueryPriceSchema

        return QueryPriceSchema().dump(self)


class Reference(_BaseType):
    type_id: "ReferenceTypeId"
    id: str

    def __init__(self, *, type_id: "ReferenceTypeId", id: str):
        self.type_id = type_id
        self.id = id
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Reference":
        if data["typeId"] == "cart-discount":
            from ._schemas.cart_discount import CartDiscountReferenceSchema

            return CartDiscountReferenceSchema().load(data)
        if data["typeId"] == "cart":
            from ._schemas.cart import CartReferenceSchema

            return CartReferenceSchema().load(data)
        if data["typeId"] == "category":
            from ._schemas.category import CategoryReferenceSchema

            return CategoryReferenceSchema().load(data)
        if data["typeId"] == "channel":
            from ._schemas.channel import ChannelReferenceSchema

            return ChannelReferenceSchema().load(data)
        if data["typeId"] == "key-value-document":
            from ._schemas.custom_object import CustomObjectReferenceSchema

            return CustomObjectReferenceSchema().load(data)
        if data["typeId"] == "customer-group":
            from ._schemas.customer_group import CustomerGroupReferenceSchema

            return CustomerGroupReferenceSchema().load(data)
        if data["typeId"] == "customer":
            from ._schemas.customer import CustomerReferenceSchema

            return CustomerReferenceSchema().load(data)
        if data["typeId"] == "discount-code":
            from ._schemas.discount_code import DiscountCodeReferenceSchema

            return DiscountCodeReferenceSchema().load(data)
        if data["typeId"] == "inventory-entry":
            from ._schemas.inventory import InventoryEntryReferenceSchema

            return InventoryEntryReferenceSchema().load(data)
        if data["typeId"] == "order-edit":
            from ._schemas.order_edit import OrderEditReferenceSchema

            return OrderEditReferenceSchema().load(data)
        if data["typeId"] == "order":
            from ._schemas.order import OrderReferenceSchema

            return OrderReferenceSchema().load(data)
        if data["typeId"] == "payment":
            from ._schemas.payment import PaymentReferenceSchema

            return PaymentReferenceSchema().load(data)
        if data["typeId"] == "product-discount":
            from ._schemas.product_discount import ProductDiscountReferenceSchema

            return ProductDiscountReferenceSchema().load(data)
        if data["typeId"] == "product-type":
            from ._schemas.product_type import ProductTypeReferenceSchema

            return ProductTypeReferenceSchema().load(data)
        if data["typeId"] == "product":
            from ._schemas.product import ProductReferenceSchema

            return ProductReferenceSchema().load(data)
        if data["typeId"] == "review":
            from ._schemas.review import ReviewReferenceSchema

            return ReviewReferenceSchema().load(data)
        if data["typeId"] == "shipping-method":
            from ._schemas.shipping_method import ShippingMethodReferenceSchema

            return ShippingMethodReferenceSchema().load(data)
        if data["typeId"] == "shopping-list":
            from ._schemas.shopping_list import ShoppingListReferenceSchema

            return ShoppingListReferenceSchema().load(data)
        if data["typeId"] == "state":
            from ._schemas.state import StateReferenceSchema

            return StateReferenceSchema().load(data)
        if data["typeId"] == "store":
            from ._schemas.store import StoreReferenceSchema

            return StoreReferenceSchema().load(data)
        if data["typeId"] == "tax-category":
            from ._schemas.tax_category import TaxCategoryReferenceSchema

            return TaxCategoryReferenceSchema().load(data)
        if data["typeId"] == "type":
            from ._schemas.type import TypeReferenceSchema

            return TypeReferenceSchema().load(data)
        if data["typeId"] == "zone":
            from ._schemas.zone import ZoneReferenceSchema

            return ZoneReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ReferenceSchema

        return ReferenceSchema().dump(self)


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


class ResourceIdentifier(_BaseType):
    type_id: typing.Optional["ReferenceTypeId"]
    id: typing.Optional[str]
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ):
        self.type_id = type_id
        self.id = id
        self.key = key
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ResourceIdentifier":
        if data["typeId"] == "cart-discount":
            from ._schemas.cart_discount import CartDiscountResourceIdentifierSchema

            return CartDiscountResourceIdentifierSchema().load(data)
        if data["typeId"] == "cart":
            from ._schemas.cart import CartResourceIdentifierSchema

            return CartResourceIdentifierSchema().load(data)
        if data["typeId"] == "category":
            from ._schemas.category import CategoryResourceIdentifierSchema

            return CategoryResourceIdentifierSchema().load(data)
        if data["typeId"] == "channel":
            from ._schemas.channel import ChannelResourceIdentifierSchema

            return ChannelResourceIdentifierSchema().load(data)
        if data["typeId"] == "customer-group":
            from ._schemas.customer_group import CustomerGroupResourceIdentifierSchema

            return CustomerGroupResourceIdentifierSchema().load(data)
        if data["typeId"] == "customer":
            from ._schemas.customer import CustomerResourceIdentifierSchema

            return CustomerResourceIdentifierSchema().load(data)
        if data["typeId"] == "discount-code":
            from ._schemas.discount_code import DiscountCodeResourceIdentifierSchema

            return DiscountCodeResourceIdentifierSchema().load(data)
        if data["typeId"] == "inventory-entry":
            from ._schemas.inventory import InventoryEntryResourceIdentifierSchema

            return InventoryEntryResourceIdentifierSchema().load(data)
        if data["typeId"] == "order-edit":
            from ._schemas.order_edit import OrderEditResourceIdentifierSchema

            return OrderEditResourceIdentifierSchema().load(data)
        if data["typeId"] == "order":
            from ._schemas.order import OrderResourceIdentifierSchema

            return OrderResourceIdentifierSchema().load(data)
        if data["typeId"] == "payment":
            from ._schemas.payment import PaymentResourceIdentifierSchema

            return PaymentResourceIdentifierSchema().load(data)
        if data["typeId"] == "product-discount":
            from ._schemas.product_discount import (
                ProductDiscountResourceIdentifierSchema,
            )

            return ProductDiscountResourceIdentifierSchema().load(data)
        if data["typeId"] == "product-type":
            from ._schemas.product_type import ProductTypeResourceIdentifierSchema

            return ProductTypeResourceIdentifierSchema().load(data)
        if data["typeId"] == "product":
            from ._schemas.product import ProductResourceIdentifierSchema

            return ProductResourceIdentifierSchema().load(data)
        if data["typeId"] == "review":
            from ._schemas.review import ReviewResourceIdentifierSchema

            return ReviewResourceIdentifierSchema().load(data)
        if data["typeId"] == "shipping-method":
            from ._schemas.shipping_method import ShippingMethodResourceIdentifierSchema

            return ShippingMethodResourceIdentifierSchema().load(data)
        if data["typeId"] == "shopping-list":
            from ._schemas.shopping_list import ShoppingListResourceIdentifierSchema

            return ShoppingListResourceIdentifierSchema().load(data)
        if data["typeId"] == "state":
            from ._schemas.state import StateResourceIdentifierSchema

            return StateResourceIdentifierSchema().load(data)
        if data["typeId"] == "store":
            from ._schemas.store import StoreResourceIdentifierSchema

            return StoreResourceIdentifierSchema().load(data)
        if data["typeId"] == "tax-category":
            from ._schemas.tax_category import TaxCategoryResourceIdentifierSchema

            return TaxCategoryResourceIdentifierSchema().load(data)
        if data["typeId"] == "type":
            from ._schemas.type import TypeResourceIdentifierSchema

            return TypeResourceIdentifierSchema().load(data)
        if data["typeId"] == "zone":
            from ._schemas.zone import ZoneResourceIdentifierSchema

            return ZoneResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ResourceIdentifierSchema

        return ResourceIdentifierSchema().dump(self)


class ScopedPrice(_BaseType):
    id: str
    value: "TypedMoney"
    current_value: "TypedMoney"
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: typing.Optional[str]
    customer_group: typing.Optional["CustomerGroupReference"]
    channel: typing.Optional["ChannelReference"]
    valid_from: typing.Optional[datetime.datetime]
    valid_until: typing.Optional[datetime.datetime]
    discounted: typing.Optional["DiscountedPrice"]
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: str,
        value: "TypedMoney",
        current_value: "TypedMoney",
        country: typing.Optional[str] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        channel: typing.Optional["ChannelReference"] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        discounted: typing.Optional["DiscountedPrice"] = None,
        custom: typing.Optional["CustomFields"] = None
    ):
        self.id = id
        self.value = value
        self.current_value = current_value
        self.country = country
        self.customer_group = customer_group
        self.channel = channel
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.discounted = discounted
        self.custom = custom
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ScopedPrice":
        from ._schemas.common import ScopedPriceSchema

        return ScopedPriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ScopedPriceSchema

        return ScopedPriceSchema().dump(self)


class TypedMoney(_BaseType):
    type: "MoneyType"
    fraction_digits: int
    cent_amount: int
    #: The currency code compliant to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).
    currency_code: str

    def __init__(
        self,
        *,
        type: "MoneyType",
        fraction_digits: int,
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
        if data["type"] == "centPrecision":
            from ._schemas.common import CentPrecisionMoneySchema

            return CentPrecisionMoneySchema().load(data)
        if data["type"] == "highPrecision":
            from ._schemas.common import HighPrecisionMoneySchema

            return HighPrecisionMoneySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import TypedMoneySchema

        return TypedMoneySchema().dump(self)


class CentPrecisionMoney(TypedMoney):
    def __init__(self, *, fraction_digits: int, cent_amount: int, currency_code: str):

        super().__init__(
            fraction_digits=fraction_digits,
            cent_amount=cent_amount,
            currency_code=currency_code,
            type=MoneyType.CENT_PRECISION,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CentPrecisionMoney":
        from ._schemas.common import CentPrecisionMoneySchema

        return CentPrecisionMoneySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CentPrecisionMoneySchema

        return CentPrecisionMoneySchema().dump(self)


class HighPrecisionMoney(TypedMoney):
    precise_amount: int

    def __init__(
        self,
        *,
        fraction_digits: int,
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


class TypedMoneyDraft(Money):
    type: "MoneyType"
    fraction_digits: typing.Optional[int]

    def __init__(
        self,
        *,
        cent_amount: int,
        currency_code: str,
        type: "MoneyType",
        fraction_digits: typing.Optional[int] = None
    ):
        self.type = type
        self.fraction_digits = fraction_digits
        super().__init__(cent_amount=cent_amount, currency_code=currency_code)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypedMoneyDraft":
        if data["type"] == "centPrecision":
            from ._schemas.common import CentPrecisionMoneyDraftSchema

            return CentPrecisionMoneyDraftSchema().load(data)
        if data["type"] == "highPrecision":
            from ._schemas.common import HighPrecisionMoneyDraftSchema

            return HighPrecisionMoneyDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import TypedMoneyDraftSchema

        return TypedMoneyDraftSchema().dump(self)


class CentPrecisionMoneyDraft(TypedMoneyDraft):
    def __init__(
        self,
        *,
        cent_amount: int,
        currency_code: str,
        fraction_digits: typing.Optional[int] = None
    ):

        super().__init__(
            cent_amount=cent_amount,
            currency_code=currency_code,
            fraction_digits=fraction_digits,
            type=MoneyType.CENT_PRECISION,
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CentPrecisionMoneyDraft":
        from ._schemas.common import CentPrecisionMoneyDraftSchema

        return CentPrecisionMoneyDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CentPrecisionMoneyDraftSchema

        return CentPrecisionMoneyDraftSchema().dump(self)


class HighPrecisionMoneyDraft(TypedMoneyDraft):
    precise_amount: int

    def __init__(
        self,
        *,
        cent_amount: int,
        currency_code: str,
        fraction_digits: typing.Optional[int] = None,
        precise_amount: int
    ):
        self.precise_amount = precise_amount
        super().__init__(
            cent_amount=cent_amount,
            currency_code=currency_code,
            fraction_digits=fraction_digits,
            type=MoneyType.HIGH_PRECISION,
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "HighPrecisionMoneyDraft":
        from ._schemas.common import HighPrecisionMoneyDraftSchema

        return HighPrecisionMoneyDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import HighPrecisionMoneyDraftSchema

        return HighPrecisionMoneyDraftSchema().dump(self)

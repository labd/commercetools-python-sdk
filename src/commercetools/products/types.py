import datetime
import decimal
from typing import List, Dict, Any

import attr
from marshmallow import EXCLUDE, Schema, fields, post_load

from commercetools import common

__all__ = [
    "ProductDraft",
    "ProductDraftSchema",
    "ProductData",
    "ProductDataSchema",
    "ProductCatalogData",
    "ProductCatalogDataSchema",
    "Product",
    "ProductSchema",
]


@attr.s(auto_attribs=True)
class PriceTier:
    minimum_quantity: decimal.Decimal
    value: decimal.Decimal


class PriceTierSchema(Schema):
    minimum_quantity = fields.Decimal(data_key="minimumQuantity")
    value = fields.Decimal()

    class Meta:
        unknown = EXCLUDE

    @post_load
    def make(self, data):
        return PriceTier(**data)


@attr.s(auto_attribs=True)
class PriceDraft:
    value: decimal.Decimal
    country: str = None
    customer_group: common.ResourceIdentifier = None
    channel: common.ResourceIdentifier = None
    valid_from: datetime.datetime = None
    valid_until: datetime.datetime = None
    tiers: List[PriceTier] = None
    # custom: CustomFieldsDraft = None  # TODO


class PriceDraftSchema(Schema):
    value = fields.Decimal()
    country = fields.String()
    customer_group = fields.Nested(common.ResourceIdentifierSchema)
    channel = fields.Nested(common.ResourceIdentifierSchema)
    valid_from = fields.DateTime(data_key="validFrom")
    valid_until = fields.DateTime(data_key="validUntil")
    tiers = fields.Nested(PriceTierSchema, many=True)

    class Meta:
        unknown = EXCLUDE

    @post_load
    def make(self, data):
        return PriceDraft(**data)


@attr.s(auto_attribs=True)
class DiscountedPrice:
    value: decimal.Decimal
    discount: common.ResourceIdentifier


class DiscountedPriceSchema(Schema):
    value = fields.Decimal()
    discount = fields.Nested(common.ResourceIdentifierSchema)


@attr.s(auto_attribs=True)
class Price:
    id: str
    value: common.Money
    country: str
    customer_group: common.ResourceIdentifier
    channel: common.ResourceIdentifier
    valid_from: datetime.datetime
    valid_until: datetime.datetime
    tiers: List[PriceTier]
    discounted: DiscountedPrice
    # custom: CustomFieldsDraft = None  # TODO


class PriceSchema(Schema):
    id = fields.String()
    value = fields.Nested(common.MoneySchema)
    country = fields.String()
    customer_group = fields.Nested(common.ResourceIdentifierSchema)
    channel = fields.Nested(common.ResourceIdentifierSchema)
    valid_from = fields.DateTime(data_key="validFrom")
    valid_until = fields.DateTime(data_key="validUntil")
    tiers = fields.Nested(PriceTierSchema, many=True)
    discounted = fields.Nested(DiscountedPriceSchema)


@attr.s(auto_attribs=True)
class ScopedPrice:
    id: str
    value: decimal.Decimal
    current_value: decimal.Decimal
    country: str
    customer_group: common.ResourceIdentifier
    channel: common.ResourceIdentifier
    valid_from: datetime.datetime
    valid_until: datetime.datetime
    tiers: List[PriceTier]
    discounted: DiscountedPrice
    # custom: CustomFieldsDraft = None  # TODO


class ScopedPriceSchema(Schema):
    id = fields.String()
    value = fields.Decimal()
    current_value = fields.Decimal(data_key="currentValue")
    country = fields.String()
    customer_group = fields.Nested(common.ResourceIdentifierSchema)
    channel = fields.Nested(common.ResourceIdentifierSchema)
    valid_from = fields.DateTime(data_key="validFrom")
    valid_until = fields.DateTime(data_key="validUntil")
    tiers = fields.Nested(PriceTierSchema, many=True)
    discounted = fields.Nested(DiscountedPriceSchema)
    # custom: CustomFieldsDraft = None  # TODO


@attr.s(auto_attribs=True)
class Image:
    url: str
    dimensions: Dict[str, int]
    label: str = None


class ImageSchema(Schema):
    url = fields.String()
    dimensions = fields.Dict()
    label = fields.String()

    class Meta:
        unknown = EXCLUDE

    @post_load
    def make(self, data):
        return Image(**data)


@attr.s(auto_attribs=True)
class Attribute:
    name: str
    value: Any


class AttributeSchema(Schema):
    name = fields.String()
    value = fields.Raw()

    class Meta:
        unknown = EXCLUDE

    @post_load
    def make(self, data):
        return Attribute(**data)


@attr.s(auto_attribs=True)
class ProductVariantDraft:
    sku: str = None
    key: str = None
    prices: List[PriceDraft] = attr.Factory(lambda: [])
    images: List[Image] = attr.Factory(lambda: [])
    assets: List[common.AssetDraft] = attr.Factory(lambda: [])
    attributes: List[Attribute] = attr.Factory(lambda: [])


class ProductVariantDraftSchema(Schema):
    sku = fields.String()
    key = fields.String()
    prices = fields.Nested(PriceDraftSchema, many=True)
    images = fields.Nested(ImageSchema, many=True)
    assets = fields.Nested(common.AssetDraftSchema, many=True)
    attributes = fields.Nested(AttributeSchema, many=True)

    class Meta:
        unknown = EXCLUDE


@attr.s(auto_attribs=True)
class ProductDraft:
    key: str
    name: common.LocalizedString
    product_type: common.ResourceIdentifier
    slug: common.LocalizedString
    description: common.LocalizedString
    categories: List[common.ResourceIdentifier]
    category_order_hints: dict
    meta_title: common.LocalizedString
    meta_description: common.LocalizedString
    meta_keywords: common.LocalizedString
    master_variant: ProductVariantDraft
    variants: List[ProductVariantDraft]
    tax_category: common.ResourceIdentifier
    search_keywords: Dict[str, List[dict]]
    state: common.ResourceIdentifier
    publish: bool = False


class ProductDraftSchema(Schema):
    key = fields.Str()

    product_type = fields.Nested(
        common.ResourceIdentifierSchema, data_key="productType"
    )

    master_variant = fields.Nested(ProductVariantDraftSchema)
    variants = fields.Nested(ProductVariantDraftSchema, many=True)

    class Meta:
        unknown = EXCLUDE

    @post_load
    def make(self, data):
        return ProductDraft(**data)


@attr.s(auto_attribs=True)
class ProductVariantAvailability:
    is_on_stock: bool
    restockable_in_days: int
    availabile_quantity: int
    channels: Dict[str, "ProductVariantAvailability"]


class ProductVariantAvailabilitySchema(Schema):
    is_on_stock = fields.Bool(data_key="isOnStock")
    restockable_in_days = fields.Integer(data_key="restockable_in_days")
    available_quantity = fields.Integer(data_key="AvailableQuantity")
    channels = fields.Dict(keys=fields.String(), values=fields.Nested("self"))


@attr.s(auto_attribs=True)
class ProductVariant:
    id: int
    sku: str
    key: str

    #: The prices of the variant. The prices does not contain two prices for
    #: the same price scope (same currency, country, customer group and
    #: channel).
    prices: List[Price]
    attributes: List[Attribute]

    #: Only appears when price selection is used. This field cannot be used in
    #: a query predicate.
    price: Price

    images: List[Image]
    assets: List[common.Asset]

    #: The availability is set if the variant is tracked by the inventory. The
    #: field might not contain the latest inventory state (it is eventually
    #: consistent) and can be used as an optimization to reduce calls to the
    #: inventory service.
    availability: ProductVariantAvailability

    #: Only appears in response to a Product Projection Search request to mark
    #: this variant as one that matches the search query.
    is_matching_variant: bool

    #: Only appears when price selection is used.
    scoped_price: ScopedPrice

    #: Only appears in response to a Product Projection Search request when
    #: price selection is used.
    scoped_price_discount: bool


class ProductVariantSchema(Schema):
    id = fields.Integer()
    sku = fields.String()
    key = fields.String(missing=None)
    prices = fields.Nested(PriceSchema, many=True)
    attributes = fields.Nested(AttributeSchema, many=True)
    price = fields.Nested(PriceSchema, missing=None)
    images = fields.Nested(ImageSchema, many=True)
    assets = fields.Nested(common.AssetSchema, many=True)
    availability = fields.Nested(ProductVariantAvailabilitySchema, missing=None)
    is_matching_variant = fields.Bool(data_key="isMatchingVariant", missing=False)
    scoped_price = fields.Nested(
        ScopedPriceSchema, data_key="scopedPrice", missing=None
    )
    scoped_price_discount = fields.Bool(data_key="scopedPriceDiscount", missing=None)

    @post_load
    def make(self, data):
        print(data)
        return ProductVariant(**data)


@attr.s(auto_attribs=True)
class ProductData:
    name: common.LocalizedString

    #: References to categories the product is in.
    categories: List[common.ResourceIdentifier]
    category_order_hints: dict
    description: common.LocalizedString

    #: human-readable identifiers usually used as deep-link URL to the related
    #: product. Each slug is unique across a project, but a product can have the
    #: same slug for different languages.
    slug: common.LocalizedString
    master_variant: ProductVariant
    variants: List[ProductVariant]
    search_keywords: dict

    meta_title: common.LocalizedString = None
    meta_description: common.LocalizedString = None
    meta_keywords: common.LocalizedString = None


class ProductDataSchema(Schema):
    name = common.LocalizedStringField()
    categories = fields.Nested(common.ResourceIdentifierSchema, many=True)
    category_order_hints = fields.Dict(data_key="categoryOrderHints")
    description = common.LocalizedStringField()
    slug = common.LocalizedStringField()

    meta_title = common.LocalizedStringField()
    meta_description = common.LocalizedStringField()
    meta_keywords = common.LocalizedStringField()

    master_variant = fields.Nested(ProductVariantSchema, data_key="masterVariant")
    variants = fields.Nested(ProductVariantSchema, many=True)
    search_keywords = fields.Dict(data_key="searchKeywords")

    class Meta:
        unknown = EXCLUDE

    @post_load
    def make(self, data):
        return ProductData(**data)


@attr.s(auto_attribs=True)
class ProductCatalogData:
    #: Whether the product is published.
    published: bool

    #: The current data of the product.
    current: ProductData

    #: The staged data of the product.
    staged: ProductData

    #: Whether the staged data is different from the current data.
    has_staged_changes: bool


class ProductCatalogDataSchema(Schema):
    published = fields.Bool()
    current = fields.Nested(ProductDataSchema)
    staged = fields.Nested(ProductDataSchema)
    has_staged_changes = fields.Bool(data_key="hasStagedChanges")

    class Meta:
        unknown = EXCLUDE

    @post_load
    def make(self, data):
        return ProductCatalogData(**data)


@attr.s(auto_attribs=True)
class ReviewRatingStatistics:
    average_rating: decimal.Decimal
    highest_rating: decimal.Decimal
    lowest_rating: decimal.Decimal
    count: int
    ratingDistribution: dict


class ReviewRatingStatisticsSchema(Schema):
    average_rating = fields.Decimal(data_key="averageRating")
    highest_rating = fields.Decimal(data_key="highestRating")
    lowest_rating = fields.Decimal(data_key="lowestRating")
    count = fields.Integer()
    ratingDistribution = fields.Raw()

    class Meta:
        unknown = EXCLUDE


@attr.s(auto_attribs=True)
class Product:
    """The full representation of a product combines the current and staged
    representations in a single representation.
    """

    #: The unique ID of the product.
    id: str

    #: The current version of the product.
    version: int
    created_at: datetime.datetime
    last_modified_at: datetime.datetime

    #: The product data in the master catalog.
    master_data: ProductCatalogData

    #: Statistics about the review ratings taken into account for this product.
    review_ratings_statistics = fields.Nested(ReviewRatingStatisticsSchema)

    # Optional arguments

    #: User-specific unique identifier for the product. Product keys are
    #: different from product variant keys.
    key: str = None

    state: common.ResourceIdentifierSchema = None
    product_type: common.ResourceIdentifier = None
    tax_category: common.ResourceIdentifier = None


class ProductSchema(Schema):
    id = fields.Str()
    key = fields.Str()
    version = fields.Integer()
    created_at = fields.DateTime(data_key="createdAt")
    last_modified_at = fields.DateTime(data_key="lastModifiedAt")
    product_type = fields.Nested(
        common.ResourceIdentifierSchema, data_key="productType"
    )
    master_data = fields.Nested(ProductCatalogDataSchema, data_key="masterData")
    tax_category = fields.Nested(
        common.ResourceIdentifierSchema, data_key="taxCategory"
    )
    state = fields.Nested(common.ResourceIdentifierSchema, missing=None)
    review_rating_statistics = fields.Raw(data_key="reviewRatingStatistics")

    class Meta:
        unknown = EXCLUDE

    @post_load
    def make(self, data):
        return Product(**data)

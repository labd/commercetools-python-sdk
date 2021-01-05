# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResource

if typing.TYPE_CHECKING:
    from .common import (
        Asset,
        CategoryKeyReference,
        ChannelKeyReference,
        CustomerGroupKeyReference,
        DiscountedPrice,
        Image,
        LocalizedString,
        PriceTier,
        ProductTypeKeyReference,
        StateKeyReference,
        TaxCategoryKeyReference,
        TypedMoney,
    )
    from .customfields import Custom
    from .products import SearchKeywords
    from .productvariants import Attribute


class ProductDraftImport(ImportResource):
    #: The product's product type. Maps to `Product.productType`.
    #:
    #: The product type referenced
    #: must already exist in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    product_type: "ProductTypeKeyReference"
    name: "LocalizedString"
    #: Human-readable identifiers usually used as deep-link URL to the related product. Each slug must be unique across a project,
    #: but a product can have the same slug for different languages. Allowed are alphabetic, numeric, underscore (_) and hyphen (-) characters.
    slug: "LocalizedString"
    #: Maps to `Product.description`.
    description: typing.Optional["LocalizedString"]
    #: An array of references to categories by their keys. Maps to `Product.categories`.
    #:
    #: The categories referenced
    #: must already exist in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    categories: typing.Optional[typing.List["CategoryKeyReference"]]
    meta_title: typing.Optional["LocalizedString"]
    meta_description: typing.Optional["LocalizedString"]
    meta_keywords: typing.Optional["LocalizedString"]
    #: The master product variant.
    #: Required if the `variants` array has product variants.
    master_variant: typing.Optional["ProductVariantDraftImport"]
    #: An array of related product variants.
    variants: typing.Optional[typing.List["ProductVariantDraftImport"]]
    #: References a tax category by its key.
    #:
    #: The tax category referenced must already exist
    #: in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    tax_category: typing.Optional["TaxCategoryKeyReference"]
    search_keywords: typing.Optional["SearchKeywords"]
    #: References a state by its key.
    #:
    #: The tax category referenced must already exist
    #: in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    state: typing.Optional["StateKeyReference"]
    #: If there were updates, only the updates will be published to `staged` and `current` projection.
    publish: typing.Optional["bool"]

    def __init__(
        self,
        *,
        key: "str",
        product_type: "ProductTypeKeyReference",
        name: "LocalizedString",
        slug: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        categories: typing.Optional[typing.List["CategoryKeyReference"]] = None,
        meta_title: typing.Optional["LocalizedString"] = None,
        meta_description: typing.Optional["LocalizedString"] = None,
        meta_keywords: typing.Optional["LocalizedString"] = None,
        master_variant: typing.Optional["ProductVariantDraftImport"] = None,
        variants: typing.Optional[typing.List["ProductVariantDraftImport"]] = None,
        tax_category: typing.Optional["TaxCategoryKeyReference"] = None,
        search_keywords: typing.Optional["SearchKeywords"] = None,
        state: typing.Optional["StateKeyReference"] = None,
        publish: typing.Optional["bool"] = None
    ):
        self.product_type = product_type
        self.name = name
        self.slug = slug
        self.description = description
        self.categories = categories
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords
        self.master_variant = master_variant
        self.variants = variants
        self.tax_category = tax_category
        self.search_keywords = search_keywords
        self.state = state
        self.publish = publish
        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductDraftImport":
        from ._schemas.productdrafts import ProductDraftImportSchema

        return ProductDraftImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productdrafts import ProductDraftImportSchema

        return ProductDraftImportSchema().dump(self)


class ProductVariantDraftImport(_BaseType):
    sku: typing.Optional["str"]
    key: typing.Optional["str"]
    prices: typing.Optional[typing.List["PriceDraftImport"]]
    attributes: typing.Optional[typing.List["Attribute"]]
    images: typing.Optional[typing.List["Image"]]
    assets: typing.Optional[typing.List["Asset"]]

    def __init__(
        self,
        *,
        sku: typing.Optional["str"] = None,
        key: typing.Optional["str"] = None,
        prices: typing.Optional[typing.List["PriceDraftImport"]] = None,
        attributes: typing.Optional[typing.List["Attribute"]] = None,
        images: typing.Optional[typing.List["Image"]] = None,
        assets: typing.Optional[typing.List["Asset"]] = None
    ):
        self.sku = sku
        self.key = key
        self.prices = prices
        self.attributes = attributes
        self.images = images
        self.assets = assets
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantDraftImport":
        from ._schemas.productdrafts import ProductVariantDraftImportSchema

        return ProductVariantDraftImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productdrafts import ProductVariantDraftImportSchema

        return ProductVariantDraftImportSchema().dump(self)


class PriceDraftImport(_BaseType):
    value: "TypedMoney"
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: typing.Optional["str"]
    #: References a customer group by its key.
    customer_group: typing.Optional["CustomerGroupKeyReference"]
    #: References a channel by its key.
    channel: typing.Optional["ChannelKeyReference"]
    valid_from: typing.Optional["datetime.datetime"]
    valid_until: typing.Optional["datetime.datetime"]
    #: The custom fields for this category.
    custom: typing.Optional["Custom"]
    #: Sets a discounted price from an external service.
    discounted: typing.Optional["DiscountedPrice"]
    #: The tiered prices for this price.
    tiers: typing.Optional[typing.List["PriceTier"]]
    key: typing.Optional["str"]

    def __init__(
        self,
        *,
        value: "TypedMoney",
        country: typing.Optional["str"] = None,
        customer_group: typing.Optional["CustomerGroupKeyReference"] = None,
        channel: typing.Optional["ChannelKeyReference"] = None,
        valid_from: typing.Optional["datetime.datetime"] = None,
        valid_until: typing.Optional["datetime.datetime"] = None,
        custom: typing.Optional["Custom"] = None,
        discounted: typing.Optional["DiscountedPrice"] = None,
        tiers: typing.Optional[typing.List["PriceTier"]] = None,
        key: typing.Optional["str"] = None
    ):
        self.value = value
        self.country = country
        self.customer_group = customer_group
        self.channel = channel
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.custom = custom
        self.discounted = discounted
        self.tiers = tiers
        self.key = key
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceDraftImport":
        from ._schemas.productdrafts import PriceDraftImportSchema

        return PriceDraftImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productdrafts import PriceDraftImportSchema

        return PriceDraftImportSchema().dump(self)

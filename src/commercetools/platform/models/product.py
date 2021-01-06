# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .cart import ProductPublishScope
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .cart import ProductPublishScope
    from .category import CategoryReference, CategoryResourceIdentifier
    from .common import (
        Asset,
        AssetDraft,
        AssetSource,
        CreatedBy,
        DiscountedPrice,
        Image,
        LastModifiedBy,
        LocalizedString,
        Price,
        PriceDraft,
        ReferenceTypeId,
        ScopedPrice,
    )
    from .product_type import ProductTypeReference, ProductTypeResourceIdentifier
    from .review import ReviewRatingStatistics
    from .state import StateReference, StateResourceIdentifier
    from .tax_category import TaxCategoryReference, TaxCategoryResourceIdentifier
    from .type import FieldContainer, TypeResourceIdentifier

__all__ = [
    "Attribute",
    "CategoryOrderHints",
    "CustomTokenizer",
    "FacetResult",
    "FacetResultRange",
    "FacetResultTerm",
    "FacetResults",
    "FacetTypes",
    "FilteredFacetResult",
    "Product",
    "ProductAddAssetAction",
    "ProductAddExternalImageAction",
    "ProductAddPriceAction",
    "ProductAddToCategoryAction",
    "ProductAddVariantAction",
    "ProductCatalogData",
    "ProductChangeAssetNameAction",
    "ProductChangeAssetOrderAction",
    "ProductChangeMasterVariantAction",
    "ProductChangeNameAction",
    "ProductChangePriceAction",
    "ProductChangeSlugAction",
    "ProductData",
    "ProductDraft",
    "ProductLegacySetSkuAction",
    "ProductMoveImageToPositionAction",
    "ProductPagedQueryResponse",
    "ProductProjection",
    "ProductProjectionPagedQueryResponse",
    "ProductProjectionPagedSearchResponse",
    "ProductPublishAction",
    "ProductReference",
    "ProductRemoveAssetAction",
    "ProductRemoveFromCategoryAction",
    "ProductRemoveImageAction",
    "ProductRemovePriceAction",
    "ProductRemoveVariantAction",
    "ProductResourceIdentifier",
    "ProductRevertStagedChangesAction",
    "ProductRevertStagedVariantChangesAction",
    "ProductSetAssetCustomFieldAction",
    "ProductSetAssetCustomTypeAction",
    "ProductSetAssetDescriptionAction",
    "ProductSetAssetKeyAction",
    "ProductSetAssetSourcesAction",
    "ProductSetAssetTagsAction",
    "ProductSetAttributeAction",
    "ProductSetAttributeInAllVariantsAction",
    "ProductSetCategoryOrderHintAction",
    "ProductSetDescriptionAction",
    "ProductSetDiscountedPriceAction",
    "ProductSetImageLabelAction",
    "ProductSetKeyAction",
    "ProductSetMetaDescriptionAction",
    "ProductSetMetaKeywordsAction",
    "ProductSetMetaTitleAction",
    "ProductSetPricesAction",
    "ProductSetProductPriceCustomFieldAction",
    "ProductSetProductPriceCustomTypeAction",
    "ProductSetProductVariantKeyAction",
    "ProductSetSearchKeywordsAction",
    "ProductSetSkuAction",
    "ProductSetTaxCategoryAction",
    "ProductTransitionStateAction",
    "ProductUnpublishAction",
    "ProductUpdate",
    "ProductUpdateAction",
    "ProductVariant",
    "ProductVariantAvailability",
    "ProductVariantChannelAvailability",
    "ProductVariantChannelAvailabilityMap",
    "ProductVariantDraft",
    "RangeFacetResult",
    "SearchKeyword",
    "SearchKeywords",
    "SuggestTokenizer",
    "Suggestion",
    "SuggestionResult",
    "TermFacetResult",
    "TermFacetResultType",
    "WhitespaceTokenizer",
]


class Attribute(_BaseType):
    name: str
    #: A valid JSON value, based on an AttributeDefinition.
    value: typing.Any

    def __init__(self, *, name: str, value: typing.Any):
        self.name = name
        self.value = value
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Attribute":
        from ._schemas.product import AttributeSchema

        return AttributeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import AttributeSchema

        return AttributeSchema().dump(self)


class CategoryOrderHints(typing.Dict[str, str]):
    pass


class FacetResult(_BaseType):
    type: "FacetTypes"

    def __init__(self, *, type: "FacetTypes"):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "FacetResult":
        if data["type"] == "filter":
            from ._schemas.product import FilteredFacetResultSchema

            return FilteredFacetResultSchema().load(data)
        if data["type"] == "range":
            from ._schemas.product import RangeFacetResultSchema

            return RangeFacetResultSchema().load(data)
        if data["type"] == "terms":
            from ._schemas.product import TermFacetResultSchema

            return TermFacetResultSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import FacetResultSchema

        return FacetResultSchema().dump(self)


class FacetResultRange(_BaseType):
    from_: float
    from_str: str
    to: float
    to_str: str
    count: int
    product_count: typing.Optional[int]
    total: int
    min: float
    max: float
    mean: float

    def __init__(
        self,
        *,
        from_: float,
        from_str: str,
        to: float,
        to_str: str,
        count: int,
        product_count: typing.Optional[int] = None,
        total: int,
        min: float,
        max: float,
        mean: float
    ):
        self.from_ = from_
        self.from_str = from_str
        self.to = to
        self.to_str = to_str
        self.count = count
        self.product_count = product_count
        self.total = total
        self.min = min
        self.max = max
        self.mean = mean
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "FacetResultRange":
        from ._schemas.product import FacetResultRangeSchema

        return FacetResultRangeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import FacetResultRangeSchema

        return FacetResultRangeSchema().dump(self)


class FacetResultTerm(_BaseType):
    term: typing.Any
    count: int
    product_count: typing.Optional[int]

    def __init__(
        self,
        *,
        term: typing.Any,
        count: int,
        product_count: typing.Optional[int] = None
    ):
        self.term = term
        self.count = count
        self.product_count = product_count
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "FacetResultTerm":
        from ._schemas.product import FacetResultTermSchema

        return FacetResultTermSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import FacetResultTermSchema

        return FacetResultTermSchema().dump(self)


class FacetResults(typing.Dict[str, str]):
    pass


class FacetTypes(enum.Enum):
    TERMS = "terms"
    RANGE = "range"
    FILTER = "filter"


class FilteredFacetResult(FacetResult):
    count: int
    product_count: typing.Optional[int]

    def __init__(self, *, count: int, product_count: typing.Optional[int] = None):
        self.count = count
        self.product_count = product_count
        super().__init__(type=FacetTypes.FILTER)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "FilteredFacetResult":
        from ._schemas.product import FilteredFacetResultSchema

        return FilteredFacetResultSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import FilteredFacetResultSchema

        return FilteredFacetResultSchema().dump(self)


class Product(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    #: User-specific unique identifier for the product.
    #: *Product keys are different from product variant keys.*
    key: typing.Optional[str]
    product_type: "ProductTypeReference"
    #: The product data in the master catalog.
    master_data: "ProductCatalogData"
    tax_category: typing.Optional["TaxCategoryReference"]
    state: typing.Optional["StateReference"]
    #: Statistics about the review ratings taken into account for this product.
    review_rating_statistics: typing.Optional["ReviewRatingStatistics"]

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
        product_type: "ProductTypeReference",
        master_data: "ProductCatalogData",
        tax_category: typing.Optional["TaxCategoryReference"] = None,
        state: typing.Optional["StateReference"] = None,
        review_rating_statistics: typing.Optional["ReviewRatingStatistics"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.product_type = product_type
        self.master_data = master_data
        self.tax_category = tax_category
        self.state = state
        self.review_rating_statistics = review_rating_statistics
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Product":
        from ._schemas.product import ProductSchema

        return ProductSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSchema

        return ProductSchema().dump(self)


class ProductCatalogData(_BaseType):
    published: bool
    current: "ProductData"
    staged: "ProductData"
    has_staged_changes: bool

    def __init__(
        self,
        *,
        published: bool,
        current: "ProductData",
        staged: "ProductData",
        has_staged_changes: bool
    ):
        self.published = published
        self.current = current
        self.staged = staged
        self.has_staged_changes = has_staged_changes
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductCatalogData":
        from ._schemas.product import ProductCatalogDataSchema

        return ProductCatalogDataSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductCatalogDataSchema

        return ProductCatalogDataSchema().dump(self)


class ProductData(_BaseType):
    name: "LocalizedString"
    categories: typing.List["CategoryReference"]
    category_order_hints: typing.Optional["CategoryOrderHints"]
    description: typing.Optional["LocalizedString"]
    slug: "LocalizedString"
    meta_title: typing.Optional["LocalizedString"]
    meta_description: typing.Optional["LocalizedString"]
    meta_keywords: typing.Optional["LocalizedString"]
    master_variant: "ProductVariant"
    variants: typing.List["ProductVariant"]
    search_keywords: "SearchKeywords"

    def __init__(
        self,
        *,
        name: "LocalizedString",
        categories: typing.List["CategoryReference"],
        category_order_hints: typing.Optional["CategoryOrderHints"] = None,
        description: typing.Optional["LocalizedString"] = None,
        slug: "LocalizedString",
        meta_title: typing.Optional["LocalizedString"] = None,
        meta_description: typing.Optional["LocalizedString"] = None,
        meta_keywords: typing.Optional["LocalizedString"] = None,
        master_variant: "ProductVariant",
        variants: typing.List["ProductVariant"],
        search_keywords: "SearchKeywords"
    ):
        self.name = name
        self.categories = categories
        self.category_order_hints = category_order_hints
        self.description = description
        self.slug = slug
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords
        self.master_variant = master_variant
        self.variants = variants
        self.search_keywords = search_keywords
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductData":
        from ._schemas.product import ProductDataSchema

        return ProductDataSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductDataSchema

        return ProductDataSchema().dump(self)


class ProductDraft(_BaseType):
    #: A predefined product type assigned to the product.
    #: All products must have a product type.
    product_type: "ProductTypeResourceIdentifier"
    name: "LocalizedString"
    #: Human-readable identifiers usually used as deep-link URLs for the product.
    #: A slug must be unique across a project, but a product can have the same slug for different languages.
    #: Slugs have a maximum size of 256.
    #: Valid characters are: alphabetic characters (`A-Z, a-z`), numeric characters (`0-9`), underscores (`_`) and hyphens (`-`).
    slug: "LocalizedString"
    #: User-specific unique identifier for the product.
    key: typing.Optional[str]
    description: typing.Optional["LocalizedString"]
    #: Categories assigned to the product.
    categories: typing.Optional[typing.List["CategoryResourceIdentifier"]]
    category_order_hints: typing.Optional["CategoryOrderHints"]
    meta_title: typing.Optional["LocalizedString"]
    meta_description: typing.Optional["LocalizedString"]
    meta_keywords: typing.Optional["LocalizedString"]
    #: The master product variant.
    #: Required if the `variants` array has product variants.
    master_variant: typing.Optional["ProductVariantDraft"]
    #: An array of related product variants.
    variants: typing.Optional[typing.List["ProductVariantDraft"]]
    tax_category: typing.Optional["TaxCategoryResourceIdentifier"]
    search_keywords: typing.Optional["SearchKeywords"]
    state: typing.Optional["StateResourceIdentifier"]
    #: If `true`, the product is published immediately.
    publish: typing.Optional[bool]

    def __init__(
        self,
        *,
        product_type: "ProductTypeResourceIdentifier",
        name: "LocalizedString",
        slug: "LocalizedString",
        key: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None,
        categories: typing.Optional[typing.List["CategoryResourceIdentifier"]] = None,
        category_order_hints: typing.Optional["CategoryOrderHints"] = None,
        meta_title: typing.Optional["LocalizedString"] = None,
        meta_description: typing.Optional["LocalizedString"] = None,
        meta_keywords: typing.Optional["LocalizedString"] = None,
        master_variant: typing.Optional["ProductVariantDraft"] = None,
        variants: typing.Optional[typing.List["ProductVariantDraft"]] = None,
        tax_category: typing.Optional["TaxCategoryResourceIdentifier"] = None,
        search_keywords: typing.Optional["SearchKeywords"] = None,
        state: typing.Optional["StateResourceIdentifier"] = None,
        publish: typing.Optional[bool] = None
    ):
        self.product_type = product_type
        self.name = name
        self.slug = slug
        self.key = key
        self.description = description
        self.categories = categories
        self.category_order_hints = category_order_hints
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords
        self.master_variant = master_variant
        self.variants = variants
        self.tax_category = tax_category
        self.search_keywords = search_keywords
        self.state = state
        self.publish = publish
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductDraft":
        from ._schemas.product import ProductDraftSchema

        return ProductDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductDraftSchema

        return ProductDraftSchema().dump(self)


class ProductPagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["Product"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["Product"]
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
    ) -> "ProductPagedQueryResponse":
        from ._schemas.product import ProductPagedQueryResponseSchema

        return ProductPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductPagedQueryResponseSchema

        return ProductPagedQueryResponseSchema().dump(self)


class ProductProjection(BaseResource):
    #: User-specific unique identifier of the Product.
    key: typing.Optional[str]
    product_type: "ProductTypeReference"
    name: "LocalizedString"
    description: typing.Optional["LocalizedString"]
    slug: "LocalizedString"
    #: References to categories the product is in.
    categories: typing.List["CategoryReference"]
    category_order_hints: typing.Optional["CategoryOrderHints"]
    meta_title: typing.Optional["LocalizedString"]
    meta_description: typing.Optional["LocalizedString"]
    meta_keywords: typing.Optional["LocalizedString"]
    search_keywords: typing.Optional["SearchKeywords"]
    has_staged_changes: typing.Optional[bool]
    published: typing.Optional[bool]
    master_variant: "ProductVariant"
    variants: typing.List["ProductVariant"]
    tax_category: typing.Optional["TaxCategoryReference"]
    state: typing.Optional["StateReference"]
    #: Statistics about the review ratings taken into account for this product.
    review_rating_statistics: typing.Optional["ReviewRatingStatistics"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        key: typing.Optional[str] = None,
        product_type: "ProductTypeReference",
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        slug: "LocalizedString",
        categories: typing.List["CategoryReference"],
        category_order_hints: typing.Optional["CategoryOrderHints"] = None,
        meta_title: typing.Optional["LocalizedString"] = None,
        meta_description: typing.Optional["LocalizedString"] = None,
        meta_keywords: typing.Optional["LocalizedString"] = None,
        search_keywords: typing.Optional["SearchKeywords"] = None,
        has_staged_changes: typing.Optional[bool] = None,
        published: typing.Optional[bool] = None,
        master_variant: "ProductVariant",
        variants: typing.List["ProductVariant"],
        tax_category: typing.Optional["TaxCategoryReference"] = None,
        state: typing.Optional["StateReference"] = None,
        review_rating_statistics: typing.Optional["ReviewRatingStatistics"] = None
    ):
        self.key = key
        self.product_type = product_type
        self.name = name
        self.description = description
        self.slug = slug
        self.categories = categories
        self.category_order_hints = category_order_hints
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords
        self.search_keywords = search_keywords
        self.has_staged_changes = has_staged_changes
        self.published = published
        self.master_variant = master_variant
        self.variants = variants
        self.tax_category = tax_category
        self.state = state
        self.review_rating_statistics = review_rating_statistics
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductProjection":
        from ._schemas.product import ProductProjectionSchema

        return ProductProjectionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductProjectionSchema

        return ProductProjectionSchema().dump(self)


class ProductProjectionPagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["ProductProjection"]
    facets: typing.Optional["FacetResults"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["ProductProjection"],
        facets: typing.Optional["FacetResults"] = None
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        self.facets = facets
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductProjectionPagedQueryResponse":
        from ._schemas.product import ProductProjectionPagedQueryResponseSchema

        return ProductProjectionPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductProjectionPagedQueryResponseSchema

        return ProductProjectionPagedQueryResponseSchema().dump(self)


class ProductProjectionPagedSearchResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["ProductProjection"]
    facets: "FacetResults"

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["ProductProjection"],
        facets: "FacetResults"
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        self.facets = facets
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductProjectionPagedSearchResponse":
        from ._schemas.product import ProductProjectionPagedSearchResponseSchema

        return ProductProjectionPagedSearchResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductProjectionPagedSearchResponseSchema

        return ProductProjectionPagedSearchResponseSchema().dump(self)


class ProductReference(Reference):
    obj: typing.Optional["Product"]

    def __init__(self, *, id: str, obj: typing.Optional["Product"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.PRODUCT)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductReference":
        from ._schemas.product import ProductReferenceSchema

        return ProductReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductReferenceSchema

        return ProductReferenceSchema().dump(self)


class ProductResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.PRODUCT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductResourceIdentifier":
        from ._schemas.product import ProductResourceIdentifierSchema

        return ProductResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductResourceIdentifierSchema

        return ProductResourceIdentifierSchema().dump(self)


class ProductUpdate(_BaseType):
    version: int
    actions: typing.List["ProductUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["ProductUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductUpdate":
        from ._schemas.product import ProductUpdateSchema

        return ProductUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductUpdateSchema

        return ProductUpdateSchema().dump(self)


class ProductUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductUpdateAction":
        if data["action"] == "addAsset":
            from ._schemas.product import ProductAddAssetActionSchema

            return ProductAddAssetActionSchema().load(data)
        if data["action"] == "addExternalImage":
            from ._schemas.product import ProductAddExternalImageActionSchema

            return ProductAddExternalImageActionSchema().load(data)
        if data["action"] == "addPrice":
            from ._schemas.product import ProductAddPriceActionSchema

            return ProductAddPriceActionSchema().load(data)
        if data["action"] == "addToCategory":
            from ._schemas.product import ProductAddToCategoryActionSchema

            return ProductAddToCategoryActionSchema().load(data)
        if data["action"] == "addVariant":
            from ._schemas.product import ProductAddVariantActionSchema

            return ProductAddVariantActionSchema().load(data)
        if data["action"] == "changeAssetName":
            from ._schemas.product import ProductChangeAssetNameActionSchema

            return ProductChangeAssetNameActionSchema().load(data)
        if data["action"] == "changeAssetOrder":
            from ._schemas.product import ProductChangeAssetOrderActionSchema

            return ProductChangeAssetOrderActionSchema().load(data)
        if data["action"] == "changeMasterVariant":
            from ._schemas.product import ProductChangeMasterVariantActionSchema

            return ProductChangeMasterVariantActionSchema().load(data)
        if data["action"] == "changeName":
            from ._schemas.product import ProductChangeNameActionSchema

            return ProductChangeNameActionSchema().load(data)
        if data["action"] == "changePrice":
            from ._schemas.product import ProductChangePriceActionSchema

            return ProductChangePriceActionSchema().load(data)
        if data["action"] == "changeSlug":
            from ._schemas.product import ProductChangeSlugActionSchema

            return ProductChangeSlugActionSchema().load(data)
        if data["action"] == "legacySetSku":
            from ._schemas.product import ProductLegacySetSkuActionSchema

            return ProductLegacySetSkuActionSchema().load(data)
        if data["action"] == "moveImageToPosition":
            from ._schemas.product import ProductMoveImageToPositionActionSchema

            return ProductMoveImageToPositionActionSchema().load(data)
        if data["action"] == "publish":
            from ._schemas.product import ProductPublishActionSchema

            return ProductPublishActionSchema().load(data)
        if data["action"] == "removeAsset":
            from ._schemas.product import ProductRemoveAssetActionSchema

            return ProductRemoveAssetActionSchema().load(data)
        if data["action"] == "removeFromCategory":
            from ._schemas.product import ProductRemoveFromCategoryActionSchema

            return ProductRemoveFromCategoryActionSchema().load(data)
        if data["action"] == "removeImage":
            from ._schemas.product import ProductRemoveImageActionSchema

            return ProductRemoveImageActionSchema().load(data)
        if data["action"] == "removePrice":
            from ._schemas.product import ProductRemovePriceActionSchema

            return ProductRemovePriceActionSchema().load(data)
        if data["action"] == "removeVariant":
            from ._schemas.product import ProductRemoveVariantActionSchema

            return ProductRemoveVariantActionSchema().load(data)
        if data["action"] == "revertStagedChanges":
            from ._schemas.product import ProductRevertStagedChangesActionSchema

            return ProductRevertStagedChangesActionSchema().load(data)
        if data["action"] == "revertStagedVariantChanges":
            from ._schemas.product import ProductRevertStagedVariantChangesActionSchema

            return ProductRevertStagedVariantChangesActionSchema().load(data)
        if data["action"] == "setAssetCustomField":
            from ._schemas.product import ProductSetAssetCustomFieldActionSchema

            return ProductSetAssetCustomFieldActionSchema().load(data)
        if data["action"] == "setAssetCustomType":
            from ._schemas.product import ProductSetAssetCustomTypeActionSchema

            return ProductSetAssetCustomTypeActionSchema().load(data)
        if data["action"] == "setAssetDescription":
            from ._schemas.product import ProductSetAssetDescriptionActionSchema

            return ProductSetAssetDescriptionActionSchema().load(data)
        if data["action"] == "setAssetKey":
            from ._schemas.product import ProductSetAssetKeyActionSchema

            return ProductSetAssetKeyActionSchema().load(data)
        if data["action"] == "setAssetSources":
            from ._schemas.product import ProductSetAssetSourcesActionSchema

            return ProductSetAssetSourcesActionSchema().load(data)
        if data["action"] == "setAssetTags":
            from ._schemas.product import ProductSetAssetTagsActionSchema

            return ProductSetAssetTagsActionSchema().load(data)
        if data["action"] == "setAttribute":
            from ._schemas.product import ProductSetAttributeActionSchema

            return ProductSetAttributeActionSchema().load(data)
        if data["action"] == "setAttributeInAllVariants":
            from ._schemas.product import ProductSetAttributeInAllVariantsActionSchema

            return ProductSetAttributeInAllVariantsActionSchema().load(data)
        if data["action"] == "setCategoryOrderHint":
            from ._schemas.product import ProductSetCategoryOrderHintActionSchema

            return ProductSetCategoryOrderHintActionSchema().load(data)
        if data["action"] == "setDescription":
            from ._schemas.product import ProductSetDescriptionActionSchema

            return ProductSetDescriptionActionSchema().load(data)
        if data["action"] == "setDiscountedPrice":
            from ._schemas.product import ProductSetDiscountedPriceActionSchema

            return ProductSetDiscountedPriceActionSchema().load(data)
        if data["action"] == "setImageLabel":
            from ._schemas.product import ProductSetImageLabelActionSchema

            return ProductSetImageLabelActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.product import ProductSetKeyActionSchema

            return ProductSetKeyActionSchema().load(data)
        if data["action"] == "setMetaDescription":
            from ._schemas.product import ProductSetMetaDescriptionActionSchema

            return ProductSetMetaDescriptionActionSchema().load(data)
        if data["action"] == "setMetaKeywords":
            from ._schemas.product import ProductSetMetaKeywordsActionSchema

            return ProductSetMetaKeywordsActionSchema().load(data)
        if data["action"] == "setMetaTitle":
            from ._schemas.product import ProductSetMetaTitleActionSchema

            return ProductSetMetaTitleActionSchema().load(data)
        if data["action"] == "setPrices":
            from ._schemas.product import ProductSetPricesActionSchema

            return ProductSetPricesActionSchema().load(data)
        if data["action"] == "setProductPriceCustomField":
            from ._schemas.product import ProductSetProductPriceCustomFieldActionSchema

            return ProductSetProductPriceCustomFieldActionSchema().load(data)
        if data["action"] == "setProductPriceCustomType":
            from ._schemas.product import ProductSetProductPriceCustomTypeActionSchema

            return ProductSetProductPriceCustomTypeActionSchema().load(data)
        if data["action"] == "setProductVariantKey":
            from ._schemas.product import ProductSetProductVariantKeyActionSchema

            return ProductSetProductVariantKeyActionSchema().load(data)
        if data["action"] == "setSearchKeywords":
            from ._schemas.product import ProductSetSearchKeywordsActionSchema

            return ProductSetSearchKeywordsActionSchema().load(data)
        if data["action"] == "setSku":
            from ._schemas.product import ProductSetSkuActionSchema

            return ProductSetSkuActionSchema().load(data)
        if data["action"] == "setTaxCategory":
            from ._schemas.product import ProductSetTaxCategoryActionSchema

            return ProductSetTaxCategoryActionSchema().load(data)
        if data["action"] == "transitionState":
            from ._schemas.product import ProductTransitionStateActionSchema

            return ProductTransitionStateActionSchema().load(data)
        if data["action"] == "unpublish":
            from ._schemas.product import ProductUnpublishActionSchema

            return ProductUnpublishActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductUpdateActionSchema

        return ProductUpdateActionSchema().dump(self)


class ProductVariant(_BaseType):
    id: int
    sku: typing.Optional[str]
    key: typing.Optional[str]
    prices: typing.Optional[typing.List["Price"]]
    attributes: typing.Optional[typing.List["Attribute"]]
    price: typing.Optional["Price"]
    images: typing.Optional[typing.List["Image"]]
    assets: typing.Optional[typing.List["Asset"]]
    availability: typing.Optional["ProductVariantAvailability"]
    is_matching_variant: typing.Optional[bool]
    scoped_price: typing.Optional["ScopedPrice"]
    scoped_price_discounted: typing.Optional[bool]

    def __init__(
        self,
        *,
        id: int,
        sku: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        prices: typing.Optional[typing.List["Price"]] = None,
        attributes: typing.Optional[typing.List["Attribute"]] = None,
        price: typing.Optional["Price"] = None,
        images: typing.Optional[typing.List["Image"]] = None,
        assets: typing.Optional[typing.List["Asset"]] = None,
        availability: typing.Optional["ProductVariantAvailability"] = None,
        is_matching_variant: typing.Optional[bool] = None,
        scoped_price: typing.Optional["ScopedPrice"] = None,
        scoped_price_discounted: typing.Optional[bool] = None
    ):
        self.id = id
        self.sku = sku
        self.key = key
        self.prices = prices
        self.attributes = attributes
        self.price = price
        self.images = images
        self.assets = assets
        self.availability = availability
        self.is_matching_variant = is_matching_variant
        self.scoped_price = scoped_price
        self.scoped_price_discounted = scoped_price_discounted
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductVariant":
        from ._schemas.product import ProductVariantSchema

        return ProductVariantSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductVariantSchema

        return ProductVariantSchema().dump(self)


class ProductVariantAvailability(_BaseType):
    is_on_stock: typing.Optional[bool]
    restockable_in_days: typing.Optional[int]
    available_quantity: typing.Optional[int]
    channels: typing.Optional["ProductVariantChannelAvailabilityMap"]

    def __init__(
        self,
        *,
        is_on_stock: typing.Optional[bool] = None,
        restockable_in_days: typing.Optional[int] = None,
        available_quantity: typing.Optional[int] = None,
        channels: typing.Optional["ProductVariantChannelAvailabilityMap"] = None
    ):
        self.is_on_stock = is_on_stock
        self.restockable_in_days = restockable_in_days
        self.available_quantity = available_quantity
        self.channels = channels
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantAvailability":
        from ._schemas.product import ProductVariantAvailabilitySchema

        return ProductVariantAvailabilitySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductVariantAvailabilitySchema

        return ProductVariantAvailabilitySchema().dump(self)


class ProductVariantChannelAvailability(_BaseType):
    is_on_stock: typing.Optional[bool]
    restockable_in_days: typing.Optional[int]
    available_quantity: typing.Optional[int]

    def __init__(
        self,
        *,
        is_on_stock: typing.Optional[bool] = None,
        restockable_in_days: typing.Optional[int] = None,
        available_quantity: typing.Optional[int] = None
    ):
        self.is_on_stock = is_on_stock
        self.restockable_in_days = restockable_in_days
        self.available_quantity = available_quantity
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantChannelAvailability":
        from ._schemas.product import ProductVariantChannelAvailabilitySchema

        return ProductVariantChannelAvailabilitySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductVariantChannelAvailabilitySchema

        return ProductVariantChannelAvailabilitySchema().dump(self)


class ProductVariantChannelAvailabilityMap(typing.Dict[str, str]):
    pass


class ProductVariantDraft(_BaseType):
    sku: typing.Optional[str]
    key: typing.Optional[str]
    prices: typing.Optional[typing.List["PriceDraft"]]
    attributes: typing.Optional[typing.List["Attribute"]]
    images: typing.Optional[typing.List["Image"]]
    assets: typing.Optional[typing.List["AssetDraft"]]

    def __init__(
        self,
        *,
        sku: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        prices: typing.Optional[typing.List["PriceDraft"]] = None,
        attributes: typing.Optional[typing.List["Attribute"]] = None,
        images: typing.Optional[typing.List["Image"]] = None,
        assets: typing.Optional[typing.List["AssetDraft"]] = None
    ):
        self.sku = sku
        self.key = key
        self.prices = prices
        self.attributes = attributes
        self.images = images
        self.assets = assets
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductVariantDraft":
        from ._schemas.product import ProductVariantDraftSchema

        return ProductVariantDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductVariantDraftSchema

        return ProductVariantDraftSchema().dump(self)


class RangeFacetResult(FacetResult):
    ranges: typing.List["FacetResultRange"]

    def __init__(self, *, ranges: typing.List["FacetResultRange"]):
        self.ranges = ranges
        super().__init__(type=FacetTypes.RANGE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "RangeFacetResult":
        from ._schemas.product import RangeFacetResultSchema

        return RangeFacetResultSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import RangeFacetResultSchema

        return RangeFacetResultSchema().dump(self)


class SearchKeyword(_BaseType):
    text: str
    suggest_tokenizer: typing.Optional[
        typing.Union["SuggestTokenizer", "WhitespaceTokenizer", "CustomTokenizer"]
    ]

    def __init__(
        self,
        *,
        text: str,
        suggest_tokenizer: typing.Optional[
            typing.Union["SuggestTokenizer", "WhitespaceTokenizer", "CustomTokenizer"]
        ] = None
    ):
        self.text = text
        self.suggest_tokenizer = suggest_tokenizer
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchKeyword":
        from ._schemas.product import SearchKeywordSchema

        return SearchKeywordSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import SearchKeywordSchema

        return SearchKeywordSchema().dump(self)


class SearchKeywords(typing.Dict[str, str]):
    pass


class SuggestTokenizer(_BaseType):
    type: str

    def __init__(self, *, type: str):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SuggestTokenizer":
        if data["type"] == "custom":
            from ._schemas.product import CustomTokenizerSchema

            return CustomTokenizerSchema().load(data)
        if data["type"] == "whitespace":
            from ._schemas.product import WhitespaceTokenizerSchema

            return WhitespaceTokenizerSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import SuggestTokenizerSchema

        return SuggestTokenizerSchema().dump(self)


class CustomTokenizer(SuggestTokenizer):
    inputs: typing.List["str"]

    def __init__(self, *, inputs: typing.List["str"]):
        self.inputs = inputs
        super().__init__(type="custom")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomTokenizer":
        from ._schemas.product import CustomTokenizerSchema

        return CustomTokenizerSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import CustomTokenizerSchema

        return CustomTokenizerSchema().dump(self)


class Suggestion(_BaseType):
    #: The suggested text.
    text: str

    def __init__(self, *, text: str):
        self.text = text
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Suggestion":
        from ._schemas.product import SuggestionSchema

        return SuggestionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import SuggestionSchema

        return SuggestionSchema().dump(self)


class SuggestionResult(typing.Dict[str, str]):
    pass


class TermFacetResult(FacetResult):
    data_type: "TermFacetResultType"
    missing: int
    total: int
    other: int
    terms: typing.List["FacetResultTerm"]

    def __init__(
        self,
        *,
        data_type: "TermFacetResultType",
        missing: int,
        total: int,
        other: int,
        terms: typing.List["FacetResultTerm"]
    ):
        self.data_type = data_type
        self.missing = missing
        self.total = total
        self.other = other
        self.terms = terms
        super().__init__(type=FacetTypes.TERMS)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TermFacetResult":
        from ._schemas.product import TermFacetResultSchema

        return TermFacetResultSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import TermFacetResultSchema

        return TermFacetResultSchema().dump(self)


class TermFacetResultType(enum.Enum):
    TEXT = "text"
    DATE = "date"
    TIME = "time"
    DATETIME = "datetime"
    BOOLEAN = "boolean"
    NUMBER = "number"


class WhitespaceTokenizer(SuggestTokenizer):
    def __init__(self):

        super().__init__(type="whitespace")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "WhitespaceTokenizer":
        from ._schemas.product import WhitespaceTokenizerSchema

        return WhitespaceTokenizerSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import WhitespaceTokenizerSchema

        return WhitespaceTokenizerSchema().dump(self)


class ProductAddAssetAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    staged: typing.Optional[bool]
    asset: "AssetDraft"
    #: Position of the new asset inside the existing list (from `0` to the size of the list)
    position: typing.Optional[int]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None,
        asset: "AssetDraft",
        position: typing.Optional[int] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.staged = staged
        self.asset = asset
        self.position = position
        super().__init__(action="addAsset")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductAddAssetAction":
        from ._schemas.product import ProductAddAssetActionSchema

        return ProductAddAssetActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductAddAssetActionSchema

        return ProductAddAssetActionSchema().dump(self)


class ProductAddExternalImageAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    image: "Image"
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        image: "Image",
        staged: typing.Optional[bool] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.image = image
        self.staged = staged
        super().__init__(action="addExternalImage")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductAddExternalImageAction":
        from ._schemas.product import ProductAddExternalImageActionSchema

        return ProductAddExternalImageActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductAddExternalImageActionSchema

        return ProductAddExternalImageActionSchema().dump(self)


class ProductAddPriceAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    price: "PriceDraft"
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        price: "PriceDraft",
        staged: typing.Optional[bool] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.price = price
        self.staged = staged
        super().__init__(action="addPrice")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductAddPriceAction":
        from ._schemas.product import ProductAddPriceActionSchema

        return ProductAddPriceActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductAddPriceActionSchema

        return ProductAddPriceActionSchema().dump(self)


class ProductAddToCategoryAction(ProductUpdateAction):
    category: "CategoryResourceIdentifier"
    order_hint: typing.Optional[str]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        category: "CategoryResourceIdentifier",
        order_hint: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None
    ):
        self.category = category
        self.order_hint = order_hint
        self.staged = staged
        super().__init__(action="addToCategory")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductAddToCategoryAction":
        from ._schemas.product import ProductAddToCategoryActionSchema

        return ProductAddToCategoryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductAddToCategoryActionSchema

        return ProductAddToCategoryActionSchema().dump(self)


class ProductAddVariantAction(ProductUpdateAction):
    sku: typing.Optional[str]
    key: typing.Optional[str]
    prices: typing.Optional[typing.List["PriceDraft"]]
    images: typing.Optional[typing.List["Image"]]
    attributes: typing.Optional[typing.List["Attribute"]]
    staged: typing.Optional[bool]
    assets: typing.Optional[typing.List["Asset"]]

    def __init__(
        self,
        *,
        sku: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        prices: typing.Optional[typing.List["PriceDraft"]] = None,
        images: typing.Optional[typing.List["Image"]] = None,
        attributes: typing.Optional[typing.List["Attribute"]] = None,
        staged: typing.Optional[bool] = None,
        assets: typing.Optional[typing.List["Asset"]] = None
    ):
        self.sku = sku
        self.key = key
        self.prices = prices
        self.images = images
        self.attributes = attributes
        self.staged = staged
        self.assets = assets
        super().__init__(action="addVariant")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductAddVariantAction":
        from ._schemas.product import ProductAddVariantActionSchema

        return ProductAddVariantActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductAddVariantActionSchema

        return ProductAddVariantActionSchema().dump(self)


class ProductChangeAssetNameAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    staged: typing.Optional[bool]
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]
    name: "LocalizedString"

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        name: "LocalizedString"
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.staged = staged
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.name = name
        super().__init__(action="changeAssetName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductChangeAssetNameAction":
        from ._schemas.product import ProductChangeAssetNameActionSchema

        return ProductChangeAssetNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductChangeAssetNameActionSchema

        return ProductChangeAssetNameActionSchema().dump(self)


class ProductChangeAssetOrderAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    staged: typing.Optional[bool]
    asset_order: typing.List["str"]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None,
        asset_order: typing.List["str"]
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.staged = staged
        self.asset_order = asset_order
        super().__init__(action="changeAssetOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductChangeAssetOrderAction":
        from ._schemas.product import ProductChangeAssetOrderActionSchema

        return ProductChangeAssetOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductChangeAssetOrderActionSchema

        return ProductChangeAssetOrderActionSchema().dump(self)


class ProductChangeMasterVariantAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.staged = staged
        super().__init__(action="changeMasterVariant")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductChangeMasterVariantAction":
        from ._schemas.product import ProductChangeMasterVariantActionSchema

        return ProductChangeMasterVariantActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductChangeMasterVariantActionSchema

        return ProductChangeMasterVariantActionSchema().dump(self)


class ProductChangeNameAction(ProductUpdateAction):
    name: "LocalizedString"
    staged: typing.Optional[bool]

    def __init__(
        self, *, name: "LocalizedString", staged: typing.Optional[bool] = None
    ):
        self.name = name
        self.staged = staged
        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductChangeNameAction":
        from ._schemas.product import ProductChangeNameActionSchema

        return ProductChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductChangeNameActionSchema

        return ProductChangeNameActionSchema().dump(self)


class ProductChangePriceAction(ProductUpdateAction):
    #: ID of the [Price](#price)
    price_id: str
    price: "PriceDraft"
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        price_id: str,
        price: "PriceDraft",
        staged: typing.Optional[bool] = None
    ):
        self.price_id = price_id
        self.price = price
        self.staged = staged
        super().__init__(action="changePrice")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductChangePriceAction":
        from ._schemas.product import ProductChangePriceActionSchema

        return ProductChangePriceActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductChangePriceActionSchema

        return ProductChangePriceActionSchema().dump(self)


class ProductChangeSlugAction(ProductUpdateAction):
    #: Every slug must be unique across a project, but a product can have the same slug for different languages.
    #: Allowed are alphabetic, numeric, underscore (`_`) and hyphen (`-`) characters.
    #: Maximum size is `256`.
    slug: "LocalizedString"
    staged: typing.Optional[bool]

    def __init__(
        self, *, slug: "LocalizedString", staged: typing.Optional[bool] = None
    ):
        self.slug = slug
        self.staged = staged
        super().__init__(action="changeSlug")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductChangeSlugAction":
        from ._schemas.product import ProductChangeSlugActionSchema

        return ProductChangeSlugActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductChangeSlugActionSchema

        return ProductChangeSlugActionSchema().dump(self)


class ProductLegacySetSkuAction(ProductUpdateAction):
    sku: typing.Optional[str]
    variant_id: int

    def __init__(self, *, sku: typing.Optional[str] = None, variant_id: int):
        self.sku = sku
        self.variant_id = variant_id
        super().__init__(action="legacySetSku")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductLegacySetSkuAction":
        from ._schemas.product import ProductLegacySetSkuActionSchema

        return ProductLegacySetSkuActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductLegacySetSkuActionSchema

        return ProductLegacySetSkuActionSchema().dump(self)


class ProductMoveImageToPositionAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    #: The URL of the image
    image_url: str
    position: int
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        image_url: str,
        position: int,
        staged: typing.Optional[bool] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.image_url = image_url
        self.position = position
        self.staged = staged
        super().__init__(action="moveImageToPosition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductMoveImageToPositionAction":
        from ._schemas.product import ProductMoveImageToPositionActionSchema

        return ProductMoveImageToPositionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductMoveImageToPositionActionSchema

        return ProductMoveImageToPositionActionSchema().dump(self)


class ProductPublishAction(ProductUpdateAction):
    scope: typing.Optional["ProductPublishScope"]

    def __init__(self, *, scope: typing.Optional["ProductPublishScope"] = None):
        self.scope = scope
        super().__init__(action="publish")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductPublishAction":
        from ._schemas.product import ProductPublishActionSchema

        return ProductPublishActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductPublishActionSchema

        return ProductPublishActionSchema().dump(self)


class ProductRemoveAssetAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    staged: typing.Optional[bool]
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.staged = staged
        self.asset_id = asset_id
        self.asset_key = asset_key
        super().__init__(action="removeAsset")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductRemoveAssetAction":
        from ._schemas.product import ProductRemoveAssetActionSchema

        return ProductRemoveAssetActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductRemoveAssetActionSchema

        return ProductRemoveAssetActionSchema().dump(self)


class ProductRemoveFromCategoryAction(ProductUpdateAction):
    category: "CategoryResourceIdentifier"
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        category: "CategoryResourceIdentifier",
        staged: typing.Optional[bool] = None
    ):
        self.category = category
        self.staged = staged
        super().__init__(action="removeFromCategory")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductRemoveFromCategoryAction":
        from ._schemas.product import ProductRemoveFromCategoryActionSchema

        return ProductRemoveFromCategoryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductRemoveFromCategoryActionSchema

        return ProductRemoveFromCategoryActionSchema().dump(self)


class ProductRemoveImageAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    #: The URL of the image.
    image_url: str
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        image_url: str,
        staged: typing.Optional[bool] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.image_url = image_url
        self.staged = staged
        super().__init__(action="removeImage")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductRemoveImageAction":
        from ._schemas.product import ProductRemoveImageActionSchema

        return ProductRemoveImageActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductRemoveImageActionSchema

        return ProductRemoveImageActionSchema().dump(self)


class ProductRemovePriceAction(ProductUpdateAction):
    #: ID of the [Price](#price)
    price_id: str
    staged: typing.Optional[bool]

    def __init__(self, *, price_id: str, staged: typing.Optional[bool] = None):
        self.price_id = price_id
        self.staged = staged
        super().__init__(action="removePrice")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductRemovePriceAction":
        from ._schemas.product import ProductRemovePriceActionSchema

        return ProductRemovePriceActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductRemovePriceActionSchema

        return ProductRemovePriceActionSchema().dump(self)


class ProductRemoveVariantAction(ProductUpdateAction):
    id: typing.Optional[int]
    sku: typing.Optional[str]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None
    ):
        self.id = id
        self.sku = sku
        self.staged = staged
        super().__init__(action="removeVariant")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductRemoveVariantAction":
        from ._schemas.product import ProductRemoveVariantActionSchema

        return ProductRemoveVariantActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductRemoveVariantActionSchema

        return ProductRemoveVariantActionSchema().dump(self)


class ProductRevertStagedChangesAction(ProductUpdateAction):
    def __init__(self):

        super().__init__(action="revertStagedChanges")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductRevertStagedChangesAction":
        from ._schemas.product import ProductRevertStagedChangesActionSchema

        return ProductRevertStagedChangesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductRevertStagedChangesActionSchema

        return ProductRevertStagedChangesActionSchema().dump(self)


class ProductRevertStagedVariantChangesAction(ProductUpdateAction):
    variant_id: int

    def __init__(self, *, variant_id: int):
        self.variant_id = variant_id
        super().__init__(action="revertStagedVariantChanges")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductRevertStagedVariantChangesAction":
        from ._schemas.product import ProductRevertStagedVariantChangesActionSchema

        return ProductRevertStagedVariantChangesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductRevertStagedVariantChangesActionSchema

        return ProductRevertStagedVariantChangesActionSchema().dump(self)


class ProductSetAssetCustomFieldAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    staged: typing.Optional[bool]
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]
    name: str
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        name: str,
        value: typing.Optional[typing.Any] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.staged = staged
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.name = name
        self.value = value
        super().__init__(action="setAssetCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetAssetCustomFieldAction":
        from ._schemas.product import ProductSetAssetCustomFieldActionSchema

        return ProductSetAssetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetAssetCustomFieldActionSchema

        return ProductSetAssetCustomFieldActionSchema().dump(self)


class ProductSetAssetCustomTypeAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    staged: typing.Optional[bool]
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]
    #: If set, the custom type is set to this new value.
    #: If absent, the custom type and any existing custom fields are removed.
    type: typing.Optional["TypeResourceIdentifier"]
    #: If set, the custom fields are set to this new value.
    fields: typing.Optional[object]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional[object] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.staged = staged
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.type = type
        self.fields = fields
        super().__init__(action="setAssetCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetAssetCustomTypeAction":
        from ._schemas.product import ProductSetAssetCustomTypeActionSchema

        return ProductSetAssetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetAssetCustomTypeActionSchema

        return ProductSetAssetCustomTypeActionSchema().dump(self)


class ProductSetAssetDescriptionAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    staged: typing.Optional[bool]
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]
    description: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.staged = staged
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.description = description
        super().__init__(action="setAssetDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetAssetDescriptionAction":
        from ._schemas.product import ProductSetAssetDescriptionActionSchema

        return ProductSetAssetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetAssetDescriptionActionSchema

        return ProductSetAssetDescriptionActionSchema().dump(self)


class ProductSetAssetKeyAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    staged: typing.Optional[bool]
    asset_id: str
    #: User-defined identifier for the asset.
    #: If left blank or set to `null`, the asset key is unset/removed.
    asset_key: typing.Optional[str]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None,
        asset_id: str,
        asset_key: typing.Optional[str] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.staged = staged
        self.asset_id = asset_id
        self.asset_key = asset_key
        super().__init__(action="setAssetKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetAssetKeyAction":
        from ._schemas.product import ProductSetAssetKeyActionSchema

        return ProductSetAssetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetAssetKeyActionSchema

        return ProductSetAssetKeyActionSchema().dump(self)


class ProductSetAssetSourcesAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    staged: typing.Optional[bool]
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]
    sources: typing.List["AssetSource"]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        sources: typing.List["AssetSource"]
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.staged = staged
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.sources = sources
        super().__init__(action="setAssetSources")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetAssetSourcesAction":
        from ._schemas.product import ProductSetAssetSourcesActionSchema

        return ProductSetAssetSourcesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetAssetSourcesActionSchema

        return ProductSetAssetSourcesActionSchema().dump(self)


class ProductSetAssetTagsAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    staged: typing.Optional[bool]
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]
    tags: typing.Optional[typing.List["str"]]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        tags: typing.Optional[typing.List["str"]] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.staged = staged
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.tags = tags
        super().__init__(action="setAssetTags")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetAssetTagsAction":
        from ._schemas.product import ProductSetAssetTagsActionSchema

        return ProductSetAssetTagsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetAssetTagsActionSchema

        return ProductSetAssetTagsActionSchema().dump(self)


class ProductSetAttributeAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    name: str
    #: If the attribute exists and the value is omitted or set to `null`, the attribute is removed.
    #: If the attribute exists and a value is provided, the new value is applied.
    #: If the attribute does not exist and a value is provided, it is added as a new attribute.
    value: typing.Optional[typing.Any]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        name: str,
        value: typing.Optional[typing.Any] = None,
        staged: typing.Optional[bool] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.name = name
        self.value = value
        self.staged = staged
        super().__init__(action="setAttribute")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetAttributeAction":
        from ._schemas.product import ProductSetAttributeActionSchema

        return ProductSetAttributeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetAttributeActionSchema

        return ProductSetAttributeActionSchema().dump(self)


class ProductSetAttributeInAllVariantsAction(ProductUpdateAction):
    name: str
    #: The same update behavior as for Set Attribute applies.
    value: typing.Optional[typing.Any]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        name: str,
        value: typing.Optional[typing.Any] = None,
        staged: typing.Optional[bool] = None
    ):
        self.name = name
        self.value = value
        self.staged = staged
        super().__init__(action="setAttributeInAllVariants")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetAttributeInAllVariantsAction":
        from ._schemas.product import ProductSetAttributeInAllVariantsActionSchema

        return ProductSetAttributeInAllVariantsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetAttributeInAllVariantsActionSchema

        return ProductSetAttributeInAllVariantsActionSchema().dump(self)


class ProductSetCategoryOrderHintAction(ProductUpdateAction):
    category_id: str
    order_hint: typing.Optional[str]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        category_id: str,
        order_hint: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None
    ):
        self.category_id = category_id
        self.order_hint = order_hint
        self.staged = staged
        super().__init__(action="setCategoryOrderHint")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetCategoryOrderHintAction":
        from ._schemas.product import ProductSetCategoryOrderHintActionSchema

        return ProductSetCategoryOrderHintActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetCategoryOrderHintActionSchema

        return ProductSetCategoryOrderHintActionSchema().dump(self)


class ProductSetDescriptionAction(ProductUpdateAction):
    description: typing.Optional["LocalizedString"]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        description: typing.Optional["LocalizedString"] = None,
        staged: typing.Optional[bool] = None
    ):
        self.description = description
        self.staged = staged
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetDescriptionAction":
        from ._schemas.product import ProductSetDescriptionActionSchema

        return ProductSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetDescriptionActionSchema

        return ProductSetDescriptionActionSchema().dump(self)


class ProductSetDiscountedPriceAction(ProductUpdateAction):
    price_id: str
    staged: typing.Optional[bool]
    discounted: typing.Optional["DiscountedPrice"]

    def __init__(
        self,
        *,
        price_id: str,
        staged: typing.Optional[bool] = None,
        discounted: typing.Optional["DiscountedPrice"] = None
    ):
        self.price_id = price_id
        self.staged = staged
        self.discounted = discounted
        super().__init__(action="setDiscountedPrice")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetDiscountedPriceAction":
        from ._schemas.product import ProductSetDiscountedPriceActionSchema

        return ProductSetDiscountedPriceActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetDiscountedPriceActionSchema

        return ProductSetDiscountedPriceActionSchema().dump(self)


class ProductSetImageLabelAction(ProductUpdateAction):
    sku: typing.Optional[str]
    variant_id: typing.Optional[int]
    #: The URL of the image.
    image_url: str
    #: The new image label.
    #: If left blank or set to null, the label is removed.
    label: typing.Optional[str]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        sku: typing.Optional[str] = None,
        variant_id: typing.Optional[int] = None,
        image_url: str,
        label: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None
    ):
        self.sku = sku
        self.variant_id = variant_id
        self.image_url = image_url
        self.label = label
        self.staged = staged
        super().__init__(action="setImageLabel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetImageLabelAction":
        from ._schemas.product import ProductSetImageLabelActionSchema

        return ProductSetImageLabelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetImageLabelActionSchema

        return ProductSetImageLabelActionSchema().dump(self)


class ProductSetKeyAction(ProductUpdateAction):
    #: User-specific unique identifier for the product.
    #: If left blank or set to `null`, the product key is unset/removed.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductSetKeyAction":
        from ._schemas.product import ProductSetKeyActionSchema

        return ProductSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetKeyActionSchema

        return ProductSetKeyActionSchema().dump(self)


class ProductSetMetaDescriptionAction(ProductUpdateAction):
    meta_description: typing.Optional["LocalizedString"]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        meta_description: typing.Optional["LocalizedString"] = None,
        staged: typing.Optional[bool] = None
    ):
        self.meta_description = meta_description
        self.staged = staged
        super().__init__(action="setMetaDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetMetaDescriptionAction":
        from ._schemas.product import ProductSetMetaDescriptionActionSchema

        return ProductSetMetaDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetMetaDescriptionActionSchema

        return ProductSetMetaDescriptionActionSchema().dump(self)


class ProductSetMetaKeywordsAction(ProductUpdateAction):
    meta_keywords: typing.Optional["LocalizedString"]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        meta_keywords: typing.Optional["LocalizedString"] = None,
        staged: typing.Optional[bool] = None
    ):
        self.meta_keywords = meta_keywords
        self.staged = staged
        super().__init__(action="setMetaKeywords")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetMetaKeywordsAction":
        from ._schemas.product import ProductSetMetaKeywordsActionSchema

        return ProductSetMetaKeywordsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetMetaKeywordsActionSchema

        return ProductSetMetaKeywordsActionSchema().dump(self)


class ProductSetMetaTitleAction(ProductUpdateAction):
    meta_title: typing.Optional["LocalizedString"]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        meta_title: typing.Optional["LocalizedString"] = None,
        staged: typing.Optional[bool] = None
    ):
        self.meta_title = meta_title
        self.staged = staged
        super().__init__(action="setMetaTitle")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetMetaTitleAction":
        from ._schemas.product import ProductSetMetaTitleActionSchema

        return ProductSetMetaTitleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetMetaTitleActionSchema

        return ProductSetMetaTitleActionSchema().dump(self)


class ProductSetPricesAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    prices: typing.List["PriceDraft"]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        prices: typing.List["PriceDraft"],
        staged: typing.Optional[bool] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.prices = prices
        self.staged = staged
        super().__init__(action="setPrices")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetPricesAction":
        from ._schemas.product import ProductSetPricesActionSchema

        return ProductSetPricesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetPricesActionSchema

        return ProductSetPricesActionSchema().dump(self)


class ProductSetProductPriceCustomFieldAction(ProductUpdateAction):
    price_id: str
    staged: typing.Optional[bool]
    name: str
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        price_id: str,
        staged: typing.Optional[bool] = None,
        name: str,
        value: typing.Optional[typing.Any] = None
    ):
        self.price_id = price_id
        self.staged = staged
        self.name = name
        self.value = value
        super().__init__(action="setProductPriceCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetProductPriceCustomFieldAction":
        from ._schemas.product import ProductSetProductPriceCustomFieldActionSchema

        return ProductSetProductPriceCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetProductPriceCustomFieldActionSchema

        return ProductSetProductPriceCustomFieldActionSchema().dump(self)


class ProductSetProductPriceCustomTypeAction(ProductUpdateAction):
    price_id: str
    staged: typing.Optional[bool]
    type: typing.Optional["TypeResourceIdentifier"]
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        price_id: str,
        staged: typing.Optional[bool] = None,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.price_id = price_id
        self.staged = staged
        self.type = type
        self.fields = fields
        super().__init__(action="setProductPriceCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetProductPriceCustomTypeAction":
        from ._schemas.product import ProductSetProductPriceCustomTypeActionSchema

        return ProductSetProductPriceCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetProductPriceCustomTypeActionSchema

        return ProductSetProductPriceCustomTypeActionSchema().dump(self)


class ProductSetProductVariantKeyAction(ProductUpdateAction):
    variant_id: typing.Optional[int]
    sku: typing.Optional[str]
    #: If left blank or set to `null`, the key is unset/removed.
    key: typing.Optional[str]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        variant_id: typing.Optional[int] = None,
        sku: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.key = key
        self.staged = staged
        super().__init__(action="setProductVariantKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetProductVariantKeyAction":
        from ._schemas.product import ProductSetProductVariantKeyActionSchema

        return ProductSetProductVariantKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetProductVariantKeyActionSchema

        return ProductSetProductVariantKeyActionSchema().dump(self)


class ProductSetSearchKeywordsAction(ProductUpdateAction):
    search_keywords: "SearchKeywords"
    staged: typing.Optional[bool]

    def __init__(
        self, *, search_keywords: "SearchKeywords", staged: typing.Optional[bool] = None
    ):
        self.search_keywords = search_keywords
        self.staged = staged
        super().__init__(action="setSearchKeywords")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetSearchKeywordsAction":
        from ._schemas.product import ProductSetSearchKeywordsActionSchema

        return ProductSetSearchKeywordsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetSearchKeywordsActionSchema

        return ProductSetSearchKeywordsActionSchema().dump(self)


class ProductSetSkuAction(ProductUpdateAction):
    variant_id: int
    #: SKU must be unique.
    #: If left blank or set to `null`, the sku is unset/removed.
    sku: typing.Optional[str]
    staged: typing.Optional[bool]

    def __init__(
        self,
        *,
        variant_id: int,
        sku: typing.Optional[str] = None,
        staged: typing.Optional[bool] = None
    ):
        self.variant_id = variant_id
        self.sku = sku
        self.staged = staged
        super().__init__(action="setSku")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductSetSkuAction":
        from ._schemas.product import ProductSetSkuActionSchema

        return ProductSetSkuActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetSkuActionSchema

        return ProductSetSkuActionSchema().dump(self)


class ProductSetTaxCategoryAction(ProductUpdateAction):
    #: If left blank or set to `null`, the tax category is unset/removed.
    tax_category: typing.Optional["TaxCategoryResourceIdentifier"]

    def __init__(
        self, *, tax_category: typing.Optional["TaxCategoryResourceIdentifier"] = None
    ):
        self.tax_category = tax_category
        super().__init__(action="setTaxCategory")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSetTaxCategoryAction":
        from ._schemas.product import ProductSetTaxCategoryActionSchema

        return ProductSetTaxCategoryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductSetTaxCategoryActionSchema

        return ProductSetTaxCategoryActionSchema().dump(self)


class ProductTransitionStateAction(ProductUpdateAction):
    state: typing.Optional["StateResourceIdentifier"]
    force: typing.Optional[bool]

    def __init__(
        self,
        *,
        state: typing.Optional["StateResourceIdentifier"] = None,
        force: typing.Optional[bool] = None
    ):
        self.state = state
        self.force = force
        super().__init__(action="transitionState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTransitionStateAction":
        from ._schemas.product import ProductTransitionStateActionSchema

        return ProductTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductTransitionStateActionSchema

        return ProductTransitionStateActionSchema().dump(self)


class ProductUnpublishAction(ProductUpdateAction):
    def __init__(self):

        super().__init__(action="unpublish")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductUnpublishAction":
        from ._schemas.product import ProductUnpublishActionSchema

        return ProductUnpublishActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product import ProductUnpublishActionSchema

        return ProductUnpublishActionSchema().dump(self)

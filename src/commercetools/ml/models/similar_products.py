# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import TaskStatusEnum

if typing.TYPE_CHECKING:
    from .common import LocalizedString, Money, ProductReference, TaskStatusEnum

__all__ = [
    "ProductSetSelector",
    "SimilarProduct",
    "SimilarProductMeta",
    "SimilarProductPair",
    "SimilarProductSearchRequest",
    "SimilarProductSearchRequestMeta",
    "SimilarProductsPagedQueryResult",
    "SimilarProductsTaskStatus",
    "SimilarityMeasures",
]


class ProductSetSelector(_BaseType):
    """A set of ProductData for comparison. If no optional attributes are specified, all `current` ProductData are selected for comparison."""

    #: The project containing the project set.
    project_key: str
    #: An array of Product IDs to compare. If unspecified, no Product ID filter is applied.
    product_ids: typing.Optional[typing.List["str"]]
    #: An array of product type IDs. Only products with product types in this array are compared. If unspecified, no product type filter is applied.
    product_type_ids: typing.Optional[typing.List["str"]]
    #: Specifies use of staged or current product data.
    staged: typing.Optional[bool]
    #: Specifies use of product variants. If set to `true`, all product variants are compared, not just the master variant.
    include_variants: typing.Optional[bool]
    #: Maximum number of products to check (if unspecified, all products are considered). Note that the maximum number of product comparisons between two productSets is 20,000,000. This limit cannot be exceeded. If you need a higher limit, contact https://support.commercetools.com
    product_set_limit: typing.Optional[int]

    def __init__(
        self,
        *,
        project_key: str,
        product_ids: typing.Optional[typing.List["str"]] = None,
        product_type_ids: typing.Optional[typing.List["str"]] = None,
        staged: typing.Optional[bool] = None,
        include_variants: typing.Optional[bool] = None,
        product_set_limit: typing.Optional[int] = None
    ):
        self.project_key = project_key
        self.product_ids = product_ids
        self.product_type_ids = product_type_ids
        self.staged = staged
        self.include_variants = include_variants
        self.product_set_limit = product_set_limit
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductSetSelector":
        from ._schemas.similar_products import ProductSetSelectorSchema

        return ProductSetSelectorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.similar_products import ProductSetSelectorSchema

        return ProductSetSelectorSchema().dump(self)


class SimilarityMeasures(_BaseType):
    """Specify which ProductData attributes to use for estimating similarity and how to weigh them. An attribute's weight can be any whole positive integer, starting with 0. The larger the integer, the higher its weight."""

    #: Importance of the `name` attribute in overall similarity.
    name: typing.Optional[int]
    #: Importance of the `description` attribute in overall similarity.
    description: typing.Optional[int]
    #: Importance of the `description` attribute in overall similarity.
    attribute: typing.Optional[int]
    #: Importance of the number of product variants in overall similarity.
    variant_count: typing.Optional[int]
    #: Importance of the `price` attribute in overall similarity.
    price: typing.Optional[int]

    def __init__(
        self,
        *,
        name: typing.Optional[int] = None,
        description: typing.Optional[int] = None,
        attribute: typing.Optional[int] = None,
        variant_count: typing.Optional[int] = None,
        price: typing.Optional[int] = None
    ):
        self.name = name
        self.description = description
        self.attribute = attribute
        self.variant_count = variant_count
        self.price = price
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SimilarityMeasures":
        from ._schemas.similar_products import SimilarityMeasuresSchema

        return SimilarityMeasuresSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.similar_products import SimilarityMeasuresSchema

        return SimilarityMeasuresSchema().dump(self)


class SimilarProductSearchRequest(_BaseType):
    limit: typing.Optional[int]
    offset: typing.Optional[int]
    #: language tag used to prioritize language for text comparisons.
    language: typing.Optional[str]
    #: The three-digit  currency code to compare prices in. When a product has multiple prices, all prices for the product are converted to the currency provided by the currency attribute and the median price is calculated for comparison. Currencies are converted using the ECB currency exchange rates at the time the request is made. Of the currency codes, only currencies with currency exchange rates provided by the ECB are supported.
    currency_code: typing.Optional[str]
    #: `similarityMeasures` defines the attributes taken into account to measure product similarity.
    similarity_measures: typing.Optional["SimilarityMeasures"]
    #: Array of length 2 of ProductSetSelector
    product_set_selectors: typing.Optional[typing.List["ProductSetSelector"]]
    confidence_min: typing.Optional[float]
    confidence_max: typing.Optional[float]

    def __init__(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        language: typing.Optional[str] = None,
        currency_code: typing.Optional[str] = None,
        similarity_measures: typing.Optional["SimilarityMeasures"] = None,
        product_set_selectors: typing.Optional[
            typing.List["ProductSetSelector"]
        ] = None,
        confidence_min: typing.Optional[float] = None,
        confidence_max: typing.Optional[float] = None
    ):
        self.limit = limit
        self.offset = offset
        self.language = language
        self.currency_code = currency_code
        self.similarity_measures = similarity_measures
        self.product_set_selectors = product_set_selectors
        self.confidence_min = confidence_min
        self.confidence_max = confidence_max
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SimilarProductSearchRequest":
        from ._schemas.similar_products import SimilarProductSearchRequestSchema

        return SimilarProductSearchRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.similar_products import SimilarProductSearchRequestSchema

        return SimilarProductSearchRequestSchema().dump(self)


class SimilarProduct(_BaseType):
    """One part of a SimilarProductPair. Refers to a specific ProductVariant."""

    #: Reference to Product
    product: typing.Optional["ProductReference"]
    #: ID of the ProductVariant that was compared.
    variant_id: typing.Optional[int]
    #: Supplementary information about the data used for similarity estimation. This information helps you understand the estimated confidence score, but it should not be used to identify a product.
    meta: typing.Optional["SimilarProductMeta"]

    def __init__(
        self,
        *,
        product: typing.Optional["ProductReference"] = None,
        variant_id: typing.Optional[int] = None,
        meta: typing.Optional["SimilarProductMeta"] = None
    ):
        self.product = product
        self.variant_id = variant_id
        self.meta = meta
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SimilarProduct":
        from ._schemas.similar_products import SimilarProductSchema

        return SimilarProductSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.similar_products import SimilarProductSchema

        return SimilarProductSchema().dump(self)


class SimilarProductMeta(_BaseType):
    #: Localized product name used for similarity estimation.
    name: typing.Optional["LocalizedString"]
    #: Localized product description used for similarity estimation.
    description: typing.Optional["LocalizedString"]
    #: The product price in cents using the currency defined in SimilarProductSearchRequest If multiple prices exist, the median value is taken as a representative amount.
    price: typing.Optional["Money"]
    #: Total number of variants associated with the product.
    variant_count: typing.Optional[int]

    def __init__(
        self,
        *,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        price: typing.Optional["Money"] = None,
        variant_count: typing.Optional[int] = None
    ):
        self.name = name
        self.description = description
        self.price = price
        self.variant_count = variant_count
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SimilarProductMeta":
        from ._schemas.similar_products import SimilarProductMetaSchema

        return SimilarProductMetaSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.similar_products import SimilarProductMetaSchema

        return SimilarProductMetaSchema().dump(self)


class SimilarProductPair(_BaseType):
    """A pair of SimilarProducts"""

    #: The probability of product similarity.
    confidence: float
    products: typing.List["SimilarProduct"]

    def __init__(self, *, confidence: float, products: typing.List["SimilarProduct"]):
        self.confidence = confidence
        self.products = products
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SimilarProductPair":
        from ._schemas.similar_products import SimilarProductPairSchema

        return SimilarProductPairSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.similar_products import SimilarProductPairSchema

        return SimilarProductPairSchema().dump(self)


class SimilarProductSearchRequestMeta(_BaseType):
    #: The SimilarityMeasures used in this search.
    similarity_measures: "SimilarityMeasures"

    def __init__(self, *, similarity_measures: "SimilarityMeasures"):
        self.similarity_measures = similarity_measures
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SimilarProductSearchRequestMeta":
        from ._schemas.similar_products import SimilarProductSearchRequestMetaSchema

        return SimilarProductSearchRequestMetaSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.similar_products import SimilarProductSearchRequestMetaSchema

        return SimilarProductSearchRequestMetaSchema().dump(self)


class SimilarProductsPagedQueryResult(_BaseType):
    count: int
    total: int
    offset: int
    results: typing.List["SimilarProductPair"]
    meta: "SimilarProductSearchRequestMeta"

    def __init__(
        self,
        *,
        count: int,
        total: int,
        offset: int,
        results: typing.List["SimilarProductPair"],
        meta: "SimilarProductSearchRequestMeta"
    ):
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        self.meta = meta
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SimilarProductsPagedQueryResult":
        from ._schemas.similar_products import SimilarProductsPagedQueryResultSchema

        return SimilarProductsPagedQueryResultSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.similar_products import SimilarProductsPagedQueryResultSchema

        return SimilarProductsPagedQueryResultSchema().dump(self)


class SimilarProductsTaskStatus(_BaseType):
    """Represents a URL path to poll to get the results of an Asynchronous Request."""

    state: "TaskStatusEnum"
    #: The expiry date of the result. You cannot access the result after the expiry date. Default: 1 day after the result first becomes available. This is only available when the TaskStatus state is SUCCESS.
    expires: typing.Optional[datetime.datetime]
    #: The response to an asynchronous request. The type depends on the request initiated. Only populated when the status is `SUCCESS`.
    result: "SimilarProductsPagedQueryResult"

    def __init__(
        self,
        *,
        state: "TaskStatusEnum",
        expires: typing.Optional[datetime.datetime] = None,
        result: "SimilarProductsPagedQueryResult"
    ):
        self.state = state
        self.expires = expires
        self.result = result
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SimilarProductsTaskStatus":
        from ._schemas.similar_products import SimilarProductsTaskStatusSchema

        return SimilarProductsTaskStatusSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.similar_products import SimilarProductsTaskStatusSchema

        return SimilarProductsTaskStatusSchema().dump(self)

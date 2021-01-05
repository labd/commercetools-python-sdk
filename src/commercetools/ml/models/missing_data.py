# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import TaskStatusEnum

if typing.TYPE_CHECKING:
    from .common import ProductReference, ProductTypeReference, TaskStatusEnum

__all__ = [
    "AttributeCount",
    "AttributeCoverage",
    "MissingAttributes",
    "MissingAttributesDetails",
    "MissingAttributesMeta",
    "MissingAttributesPagedQueryResult",
    "MissingAttributesSearchRequest",
    "MissingDataTaskStatus",
    "MissingImages",
    "MissingImagesCount",
    "MissingImagesMeta",
    "MissingImagesPagedQueryResult",
    "MissingImagesProductLevel",
    "MissingImagesSearchRequest",
    "MissingImagesTaskStatus",
    "MissingImagesVariantLevel",
    "MissingPrices",
    "MissingPricesMeta",
    "MissingPricesPagedQueryResult",
    "MissingPricesProductCount",
    "MissingPricesProductLevel",
    "MissingPricesSearchRequest",
    "MissingPricesTaskStatus",
    "MissingPricesVariantLevel",
]


class AttributeCount(_BaseType):
    #: Number of attributes defined in the product type.
    product_type_attributes: int
    #: Number of attributes defined in the variant.
    variant_attributes: int
    #: Number of attributes missing values in the variant.
    missing_attribute_values: int

    def __init__(
        self,
        *,
        product_type_attributes: int,
        variant_attributes: int,
        missing_attribute_values: int
    ):
        self.product_type_attributes = product_type_attributes
        self.variant_attributes = variant_attributes
        self.missing_attribute_values = missing_attribute_values
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeCount":
        from ._schemas.missing_data import AttributeCountSchema

        return AttributeCountSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import AttributeCountSchema

        return AttributeCountSchema().dump(self)


class AttributeCoverage(_BaseType):
    #: The percentage of attributes from the product type defined in the product variant. A value of `1.0` indicates a product variant contains all attributes defined in the product type.
    names: float
    #: Represents the percentage of attributes in the product variant that contain values.
    values: float

    def __init__(self, *, names: float, values: float):
        self.names = names
        self.values = values
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeCoverage":
        from ._schemas.missing_data import AttributeCoverageSchema

        return AttributeCoverageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import AttributeCoverageSchema

        return AttributeCoverageSchema().dump(self)


class MissingAttributesDetails(_BaseType):
    #: Number of products scanned.
    total: int
    #: Number of products missing attribute names.
    missing_attribute_names: int
    #: Number of products missing attribute values.
    missing_attribute_values: int

    def __init__(
        self, *, total: int, missing_attribute_names: int, missing_attribute_values: int
    ):
        self.total = total
        self.missing_attribute_names = missing_attribute_names
        self.missing_attribute_values = missing_attribute_values
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingAttributesDetails":
        from ._schemas.missing_data import MissingAttributesDetailsSchema

        return MissingAttributesDetailsSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingAttributesDetailsSchema

        return MissingAttributesDetailsSchema().dump(self)


class MissingAttributes(_BaseType):
    product: "ProductReference"
    product_type: "ProductTypeReference"
    #: ID of a ProductVariant.
    variant_id: int
    #: The names of the attributes of the product type that the variant is missing, sorted by attribute importance in descending order.
    missing_attribute_values: typing.List["str"]
    #: The names of the attributes of the product type that the variant is missing, sorted by attribute importance in descending order.
    missing_attribute_names: typing.Optional[typing.List["str"]]
    attribute_count: typing.Optional["AttributeCount"]
    attribute_coverage: typing.Optional["AttributeCoverage"]

    def __init__(
        self,
        *,
        product: "ProductReference",
        product_type: "ProductTypeReference",
        variant_id: int,
        missing_attribute_values: typing.List["str"],
        missing_attribute_names: typing.Optional[typing.List["str"]] = None,
        attribute_count: typing.Optional["AttributeCount"] = None,
        attribute_coverage: typing.Optional["AttributeCoverage"] = None
    ):
        self.product = product
        self.product_type = product_type
        self.variant_id = variant_id
        self.missing_attribute_values = missing_attribute_values
        self.missing_attribute_names = missing_attribute_names
        self.attribute_count = attribute_count
        self.attribute_coverage = attribute_coverage
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MissingAttributes":
        from ._schemas.missing_data import MissingAttributesSchema

        return MissingAttributesSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingAttributesSchema

        return MissingAttributesSchema().dump(self)


class MissingAttributesMeta(_BaseType):
    product_level: "MissingAttributesDetails"
    variant_level: "MissingAttributesDetails"
    #: The IDs of the product types containing the requested `attributeName`.
    product_type_ids: typing.Optional[typing.List["str"]]

    def __init__(
        self,
        *,
        product_level: "MissingAttributesDetails",
        variant_level: "MissingAttributesDetails",
        product_type_ids: typing.Optional[typing.List["str"]] = None
    ):
        self.product_level = product_level
        self.variant_level = variant_level
        self.product_type_ids = product_type_ids
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MissingAttributesMeta":
        from ._schemas.missing_data import MissingAttributesMetaSchema

        return MissingAttributesMetaSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingAttributesMetaSchema

        return MissingAttributesMetaSchema().dump(self)


class MissingAttributesSearchRequest(_BaseType):
    limit: typing.Optional[int]
    offset: typing.Optional[int]
    #: If true, searches data from staged products in addition to published products.
    staged: typing.Optional[bool]
    #: Maximum number of products to scan.
    product_set_limit: typing.Optional[int]
    #: If true, searches all product variants. If false, only searches master variants.
    include_variants: typing.Optional[bool]
    #: Minimum attribute coverage of variants to display, applied to both coverage types.
    coverage_min: typing.Optional[float]
    #: Maximum attribute coverage of variants to display, applied to both coverage types.
    coverage_max: typing.Optional[float]
    #: Default value: `coverageAttributeValues` - Allowed values: [`coverageAttributeValues`, `coverageAttributeNames`]
    #: `coverageAttributeValues` shows the product variants with the most missing attribute values first and `coverageAttributeNames` the ones with the most missing attribute names.
    sort_by: typing.Optional[str]
    #: If true, the `missingAttributeNames` will be included in the results.
    show_missing_attribute_names: typing.Optional[bool]
    #: Filters results by the provided Product IDs.
    #: Cannot be applied in combination with any other filter.
    product_ids: typing.Optional[typing.List["str"]]
    #: Filters results by the provided product type IDs.
    #: Cannot be applied in combination with any other filter.
    product_type_ids: typing.Optional[typing.List["str"]]
    #: Filters results by the provided attribute name. If provided,  products are only checked for this attribute. Therefore, only products of product types which define the attribute name are considered. These product type IDs
    #: are then listed in `MissingAttributesMeta`. The  `attributeCount` and `attributeCoverage` fields are not part of the response when using this filter. Cannot be applied in combination with any other filter.
    attribute_name: typing.Optional[str]

    def __init__(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        staged: typing.Optional[bool] = None,
        product_set_limit: typing.Optional[int] = None,
        include_variants: typing.Optional[bool] = None,
        coverage_min: typing.Optional[float] = None,
        coverage_max: typing.Optional[float] = None,
        sort_by: typing.Optional[str] = None,
        show_missing_attribute_names: typing.Optional[bool] = None,
        product_ids: typing.Optional[typing.List["str"]] = None,
        product_type_ids: typing.Optional[typing.List["str"]] = None,
        attribute_name: typing.Optional[str] = None
    ):
        self.limit = limit
        self.offset = offset
        self.staged = staged
        self.product_set_limit = product_set_limit
        self.include_variants = include_variants
        self.coverage_min = coverage_min
        self.coverage_max = coverage_max
        self.sort_by = sort_by
        self.show_missing_attribute_names = show_missing_attribute_names
        self.product_ids = product_ids
        self.product_type_ids = product_type_ids
        self.attribute_name = attribute_name
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingAttributesSearchRequest":
        from ._schemas.missing_data import MissingAttributesSearchRequestSchema

        return MissingAttributesSearchRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingAttributesSearchRequestSchema

        return MissingAttributesSearchRequestSchema().dump(self)


class MissingAttributesPagedQueryResult(_BaseType):
    count: int
    total: int
    offset: int
    results: typing.List["MissingAttributes"]
    meta: "MissingAttributesMeta"

    def __init__(
        self,
        *,
        count: int,
        total: int,
        offset: int,
        results: typing.List["MissingAttributes"],
        meta: "MissingAttributesMeta"
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
    ) -> "MissingAttributesPagedQueryResult":
        from ._schemas.missing_data import MissingAttributesPagedQueryResultSchema

        return MissingAttributesPagedQueryResultSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingAttributesPagedQueryResultSchema

        return MissingAttributesPagedQueryResultSchema().dump(self)


class MissingDataTaskStatus(_BaseType):
    """Represents a URL path to poll to get the results of an Asynchronous Request."""

    state: "TaskStatusEnum"
    #: The expiry date of the result. You cannot access the result after the expiry date. Default: 1 day after the result first becomes available. This is only available when the TaskStatus state is SUCCESS.
    expires: datetime.datetime
    #: The response to an asynchronous request. The type depends on the request initiated. Only populated when the status is `SUCCESS`.
    result: "MissingAttributesPagedQueryResult"

    def __init__(
        self,
        *,
        state: "TaskStatusEnum",
        expires: datetime.datetime,
        result: "MissingAttributesPagedQueryResult"
    ):
        self.state = state
        self.expires = expires
        self.result = result
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MissingDataTaskStatus":
        from ._schemas.missing_data import MissingDataTaskStatusSchema

        return MissingDataTaskStatusSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingDataTaskStatusSchema

        return MissingDataTaskStatusSchema().dump(self)


class MissingImages(_BaseType):
    product: "ProductReference"
    #: ID of the variant
    variant_id: int
    #: Number of images the variant contains.
    image_count: int

    def __init__(
        self, *, product: "ProductReference", variant_id: int, image_count: int
    ):
        self.product = product
        self.variant_id = variant_id
        self.image_count = image_count
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MissingImages":
        from ._schemas.missing_data import MissingImagesSchema

        return MissingImagesSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingImagesSchema

        return MissingImagesSchema().dump(self)


class MissingImagesCount(_BaseType):
    missing_images: int
    #: Number of products scanned.
    total: int

    def __init__(self, *, missing_images: int, total: int):
        self.missing_images = missing_images
        self.total = total
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MissingImagesCount":
        from ._schemas.missing_data import MissingImagesCountSchema

        return MissingImagesCountSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingImagesCountSchema

        return MissingImagesCountSchema().dump(self)


class MissingImagesProductLevel(MissingImagesCount):
    def __init__(self, *, missing_images: int, total: int):

        super().__init__(missing_images=missing_images, total=total)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingImagesProductLevel":
        from ._schemas.missing_data import MissingImagesProductLevelSchema

        return MissingImagesProductLevelSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingImagesProductLevelSchema

        return MissingImagesProductLevelSchema().dump(self)


class MissingImagesVariantLevel(MissingImagesCount):
    def __init__(self, *, missing_images: int, total: int):

        super().__init__(missing_images=missing_images, total=total)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingImagesVariantLevel":
        from ._schemas.missing_data import MissingImagesVariantLevelSchema

        return MissingImagesVariantLevelSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingImagesVariantLevelSchema

        return MissingImagesVariantLevelSchema().dump(self)


class MissingImagesMeta(_BaseType):
    product_level: "MissingImagesProductLevel"
    variant_level: "MissingImagesVariantLevel"
    #: The minimum number of images a product variant must have. Anything below this value is considered a product variant with missing images.
    threshold: int

    def __init__(
        self,
        *,
        product_level: "MissingImagesProductLevel",
        variant_level: "MissingImagesVariantLevel",
        threshold: int
    ):
        self.product_level = product_level
        self.variant_level = variant_level
        self.threshold = threshold
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MissingImagesMeta":
        from ._schemas.missing_data import MissingImagesMetaSchema

        return MissingImagesMetaSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingImagesMetaSchema

        return MissingImagesMetaSchema().dump(self)


class MissingImagesSearchRequest(_BaseType):
    limit: typing.Optional[int]
    offset: typing.Optional[int]
    #: If true, searches data from staged products in addition to published products.
    staged: typing.Optional[bool]
    #: Maximum number of products to scan.
    product_set_limit: typing.Optional[int]
    #: If true, searches all product variants. If false, only searches master variants.
    include_variants: typing.Optional[bool]
    #: If true, uses the median number of images per product variant as a threshold value.
    auto_threshold: typing.Optional[bool]
    #: The minimum number of images a product variant must have. Anything below this value is considered a product variant with missing images.
    threshold: typing.Optional[int]
    #: Filters results by the provided Product IDs. Cannot be applied in combination with any other filter.
    product_ids: typing.Optional[typing.List["str"]]
    #: Filters results by the provided product type IDs. It cannot be applied in combination with any other filter.
    product_type_ids: typing.Optional[typing.List["str"]]

    def __init__(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        staged: typing.Optional[bool] = None,
        product_set_limit: typing.Optional[int] = None,
        include_variants: typing.Optional[bool] = None,
        auto_threshold: typing.Optional[bool] = None,
        threshold: typing.Optional[int] = None,
        product_ids: typing.Optional[typing.List["str"]] = None,
        product_type_ids: typing.Optional[typing.List["str"]] = None
    ):
        self.limit = limit
        self.offset = offset
        self.staged = staged
        self.product_set_limit = product_set_limit
        self.include_variants = include_variants
        self.auto_threshold = auto_threshold
        self.threshold = threshold
        self.product_ids = product_ids
        self.product_type_ids = product_type_ids
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingImagesSearchRequest":
        from ._schemas.missing_data import MissingImagesSearchRequestSchema

        return MissingImagesSearchRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingImagesSearchRequestSchema

        return MissingImagesSearchRequestSchema().dump(self)


class MissingImagesPagedQueryResult(_BaseType):
    count: int
    total: int
    offset: int
    results: typing.List["MissingImages"]
    meta: "MissingImagesMeta"

    def __init__(
        self,
        *,
        count: int,
        total: int,
        offset: int,
        results: typing.List["MissingImages"],
        meta: "MissingImagesMeta"
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
    ) -> "MissingImagesPagedQueryResult":
        from ._schemas.missing_data import MissingImagesPagedQueryResultSchema

        return MissingImagesPagedQueryResultSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingImagesPagedQueryResultSchema

        return MissingImagesPagedQueryResultSchema().dump(self)


class MissingImagesTaskStatus(_BaseType):
    """Represents a URL path to poll to get the results of an Asynchronous Request."""

    state: "TaskStatusEnum"
    #: The expiry date of the result. You cannot access the result after the expiry date. Default: 1 day after the result first becomes available. This is only available when the TaskStatus state is SUCCESS.
    expires: datetime.datetime
    #: The response to an asynchronous request. The type depends on the request initiated. Only populated when the status is `SUCCESS`.
    result: "MissingImagesPagedQueryResult"

    def __init__(
        self,
        *,
        state: "TaskStatusEnum",
        expires: datetime.datetime,
        result: "MissingImagesPagedQueryResult"
    ):
        self.state = state
        self.expires = expires
        self.result = result
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingImagesTaskStatus":
        from ._schemas.missing_data import MissingImagesTaskStatusSchema

        return MissingImagesTaskStatusSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingImagesTaskStatusSchema

        return MissingImagesTaskStatusSchema().dump(self)


class MissingPrices(_BaseType):
    product: "ProductReference"
    #: Id of the `ProductVariant`.
    variant_id: int

    def __init__(self, *, product: "ProductReference", variant_id: int):
        self.product = product
        self.variant_id = variant_id
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MissingPrices":
        from ._schemas.missing_data import MissingPricesSchema

        return MissingPricesSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingPricesSchema

        return MissingPricesSchema().dump(self)


class MissingPricesProductCount(_BaseType):
    total: int
    missing_prices: int

    def __init__(self, *, total: int, missing_prices: int):
        self.total = total
        self.missing_prices = missing_prices
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingPricesProductCount":
        from ._schemas.missing_data import MissingPricesProductCountSchema

        return MissingPricesProductCountSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingPricesProductCountSchema

        return MissingPricesProductCountSchema().dump(self)


class MissingPricesProductLevel(MissingPricesProductCount):
    def __init__(self, *, total: int, missing_prices: int):

        super().__init__(total=total, missing_prices=missing_prices)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingPricesProductLevel":
        from ._schemas.missing_data import MissingPricesProductLevelSchema

        return MissingPricesProductLevelSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingPricesProductLevelSchema

        return MissingPricesProductLevelSchema().dump(self)


class MissingPricesVariantLevel(MissingPricesProductCount):
    def __init__(self, *, total: int, missing_prices: int):

        super().__init__(total=total, missing_prices=missing_prices)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingPricesVariantLevel":
        from ._schemas.missing_data import MissingPricesVariantLevelSchema

        return MissingPricesVariantLevelSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingPricesVariantLevelSchema

        return MissingPricesVariantLevelSchema().dump(self)


class MissingPricesMeta(_BaseType):
    product_level: "MissingPricesProductLevel"
    variant_level: "MissingPricesVariantLevel"

    def __init__(
        self,
        *,
        product_level: "MissingPricesProductLevel",
        variant_level: "MissingPricesVariantLevel"
    ):
        self.product_level = product_level
        self.variant_level = variant_level
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MissingPricesMeta":
        from ._schemas.missing_data import MissingPricesMetaSchema

        return MissingPricesMetaSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingPricesMetaSchema

        return MissingPricesMetaSchema().dump(self)


class MissingPricesSearchRequest(_BaseType):
    limit: typing.Optional[int]
    offset: typing.Optional[int]
    #: If true, searches data from staged products in addition to published products.
    staged: typing.Optional[bool]
    #: Maximum number of products to scan.
    product_set_limit: typing.Optional[int]
    #: If true, searches all product variants. If false, only searches master variants.
    include_variants: typing.Optional[bool]
    #: If used, only checks if a product variant has a price in the provided currency code.
    currency_code: typing.Optional[str]
    #: If true, checks if there are prices for the specified date range and time.
    check_date: typing.Optional[bool]
    #: Starting date of the range to check. If no value is given, checks prices valid at the time the search is initiated.
    valid_from: typing.Optional[datetime.datetime]
    #: Ending date of the range to check. If no value is given, it is equal to `validFrom`.
    valid_until: typing.Optional[datetime.datetime]
    #: Filters results by the provided Product IDs. Cannot be applied in combination with the `productTypeIds` filter.
    product_ids: typing.Optional[typing.List["str"]]
    #: Filters results by the provided product type IDs. Cannot be applied in combination with the `productIds` filter.
    product_type_ids: typing.Optional[typing.List["str"]]

    def __init__(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        staged: typing.Optional[bool] = None,
        product_set_limit: typing.Optional[int] = None,
        include_variants: typing.Optional[bool] = None,
        currency_code: typing.Optional[str] = None,
        check_date: typing.Optional[bool] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        product_ids: typing.Optional[typing.List["str"]] = None,
        product_type_ids: typing.Optional[typing.List["str"]] = None
    ):
        self.limit = limit
        self.offset = offset
        self.staged = staged
        self.product_set_limit = product_set_limit
        self.include_variants = include_variants
        self.currency_code = currency_code
        self.check_date = check_date
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.product_ids = product_ids
        self.product_type_ids = product_type_ids
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingPricesSearchRequest":
        from ._schemas.missing_data import MissingPricesSearchRequestSchema

        return MissingPricesSearchRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingPricesSearchRequestSchema

        return MissingPricesSearchRequestSchema().dump(self)


class MissingPricesPagedQueryResult(_BaseType):
    count: int
    total: int
    offset: int
    results: typing.List["MissingPrices"]
    meta: "MissingPricesMeta"

    def __init__(
        self,
        *,
        count: int,
        total: int,
        offset: int,
        results: typing.List["MissingPrices"],
        meta: "MissingPricesMeta"
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
    ) -> "MissingPricesPagedQueryResult":
        from ._schemas.missing_data import MissingPricesPagedQueryResultSchema

        return MissingPricesPagedQueryResultSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingPricesPagedQueryResultSchema

        return MissingPricesPagedQueryResultSchema().dump(self)


class MissingPricesTaskStatus(_BaseType):
    """Represents a URL path to poll to get the results of an Asynchronous Request."""

    state: "TaskStatusEnum"
    #: The expiry date of the result. You cannot access the result after the expiry date. Default: 1 day after the result first becomes available. This is only available when the TaskStatus state is SUCCESS.
    expires: datetime.datetime
    #: The response to an asynchronous request. The type depends on the request initiated. Only populated when the status is `SUCCESS`.
    result: "MissingPricesPagedQueryResult"

    def __init__(
        self,
        *,
        state: "TaskStatusEnum",
        expires: datetime.datetime,
        result: "MissingPricesPagedQueryResult"
    ):
        self.state = state
        self.expires = expires
        self.result = result
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "MissingPricesTaskStatus":
        from ._schemas.missing_data import MissingPricesTaskStatusSchema

        return MissingPricesTaskStatusSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.missing_data import MissingPricesTaskStatusSchema

        return MissingPricesTaskStatusSchema().dump(self)

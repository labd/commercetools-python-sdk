# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType

if typing.TYPE_CHECKING:
    from .common import ProductVariant


class ImageSearchResponse(_BaseType):
    """Response format from image search endpoint."""

    #: The maximum number of results to return from a query.
    count: "int"
    #: The offset into the results matching the query. An offset of 0 is the default value indicating that no results should be skipped.
    offset: "float"
    #: The total number of product images that were have been analyzed.
    total: "int"
    #: An array of image URLs of images that are similar to the query image. If no matching images are found, results is empty.
    results: typing.List["ResultItem"]

    def __init__(
        self,
        *,
        count: "int",
        offset: "float",
        total: "int",
        results: typing.List["ResultItem"]
    ):
        self.count = count
        self.offset = offset
        self.total = total
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImageSearchResponse":
        from ._schemas.image_search import ImageSearchResponseSchema

        return ImageSearchResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.image_search import ImageSearchResponseSchema

        return ImageSearchResponseSchema().dump(self)


class ResultItem(_BaseType):
    """An image URL and the product variants it is contained in. If no matching images are found, ResultItem is not present."""

    #: The URL of the image.
    image_url: "str"
    #: An array of product variants containing the image URL.
    product_variants: typing.List["ProductVariant"]

    def __init__(
        self, *, image_url: "str", product_variants: typing.List["ProductVariant"]
    ):
        self.image_url = image_url
        self.product_variants = product_variants
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ResultItem":
        from ._schemas.image_search import ResultItemSchema

        return ResultItemSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.image_search import ResultItemSchema

        return ResultItemSchema().dump(self)

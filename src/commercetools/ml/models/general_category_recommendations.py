# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType


class GeneralCategoryRecommendation(_BaseType):
    #: An English category name that is recommended for a product.
    category_name: "str"
    #: Probability score for the category recommendation.
    confidence: "float"

    def __init__(self, *, category_name: "str", confidence: "float"):
        self.category_name = category_name
        self.confidence = confidence
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "GeneralCategoryRecommendation":
        from ._schemas.general_category_recommendations import (
            GeneralCategoryRecommendationSchema,
        )

        return GeneralCategoryRecommendationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.general_category_recommendations import (
            GeneralCategoryRecommendationSchema,
        )

        return GeneralCategoryRecommendationSchema().dump(self)


class GeneralCategoryRecommendationPagedQueryResponse(_BaseType):
    count: "int"
    total: "int"
    offset: "int"
    results: typing.List["GeneralCategoryRecommendation"]

    def __init__(
        self,
        *,
        count: "int",
        total: "int",
        offset: "int",
        results: typing.List["GeneralCategoryRecommendation"]
    ):
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "GeneralCategoryRecommendationPagedQueryResponse":
        from ._schemas.general_category_recommendations import (
            GeneralCategoryRecommendationPagedQueryResponseSchema,
        )

        return GeneralCategoryRecommendationPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.general_category_recommendations import (
            GeneralCategoryRecommendationPagedQueryResponseSchema,
        )

        return GeneralCategoryRecommendationPagedQueryResponseSchema().dump(self)

# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType

if typing.TYPE_CHECKING:
    from .common import CategoryReference


class ProjectCategoryRecommendation(_BaseType):
    #: A category that is recommended for a product.
    category: "CategoryReference"
    #: Probability score for the category recommendation.
    confidence: "float"
    #: Breadcrumb path to the recommended category. This only picks up one language, not all available languages for the category. English is prioritized, but if English data is not available, an arbitrary language is selected. Do not use this to identify a category,use the category ID from the category reference instead.
    path: "str"

    def __init__(
        self, *, category: "CategoryReference", confidence: "float", path: "str"
    ):
        self.category = category
        self.confidence = confidence
        self.path = path
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectCategoryRecommendation":
        from ._schemas.category_recommendations import (
            ProjectCategoryRecommendationSchema,
        )

        return ProjectCategoryRecommendationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category_recommendations import (
            ProjectCategoryRecommendationSchema,
        )

        return ProjectCategoryRecommendationSchema().dump(self)


class ProjectCategoryRecommendationMeta(_BaseType):
    #: The product name that was used to generate recommendations.
    product_name: typing.Optional["str"]
    #: The product image that was used to generate recommendations.
    product_image_url: typing.Optional["str"]
    #: Top 5 general categories that were used internally to generate the project-specific categories. These category names are not related to the categories defined in the project, but they provide additional information to understand the project-specific categories in the results section.
    general_category_names: typing.List["str"]

    def __init__(
        self,
        *,
        product_name: typing.Optional["str"] = None,
        product_image_url: typing.Optional["str"] = None,
        general_category_names: typing.List["str"]
    ):
        self.product_name = product_name
        self.product_image_url = product_image_url
        self.general_category_names = general_category_names
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectCategoryRecommendationMeta":
        from ._schemas.category_recommendations import (
            ProjectCategoryRecommendationMetaSchema,
        )

        return ProjectCategoryRecommendationMetaSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category_recommendations import (
            ProjectCategoryRecommendationMetaSchema,
        )

        return ProjectCategoryRecommendationMetaSchema().dump(self)


class ProjectCategoryRecommendationPagedQueryResponse(_BaseType):
    count: "int"
    total: "int"
    offset: "int"
    results: typing.List["ProjectCategoryRecommendation"]
    meta: "ProjectCategoryRecommendationMeta"

    def __init__(
        self,
        *,
        count: "int",
        total: "int",
        offset: "int",
        results: typing.List["ProjectCategoryRecommendation"],
        meta: "ProjectCategoryRecommendationMeta"
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
    ) -> "ProjectCategoryRecommendationPagedQueryResponse":
        from ._schemas.category_recommendations import (
            ProjectCategoryRecommendationPagedQueryResponseSchema,
        )

        return ProjectCategoryRecommendationPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category_recommendations import (
            ProjectCategoryRecommendationPagedQueryResponseSchema,
        )

        return ProjectCategoryRecommendationPagedQueryResponseSchema().dump(self)

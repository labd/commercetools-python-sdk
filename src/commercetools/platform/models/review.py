# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .channel import ChannelReference, ChannelResourceIdentifier
    from .common import CreatedBy, LastModifiedBy, ReferenceTypeId
    from .customer import CustomerReference, CustomerResourceIdentifier
    from .product import ProductReference, ProductResourceIdentifier
    from .state import StateReference, StateResourceIdentifier
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "Review",
    "ReviewDraft",
    "ReviewPagedQueryResponse",
    "ReviewRatingStatistics",
    "ReviewReference",
    "ReviewResourceIdentifier",
    "ReviewSetAuthorNameAction",
    "ReviewSetCustomFieldAction",
    "ReviewSetCustomTypeAction",
    "ReviewSetCustomerAction",
    "ReviewSetKeyAction",
    "ReviewSetLocaleAction",
    "ReviewSetRatingAction",
    "ReviewSetTargetAction",
    "ReviewSetTextAction",
    "ReviewSetTitleAction",
    "ReviewTransitionStateAction",
    "ReviewUpdate",
    "ReviewUpdateAction",
]


class Review(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    #: User-specific unique identifier for the review.
    key: typing.Optional[str]
    uniqueness_value: typing.Optional[str]
    locale: typing.Optional[str]
    author_name: typing.Optional[str]
    title: typing.Optional[str]
    text: typing.Optional[str]
    #: Identifies the target of the review.
    #: Can be a Product or a Channel
    target: typing.Optional[typing.Union["ProductReference", "ChannelReference"]]
    #: Indicates if this review is taken into account in the ratings statistics of the target.
    #: A review is per default used in the statistics, unless the review is in a state that does not have the role `ReviewIncludedInStatistics`.
    #: If the role of a State is modified after the calculation of this field, the calculation is not updated.
    included_in_statistics: bool
    #: Number between -100 and 100 included.
    rating: typing.Optional[int]
    state: typing.Optional["StateReference"]
    #: The customer who created the review.
    customer: typing.Optional["CustomerReference"]
    custom: typing.Optional["CustomFields"]

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
        uniqueness_value: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        author_name: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        target: typing.Optional[
            typing.Union["ProductReference", "ChannelReference"]
        ] = None,
        included_in_statistics: bool,
        rating: typing.Optional[int] = None,
        state: typing.Optional["StateReference"] = None,
        customer: typing.Optional["CustomerReference"] = None,
        custom: typing.Optional["CustomFields"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.uniqueness_value = uniqueness_value
        self.locale = locale
        self.author_name = author_name
        self.title = title
        self.text = text
        self.target = target
        self.included_in_statistics = included_in_statistics
        self.rating = rating
        self.state = state
        self.customer = customer
        self.custom = custom
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Review":
        from ._schemas.review import ReviewSchema

        return ReviewSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewSchema

        return ReviewSchema().dump(self)


class ReviewDraft(_BaseType):
    #: User-specific unique identifier for the review.
    key: typing.Optional[str]
    #: If set, this value must be unique among reviews.
    #: For example, if you want to have only one review per customer and per product, you can set the value to `customer's id` and `product's id`.
    uniqueness_value: typing.Optional[str]
    locale: typing.Optional[str]
    author_name: typing.Optional[str]
    title: typing.Optional[str]
    text: typing.Optional[str]
    #: Identifies the target of the review.
    #: Can be a Product or a Channel
    target: typing.Optional[
        typing.Union["ProductResourceIdentifier", "ChannelResourceIdentifier"]
    ]
    state: typing.Optional["StateResourceIdentifier"]
    #: Number between -100 and 100 included.
    #: Rating of the targeted object, like a product.
    #: This rating can represent the number of stars, or a percentage, or a like (+1)/dislike (-1)
    #: A rating is used in the ratings statistics of the targeted object, unless the review is in a state that does not have the role `ReviewIncludedInStatistics`.
    rating: typing.Optional[int]
    #: The customer who created the review.
    customer: typing.Optional["CustomerResourceIdentifier"]
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        uniqueness_value: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        author_name: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        target: typing.Optional[
            typing.Union["ProductResourceIdentifier", "ChannelResourceIdentifier"]
        ] = None,
        state: typing.Optional["StateResourceIdentifier"] = None,
        rating: typing.Optional[int] = None,
        customer: typing.Optional["CustomerResourceIdentifier"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.key = key
        self.uniqueness_value = uniqueness_value
        self.locale = locale
        self.author_name = author_name
        self.title = title
        self.text = text
        self.target = target
        self.state = state
        self.rating = rating
        self.customer = customer
        self.custom = custom
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReviewDraft":
        from ._schemas.review import ReviewDraftSchema

        return ReviewDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewDraftSchema

        return ReviewDraftSchema().dump(self)


class ReviewPagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["Review"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["Review"]
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
    ) -> "ReviewPagedQueryResponse":
        from ._schemas.review import ReviewPagedQueryResponseSchema

        return ReviewPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewPagedQueryResponseSchema

        return ReviewPagedQueryResponseSchema().dump(self)


class ReviewRatingStatistics(_BaseType):
    #: Average rating of one target
    #: This number is rounded with 5 decimals.
    average_rating: float
    #: Highest rating of one target
    highest_rating: float
    #: Lowest rating of one target
    lowest_rating: float
    #: Number of ratings taken into account
    count: int
    #: The full distribution of the ratings.
    #: The keys are the different ratings and the values are the count of reviews having this rating.
    #: Only the used ratings appear in this object.
    ratings_distribution: object

    def __init__(
        self,
        *,
        average_rating: float,
        highest_rating: float,
        lowest_rating: float,
        count: int,
        ratings_distribution: object
    ):
        self.average_rating = average_rating
        self.highest_rating = highest_rating
        self.lowest_rating = lowest_rating
        self.count = count
        self.ratings_distribution = ratings_distribution
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReviewRatingStatistics":
        from ._schemas.review import ReviewRatingStatisticsSchema

        return ReviewRatingStatisticsSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewRatingStatisticsSchema

        return ReviewRatingStatisticsSchema().dump(self)


class ReviewReference(Reference):
    obj: typing.Optional["Review"]

    def __init__(self, *, id: str, obj: typing.Optional["Review"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.REVIEW)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReviewReference":
        from ._schemas.review import ReviewReferenceSchema

        return ReviewReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewReferenceSchema

        return ReviewReferenceSchema().dump(self)


class ReviewResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.REVIEW)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReviewResourceIdentifier":
        from ._schemas.review import ReviewResourceIdentifierSchema

        return ReviewResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewResourceIdentifierSchema

        return ReviewResourceIdentifierSchema().dump(self)


class ReviewUpdate(_BaseType):
    version: int
    actions: typing.List["ReviewUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["ReviewUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReviewUpdate":
        from ._schemas.review import ReviewUpdateSchema

        return ReviewUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewUpdateSchema

        return ReviewUpdateSchema().dump(self)


class ReviewUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReviewUpdateAction":
        if data["action"] == "setAuthorName":
            from ._schemas.review import ReviewSetAuthorNameActionSchema

            return ReviewSetAuthorNameActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.review import ReviewSetCustomFieldActionSchema

            return ReviewSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.review import ReviewSetCustomTypeActionSchema

            return ReviewSetCustomTypeActionSchema().load(data)
        if data["action"] == "setCustomer":
            from ._schemas.review import ReviewSetCustomerActionSchema

            return ReviewSetCustomerActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.review import ReviewSetKeyActionSchema

            return ReviewSetKeyActionSchema().load(data)
        if data["action"] == "setLocale":
            from ._schemas.review import ReviewSetLocaleActionSchema

            return ReviewSetLocaleActionSchema().load(data)
        if data["action"] == "setRating":
            from ._schemas.review import ReviewSetRatingActionSchema

            return ReviewSetRatingActionSchema().load(data)
        if data["action"] == "setTarget":
            from ._schemas.review import ReviewSetTargetActionSchema

            return ReviewSetTargetActionSchema().load(data)
        if data["action"] == "setText":
            from ._schemas.review import ReviewSetTextActionSchema

            return ReviewSetTextActionSchema().load(data)
        if data["action"] == "setTitle":
            from ._schemas.review import ReviewSetTitleActionSchema

            return ReviewSetTitleActionSchema().load(data)
        if data["action"] == "transitionState":
            from ._schemas.review import ReviewTransitionStateActionSchema

            return ReviewTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewUpdateActionSchema

        return ReviewUpdateActionSchema().dump(self)


class ReviewSetAuthorNameAction(ReviewUpdateAction):
    #: If `authorName` is absent or `null`, this field will be removed if it exists.
    author_name: typing.Optional[str]

    def __init__(self, *, author_name: typing.Optional[str] = None):
        self.author_name = author_name
        super().__init__(action="setAuthorName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReviewSetAuthorNameAction":
        from ._schemas.review import ReviewSetAuthorNameActionSchema

        return ReviewSetAuthorNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewSetAuthorNameActionSchema

        return ReviewSetAuthorNameActionSchema().dump(self)


class ReviewSetCustomFieldAction(ReviewUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReviewSetCustomFieldAction":
        from ._schemas.review import ReviewSetCustomFieldActionSchema

        return ReviewSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewSetCustomFieldActionSchema

        return ReviewSetCustomFieldActionSchema().dump(self)


class ReviewSetCustomTypeAction(ReviewUpdateAction):
    #: If absent, the custom type and any existing custom fields are removed.
    type: typing.Optional["TypeResourceIdentifier"]
    #: A valid JSON object, based on the FieldDefinitions of the Type.
    #: Sets the CustomFields to this value.
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReviewSetCustomTypeAction":
        from ._schemas.review import ReviewSetCustomTypeActionSchema

        return ReviewSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewSetCustomTypeActionSchema

        return ReviewSetCustomTypeActionSchema().dump(self)


class ReviewSetCustomerAction(ReviewUpdateAction):
    #: The customer who created the review.
    #: If `customer` is absent or `null`, this field will be removed if it exists.
    customer: typing.Optional["CustomerResourceIdentifier"]

    def __init__(
        self, *, customer: typing.Optional["CustomerResourceIdentifier"] = None
    ):
        self.customer = customer
        super().__init__(action="setCustomer")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReviewSetCustomerAction":
        from ._schemas.review import ReviewSetCustomerActionSchema

        return ReviewSetCustomerActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewSetCustomerActionSchema

        return ReviewSetCustomerActionSchema().dump(self)


class ReviewSetKeyAction(ReviewUpdateAction):
    #: If `key` is absent or `null`, this field will be removed if it exists.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReviewSetKeyAction":
        from ._schemas.review import ReviewSetKeyActionSchema

        return ReviewSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewSetKeyActionSchema

        return ReviewSetKeyActionSchema().dump(self)


class ReviewSetLocaleAction(ReviewUpdateAction):
    #: If `locale` is absent or `null`, this field will be removed if it exists.
    locale: typing.Optional[str]

    def __init__(self, *, locale: typing.Optional[str] = None):
        self.locale = locale
        super().__init__(action="setLocale")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReviewSetLocaleAction":
        from ._schemas.review import ReviewSetLocaleActionSchema

        return ReviewSetLocaleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewSetLocaleActionSchema

        return ReviewSetLocaleActionSchema().dump(self)


class ReviewSetRatingAction(ReviewUpdateAction):
    #: Number between -100 and 100 included.
    #: If `rating` is absent or `null`, this field will be removed if it exists.
    rating: typing.Optional[int]

    def __init__(self, *, rating: typing.Optional[int] = None):
        self.rating = rating
        super().__init__(action="setRating")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReviewSetRatingAction":
        from ._schemas.review import ReviewSetRatingActionSchema

        return ReviewSetRatingActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewSetRatingActionSchema

        return ReviewSetRatingActionSchema().dump(self)


class ReviewSetTargetAction(ReviewUpdateAction):
    #: Identifies the target of the review.
    #: Can be a Product or a Channel.
    #: If `target` is absent or `null`, this field will be removed if it exists.
    target: typing.Union["ProductResourceIdentifier", "ChannelResourceIdentifier"]

    def __init__(
        self,
        *,
        target: typing.Union["ProductResourceIdentifier", "ChannelResourceIdentifier"]
    ):
        self.target = target
        super().__init__(action="setTarget")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReviewSetTargetAction":
        from ._schemas.review import ReviewSetTargetActionSchema

        return ReviewSetTargetActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewSetTargetActionSchema

        return ReviewSetTargetActionSchema().dump(self)


class ReviewSetTextAction(ReviewUpdateAction):
    #: If `text` is absent or `null`, this field will be removed if it exists.
    text: typing.Optional[str]

    def __init__(self, *, text: typing.Optional[str] = None):
        self.text = text
        super().__init__(action="setText")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReviewSetTextAction":
        from ._schemas.review import ReviewSetTextActionSchema

        return ReviewSetTextActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewSetTextActionSchema

        return ReviewSetTextActionSchema().dump(self)


class ReviewSetTitleAction(ReviewUpdateAction):
    #: If `title` is absent or `null`, this field will be removed if it exists.
    title: typing.Optional[str]

    def __init__(self, *, title: typing.Optional[str] = None):
        self.title = title
        super().__init__(action="setTitle")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReviewSetTitleAction":
        from ._schemas.review import ReviewSetTitleActionSchema

        return ReviewSetTitleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewSetTitleActionSchema

        return ReviewSetTitleActionSchema().dump(self)


class ReviewTransitionStateAction(ReviewUpdateAction):
    state: "StateResourceIdentifier"
    force: typing.Optional[bool]

    def __init__(
        self, *, state: "StateResourceIdentifier", force: typing.Optional[bool] = None
    ):
        self.state = state
        self.force = force
        super().__init__(action="transitionState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ReviewTransitionStateAction":
        from ._schemas.review import ReviewTransitionStateActionSchema

        return ReviewTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.review import ReviewTransitionStateActionSchema

        return ReviewTransitionStateActionSchema().dump(self)

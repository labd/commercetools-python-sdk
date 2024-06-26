# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen

import datetime
import enum
import typing

from ._abstract import _BaseType

__all__ = [
    "SearchAndExpression",
    "SearchAnyValue",
    "SearchCompoundExpression",
    "SearchDateRangeExpression",
    "SearchDateRangeValue",
    "SearchDateTimeRangeExpression",
    "SearchDateTimeRangeValue",
    "SearchExactExpression",
    "SearchExistsExpression",
    "SearchExistsValue",
    "SearchFieldType",
    "SearchFilterExpression",
    "SearchFullTextExpression",
    "SearchFullTextPrefixExpression",
    "SearchFullTextPrefixValue",
    "SearchFullTextValue",
    "SearchLongRangeExpression",
    "SearchLongRangeValue",
    "SearchMatchType",
    "SearchMatchingVariant",
    "SearchNotExpression",
    "SearchNumberRangeExpression",
    "SearchNumberRangeValue",
    "SearchOrExpression",
    "SearchPrefixExpression",
    "SearchQuery",
    "SearchQueryExpression",
    "SearchQueryExpressionValue",
    "SearchSortMode",
    "SearchSortOrder",
    "SearchSorting",
    "SearchTimeRangeExpression",
    "SearchTimeRangeValue",
    "SearchWildCardExpression",
]


class SearchFieldType(enum.Enum):
    """Possible values for the `fieldType` property on query expressions indicating the data type of the `field`."""

    BOOLEAN = "boolean"
    TEXT = "text"
    LTEXT = "ltext"
    ENUM = "enum"
    LENUM = "lenum"
    NUMBER = "number"
    MONEY = "money"
    DATE = "date"
    DATETIME = "datetime"
    TIME = "time"
    REFERENCE = "reference"
    SET_BOOLEAN = "set_boolean"
    SET_TEXT = "set_text"
    SET_LTEXT = "set_ltext"
    SET_ENUM = "set_enum"
    SET_LENUM = "set_lenum"
    SET_NUMBER = "set_number"
    SET_MONEY = "set_money"
    SET_DATE = "set_date"
    SET_DATETIME = "set_datetime"
    SET_TIME = "set_time"
    SET_REFERENCE = "set_reference"


class SearchMatchType(enum.Enum):
    ANY = "any"
    ALL = "all"


class SearchMatchingVariant(_BaseType):
    #: Unique identifier of the variant.
    id: int
    #: SKU of the matching variant.
    sku: typing.Optional[str]

    def __init__(self, *, id: int, sku: typing.Optional[str] = None):
        self.id = id
        self.sku = sku

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchMatchingVariant":
        from ._schemas.search import SearchMatchingVariantSchema

        return SearchMatchingVariantSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchMatchingVariantSchema

        return SearchMatchingVariantSchema().dump(self)


class SearchQuery(typing.Dict[str, typing.Any]):
    pass


class SearchCompoundExpression(typing.Dict[str, typing.Any]):
    pass


class SearchAndExpression(SearchCompoundExpression):
    and_: typing.List["SearchQuery"]

    def __init__(self, *, and_: typing.List["SearchQuery"]):
        self.and_ = and_

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchAndExpression":
        from ._schemas.search import SearchAndExpressionSchema

        return SearchAndExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchAndExpressionSchema

        return SearchAndExpressionSchema().dump(self)


class SearchFilterExpression(SearchCompoundExpression):
    filter: typing.List["SearchQueryExpression"]

    def __init__(self, *, filter: typing.List["SearchQueryExpression"]):
        self.filter = filter

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchFilterExpression":
        from ._schemas.search import SearchFilterExpressionSchema

        return SearchFilterExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchFilterExpressionSchema

        return SearchFilterExpressionSchema().dump(self)


class SearchNotExpression(SearchCompoundExpression):
    not_: typing.List["SearchQuery"]

    def __init__(self, *, not_: typing.List["SearchQuery"]):
        self.not_ = not_

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchNotExpression":
        from ._schemas.search import SearchNotExpressionSchema

        return SearchNotExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchNotExpressionSchema

        return SearchNotExpressionSchema().dump(self)


class SearchOrExpression(SearchCompoundExpression):
    or_: typing.List["SearchQuery"]

    def __init__(self, *, or_: typing.List["SearchQuery"]):
        self.or_ = or_

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchOrExpression":
        from ._schemas.search import SearchOrExpressionSchema

        return SearchOrExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchOrExpressionSchema

        return SearchOrExpressionSchema().dump(self)


class SearchQueryExpression(typing.Dict[str, typing.Any]):
    pass


class SearchDateRangeExpression(SearchQueryExpression):
    range: "SearchDateRangeValue"

    def __init__(self, *, range: "SearchDateRangeValue"):
        self.range = range

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchDateRangeExpression":
        from ._schemas.search import SearchDateRangeExpressionSchema

        return SearchDateRangeExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchDateRangeExpressionSchema

        return SearchDateRangeExpressionSchema().dump(self)


class SearchDateTimeRangeExpression(SearchQueryExpression):
    range: "SearchDateTimeRangeValue"

    def __init__(self, *, range: "SearchDateTimeRangeValue"):
        self.range = range

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchDateTimeRangeExpression":
        from ._schemas.search import SearchDateTimeRangeExpressionSchema

        return SearchDateTimeRangeExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchDateTimeRangeExpressionSchema

        return SearchDateTimeRangeExpressionSchema().dump(self)


class SearchExactExpression(SearchQueryExpression):
    exact: "SearchAnyValue"

    def __init__(self, *, exact: "SearchAnyValue"):
        self.exact = exact

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchExactExpression":
        from ._schemas.search import SearchExactExpressionSchema

        return SearchExactExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchExactExpressionSchema

        return SearchExactExpressionSchema().dump(self)


class SearchExistsExpression(SearchQueryExpression):
    exists: "SearchExistsValue"

    def __init__(self, *, exists: "SearchExistsValue"):
        self.exists = exists

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchExistsExpression":
        from ._schemas.search import SearchExistsExpressionSchema

        return SearchExistsExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchExistsExpressionSchema

        return SearchExistsExpressionSchema().dump(self)


class SearchFullTextExpression(SearchQueryExpression):
    full_text: "SearchFullTextValue"

    def __init__(self, *, full_text: "SearchFullTextValue"):
        self.full_text = full_text

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchFullTextExpression":
        from ._schemas.search import SearchFullTextExpressionSchema

        return SearchFullTextExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchFullTextExpressionSchema

        return SearchFullTextExpressionSchema().dump(self)


class SearchFullTextPrefixExpression(SearchQueryExpression):
    full_text_prefix: "SearchFullTextPrefixValue"

    def __init__(self, *, full_text_prefix: "SearchFullTextPrefixValue"):
        self.full_text_prefix = full_text_prefix

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchFullTextPrefixExpression":
        from ._schemas.search import SearchFullTextPrefixExpressionSchema

        return SearchFullTextPrefixExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchFullTextPrefixExpressionSchema

        return SearchFullTextPrefixExpressionSchema().dump(self)


class SearchLongRangeExpression(SearchQueryExpression):
    range: "SearchLongRangeValue"

    def __init__(self, *, range: "SearchLongRangeValue"):
        self.range = range

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchLongRangeExpression":
        from ._schemas.search import SearchLongRangeExpressionSchema

        return SearchLongRangeExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchLongRangeExpressionSchema

        return SearchLongRangeExpressionSchema().dump(self)


class SearchNumberRangeExpression(SearchQueryExpression):
    range: "SearchNumberRangeValue"

    def __init__(self, *, range: "SearchNumberRangeValue"):
        self.range = range

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchNumberRangeExpression":
        from ._schemas.search import SearchNumberRangeExpressionSchema

        return SearchNumberRangeExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchNumberRangeExpressionSchema

        return SearchNumberRangeExpressionSchema().dump(self)


class SearchPrefixExpression(SearchQueryExpression):
    prefix: "SearchAnyValue"

    def __init__(self, *, prefix: "SearchAnyValue"):
        self.prefix = prefix

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchPrefixExpression":
        from ._schemas.search import SearchPrefixExpressionSchema

        return SearchPrefixExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchPrefixExpressionSchema

        return SearchPrefixExpressionSchema().dump(self)


class SearchQueryExpressionValue(_BaseType):
    field: str
    boost: typing.Optional[float]
    #: Possible values for the `fieldType` property on query expressions indicating the data type of the `field`.
    field_type: typing.Optional["SearchFieldType"]

    def __init__(
        self,
        *,
        field: str,
        boost: typing.Optional[float] = None,
        field_type: typing.Optional["SearchFieldType"] = None
    ):
        self.field = field
        self.boost = boost
        self.field_type = field_type

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchQueryExpressionValue":
        from ._schemas.search import SearchQueryExpressionValueSchema

        return SearchQueryExpressionValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchQueryExpressionValueSchema

        return SearchQueryExpressionValueSchema().dump(self)


class SearchAnyValue(SearchQueryExpressionValue):
    value: typing.Any
    #: String value specifying linguistic and regional preferences using the [IETF language tag format](https://en.wikipedia.org/wiki/IETF_language_tag), as described in [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). The format combines language, script, and region using hyphen-separated subtags. For example: `en`, `en-US`, `zh-Hans-SG`.
    language: typing.Optional[str]
    case_insensitive: typing.Optional[bool]

    def __init__(
        self,
        *,
        field: str,
        boost: typing.Optional[float] = None,
        field_type: typing.Optional["SearchFieldType"] = None,
        value: typing.Any,
        language: typing.Optional[str] = None,
        case_insensitive: typing.Optional[bool] = None
    ):
        self.value = value
        self.language = language
        self.case_insensitive = case_insensitive

        super().__init__(field=field, boost=boost, field_type=field_type)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchAnyValue":
        from ._schemas.search import SearchAnyValueSchema

        return SearchAnyValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchAnyValueSchema

        return SearchAnyValueSchema().dump(self)


class SearchDateRangeValue(SearchQueryExpressionValue):
    gte: typing.Optional[datetime.date]
    gt: typing.Optional[datetime.date]
    lte: typing.Optional[datetime.date]
    lt: typing.Optional[datetime.date]

    def __init__(
        self,
        *,
        field: str,
        boost: typing.Optional[float] = None,
        field_type: typing.Optional["SearchFieldType"] = None,
        gte: typing.Optional[datetime.date] = None,
        gt: typing.Optional[datetime.date] = None,
        lte: typing.Optional[datetime.date] = None,
        lt: typing.Optional[datetime.date] = None
    ):
        self.gte = gte
        self.gt = gt
        self.lte = lte
        self.lt = lt

        super().__init__(field=field, boost=boost, field_type=field_type)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchDateRangeValue":
        from ._schemas.search import SearchDateRangeValueSchema

        return SearchDateRangeValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchDateRangeValueSchema

        return SearchDateRangeValueSchema().dump(self)


class SearchDateTimeRangeValue(SearchQueryExpressionValue):
    gte: typing.Optional[datetime.datetime]
    gt: typing.Optional[datetime.datetime]
    lte: typing.Optional[datetime.datetime]
    lt: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        field: str,
        boost: typing.Optional[float] = None,
        field_type: typing.Optional["SearchFieldType"] = None,
        gte: typing.Optional[datetime.datetime] = None,
        gt: typing.Optional[datetime.datetime] = None,
        lte: typing.Optional[datetime.datetime] = None,
        lt: typing.Optional[datetime.datetime] = None
    ):
        self.gte = gte
        self.gt = gt
        self.lte = lte
        self.lt = lt

        super().__init__(field=field, boost=boost, field_type=field_type)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchDateTimeRangeValue":
        from ._schemas.search import SearchDateTimeRangeValueSchema

        return SearchDateTimeRangeValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchDateTimeRangeValueSchema

        return SearchDateTimeRangeValueSchema().dump(self)


class SearchExistsValue(SearchQueryExpressionValue):
    #: String value specifying linguistic and regional preferences using the [IETF language tag format](https://en.wikipedia.org/wiki/IETF_language_tag), as described in [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). The format combines language, script, and region using hyphen-separated subtags. For example: `en`, `en-US`, `zh-Hans-SG`.
    language: typing.Optional[str]

    def __init__(
        self,
        *,
        field: str,
        boost: typing.Optional[float] = None,
        field_type: typing.Optional["SearchFieldType"] = None,
        language: typing.Optional[str] = None
    ):
        self.language = language

        super().__init__(field=field, boost=boost, field_type=field_type)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchExistsValue":
        from ._schemas.search import SearchExistsValueSchema

        return SearchExistsValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchExistsValueSchema

        return SearchExistsValueSchema().dump(self)


class SearchFullTextPrefixValue(SearchQueryExpressionValue):
    value: typing.Any
    #: String value specifying linguistic and regional preferences using the [IETF language tag format](https://en.wikipedia.org/wiki/IETF_language_tag), as described in [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). The format combines language, script, and region using hyphen-separated subtags. For example: `en`, `en-US`, `zh-Hans-SG`.
    language: typing.Optional[str]
    must_match: typing.Optional["SearchMatchType"]

    def __init__(
        self,
        *,
        field: str,
        boost: typing.Optional[float] = None,
        field_type: typing.Optional["SearchFieldType"] = None,
        value: typing.Any,
        language: typing.Optional[str] = None,
        must_match: typing.Optional["SearchMatchType"] = None
    ):
        self.value = value
        self.language = language
        self.must_match = must_match

        super().__init__(field=field, boost=boost, field_type=field_type)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchFullTextPrefixValue":
        from ._schemas.search import SearchFullTextPrefixValueSchema

        return SearchFullTextPrefixValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchFullTextPrefixValueSchema

        return SearchFullTextPrefixValueSchema().dump(self)


class SearchFullTextValue(SearchQueryExpressionValue):
    value: typing.Any
    #: String value specifying linguistic and regional preferences using the [IETF language tag format](https://en.wikipedia.org/wiki/IETF_language_tag), as described in [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). The format combines language, script, and region using hyphen-separated subtags. For example: `en`, `en-US`, `zh-Hans-SG`.
    language: typing.Optional[str]
    must_match: typing.Optional["SearchMatchType"]

    def __init__(
        self,
        *,
        field: str,
        boost: typing.Optional[float] = None,
        field_type: typing.Optional["SearchFieldType"] = None,
        value: typing.Any,
        language: typing.Optional[str] = None,
        must_match: typing.Optional["SearchMatchType"] = None
    ):
        self.value = value
        self.language = language
        self.must_match = must_match

        super().__init__(field=field, boost=boost, field_type=field_type)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchFullTextValue":
        from ._schemas.search import SearchFullTextValueSchema

        return SearchFullTextValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchFullTextValueSchema

        return SearchFullTextValueSchema().dump(self)


class SearchLongRangeValue(SearchQueryExpressionValue):
    gte: typing.Optional[int]
    gt: typing.Optional[int]
    lte: typing.Optional[int]
    lt: typing.Optional[int]

    def __init__(
        self,
        *,
        field: str,
        boost: typing.Optional[float] = None,
        field_type: typing.Optional["SearchFieldType"] = None,
        gte: typing.Optional[int] = None,
        gt: typing.Optional[int] = None,
        lte: typing.Optional[int] = None,
        lt: typing.Optional[int] = None
    ):
        self.gte = gte
        self.gt = gt
        self.lte = lte
        self.lt = lt

        super().__init__(field=field, boost=boost, field_type=field_type)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchLongRangeValue":
        from ._schemas.search import SearchLongRangeValueSchema

        return SearchLongRangeValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchLongRangeValueSchema

        return SearchLongRangeValueSchema().dump(self)


class SearchNumberRangeValue(SearchQueryExpressionValue):
    gte: typing.Optional[float]
    gt: typing.Optional[float]
    lte: typing.Optional[float]
    lt: typing.Optional[float]

    def __init__(
        self,
        *,
        field: str,
        boost: typing.Optional[float] = None,
        field_type: typing.Optional["SearchFieldType"] = None,
        gte: typing.Optional[float] = None,
        gt: typing.Optional[float] = None,
        lte: typing.Optional[float] = None,
        lt: typing.Optional[float] = None
    ):
        self.gte = gte
        self.gt = gt
        self.lte = lte
        self.lt = lt

        super().__init__(field=field, boost=boost, field_type=field_type)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchNumberRangeValue":
        from ._schemas.search import SearchNumberRangeValueSchema

        return SearchNumberRangeValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchNumberRangeValueSchema

        return SearchNumberRangeValueSchema().dump(self)


class SearchSortMode(enum.Enum):
    """For set-type fields, only a single value of the set is taken into account for sorting.
    The sort mode determines whether the minimum or maximum value, or a calculated statistical value should be used as sorting value.

    """

    MIN = "min"
    MAX = "max"
    AVG = "avg"
    SUM = "sum"


class SearchSortOrder(enum.Enum):
    ASC = "asc"
    DESC = "desc"


class SearchSorting(_BaseType):
    """Sorting parameters provided with a Search request.
    Sorting allows you to control how results to your query are sorted.
    If no sorting is specified, the results are sorted by relevance in descending (`desc`) order.

    """

    #: Use any searchable field of the resource as sort criterion.
    field: str
    #: String value specifying linguistic and regional preferences using the [IETF language tag format](https://en.wikipedia.org/wiki/IETF_language_tag), as described in [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). The format combines language, script, and region using hyphen-separated subtags. For example: `en`, `en-US`, `zh-Hans-SG`.
    language: typing.Optional[str]
    #: Specify the order in which the search results should be sorted.
    #: Can be `asc` for ascending, or `desc` for descending order.
    order: "SearchSortOrder"
    #: Specify the sort mode to be applied for a set-type `field`.
    mode: typing.Optional["SearchSortMode"]
    #: Provide the data type of the given `field`.
    field_type: typing.Optional["SearchFieldType"]
    #: Allows you to apply a [sort filter](/../api/search-query-language#sort-filter).
    filter: typing.Optional["SearchQueryExpression"]

    def __init__(
        self,
        *,
        field: str,
        language: typing.Optional[str] = None,
        order: "SearchSortOrder",
        mode: typing.Optional["SearchSortMode"] = None,
        field_type: typing.Optional["SearchFieldType"] = None,
        filter: typing.Optional["SearchQueryExpression"] = None
    ):
        self.field = field
        self.language = language
        self.order = order
        self.mode = mode
        self.field_type = field_type
        self.filter = filter

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchSorting":
        from ._schemas.search import SearchSortingSchema

        return SearchSortingSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchSortingSchema

        return SearchSortingSchema().dump(self)


class SearchTimeRangeExpression(SearchQueryExpression):
    range: "SearchTimeRangeValue"

    def __init__(self, *, range: "SearchTimeRangeValue"):
        self.range = range

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchTimeRangeExpression":
        from ._schemas.search import SearchTimeRangeExpressionSchema

        return SearchTimeRangeExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchTimeRangeExpressionSchema

        return SearchTimeRangeExpressionSchema().dump(self)


class SearchTimeRangeValue(SearchQueryExpressionValue):
    gte: typing.Optional[datetime.time]
    gt: typing.Optional[datetime.time]
    lte: typing.Optional[datetime.time]
    lt: typing.Optional[datetime.time]

    def __init__(
        self,
        *,
        field: str,
        boost: typing.Optional[float] = None,
        field_type: typing.Optional["SearchFieldType"] = None,
        gte: typing.Optional[datetime.time] = None,
        gt: typing.Optional[datetime.time] = None,
        lte: typing.Optional[datetime.time] = None,
        lt: typing.Optional[datetime.time] = None
    ):
        self.gte = gte
        self.gt = gt
        self.lte = lte
        self.lt = lt

        super().__init__(field=field, boost=boost, field_type=field_type)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchTimeRangeValue":
        from ._schemas.search import SearchTimeRangeValueSchema

        return SearchTimeRangeValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchTimeRangeValueSchema

        return SearchTimeRangeValueSchema().dump(self)


class SearchWildCardExpression(SearchQueryExpression):
    wildcard: "SearchAnyValue"

    def __init__(self, *, wildcard: "SearchAnyValue"):
        self.wildcard = wildcard

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchWildCardExpression":
        from ._schemas.search import SearchWildCardExpressionSchema

        return SearchWildCardExpressionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.search import SearchWildCardExpressionSchema

        return SearchWildCardExpressionSchema().dump(self)

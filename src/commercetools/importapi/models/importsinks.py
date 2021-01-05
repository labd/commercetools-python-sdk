# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResourceType

if typing.TYPE_CHECKING:
    from .common import ImportResourceType


class ImportSink(_BaseType):
    """An import sink is the entry point for import resources from other systems.

    It has an unique key and is specific to an import resource type.

    """

    #: The unique key of the import sink.
    #:
    #: Valid characters are: alphabetic characters (A-Z, a-z), numeric characters (0-9), underscores (_) and hyphens (-).
    key: "str"
    #: The type of import resource sent to this import sink.
    #: You can only send one resource type per import sink.
    resource_type: "ImportResourceType"
    #: The version of this resource.
    version: "int"
    #: When the import sink was created.
    created_at: "datetime.datetime"
    #: When the import sink was modified.
    last_modified_at: "datetime.datetime"

    def __init__(
        self,
        *,
        key: "str",
        resource_type: "ImportResourceType",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime"
    ):
        self.key = key
        self.resource_type = resource_type
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImportSink":
        from ._schemas.importsinks import ImportSinkSchema

        return ImportSinkSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importsinks import ImportSinkSchema

        return ImportSinkSchema().dump(self)


class ImportSinkDraft(_BaseType):
    """The representation sent to the server when creating or updating an import sink."""

    #: The version of this resource.
    version: typing.Optional["int"]
    #: The unique key of the import sink.
    key: "str"
    #: The type of import resource sent to this import sink.
    resource_type: "ImportResourceType"

    def __init__(
        self,
        *,
        version: typing.Optional["int"] = None,
        key: "str",
        resource_type: "ImportResourceType"
    ):
        self.version = version
        self.key = key
        self.resource_type = resource_type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImportSinkDraft":
        from ._schemas.importsinks import ImportSinkDraftSchema

        return ImportSinkDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importsinks import ImportSinkDraftSchema

        return ImportSinkDraftSchema().dump(self)


class ImportSinkPagedResponse(_BaseType):
    """This type represents a paged importsink result."""

    #: The maximum number of import operations returned for a page.
    limit: "int"
    #: The offset supplied by the client or the server default. It is the number of elements skipped.
    offset: "int"
    #: The actual number of results returned by this response.
    count: "int"
    #: The results for this paged response.
    results: typing.List["ImportSink"]

    def __init__(
        self,
        *,
        limit: "int",
        offset: "int",
        count: "int",
        results: typing.List["ImportSink"]
    ):
        self.limit = limit
        self.offset = offset
        self.count = count
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ImportSinkPagedResponse":
        from ._schemas.importsinks import ImportSinkPagedResponseSchema

        return ImportSinkPagedResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importsinks import ImportSinkPagedResponseSchema

        return ImportSinkPagedResponseSchema().dump(self)

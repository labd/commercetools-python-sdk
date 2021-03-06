# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ProcessingState

if typing.TYPE_CHECKING:
    from .common import ProcessingState
    from .errors import ErrorObject

__all__ = [
    "ImportOperation",
    "ImportOperationPagedResponse",
    "ImportOperationState",
    "ImportOperationStatus",
]


class ImportOperation(_BaseType):
    """Tracks the status of a single import resource as it is imported into the commercetools project."""

    #: The import operation version.
    version: int
    #: The key of the import sink.
    import_sink_key: str
    #: The key of the import resource.
    resource_key: str
    #: The identifier of the operaton that is to be commited
    id: str
    #: The status of the import resource.
    state: "ProcessingState"
    #: When the resource is successfully imported, this represents the imported resource version
    resource_version: typing.Optional[int]
    #: The number of request retries for processing the import resource.
    retry_count: int
    #: If an import resource does not import correctly, the state is set to `Rejected` or `ValidationFailed`
    #: and this property contains the errors.
    errors: typing.Optional[typing.List["ErrorObject"]]
    #: When the import operation was created.
    created_at: datetime.datetime
    #: When the import operation was modified.
    last_modified_at: datetime.datetime
    #: When the import operation expires.
    expires_at: datetime.datetime

    def __init__(
        self,
        *,
        version: int,
        import_sink_key: str,
        resource_key: str,
        id: str,
        state: "ProcessingState",
        resource_version: typing.Optional[int] = None,
        retry_count: int,
        errors: typing.Optional[typing.List["ErrorObject"]] = None,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        expires_at: datetime.datetime
    ):
        self.version = version
        self.import_sink_key = import_sink_key
        self.resource_key = resource_key
        self.id = id
        self.state = state
        self.resource_version = resource_version
        self.retry_count = retry_count
        self.errors = errors
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        self.expires_at = expires_at
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImportOperation":
        from ._schemas.importoperations import ImportOperationSchema

        return ImportOperationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importoperations import ImportOperationSchema

        return ImportOperationSchema().dump(self)


class ImportOperationPagedResponse(_BaseType):
    """This type represents a paged import operation result."""

    #: The maximum number of import operations returned for a page.
    limit: int
    #: The offset supplied by the client or the server default. It is the number of elements skipped.
    offset: int
    #: The actual number of results returned by this response.
    count: int
    #: The results for this paged response.
    results: typing.List["ImportOperation"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        results: typing.List["ImportOperation"]
    ):
        self.limit = limit
        self.offset = offset
        self.count = count
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ImportOperationPagedResponse":
        from ._schemas.importoperations import ImportOperationPagedResponseSchema

        return ImportOperationPagedResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importoperations import ImportOperationPagedResponseSchema

        return ImportOperationPagedResponseSchema().dump(self)


class ImportOperationState(enum.Enum):
    """This enumeration describes the operation state of a newly created import operation."""

    UNRESOLVED = "Unresolved"
    VALIDATION_FAILED = "ValidationFailed"
    DELETE = "Delete"


class ImportOperationStatus(_BaseType):
    """The validation status of a created operation."""

    #: Id of the import operation.
    operation_id: typing.Optional[str]
    #: Validation state of the import operation.
    state: "ImportOperationState"
    #: Validation errors for the import operation.
    errors: typing.Optional[typing.List["ErrorObject"]]

    def __init__(
        self,
        *,
        operation_id: typing.Optional[str] = None,
        state: "ImportOperationState",
        errors: typing.Optional[typing.List["ErrorObject"]] = None
    ):
        self.operation_id = operation_id
        self.state = state
        self.errors = errors
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImportOperationStatus":
        from ._schemas.importoperations import ImportOperationStatusSchema

        return ImportOperationStatusSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importoperations import ImportOperationStatusSchema

        return ImportOperationStatusSchema().dump(self)

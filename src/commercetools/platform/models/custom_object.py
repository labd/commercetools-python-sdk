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
from .common import BaseResource, Reference, ReferenceTypeId

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, ReferenceTypeId

__all__ = [
    "CustomObject",
    "CustomObjectDraft",
    "CustomObjectPagedQueryResponse",
    "CustomObjectReference",
]


class CustomObject(BaseResource):
    #: IDs and references that last modified the CustomObject.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: IDs and references that created the CustomObject.
    created_by: typing.Optional["CreatedBy"]
    #: Namespace to group CustomObjects.
    container: str
    #: User-defined unique identifier of the CustomObject within the defined `container`.
    key: str
    #: JSON standard types Number, String, Boolean, Array, Object, and [common API data types](/../api/types).
    #: For values of type [Reference](ctp:api:type:Reference) the integrity of the data is not guaranteed.
    #: If the referenced object is deleted, the API does not delete the corresponding reference to it and the `value` points to a non-existing object in such case.
    value: typing.Any

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        container: str,
        key: str,
        value: typing.Any
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.container = container
        self.key = key
        self.value = value

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomObject":
        from ._schemas.custom_object import CustomObjectSchema

        return CustomObjectSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.custom_object import CustomObjectSchema

        return CustomObjectSchema().dump(self)


class CustomObjectDraft(_BaseType):
    #: Namespace to group CustomObjects.
    container: str
    #: User-defined unique identifier of the CustomObject within the defined `container`.
    key: str
    #: JSON standard types Number, String, Boolean, Array, Object, and [common API data types](/../api/types).
    #: For values of type [Reference](ctp:api:type:Reference) the integrity of the data is not guaranteed.
    #: If the referenced object is deleted, the API does not delete the corresponding reference to it and the `value` points to a non-existing object in such case.
    value: typing.Any
    #: Current version of the CustomObject.
    version: typing.Optional[int]

    def __init__(
        self,
        *,
        container: str,
        key: str,
        value: typing.Any,
        version: typing.Optional[int] = None
    ):
        self.container = container
        self.key = key
        self.value = value
        self.version = version

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomObjectDraft":
        from ._schemas.custom_object import CustomObjectDraftSchema

        return CustomObjectDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.custom_object import CustomObjectDraftSchema

        return CustomObjectDraftSchema().dump(self)


class CustomObjectPagedQueryResponse(_BaseType):
    """[PagedQueryResult](/../api/general-concepts#pagedqueryresult) with `results` containing an array of [CustomObject](ctp:api:type:CustomObject)."""

    #: Number of [results requested](/../api/general-concepts#limit).
    limit: int
    #: Number of [elements skipped](/../api/general-concepts#offset).
    offset: int
    #: Actual number of results returned.
    count: int
    #: The total number of results matching the query.
    #: This number is an estimation that is not [strongly consistent](/../api/general-concepts#strong-consistency).
    #: This field is returned by default.
    #: For improved performance, calculating this field can be deactivated by using the query parameter `withTotal=false`.
    #: When the results are filtered with a [Query Predicate](/../api/predicates/query), `total` is subject to a [limit](/../api/limits#queries).
    total: typing.Optional[int]
    #: [CustomObjects](ctp:api:type:CustomObject) matching the query.
    results: typing.List["CustomObject"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["CustomObject"]
    ):
        self.limit = limit
        self.offset = offset
        self.count = count
        self.total = total
        self.results = results

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomObjectPagedQueryResponse":
        from ._schemas.custom_object import CustomObjectPagedQueryResponseSchema

        return CustomObjectPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.custom_object import CustomObjectPagedQueryResponseSchema

        return CustomObjectPagedQueryResponseSchema().dump(self)


class CustomObjectReference(Reference):
    """[Reference](ctp:api:type:Reference) to a [CustomObject](ctp:api:type:CustomObject)."""

    #: Contains the representation of the expanded CustomObject. Only present in responses to requests with [Reference Expansion](/../api/general-concepts#reference-expansion) for CustomObjects.
    obj: typing.Optional["CustomObject"]

    def __init__(self, *, id: str, obj: typing.Optional["CustomObject"] = None):
        self.obj = obj

        super().__init__(id=id, type_id=ReferenceTypeId.KEY_VALUE_DOCUMENT)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomObjectReference":
        from ._schemas.custom_object import CustomObjectReferenceSchema

        return CustomObjectReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.custom_object import CustomObjectReferenceSchema

        return CustomObjectReferenceSchema().dump(self)

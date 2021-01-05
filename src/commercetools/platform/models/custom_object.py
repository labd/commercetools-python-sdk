# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, ReferenceTypeId


class CustomObject(BaseResource):
    last_modified_by: typing.Optional["LastModifiedBy"]
    created_by: typing.Optional["CreatedBy"]
    #: A namespace to group custom objects.
    container: "str"
    key: "str"
    value: "any"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        container: "str",
        key: "str",
        value: "any"
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
    #: A namespace to group custom objects.
    container: "str"
    #: A user-defined key that is unique within the given container.
    key: "str"
    value: "any"
    version: typing.Optional["int"]

    def __init__(
        self,
        *,
        container: "str",
        key: "str",
        value: "any",
        version: typing.Optional["int"] = None
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
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["CustomObject"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["CustomObject"]
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
    ) -> "CustomObjectPagedQueryResponse":
        from ._schemas.custom_object import CustomObjectPagedQueryResponseSchema

        return CustomObjectPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.custom_object import CustomObjectPagedQueryResponseSchema

        return CustomObjectPagedQueryResponseSchema().dump(self)


class CustomObjectReference(Reference):
    obj: typing.Optional["CustomObject"]

    def __init__(self, *, id: "str", obj: typing.Optional["CustomObject"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.KEY_VALUE_DOCUMENT)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomObjectReference":
        from ._schemas.custom_object import CustomObjectReferenceSchema

        return CustomObjectReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.custom_object import CustomObjectReferenceSchema

        return CustomObjectReferenceSchema().dump(self)

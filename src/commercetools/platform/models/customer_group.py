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
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, ReferenceTypeId
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "CustomerGroup",
    "CustomerGroupChangeNameAction",
    "CustomerGroupDraft",
    "CustomerGroupPagedQueryResponse",
    "CustomerGroupReference",
    "CustomerGroupResourceIdentifier",
    "CustomerGroupSetCustomFieldAction",
    "CustomerGroupSetCustomTypeAction",
    "CustomerGroupSetKeyAction",
    "CustomerGroupUpdate",
    "CustomerGroupUpdateAction",
]


class CustomerGroup(BaseResource):
    #: IDs and references that last modified the CustomerGroup.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: IDs and references that created the CustomerGroup.
    created_by: typing.Optional["CreatedBy"]
    #: User-defined unique identifier for the CustomerGroup.
    key: typing.Optional[str]
    #: Unique name of the CustomerGroup.
    name: str
    #: Custom Fields for the CustomerGroup.
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
        name: str,
        custom: typing.Optional["CustomFields"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.custom = custom

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerGroup":
        from ._schemas.customer_group import CustomerGroupSchema

        return CustomerGroupSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupSchema

        return CustomerGroupSchema().dump(self)


class CustomerGroupDraft(_BaseType):
    #: User-defined unique identifier for the CustomerGroup.
    key: typing.Optional[str]
    #: Unique value which must be different from any value used for `name` in [CustomerGroup](ctp:api:type:CustomerGroup) in the Project.
    #: If not, a [DuplicateField](ctp:api:type:DuplicateFieldError) error is returned.
    group_name: str
    #: Custom Fields for the CustomerGroup.
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        group_name: str,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.key = key
        self.group_name = group_name
        self.custom = custom

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerGroupDraft":
        from ._schemas.customer_group import CustomerGroupDraftSchema

        return CustomerGroupDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupDraftSchema

        return CustomerGroupDraftSchema().dump(self)


class CustomerGroupPagedQueryResponse(_BaseType):
    """[PagedQueryResult](/general-concepts#pagedqueryresult) with `results` containing an array of [CustomerGroup](ctp:api:type:CustomerGroup)."""

    #: Number of [results requested](/../api/general-concepts#limit).
    limit: int
    #: Number of [elements skipped](/../api/general-concepts#offset).
    offset: int
    #: Actual number of results returned.
    count: int
    #: Total number of results matching the query.
    #: This number is an estimation that is not [strongly consistent](/../api/general-concepts#strong-consistency).
    #: This field is returned by default.
    #: For improved performance, calculating this field can be deactivated by using the query parameter `withTotal=false`.
    #: When the results are filtered with a [Query Predicate](/../api/predicates/query), `total` is subject to a [limit](/../api/limits#queries).
    total: typing.Optional[int]
    #: [CustomerGroups](ctp:api:type:CustomerGroup) matching the query.
    results: typing.List["CustomerGroup"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["CustomerGroup"]
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
    ) -> "CustomerGroupPagedQueryResponse":
        from ._schemas.customer_group import CustomerGroupPagedQueryResponseSchema

        return CustomerGroupPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupPagedQueryResponseSchema

        return CustomerGroupPagedQueryResponseSchema().dump(self)


class CustomerGroupReference(Reference):
    """[Reference](ctp:api:type:Reference) to a [CustomerGroup](ctp:api:type:CustomerGroup)."""

    #: Contains the representation of the expanded CustomerGroup. Only present in responses to requests with [Reference Expansion](/../api/general-concepts#reference-expansion) for CustomerGroups.
    obj: typing.Optional["CustomerGroup"]

    def __init__(self, *, id: str, obj: typing.Optional["CustomerGroup"] = None):
        self.obj = obj

        super().__init__(id=id, type_id=ReferenceTypeId.CUSTOMER_GROUP)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerGroupReference":
        from ._schemas.customer_group import CustomerGroupReferenceSchema

        return CustomerGroupReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupReferenceSchema

        return CustomerGroupReferenceSchema().dump(self)


class CustomerGroupResourceIdentifier(ResourceIdentifier):
    """[ResourceIdentifier](ctp:api:type:ResourceIdentifier) to a [CustomerGroup](ctp:api:type:CustomerGroup). Either `id` or `key` is required. If both are set, an [InvalidJsonInput](/../api/errors#invalidjsoninput) error is returned."""

    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.CUSTOMER_GROUP)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerGroupResourceIdentifier":
        from ._schemas.customer_group import CustomerGroupResourceIdentifierSchema

        return CustomerGroupResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupResourceIdentifierSchema

        return CustomerGroupResourceIdentifierSchema().dump(self)


class CustomerGroupUpdate(_BaseType):
    #: Expected version of the CustomerGroup on which the changes should be applied.
    #: If the expected version does not match the actual version, a [ConcurrentModification](ctp:api:type:ConcurrentModificationError) error will be returned.
    version: int
    #: Update actions to be performed on the CustomerGroup.
    actions: typing.List["CustomerGroupUpdateAction"]

    def __init__(
        self, *, version: int, actions: typing.List["CustomerGroupUpdateAction"]
    ):
        self.version = version
        self.actions = actions

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerGroupUpdate":
        from ._schemas.customer_group import CustomerGroupUpdateSchema

        return CustomerGroupUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupUpdateSchema

        return CustomerGroupUpdateSchema().dump(self)


class CustomerGroupUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerGroupUpdateAction":
        if data["action"] == "changeName":
            from ._schemas.customer_group import CustomerGroupChangeNameActionSchema

            return CustomerGroupChangeNameActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.customer_group import CustomerGroupSetCustomFieldActionSchema

            return CustomerGroupSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.customer_group import CustomerGroupSetCustomTypeActionSchema

            return CustomerGroupSetCustomTypeActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.customer_group import CustomerGroupSetKeyActionSchema

            return CustomerGroupSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupUpdateActionSchema

        return CustomerGroupUpdateActionSchema().dump(self)


class CustomerGroupChangeNameAction(CustomerGroupUpdateAction):
    #: New name of the CustomerGroup.
    name: str

    def __init__(self, *, name: str):
        self.name = name

        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerGroupChangeNameAction":
        from ._schemas.customer_group import CustomerGroupChangeNameActionSchema

        return CustomerGroupChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupChangeNameActionSchema

        return CustomerGroupChangeNameActionSchema().dump(self)


class CustomerGroupSetCustomFieldAction(CustomerGroupUpdateAction):
    #: Name of the [Custom Field](/../api/projects/custom-fields).
    name: str
    #: If `value` is absent or `null`, this field will be removed if it exists.
    #: Removing a field that does not exist returns an [InvalidOperation](ctp:api:type:InvalidOperationError) error.
    #: If `value` is provided, it is set for the field defined by `name`.
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value

        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerGroupSetCustomFieldAction":
        from ._schemas.customer_group import CustomerGroupSetCustomFieldActionSchema

        return CustomerGroupSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupSetCustomFieldActionSchema

        return CustomerGroupSetCustomFieldActionSchema().dump(self)


class CustomerGroupSetCustomTypeAction(CustomerGroupUpdateAction):
    """This action sets or removes the custom type for an existing CustomerGroup.
    If present, this action overwrites any existing [custom](/../api/projects/custom-fields) type and fields.

    """

    #: Defines the [Type](ctp:api:type:Type) that extends the CustomerGroup with [Custom Fields](/../api/projects/custom-fields).
    #: If absent, any existing Type and Custom Fields are removed from the CustomerGroup.
    type: typing.Optional["TypeResourceIdentifier"]
    #: Sets the [Custom Fields](/../api/projects/custom-fields) fields for the CustomerGroup.
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
    ) -> "CustomerGroupSetCustomTypeAction":
        from ._schemas.customer_group import CustomerGroupSetCustomTypeActionSchema

        return CustomerGroupSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupSetCustomTypeActionSchema

        return CustomerGroupSetCustomTypeActionSchema().dump(self)


class CustomerGroupSetKeyAction(CustomerGroupUpdateAction):
    #: If `key` is absent or `null`, the existing key, if any, will be removed.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key

        super().__init__(action="setKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerGroupSetKeyAction":
        from ._schemas.customer_group import CustomerGroupSetKeyActionSchema

        return CustomerGroupSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupSetKeyActionSchema

        return CustomerGroupSetKeyActionSchema().dump(self)

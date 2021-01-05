# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, ReferenceTypeId
    from .type import CustomFields, FieldContainer, TypeResourceIdentifier


class CustomerGroup(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    #: User-specific unique identifier for the customer group.
    key: typing.Optional["str"]
    name: "str"
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional["str"] = None,
        name: "str",
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
    #: User-specific unique identifier for the customer group.
    key: typing.Optional["str"]
    group_name: "str"
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        key: typing.Optional["str"] = None,
        group_name: "str",
        custom: typing.Optional["CustomFields"] = None
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
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["CustomerGroup"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["CustomerGroup"]
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
    ) -> "CustomerGroupPagedQueryResponse":
        from ._schemas.customer_group import CustomerGroupPagedQueryResponseSchema

        return CustomerGroupPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupPagedQueryResponseSchema

        return CustomerGroupPagedQueryResponseSchema().dump(self)


class CustomerGroupReference(Reference):
    obj: typing.Optional["CustomerGroup"]

    def __init__(self, *, id: "str", obj: typing.Optional["CustomerGroup"] = None):
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
    def __init__(
        self, *, id: typing.Optional["str"] = None, key: typing.Optional["str"] = None
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
    version: "int"
    actions: typing.List["CustomerGroupUpdateAction"]

    def __init__(
        self, *, version: "int", actions: typing.List["CustomerGroupUpdateAction"]
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
    action: "str"

    def __init__(self, *, action: "str"):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerGroupUpdateAction":
        from ._schemas.customer_group import CustomerGroupUpdateActionSchema

        return CustomerGroupUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.customer_group import CustomerGroupUpdateActionSchema

        return CustomerGroupUpdateActionSchema().dump(self)


class CustomerGroupChangeNameAction(CustomerGroupUpdateAction):
    name: "str"

    def __init__(self, *, name: "str"):
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
    name: "str"
    value: typing.Optional["any"]

    def __init__(self, *, name: "str", value: typing.Optional["any"] = None):
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
    #: If absent, the custom type and any existing CustomFields are removed.
    type: typing.Optional["TypeResourceIdentifier"]
    #: A valid JSON object, based on the FieldDefinitions of the Type.
    #: Sets the custom fields to this value.
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
    #: User-specific unique identifier for the customer group.
    key: typing.Optional["str"]

    def __init__(self, *, key: typing.Optional["str"] = None):
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

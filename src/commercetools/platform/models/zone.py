# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, ReferenceTypeId


class Location(_BaseType):
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: "str"
    state: typing.Optional["str"]

    def __init__(self, *, country: "str", state: typing.Optional["str"] = None):
        self.country = country
        self.state = state
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Location":
        from ._schemas.zone import LocationSchema

        return LocationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import LocationSchema

        return LocationSchema().dump(self)


class Zone(BaseResource):
    last_modified_by: typing.Optional["LastModifiedBy"]
    created_by: typing.Optional["CreatedBy"]
    #: User-specific unique identifier for a zone.
    #: Must be unique across a project.
    #: The field can be reset using the Set Key UpdateAction.
    key: typing.Optional["str"]
    name: "str"
    description: typing.Optional["str"]
    locations: typing.List["Location"]

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
        description: typing.Optional["str"] = None,
        locations: typing.List["Location"]
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.description = description
        self.locations = locations
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Zone":
        from ._schemas.zone import ZoneSchema

        return ZoneSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneSchema

        return ZoneSchema().dump(self)


class ZoneDraft(_BaseType):
    #: User-specific unique identifier for a zone.
    #: Must be unique across a project.
    #: The field can be reset using the Set Key UpdateAction.
    key: typing.Optional["str"]
    name: "str"
    description: typing.Optional["str"]
    locations: typing.List["Location"]

    def __init__(
        self,
        *,
        key: typing.Optional["str"] = None,
        name: "str",
        description: typing.Optional["str"] = None,
        locations: typing.List["Location"]
    ):
        self.key = key
        self.name = name
        self.description = description
        self.locations = locations
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneDraft":
        from ._schemas.zone import ZoneDraftSchema

        return ZoneDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneDraftSchema

        return ZoneDraftSchema().dump(self)


class ZonePagedQueryResponse(_BaseType):
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["Zone"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["Zone"]
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
    ) -> "ZonePagedQueryResponse":
        from ._schemas.zone import ZonePagedQueryResponseSchema

        return ZonePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZonePagedQueryResponseSchema

        return ZonePagedQueryResponseSchema().dump(self)


class ZoneReference(Reference):
    obj: typing.Optional["Zone"]

    def __init__(self, *, id: "str", obj: typing.Optional["Zone"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.ZONE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneReference":
        from ._schemas.zone import ZoneReferenceSchema

        return ZoneReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneReferenceSchema

        return ZoneReferenceSchema().dump(self)


class ZoneResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional["str"] = None, key: typing.Optional["str"] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.ZONE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ZoneResourceIdentifier":
        from ._schemas.zone import ZoneResourceIdentifierSchema

        return ZoneResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneResourceIdentifierSchema

        return ZoneResourceIdentifierSchema().dump(self)


class ZoneUpdate(_BaseType):
    version: "int"
    actions: typing.List["ZoneUpdateAction"]

    def __init__(self, *, version: "int", actions: typing.List["ZoneUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneUpdate":
        from ._schemas.zone import ZoneUpdateSchema

        return ZoneUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneUpdateSchema

        return ZoneUpdateSchema().dump(self)


class ZoneUpdateAction(_BaseType):
    action: "str"

    def __init__(self, *, action: "str"):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneUpdateAction":
        from ._schemas.zone import ZoneUpdateActionSchema

        return ZoneUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneUpdateActionSchema

        return ZoneUpdateActionSchema().dump(self)


class ZoneAddLocationAction(ZoneUpdateAction):
    location: "Location"

    def __init__(self, *, location: "Location"):
        self.location = location
        super().__init__(action="addLocation")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneAddLocationAction":
        from ._schemas.zone import ZoneAddLocationActionSchema

        return ZoneAddLocationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneAddLocationActionSchema

        return ZoneAddLocationActionSchema().dump(self)


class ZoneChangeNameAction(ZoneUpdateAction):
    name: "str"

    def __init__(self, *, name: "str"):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneChangeNameAction":
        from ._schemas.zone import ZoneChangeNameActionSchema

        return ZoneChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneChangeNameActionSchema

        return ZoneChangeNameActionSchema().dump(self)


class ZoneRemoveLocationAction(ZoneUpdateAction):
    location: "Location"

    def __init__(self, *, location: "Location"):
        self.location = location
        super().__init__(action="removeLocation")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ZoneRemoveLocationAction":
        from ._schemas.zone import ZoneRemoveLocationActionSchema

        return ZoneRemoveLocationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneRemoveLocationActionSchema

        return ZoneRemoveLocationActionSchema().dump(self)


class ZoneSetDescriptionAction(ZoneUpdateAction):
    description: typing.Optional["str"]

    def __init__(self, *, description: typing.Optional["str"] = None):
        self.description = description
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ZoneSetDescriptionAction":
        from ._schemas.zone import ZoneSetDescriptionActionSchema

        return ZoneSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneSetDescriptionActionSchema

        return ZoneSetDescriptionActionSchema().dump(self)


class ZoneSetKeyAction(ZoneUpdateAction):
    #: If `key` is absent or `null`, this field will be removed if it exists.
    key: typing.Optional["str"]

    def __init__(self, *, key: typing.Optional["str"] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneSetKeyAction":
        from ._schemas.zone import ZoneSetKeyActionSchema

        return ZoneSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneSetKeyActionSchema

        return ZoneSetKeyActionSchema().dump(self)

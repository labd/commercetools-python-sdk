# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import (
        Address,
        CreatedBy,
        GeoJson,
        LastModifiedBy,
        LocalizedString,
        ReferenceTypeId,
    )
    from .review import ReviewRatingStatistics
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )


class Channel(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    #: Any arbitrary string key that uniquely identifies this channel within the project.
    key: "str"
    #: The roles of this channel.
    #: Each channel must have at least one role.
    roles: typing.List["ChannelRoleEnum"]
    #: A human-readable name of the channel.
    name: typing.Optional["LocalizedString"]
    #: A human-readable description of the channel.
    description: typing.Optional["LocalizedString"]
    #: The address where this channel is located (e.g.
    #: if the channel is a physical store).
    address: typing.Optional["Address"]
    #: Statistics about the review ratings taken into account for this channel.
    review_rating_statistics: typing.Optional["ReviewRatingStatistics"]
    custom: typing.Optional["CustomFields"]
    #: A GeoJSON geometry object encoding the geo location of the channel.
    geo_location: typing.Optional["GeoJson"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: "str",
        roles: typing.List["ChannelRoleEnum"],
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        address: typing.Optional["Address"] = None,
        review_rating_statistics: typing.Optional["ReviewRatingStatistics"] = None,
        custom: typing.Optional["CustomFields"] = None,
        geo_location: typing.Optional["GeoJson"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.roles = roles
        self.name = name
        self.description = description
        self.address = address
        self.review_rating_statistics = review_rating_statistics
        self.custom = custom
        self.geo_location = geo_location
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Channel":
        from ._schemas.channel import ChannelSchema

        return ChannelSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelSchema

        return ChannelSchema().dump(self)


class ChannelDraft(_BaseType):
    key: "str"
    #: If not specified, then channel will get InventorySupply role by default
    roles: typing.Optional[typing.List["ChannelRoleEnum"]]
    name: typing.Optional["LocalizedString"]
    description: typing.Optional["LocalizedString"]
    address: typing.Optional["Address"]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    geo_location: typing.Optional["GeoJson"]

    def __init__(
        self,
        *,
        key: "str",
        roles: typing.Optional[typing.List["ChannelRoleEnum"]] = None,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        address: typing.Optional["Address"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        geo_location: typing.Optional["GeoJson"] = None
    ):
        self.key = key
        self.roles = roles
        self.name = name
        self.description = description
        self.address = address
        self.custom = custom
        self.geo_location = geo_location
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ChannelDraft":
        from ._schemas.channel import ChannelDraftSchema

        return ChannelDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelDraftSchema

        return ChannelDraftSchema().dump(self)


class ChannelPagedQueryResponse(_BaseType):
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["Channel"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["Channel"]
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
    ) -> "ChannelPagedQueryResponse":
        from ._schemas.channel import ChannelPagedQueryResponseSchema

        return ChannelPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelPagedQueryResponseSchema

        return ChannelPagedQueryResponseSchema().dump(self)


class ChannelReference(Reference):
    obj: typing.Optional["Channel"]

    def __init__(self, *, id: "str", obj: typing.Optional["Channel"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.CHANNEL)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ChannelReference":
        from ._schemas.channel import ChannelReferenceSchema

        return ChannelReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelReferenceSchema

        return ChannelReferenceSchema().dump(self)


class ChannelResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional["str"] = None, key: typing.Optional["str"] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.CHANNEL)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ChannelResourceIdentifier":
        from ._schemas.channel import ChannelResourceIdentifierSchema

        return ChannelResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelResourceIdentifierSchema

        return ChannelResourceIdentifierSchema().dump(self)


class ChannelRoleEnum(enum.Enum):
    INVENTORY_SUPPLY = "InventorySupply"
    PRODUCT_DISTRIBUTION = "ProductDistribution"
    ORDER_EXPORT = "OrderExport"
    ORDER_IMPORT = "OrderImport"
    PRIMARY = "Primary"


class ChannelUpdate(_BaseType):
    version: "int"
    actions: typing.List["ChannelUpdateAction"]

    def __init__(self, *, version: "int", actions: typing.List["ChannelUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ChannelUpdate":
        from ._schemas.channel import ChannelUpdateSchema

        return ChannelUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelUpdateSchema

        return ChannelUpdateSchema().dump(self)


class ChannelUpdateAction(_BaseType):
    action: "str"

    def __init__(self, *, action: "str"):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ChannelUpdateAction":
        from ._schemas.channel import ChannelUpdateActionSchema

        return ChannelUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelUpdateActionSchema

        return ChannelUpdateActionSchema().dump(self)


class ChannelAddRolesAction(ChannelUpdateAction):
    roles: typing.List["ChannelRoleEnum"]

    def __init__(self, *, roles: typing.List["ChannelRoleEnum"]):
        self.roles = roles
        super().__init__(action="addRoles")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ChannelAddRolesAction":
        from ._schemas.channel import ChannelAddRolesActionSchema

        return ChannelAddRolesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelAddRolesActionSchema

        return ChannelAddRolesActionSchema().dump(self)


class ChannelChangeDescriptionAction(ChannelUpdateAction):
    description: "LocalizedString"

    def __init__(self, *, description: "LocalizedString"):
        self.description = description
        super().__init__(action="changeDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ChannelChangeDescriptionAction":
        from ._schemas.channel import ChannelChangeDescriptionActionSchema

        return ChannelChangeDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelChangeDescriptionActionSchema

        return ChannelChangeDescriptionActionSchema().dump(self)


class ChannelChangeKeyAction(ChannelUpdateAction):
    key: "str"

    def __init__(self, *, key: "str"):
        self.key = key
        super().__init__(action="changeKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ChannelChangeKeyAction":
        from ._schemas.channel import ChannelChangeKeyActionSchema

        return ChannelChangeKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelChangeKeyActionSchema

        return ChannelChangeKeyActionSchema().dump(self)


class ChannelChangeNameAction(ChannelUpdateAction):
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString"):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ChannelChangeNameAction":
        from ._schemas.channel import ChannelChangeNameActionSchema

        return ChannelChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelChangeNameActionSchema

        return ChannelChangeNameActionSchema().dump(self)


class ChannelRemoveRolesAction(ChannelUpdateAction):
    roles: typing.List["ChannelRoleEnum"]

    def __init__(self, *, roles: typing.List["ChannelRoleEnum"]):
        self.roles = roles
        super().__init__(action="removeRoles")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ChannelRemoveRolesAction":
        from ._schemas.channel import ChannelRemoveRolesActionSchema

        return ChannelRemoveRolesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelRemoveRolesActionSchema

        return ChannelRemoveRolesActionSchema().dump(self)


class ChannelSetAddressAction(ChannelUpdateAction):
    address: typing.Optional["Address"]

    def __init__(self, *, address: typing.Optional["Address"] = None):
        self.address = address
        super().__init__(action="setAddress")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ChannelSetAddressAction":
        from ._schemas.channel import ChannelSetAddressActionSchema

        return ChannelSetAddressActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelSetAddressActionSchema

        return ChannelSetAddressActionSchema().dump(self)


class ChannelSetCustomFieldAction(ChannelUpdateAction):
    name: "str"
    value: typing.Optional["any"]

    def __init__(self, *, name: "str", value: typing.Optional["any"] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ChannelSetCustomFieldAction":
        from ._schemas.channel import ChannelSetCustomFieldActionSchema

        return ChannelSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelSetCustomFieldActionSchema

        return ChannelSetCustomFieldActionSchema().dump(self)


class ChannelSetCustomTypeAction(ChannelUpdateAction):
    type: typing.Optional["TypeResourceIdentifier"]
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
    ) -> "ChannelSetCustomTypeAction":
        from ._schemas.channel import ChannelSetCustomTypeActionSchema

        return ChannelSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelSetCustomTypeActionSchema

        return ChannelSetCustomTypeActionSchema().dump(self)


class ChannelSetGeoLocationAction(ChannelUpdateAction):
    geo_location: typing.Optional["GeoJson"]

    def __init__(self, *, geo_location: typing.Optional["GeoJson"] = None):
        self.geo_location = geo_location
        super().__init__(action="setGeoLocation")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ChannelSetGeoLocationAction":
        from ._schemas.channel import ChannelSetGeoLocationActionSchema

        return ChannelSetGeoLocationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelSetGeoLocationActionSchema

        return ChannelSetGeoLocationActionSchema().dump(self)


class ChannelSetRolesAction(ChannelUpdateAction):
    roles: typing.List["ChannelRoleEnum"]

    def __init__(self, *, roles: typing.List["ChannelRoleEnum"]):
        self.roles = roles
        super().__init__(action="setRoles")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ChannelSetRolesAction":
        from ._schemas.channel import ChannelSetRolesActionSchema

        return ChannelSetRolesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.channel import ChannelSetRolesActionSchema

        return ChannelSetRolesActionSchema().dump(self)

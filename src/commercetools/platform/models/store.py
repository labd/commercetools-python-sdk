# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import (
    BaseResource,
    KeyReference,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from .channel import ChannelReference, ChannelResourceIdentifier
    from .common import CreatedBy, LastModifiedBy, LocalizedString, ReferenceTypeId

__all__ = [
    "Store",
    "StoreDraft",
    "StoreKeyReference",
    "StorePagedQueryResponse",
    "StoreReference",
    "StoreResourceIdentifier",
    "StoreSetLanguagesAction",
    "StoreSetNameAction",
    "StoreUpdate",
    "StoreUpdateAction",
    "StoresAddDistributionChannelsAction",
    "StoresAddSupplyChannelsAction",
    "StoresRemoveDistributionChannelsAction",
    "StoresRemoveSupplyChannelsAction",
    "StoresSetDistributionChannelsAction",
    "StoresSetSupplyChannelsAction",
]


class Store(BaseResource):
    last_modified_by: typing.Optional["LastModifiedBy"]
    created_by: typing.Optional["CreatedBy"]
    #: User-specific unique identifier for the store.
    #: The `key` is mandatory and immutable.
    #: It is used to reference the store.
    key: str
    #: The name of the store
    name: typing.Optional["LocalizedString"]
    languages: typing.Optional[typing.List["str"]]
    #: Set of References to a Channel with `ProductDistribution` role
    distribution_channels: typing.List["ChannelReference"]
    #: Set of ResourceIdentifiers of Channels with `InventorySupply` role
    supply_channels: typing.Optional[typing.List["ChannelReference"]]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: str,
        name: typing.Optional["LocalizedString"] = None,
        languages: typing.Optional[typing.List["str"]] = None,
        distribution_channels: typing.List["ChannelReference"],
        supply_channels: typing.Optional[typing.List["ChannelReference"]] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.languages = languages
        self.distribution_channels = distribution_channels
        self.supply_channels = supply_channels
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Store":
        from ._schemas.store import StoreSchema

        return StoreSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSchema

        return StoreSchema().dump(self)


class StoreDraft(_BaseType):
    #: User-specific unique identifier for the store.
    #: The `key` is mandatory and immutable.
    #: It is used to reference the store.
    key: str
    #: The name of the store
    name: "LocalizedString"
    languages: typing.Optional[typing.List["str"]]
    #: Set of ResourceIdentifiers to a Channel with `ProductDistribution` role
    distribution_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]
    #: Set of ResourceIdentifiers of Channels with `InventorySupply` role
    supply_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]

    def __init__(
        self,
        *,
        key: str,
        name: "LocalizedString",
        languages: typing.Optional[typing.List["str"]] = None,
        distribution_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None,
        supply_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None
    ):
        self.key = key
        self.name = name
        self.languages = languages
        self.distribution_channels = distribution_channels
        self.supply_channels = supply_channels
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreDraft":
        from ._schemas.store import StoreDraftSchema

        return StoreDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreDraftSchema

        return StoreDraftSchema().dump(self)


class StoreKeyReference(KeyReference):
    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceTypeId.STORE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreKeyReference":
        from ._schemas.store import StoreKeyReferenceSchema

        return StoreKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreKeyReferenceSchema

        return StoreKeyReferenceSchema().dump(self)


class StorePagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["Store"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["Store"]
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
    ) -> "StorePagedQueryResponse":
        from ._schemas.store import StorePagedQueryResponseSchema

        return StorePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StorePagedQueryResponseSchema

        return StorePagedQueryResponseSchema().dump(self)


class StoreReference(Reference):
    obj: typing.Optional["Store"]

    def __init__(self, *, id: str, obj: typing.Optional["Store"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.STORE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreReference":
        from ._schemas.store import StoreReferenceSchema

        return StoreReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreReferenceSchema

        return StoreReferenceSchema().dump(self)


class StoreResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.STORE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreResourceIdentifier":
        from ._schemas.store import StoreResourceIdentifierSchema

        return StoreResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreResourceIdentifierSchema

        return StoreResourceIdentifierSchema().dump(self)


class StoreUpdate(_BaseType):
    version: int
    actions: typing.List["StoreUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["StoreUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreUpdate":
        from ._schemas.store import StoreUpdateSchema

        return StoreUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreUpdateSchema

        return StoreUpdateSchema().dump(self)


class StoreUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreUpdateAction":
        if data["action"] == "setLanguages":
            from ._schemas.store import StoreSetLanguagesActionSchema

            return StoreSetLanguagesActionSchema().load(data)
        if data["action"] == "setName":
            from ._schemas.store import StoreSetNameActionSchema

            return StoreSetNameActionSchema().load(data)
        if data["action"] == "addDistributionChannel":
            from ._schemas.store import StoresAddDistributionChannelsActionSchema

            return StoresAddDistributionChannelsActionSchema().load(data)
        if data["action"] == "addSupplyChannel":
            from ._schemas.store import StoresAddSupplyChannelsActionSchema

            return StoresAddSupplyChannelsActionSchema().load(data)
        if data["action"] == "removeDistributionChannel":
            from ._schemas.store import StoresRemoveDistributionChannelsActionSchema

            return StoresRemoveDistributionChannelsActionSchema().load(data)
        if data["action"] == "removeSupplyChannel":
            from ._schemas.store import StoresRemoveSupplyChannelsActionSchema

            return StoresRemoveSupplyChannelsActionSchema().load(data)
        if data["action"] == "setDistributionChannels":
            from ._schemas.store import StoresSetDistributionChannelsActionSchema

            return StoresSetDistributionChannelsActionSchema().load(data)
        if data["action"] == "setSupplyChannels":
            from ._schemas.store import StoresSetSupplyChannelsActionSchema

            return StoresSetSupplyChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreUpdateActionSchema

        return StoreUpdateActionSchema().dump(self)


class StoreSetLanguagesAction(StoreUpdateAction):
    languages: typing.Optional[typing.List["str"]]

    def __init__(self, *, languages: typing.Optional[typing.List["str"]] = None):
        self.languages = languages
        super().__init__(action="setLanguages")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetLanguagesAction":
        from ._schemas.store import StoreSetLanguagesActionSchema

        return StoreSetLanguagesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetLanguagesActionSchema

        return StoreSetLanguagesActionSchema().dump(self)


class StoreSetNameAction(StoreUpdateAction):
    #: The updated name of the store
    name: typing.Optional["LocalizedString"]

    def __init__(self, *, name: typing.Optional["LocalizedString"] = None):
        self.name = name
        super().__init__(action="setName")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreSetNameAction":
        from ._schemas.store import StoreSetNameActionSchema

        return StoreSetNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetNameActionSchema

        return StoreSetNameActionSchema().dump(self)


class StoresAddDistributionChannelsAction(StoreUpdateAction):
    distribution_channel: "ChannelResourceIdentifier"

    def __init__(self, *, distribution_channel: "ChannelResourceIdentifier"):
        self.distribution_channel = distribution_channel
        super().__init__(action="addDistributionChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoresAddDistributionChannelsAction":
        from ._schemas.store import StoresAddDistributionChannelsActionSchema

        return StoresAddDistributionChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoresAddDistributionChannelsActionSchema

        return StoresAddDistributionChannelsActionSchema().dump(self)


class StoresAddSupplyChannelsAction(StoreUpdateAction):
    supply_channel: "ChannelResourceIdentifier"

    def __init__(self, *, supply_channel: "ChannelResourceIdentifier"):
        self.supply_channel = supply_channel
        super().__init__(action="addSupplyChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoresAddSupplyChannelsAction":
        from ._schemas.store import StoresAddSupplyChannelsActionSchema

        return StoresAddSupplyChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoresAddSupplyChannelsActionSchema

        return StoresAddSupplyChannelsActionSchema().dump(self)


class StoresRemoveDistributionChannelsAction(StoreUpdateAction):
    distribution_channel: "ChannelResourceIdentifier"

    def __init__(self, *, distribution_channel: "ChannelResourceIdentifier"):
        self.distribution_channel = distribution_channel
        super().__init__(action="removeDistributionChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoresRemoveDistributionChannelsAction":
        from ._schemas.store import StoresRemoveDistributionChannelsActionSchema

        return StoresRemoveDistributionChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoresRemoveDistributionChannelsActionSchema

        return StoresRemoveDistributionChannelsActionSchema().dump(self)


class StoresRemoveSupplyChannelsAction(StoreUpdateAction):
    supply_channel: "ChannelResourceIdentifier"

    def __init__(self, *, supply_channel: "ChannelResourceIdentifier"):
        self.supply_channel = supply_channel
        super().__init__(action="removeSupplyChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoresRemoveSupplyChannelsAction":
        from ._schemas.store import StoresRemoveSupplyChannelsActionSchema

        return StoresRemoveSupplyChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoresRemoveSupplyChannelsActionSchema

        return StoresRemoveSupplyChannelsActionSchema().dump(self)


class StoresSetDistributionChannelsAction(StoreUpdateAction):
    distribution_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]

    def __init__(
        self,
        *,
        distribution_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None
    ):
        self.distribution_channels = distribution_channels
        super().__init__(action="setDistributionChannels")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoresSetDistributionChannelsAction":
        from ._schemas.store import StoresSetDistributionChannelsActionSchema

        return StoresSetDistributionChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoresSetDistributionChannelsActionSchema

        return StoresSetDistributionChannelsActionSchema().dump(self)


class StoresSetSupplyChannelsAction(StoreUpdateAction):
    supply_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]

    def __init__(
        self,
        *,
        supply_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None
    ):
        self.supply_channels = supply_channels
        super().__init__(action="setSupplyChannels")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoresSetSupplyChannelsAction":
        from ._schemas.store import StoresSetSupplyChannelsActionSchema

        return StoresSetSupplyChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoresSetSupplyChannelsActionSchema

        return StoresSetSupplyChannelsActionSchema().dump(self)

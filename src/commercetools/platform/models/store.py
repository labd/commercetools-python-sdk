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
    from .product_selection import (
        ProductSelectionReference,
        ProductSelectionResourceIdentifier,
    )
    from .store_country import StoreCountry
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "ProductSelectionSetting",
    "ProductSelectionSettingDraft",
    "Store",
    "StoreAddCountryAction",
    "StoreAddDistributionChannelAction",
    "StoreAddProductSelectionAction",
    "StoreAddSupplyChannelAction",
    "StoreChangeProductSelectionAction",
    "StoreDraft",
    "StoreKeyReference",
    "StorePagedQueryResponse",
    "StoreReference",
    "StoreRemoveCountryAction",
    "StoreRemoveDistributionChannelAction",
    "StoreRemoveProductSelectionAction",
    "StoreRemoveSupplyChannelAction",
    "StoreResourceIdentifier",
    "StoreSetCountriesAction",
    "StoreSetCustomFieldAction",
    "StoreSetCustomTypeAction",
    "StoreSetDistributionChannelsAction",
    "StoreSetLanguagesAction",
    "StoreSetNameAction",
    "StoreSetProductSelectionsAction",
    "StoreSetSupplyChannelsAction",
    "StoreUpdate",
    "StoreUpdateAction",
]


class ProductSelectionSetting(_BaseType):
    #: Reference to a ProductSelection.
    product_selection: "ProductSelectionReference"
    #: If `true`, all Products assigned to this Product Selection are part of the Store's assortment.
    active: bool

    def __init__(self, *, product_selection: "ProductSelectionReference", active: bool):
        self.product_selection = product_selection
        self.active = active

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionSetting":
        from ._schemas.store import ProductSelectionSettingSchema

        return ProductSelectionSettingSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import ProductSelectionSettingSchema

        return ProductSelectionSettingSchema().dump(self)


class ProductSelectionSettingDraft(_BaseType):
    #: Resource Identifier of a ProductSelection.
    product_selection: "ProductSelectionResourceIdentifier"
    #: Set to `true` if all Products assigned to the Product Selection should become part of the Store's assortment.
    active: typing.Optional[bool]

    def __init__(
        self,
        *,
        product_selection: "ProductSelectionResourceIdentifier",
        active: typing.Optional[bool] = None
    ):
        self.product_selection = product_selection
        self.active = active

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionSettingDraft":
        from ._schemas.store import ProductSelectionSettingDraftSchema

        return ProductSelectionSettingDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import ProductSelectionSettingDraftSchema

        return ProductSelectionSettingDraftSchema().dump(self)


class Store(BaseResource):
    #: IDs and references that last modified the Store.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: IDs and references that created the Store.
    created_by: typing.Optional["CreatedBy"]
    #: User-defined unique and immutable identifier for the Store.
    key: str
    #: Name of the Store.
    name: typing.Optional["LocalizedString"]
    #: Languages configured for the Store.
    languages: typing.List["str"]
    #: Countries defined for the Store.
    countries: typing.List["StoreCountry"]
    #: Product Distribution Channels allowed for the Store.
    distribution_channels: typing.List["ChannelReference"]
    #: Inventory Supply Channels allowed for the Store.
    supply_channels: typing.List["ChannelReference"]
    #: Controls availability of Products for this Store via Product Selections:
    #:
    #: - Leave empty if all Products in the [Project](ctp:api:type:Project) should be available in this Store.
    #: - If only `inactive` Product Selections with `IndividualExclusion` [ProductSelectionMode](ctp:api:type:ProductSelectionMode) are provided, all the Products are availlable in this Store.
    #: - If all the Product Selections provided are `inactive` and there's at least a Product Selection of mode `Individual`, no Product is availlable in this Store.
    #: - If at least an `active` Product Selection is provided, only `active` Product Selections are considered to compute the availlability in this Store.
    product_selections: typing.List["ProductSelectionSetting"]
    #: Custom fields for the Store.
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
        key: str,
        name: typing.Optional["LocalizedString"] = None,
        languages: typing.List["str"],
        countries: typing.List["StoreCountry"],
        distribution_channels: typing.List["ChannelReference"],
        supply_channels: typing.List["ChannelReference"],
        product_selections: typing.List["ProductSelectionSetting"],
        custom: typing.Optional["CustomFields"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.languages = languages
        self.countries = countries
        self.distribution_channels = distribution_channels
        self.supply_channels = supply_channels
        self.product_selections = product_selections
        self.custom = custom

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
    #: User-defined unique and immutable identifier for the Store.
    #: Keys can only contain alphanumeric characters, underscores, and hyphens.
    key: str
    #: Name of the Store.
    name: typing.Optional["LocalizedString"]
    #: Languages defined in [Project](ctp:api:type:Project). Only languages defined in the Project can be used.
    languages: typing.Optional[typing.List["str"]]
    #: Countries defined for the Store.
    countries: typing.Optional[typing.List["StoreCountry"]]
    #: ResourceIdentifier of a Channel with `ProductDistribution` [ChannelRoleEnum](ctp:api:type:ChannelRoleEnum).
    distribution_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]
    #: ResourceIdentifier of a Channel with `InventorySupply` [ChannelRoleEnum](ctp:api:type:ChannelRoleEnum).
    supply_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]
    #: Controls availability of Products for this Store via active/inactive Product Selections:
    #:
    #: - Leave empty if all Products in the [Project](ctp:api:type:Project) should be available in this Store.
    #: - If only `inactive` Product Selections with `IndividualExclusion` [ProductSelectionMode](ctp:api:type:ProductSelectionMode) are provided, all the Products are available in this Store.
    #: - If all the Product Selections provided are `inactive` and there's at least a Product Selection of mode `Individual`, no Product is available in this Store.
    #: - If at least an `active` Product Selection is provided, only `active` Product Selections are considered to compute the availability in this Store.
    product_selections: typing.Optional[typing.List["ProductSelectionSettingDraft"]]
    #: Custom fields for the Store.
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        key: str,
        name: typing.Optional["LocalizedString"] = None,
        languages: typing.Optional[typing.List["str"]] = None,
        countries: typing.Optional[typing.List["StoreCountry"]] = None,
        distribution_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None,
        supply_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None,
        product_selections: typing.Optional[
            typing.List["ProductSelectionSettingDraft"]
        ] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.key = key
        self.name = name
        self.languages = languages
        self.countries = countries
        self.distribution_channels = distribution_channels
        self.supply_channels = supply_channels
        self.product_selections = product_selections
        self.custom = custom

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreDraft":
        from ._schemas.store import StoreDraftSchema

        return StoreDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreDraftSchema

        return StoreDraftSchema().dump(self)


class StoreKeyReference(KeyReference):
    """[Reference](ctp:api:type:Reference) to a [Store](ctp:api:type:Store) by its key."""

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
    """[PagedQueryResult](/../api/general-concepts#pagedqueryresult) with results containing an array of [Store](ctp:api:type:Store)."""

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
    #: [Stores](ctp:api:type:Store) matching the query.
    results: typing.List["Store"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["Store"]
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
    ) -> "StorePagedQueryResponse":
        from ._schemas.store import StorePagedQueryResponseSchema

        return StorePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StorePagedQueryResponseSchema

        return StorePagedQueryResponseSchema().dump(self)


class StoreReference(Reference):
    """[Reference](ctp:api:type:Reference) to a [Store](ctp:api:type:Store)."""

    #: Contains the representation of the expanded Store. Only present in responses to requests with [Reference Expansion](/../api/general-concepts#reference-expansion) for Stores.
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
    """[ResourceIdentifier](ctp:api:type:ResourceIdentifier) to a [Store](ctp:api:type:Store). Either `id` or `key` is required. If both are set, an [InvalidJsonInput](/../api/errors#invalidjsoninput) error is returned."""

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
    #: Expected version of the Store on which the changes should be applied.
    #: If the expected version does not match the actual version, a [ConcurrentModification](ctp:api:type:ConcurrentModificationError) error will be returned.
    version: int
    #: Update actions to be performed on the Store.
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
        if data["action"] == "addCountry":
            from ._schemas.store import StoreAddCountryActionSchema

            return StoreAddCountryActionSchema().load(data)
        if data["action"] == "addDistributionChannel":
            from ._schemas.store import StoreAddDistributionChannelActionSchema

            return StoreAddDistributionChannelActionSchema().load(data)
        if data["action"] == "addProductSelection":
            from ._schemas.store import StoreAddProductSelectionActionSchema

            return StoreAddProductSelectionActionSchema().load(data)
        if data["action"] == "addSupplyChannel":
            from ._schemas.store import StoreAddSupplyChannelActionSchema

            return StoreAddSupplyChannelActionSchema().load(data)
        if data["action"] == "changeProductSelectionActive":
            from ._schemas.store import StoreChangeProductSelectionActionSchema

            return StoreChangeProductSelectionActionSchema().load(data)
        if data["action"] == "removeCountry":
            from ._schemas.store import StoreRemoveCountryActionSchema

            return StoreRemoveCountryActionSchema().load(data)
        if data["action"] == "removeDistributionChannel":
            from ._schemas.store import StoreRemoveDistributionChannelActionSchema

            return StoreRemoveDistributionChannelActionSchema().load(data)
        if data["action"] == "removeProductSelection":
            from ._schemas.store import StoreRemoveProductSelectionActionSchema

            return StoreRemoveProductSelectionActionSchema().load(data)
        if data["action"] == "removeSupplyChannel":
            from ._schemas.store import StoreRemoveSupplyChannelActionSchema

            return StoreRemoveSupplyChannelActionSchema().load(data)
        if data["action"] == "setCountries":
            from ._schemas.store import StoreSetCountriesActionSchema

            return StoreSetCountriesActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.store import StoreSetCustomFieldActionSchema

            return StoreSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.store import StoreSetCustomTypeActionSchema

            return StoreSetCustomTypeActionSchema().load(data)
        if data["action"] == "setDistributionChannels":
            from ._schemas.store import StoreSetDistributionChannelsActionSchema

            return StoreSetDistributionChannelsActionSchema().load(data)
        if data["action"] == "setLanguages":
            from ._schemas.store import StoreSetLanguagesActionSchema

            return StoreSetLanguagesActionSchema().load(data)
        if data["action"] == "setName":
            from ._schemas.store import StoreSetNameActionSchema

            return StoreSetNameActionSchema().load(data)
        if data["action"] == "setProductSelections":
            from ._schemas.store import StoreSetProductSelectionsActionSchema

            return StoreSetProductSelectionsActionSchema().load(data)
        if data["action"] == "setSupplyChannels":
            from ._schemas.store import StoreSetSupplyChannelsActionSchema

            return StoreSetSupplyChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreUpdateActionSchema

        return StoreUpdateActionSchema().dump(self)


class StoreAddCountryAction(StoreUpdateAction):
    """This update action produces the [StoreCountriesChanged](ctp:api:type:StoreCountriesChangedMessage) Message.
    It has no effect if the given country is already present in a Store.

    """

    #: Value to append to `countries`.
    country: "StoreCountry"

    def __init__(self, *, country: "StoreCountry"):
        self.country = country

        super().__init__(action="addCountry")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreAddCountryAction":
        from ._schemas.store import StoreAddCountryActionSchema

        return StoreAddCountryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreAddCountryActionSchema

        return StoreAddCountryActionSchema().dump(self)


class StoreAddDistributionChannelAction(StoreUpdateAction):
    """This update action produces the [StoreDistributionChannelsChanged](ctp:api:type:StoreDistributionChannelsChangedMessage) Message.
    It has no effect if a given distribution channel is already present in a Store.

    Adding a [Channel](ctp:api:type:Channel) without the `ProductDistribution` [ChannelRoleEnum](ctp:api:type:ChannelRoleEnum) returns a [MissingRoleOnChannel](ctp:api:type:MissingRoleOnChannelError) error.

    """

    #: Value to append.
    distribution_channel: "ChannelResourceIdentifier"

    def __init__(self, *, distribution_channel: "ChannelResourceIdentifier"):
        self.distribution_channel = distribution_channel

        super().__init__(action="addDistributionChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreAddDistributionChannelAction":
        from ._schemas.store import StoreAddDistributionChannelActionSchema

        return StoreAddDistributionChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreAddDistributionChannelActionSchema

        return StoreAddDistributionChannelActionSchema().dump(self)


class StoreAddProductSelectionAction(StoreUpdateAction):
    """To make all included Products available to your customers of a given Store, add the [Product Selections](/../api/projects/product-selections) to the respective Store. This action has no effect if the given Product Selection is already present in the Store and has the same `active` flag."""

    #: Product Selection to add to the Store either activated or deactivated.
    product_selection: "ProductSelectionResourceIdentifier"
    #: Set to `true` to make all Products assigned to the referenced Product Selection available in the Store.
    active: typing.Optional[bool]

    def __init__(
        self,
        *,
        product_selection: "ProductSelectionResourceIdentifier",
        active: typing.Optional[bool] = None
    ):
        self.product_selection = product_selection
        self.active = active

        super().__init__(action="addProductSelection")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreAddProductSelectionAction":
        from ._schemas.store import StoreAddProductSelectionActionSchema

        return StoreAddProductSelectionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreAddProductSelectionActionSchema

        return StoreAddProductSelectionActionSchema().dump(self)


class StoreAddSupplyChannelAction(StoreUpdateAction):
    """This action has no effect if a given supply channel is already present in a Store.

    Adding a supply channel produces the [StoreSupplyChannelsChanged](ctp:api:type:StoreSupplyChannelsChangedMessage) Message.

    Adding a [Channel](ctp:api:type:Channel) without the `InventorySupply` [ChannelRoleEnum](ctp:api:type:ChannelRoleEnum) returns a [MissingRoleOnChannel](ctp:api:type:MissingRoleOnChannelError) error.

    """

    #: Value to append.
    supply_channel: "ChannelResourceIdentifier"

    def __init__(self, *, supply_channel: "ChannelResourceIdentifier"):
        self.supply_channel = supply_channel

        super().__init__(action="addSupplyChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreAddSupplyChannelAction":
        from ._schemas.store import StoreAddSupplyChannelActionSchema

        return StoreAddSupplyChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreAddSupplyChannelActionSchema

        return StoreAddSupplyChannelActionSchema().dump(self)


class StoreChangeProductSelectionAction(StoreUpdateAction):
    """[ProductSelection](ctp:api:type:ProductSelection) in a Store can be activated or deactivated using this update action."""

    #: Current Product Selection of the Store to be activated or deactivated.
    product_selection: "ProductSelectionResourceIdentifier"
    #: Set to `true` if all Products assigned to the Product Selection should become part of the Store's assortment.
    active: typing.Optional[bool]

    def __init__(
        self,
        *,
        product_selection: "ProductSelectionResourceIdentifier",
        active: typing.Optional[bool] = None
    ):
        self.product_selection = product_selection
        self.active = active

        super().__init__(action="changeProductSelectionActive")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreChangeProductSelectionAction":
        from ._schemas.store import StoreChangeProductSelectionActionSchema

        return StoreChangeProductSelectionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreChangeProductSelectionActionSchema

        return StoreChangeProductSelectionActionSchema().dump(self)


class StoreRemoveCountryAction(StoreUpdateAction):
    """This update action produces the [StoreCountriesChanged](ctp:api:type:StoreCountriesChangedMessage) Message.
    It has no effect if a given country is not present in a Store.

    """

    #: Value to remove from `countries`.
    country: "StoreCountry"

    def __init__(self, *, country: "StoreCountry"):
        self.country = country

        super().__init__(action="removeCountry")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreRemoveCountryAction":
        from ._schemas.store import StoreRemoveCountryActionSchema

        return StoreRemoveCountryActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreRemoveCountryActionSchema

        return StoreRemoveCountryActionSchema().dump(self)


class StoreRemoveDistributionChannelAction(StoreUpdateAction):
    """This update action produces the [StoreDistributionChannelsChanged](ctp:api:type:StoreDistributionChannelsChangedMessage) Message."""

    #: Value to remove. ResourceIdentifier of a Channel with the `ProductDistribution` [ChannelRoleEnum](ctp:api:type:ChannelRoleEnum).
    distribution_channel: "ChannelResourceIdentifier"

    def __init__(self, *, distribution_channel: "ChannelResourceIdentifier"):
        self.distribution_channel = distribution_channel

        super().__init__(action="removeDistributionChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreRemoveDistributionChannelAction":
        from ._schemas.store import StoreRemoveDistributionChannelActionSchema

        return StoreRemoveDistributionChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreRemoveDistributionChannelActionSchema

        return StoreRemoveDistributionChannelActionSchema().dump(self)


class StoreRemoveProductSelectionAction(StoreUpdateAction):
    """This action has no effect if the given Product Selection is not in the Store."""

    #: Value to remove. The removed Product Selection is made offline.
    product_selection: "ProductSelectionResourceIdentifier"

    def __init__(self, *, product_selection: "ProductSelectionResourceIdentifier"):
        self.product_selection = product_selection

        super().__init__(action="removeProductSelection")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreRemoveProductSelectionAction":
        from ._schemas.store import StoreRemoveProductSelectionActionSchema

        return StoreRemoveProductSelectionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreRemoveProductSelectionActionSchema

        return StoreRemoveProductSelectionActionSchema().dump(self)


class StoreRemoveSupplyChannelAction(StoreUpdateAction):
    """This update action produces the [StoreSupplyChannelsChanged](ctp:api:type:StoreSupplyChannelsChangedMessage) Message."""

    #: Value to remove. ResourceIdentifier of a Channel with the `InventorySupply` [ChannelRoleEnum](ctp:api:type:ChannelRoleEnum).
    supply_channel: "ChannelResourceIdentifier"

    def __init__(self, *, supply_channel: "ChannelResourceIdentifier"):
        self.supply_channel = supply_channel

        super().__init__(action="removeSupplyChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreRemoveSupplyChannelAction":
        from ._schemas.store import StoreRemoveSupplyChannelActionSchema

        return StoreRemoveSupplyChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreRemoveSupplyChannelActionSchema

        return StoreRemoveSupplyChannelActionSchema().dump(self)


class StoreSetCountriesAction(StoreUpdateAction):
    """This update action produces the [StoreCountriesChanged](ctp:api:type:StoreCountriesChangedMessage) Message."""

    #: New value to set.
    countries: typing.Optional[typing.List["StoreCountry"]]

    def __init__(
        self, *, countries: typing.Optional[typing.List["StoreCountry"]] = None
    ):
        self.countries = countries

        super().__init__(action="setCountries")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetCountriesAction":
        from ._schemas.store import StoreSetCountriesActionSchema

        return StoreSetCountriesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetCountriesActionSchema

        return StoreSetCountriesActionSchema().dump(self)


class StoreSetCustomFieldAction(StoreUpdateAction):
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
    ) -> "StoreSetCustomFieldAction":
        from ._schemas.store import StoreSetCustomFieldActionSchema

        return StoreSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetCustomFieldActionSchema

        return StoreSetCustomFieldActionSchema().dump(self)


class StoreSetCustomTypeAction(StoreUpdateAction):
    #: Defines the [Type](ctp:api:type:Type) that extends the Store with [Custom Fields](/../api/projects/custom-fields).
    #: If absent, any existing Type and Custom Fields are removed from the Store.
    type: typing.Optional["TypeResourceIdentifier"]
    #: Sets the [Custom Fields](/../api/projects/custom-fields) fields for the Store.
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
    ) -> "StoreSetCustomTypeAction":
        from ._schemas.store import StoreSetCustomTypeActionSchema

        return StoreSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetCustomTypeActionSchema

        return StoreSetCustomTypeActionSchema().dump(self)


class StoreSetDistributionChannelsAction(StoreUpdateAction):
    """This update action produces the [StoreDistributionChannelsChanged](ctp:api:type:StoreDistributionChannelsChangedMessage) Message.

    Setting a [Channel](ctp:api:type:Channel) without the `ProductDistribution` [ChannelRoleEnum](ctp:api:type:ChannelRoleEnum) returns a [MissingRoleOnChannel](ctp:api:type:MissingRoleOnChannelError) error.

    """

    #: Value to set.
    #: If not defined, the Store's `distributionChannels` are unset.
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
    ) -> "StoreSetDistributionChannelsAction":
        from ._schemas.store import StoreSetDistributionChannelsActionSchema

        return StoreSetDistributionChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetDistributionChannelsActionSchema

        return StoreSetDistributionChannelsActionSchema().dump(self)


class StoreSetLanguagesAction(StoreUpdateAction):
    """This update action produces the [StoreLanguagesChanged](ctp:api:type:StoreLanguagesChangedMessage) Message.
    Adding a language other than the ones defined in the [Project](ctp:api:type:Project) returns a [ProjectNotConfiguredForLanguages](ctp:api:type:ProjectNotConfiguredForLanguagesError) error.

    """

    #: Value to set.
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
    """This update action produces the [StoreNameSet](ctp:api:type:StoreNameSetMessage) Message."""

    #: Value to set.
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


class StoreSetProductSelectionsAction(StoreUpdateAction):
    """Instead of adding or removing [Product Selections](/../api/projects/product-selections) individually, you can also change all the Store's Product Selections in one go using this update action. The Store will only contain the Product Selections specified in the request."""

    #: Value to set.
    #:
    #: - If provided, Product Selections for which `active` is set to `true` are available in the Store.
    #: - If not provided or provided as empty array, the action removes all Product Selections from this Store, meaning all Products in the [Project](ctp:api:type:Project) are available in this Store.
    product_selections: typing.Optional[typing.List["ProductSelectionSettingDraft"]]

    def __init__(
        self,
        *,
        product_selections: typing.Optional[
            typing.List["ProductSelectionSettingDraft"]
        ] = None
    ):
        self.product_selections = product_selections

        super().__init__(action="setProductSelections")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetProductSelectionsAction":
        from ._schemas.store import StoreSetProductSelectionsActionSchema

        return StoreSetProductSelectionsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetProductSelectionsActionSchema

        return StoreSetProductSelectionsActionSchema().dump(self)


class StoreSetSupplyChannelsAction(StoreUpdateAction):
    """Setting a supply channel produces the [StoreSupplyChannelsChanged](ctp:api:type:StoreSupplyChannelsChangedMessage) Message.

    Setting a [Channel](ctp:api:type:Channel) without the `InventorySupply` [ChannelRoleEnum](ctp:api:type:ChannelRoleEnum) returns a [MissingRoleOnChannel](ctp:api:type:MissingRoleOnChannelError) error.

    """

    #: Value to set.
    #: If not defined, the Store's `supplyChannels` are unset.
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
    ) -> "StoreSetSupplyChannelsAction":
        from ._schemas.store import StoreSetSupplyChannelsActionSchema

        return StoreSetSupplyChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetSupplyChannelsActionSchema

        return StoreSetSupplyChannelsActionSchema().dump(self)

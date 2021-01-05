# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, LocalizedString, ReferenceTypeId


class State(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    #: A unique identifier for the state.
    key: "str"
    type: "StateTypeEnum"
    #: A human-readable name of the state.
    name: typing.Optional["LocalizedString"]
    #: A human-readable description of the state.
    description: typing.Optional["LocalizedString"]
    #: A state can be declared as an initial state for any state machine.
    #: When a workflow starts, this first state must be an `initial` state.
    initial: "bool"
    #: Builtin states are integral parts of the project that cannot be deleted nor the key can be changed.
    built_in: "bool"
    roles: typing.Optional[typing.List["StateRoleEnum"]]
    #: Transitions are a way to describe possible transformations of the current state to other states of the same `type` (e.g.: _Initial_ -> _Shipped_).
    #: When performing a `transitionState` update action and `transitions` is set, the currently referenced state must have a transition to the new state.
    #: If `transitions` is an empty list, it means the current state is a final state and no further transitions are allowed.
    #: If `transitions` is not set, the validation is turned off.
    #: When performing a `transitionState` update action, any other state of the same `type` can be transitioned to.
    transitions: typing.Optional[typing.List["StateReference"]]

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
        type: "StateTypeEnum",
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        initial: "bool",
        built_in: "bool",
        roles: typing.Optional[typing.List["StateRoleEnum"]] = None,
        transitions: typing.Optional[typing.List["StateReference"]] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.type = type
        self.name = name
        self.description = description
        self.initial = initial
        self.built_in = built_in
        self.roles = roles
        self.transitions = transitions
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "State":
        from ._schemas.state import StateSchema

        return StateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateSchema

        return StateSchema().dump(self)


class StateDraft(_BaseType):
    key: "str"
    type: "StateTypeEnum"
    name: typing.Optional["LocalizedString"]
    description: typing.Optional["LocalizedString"]
    initial: typing.Optional["bool"]
    roles: typing.Optional[typing.List["StateRoleEnum"]]
    transitions: typing.Optional[typing.List["StateResourceIdentifier"]]

    def __init__(
        self,
        *,
        key: "str",
        type: "StateTypeEnum",
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        initial: typing.Optional["bool"] = None,
        roles: typing.Optional[typing.List["StateRoleEnum"]] = None,
        transitions: typing.Optional[typing.List["StateResourceIdentifier"]] = None
    ):
        self.key = key
        self.type = type
        self.name = name
        self.description = description
        self.initial = initial
        self.roles = roles
        self.transitions = transitions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateDraft":
        from ._schemas.state import StateDraftSchema

        return StateDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateDraftSchema

        return StateDraftSchema().dump(self)


class StatePagedQueryResponse(_BaseType):
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["State"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["State"]
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
    ) -> "StatePagedQueryResponse":
        from ._schemas.state import StatePagedQueryResponseSchema

        return StatePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StatePagedQueryResponseSchema

        return StatePagedQueryResponseSchema().dump(self)


class StateReference(Reference):
    obj: typing.Optional["State"]

    def __init__(self, *, id: "str", obj: typing.Optional["State"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.STATE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateReference":
        from ._schemas.state import StateReferenceSchema

        return StateReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateReferenceSchema

        return StateReferenceSchema().dump(self)


class StateResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional["str"] = None, key: typing.Optional["str"] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.STATE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StateResourceIdentifier":
        from ._schemas.state import StateResourceIdentifierSchema

        return StateResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateResourceIdentifierSchema

        return StateResourceIdentifierSchema().dump(self)


class StateRoleEnum(enum.Enum):
    REVIEW_INCLUDED_IN_STATISTICS = "ReviewIncludedInStatistics"
    RETURN = "Return"


class StateTypeEnum(enum.Enum):
    ORDER_STATE = "OrderState"
    LINE_ITEM_STATE = "LineItemState"
    PRODUCT_STATE = "ProductState"
    REVIEW_STATE = "ReviewState"
    PAYMENT_STATE = "PaymentState"


class StateUpdate(_BaseType):
    version: "int"
    actions: typing.List["StateUpdateAction"]

    def __init__(self, *, version: "int", actions: typing.List["StateUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateUpdate":
        from ._schemas.state import StateUpdateSchema

        return StateUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateUpdateSchema

        return StateUpdateSchema().dump(self)


class StateUpdateAction(_BaseType):
    action: "str"

    def __init__(self, *, action: "str"):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateUpdateAction":
        from ._schemas.state import StateUpdateActionSchema

        return StateUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateUpdateActionSchema

        return StateUpdateActionSchema().dump(self)


class StateAddRolesAction(StateUpdateAction):
    roles: typing.List["StateRoleEnum"]

    def __init__(self, *, roles: typing.List["StateRoleEnum"]):
        self.roles = roles
        super().__init__(action="addRoles")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateAddRolesAction":
        from ._schemas.state import StateAddRolesActionSchema

        return StateAddRolesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateAddRolesActionSchema

        return StateAddRolesActionSchema().dump(self)


class StateChangeInitialAction(StateUpdateAction):
    initial: "bool"

    def __init__(self, *, initial: "bool"):
        self.initial = initial
        super().__init__(action="changeInitial")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StateChangeInitialAction":
        from ._schemas.state import StateChangeInitialActionSchema

        return StateChangeInitialActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateChangeInitialActionSchema

        return StateChangeInitialActionSchema().dump(self)


class StateChangeKeyAction(StateUpdateAction):
    key: "str"

    def __init__(self, *, key: "str"):
        self.key = key
        super().__init__(action="changeKey")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateChangeKeyAction":
        from ._schemas.state import StateChangeKeyActionSchema

        return StateChangeKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateChangeKeyActionSchema

        return StateChangeKeyActionSchema().dump(self)


class StateChangeTypeAction(StateUpdateAction):
    type: "StateTypeEnum"

    def __init__(self, *, type: "StateTypeEnum"):
        self.type = type
        super().__init__(action="changeType")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateChangeTypeAction":
        from ._schemas.state import StateChangeTypeActionSchema

        return StateChangeTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateChangeTypeActionSchema

        return StateChangeTypeActionSchema().dump(self)


class StateRemoveRolesAction(StateUpdateAction):
    roles: typing.List["StateRoleEnum"]

    def __init__(self, *, roles: typing.List["StateRoleEnum"]):
        self.roles = roles
        super().__init__(action="removeRoles")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StateRemoveRolesAction":
        from ._schemas.state import StateRemoveRolesActionSchema

        return StateRemoveRolesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateRemoveRolesActionSchema

        return StateRemoveRolesActionSchema().dump(self)


class StateSetDescriptionAction(StateUpdateAction):
    description: "LocalizedString"

    def __init__(self, *, description: "LocalizedString"):
        self.description = description
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StateSetDescriptionAction":
        from ._schemas.state import StateSetDescriptionActionSchema

        return StateSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateSetDescriptionActionSchema

        return StateSetDescriptionActionSchema().dump(self)


class StateSetNameAction(StateUpdateAction):
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString"):
        self.name = name
        super().__init__(action="setName")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateSetNameAction":
        from ._schemas.state import StateSetNameActionSchema

        return StateSetNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateSetNameActionSchema

        return StateSetNameActionSchema().dump(self)


class StateSetRolesAction(StateUpdateAction):
    roles: typing.List["StateRoleEnum"]

    def __init__(self, *, roles: typing.List["StateRoleEnum"]):
        self.roles = roles
        super().__init__(action="setRoles")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateSetRolesAction":
        from ._schemas.state import StateSetRolesActionSchema

        return StateSetRolesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateSetRolesActionSchema

        return StateSetRolesActionSchema().dump(self)


class StateSetTransitionsAction(StateUpdateAction):
    transitions: typing.Optional[typing.List["StateResourceIdentifier"]]

    def __init__(
        self,
        *,
        transitions: typing.Optional[typing.List["StateResourceIdentifier"]] = None
    ):
        self.transitions = transitions
        super().__init__(action="setTransitions")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StateSetTransitionsAction":
        from ._schemas.state import StateSetTransitionsActionSchema

        return StateSetTransitionsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateSetTransitionsActionSchema

        return StateSetTransitionsActionSchema().dump(self)

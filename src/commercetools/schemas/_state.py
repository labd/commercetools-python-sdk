# DO NOT EDIT! This file is automatically generated

import marshmallow
import marshmallow_enum

from commercetools import helpers, types
from commercetools.schemas._common import (
    LocalizedStringField,
    LoggedResourceSchema,
    ReferenceSchema,
    ResourceIdentifierSchema,
)

__all__ = [
    "StateAddRolesActionSchema",
    "StateChangeInitialActionSchema",
    "StateChangeKeyActionSchema",
    "StateChangeTypeActionSchema",
    "StateDraftSchema",
    "StatePagedQueryResponseSchema",
    "StateReferenceSchema",
    "StateRemoveRolesActionSchema",
    "StateResourceIdentifierSchema",
    "StateSchema",
    "StateSetDescriptionActionSchema",
    "StateSetNameActionSchema",
    "StateSetRolesActionSchema",
    "StateSetTransitionsActionSchema",
    "StateUpdateActionSchema",
    "StateUpdateSchema",
]


class StateDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.StateDraft`."
    key = marshmallow.fields.String(allow_none=True)
    type = marshmallow_enum.EnumField(types.StateTypeEnum, by_value=True)
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    initial = marshmallow.fields.Bool(allow_none=True, missing=None)
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.StateRoleEnum, by_value=True), missing=None
    )
    transitions = marshmallow.fields.Nested(
        nested="commercetools.schemas._state.StateResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.StateDraft(**data)


class StatePagedQueryResponseSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.StatePagedQueryResponse`."
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = marshmallow.fields.Nested(
        nested="commercetools.schemas._state.StateSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.StatePagedQueryResponse(**data)


class StateReferenceSchema(ReferenceSchema):
    "Marshmallow schema for :class:`commercetools.types.StateReference`."
    obj = marshmallow.fields.Nested(
        nested="commercetools.schemas._state.StateSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type_id"]
        return types.StateReference(**data)


class StateResourceIdentifierSchema(ResourceIdentifierSchema):
    "Marshmallow schema for :class:`commercetools.types.StateResourceIdentifier`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type_id"]
        return types.StateResourceIdentifier(**data)


class StateSchema(LoggedResourceSchema):
    "Marshmallow schema for :class:`commercetools.types.State`."
    key = marshmallow.fields.String(allow_none=True)
    type = marshmallow_enum.EnumField(types.StateTypeEnum, by_value=True)
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    initial = marshmallow.fields.Bool(allow_none=True)
    built_in = marshmallow.fields.Bool(allow_none=True, data_key="builtIn", attribute="builtIn")
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.StateRoleEnum, by_value=True), missing=None
    )
    transitions = marshmallow.fields.Nested(
        nested="commercetools.schemas._state.StateReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.State(**data)


class StateUpdateActionSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.StateUpdateAction`."
    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.StateUpdateAction(**data)


class StateUpdateSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.StateUpdate`."
    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addRoles": "commercetools.schemas._state.StateAddRolesActionSchema",
                "changeInitial": "commercetools.schemas._state.StateChangeInitialActionSchema",
                "changeKey": "commercetools.schemas._state.StateChangeKeyActionSchema",
                "changeType": "commercetools.schemas._state.StateChangeTypeActionSchema",
                "removeRoles": "commercetools.schemas._state.StateRemoveRolesActionSchema",
                "setDescription": "commercetools.schemas._state.StateSetDescriptionActionSchema",
                "setName": "commercetools.schemas._state.StateSetNameActionSchema",
                "setRoles": "commercetools.schemas._state.StateSetRolesActionSchema",
                "setTransitions": "commercetools.schemas._state.StateSetTransitionsActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.StateUpdate(**data)


class StateAddRolesActionSchema(StateUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.StateAddRolesAction`."
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.StateRoleEnum, by_value=True)
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.StateAddRolesAction(**data)


class StateChangeInitialActionSchema(StateUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.StateChangeInitialAction`."
    initial = marshmallow.fields.Bool(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.StateChangeInitialAction(**data)


class StateChangeKeyActionSchema(StateUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.StateChangeKeyAction`."
    key = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.StateChangeKeyAction(**data)


class StateChangeTypeActionSchema(StateUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.StateChangeTypeAction`."
    type = marshmallow_enum.EnumField(types.StateTypeEnum, by_value=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.StateChangeTypeAction(**data)


class StateRemoveRolesActionSchema(StateUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.StateRemoveRolesAction`."
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.StateRoleEnum, by_value=True)
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.StateRemoveRolesAction(**data)


class StateSetDescriptionActionSchema(StateUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.StateSetDescriptionAction`."
    description = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.StateSetDescriptionAction(**data)


class StateSetNameActionSchema(StateUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.StateSetNameAction`."
    name = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.StateSetNameAction(**data)


class StateSetRolesActionSchema(StateUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.StateSetRolesAction`."
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.StateRoleEnum, by_value=True)
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.StateSetRolesAction(**data)


class StateSetTransitionsActionSchema(StateUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.StateSetTransitionsAction`."
    transitions = marshmallow.fields.Nested(
        nested="commercetools.schemas._state.StateResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.StateSetTransitionsAction(**data)

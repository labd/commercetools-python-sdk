# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from ..state import StateRoleEnum, StateTypeEnum
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)

# Fields


# Marshmallow Schemas
class StateSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)
    type = marshmallow_enum.EnumField(
        StateTypeEnum, by_value=True, allow_none=True, missing=None
    )
    name = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    description = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    initial = marshmallow.fields.Boolean(allow_none=True, missing=None)
    built_in = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="builtIn"
    )
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(StateRoleEnum, by_value=True, allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )
    transitions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".StateReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.State(**data)


class StateDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    type = marshmallow_enum.EnumField(
        StateTypeEnum, by_value=True, allow_none=True, missing=None
    )
    name = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    description = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    initial = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(StateRoleEnum, by_value=True, allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )
    transitions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".StateResourceIdentifierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.StateDraft(**data)


class StatePagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".StateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.StatePagedQueryResponse(**data)


class StateReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".StateSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.StateReference(**data)


class StateResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.StateResourceIdentifier(**data)


class StateUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addRoles": helpers.absmod(__name__, ".StateAddRolesActionSchema"),
                "changeInitial": helpers.absmod(
                    __name__, ".StateChangeInitialActionSchema"
                ),
                "changeKey": helpers.absmod(__name__, ".StateChangeKeyActionSchema"),
                "changeType": helpers.absmod(__name__, ".StateChangeTypeActionSchema"),
                "removeRoles": helpers.absmod(
                    __name__, ".StateRemoveRolesActionSchema"
                ),
                "setDescription": helpers.absmod(
                    __name__, ".StateSetDescriptionActionSchema"
                ),
                "setName": helpers.absmod(__name__, ".StateSetNameActionSchema"),
                "setRoles": helpers.absmod(__name__, ".StateSetRolesActionSchema"),
                "setTransitions": helpers.absmod(
                    __name__, ".StateSetTransitionsActionSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.StateUpdate(**data)


class StateUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StateUpdateAction(**data)


class StateAddRolesActionSchema(StateUpdateActionSchema):
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(StateRoleEnum, by_value=True, allow_none=True),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StateAddRolesAction(**data)


class StateChangeInitialActionSchema(StateUpdateActionSchema):
    initial = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StateChangeInitialAction(**data)


class StateChangeKeyActionSchema(StateUpdateActionSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StateChangeKeyAction(**data)


class StateChangeTypeActionSchema(StateUpdateActionSchema):
    type = marshmallow_enum.EnumField(
        StateTypeEnum, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StateChangeTypeAction(**data)


class StateRemoveRolesActionSchema(StateUpdateActionSchema):
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(StateRoleEnum, by_value=True, allow_none=True),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StateRemoveRolesAction(**data)


class StateSetDescriptionActionSchema(StateUpdateActionSchema):
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StateSetDescriptionAction(**data)


class StateSetNameActionSchema(StateUpdateActionSchema):
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StateSetNameAction(**data)


class StateSetRolesActionSchema(StateUpdateActionSchema):
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(StateRoleEnum, by_value=True, allow_none=True),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StateSetRolesAction(**data)


class StateSetTransitionsActionSchema(StateUpdateActionSchema):
    transitions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".StateResourceIdentifierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.StateSetTransitionsAction(**data)

# DO NOT EDIT! This file is automatically generated
import marshmallow

from commercetools import helpers, types
from commercetools.schemas._common import (
    BaseResourceSchema,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from commercetools.schemas._type import FieldContainerField

__all__ = [
    "CustomerGroupChangeNameActionSchema",
    "CustomerGroupDraftSchema",
    "CustomerGroupPagedQueryResponseSchema",
    "CustomerGroupReferenceSchema",
    "CustomerGroupResourceIdentifierSchema",
    "CustomerGroupSchema",
    "CustomerGroupSetCustomFieldActionSchema",
    "CustomerGroupSetCustomTypeActionSchema",
    "CustomerGroupSetKeyActionSchema",
    "CustomerGroupUpdateActionSchema",
    "CustomerGroupUpdateSchema",
]


class CustomerGroupDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerGroupDraft`."""

    key = marshmallow.fields.String(allow_none=True, missing=None)
    group_name = marshmallow.fields.String(allow_none=True, data_key="groupName")
    custom = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerGroupDraft(**data)


class CustomerGroupPagedQueryResponseSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerGroupPagedQueryResponse`."""

    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = marshmallow.fields.Nested(
        nested="commercetools.schemas._customer_group.CustomerGroupSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerGroupPagedQueryResponse(**data)


class CustomerGroupReferenceSchema(ReferenceSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerGroupReference`."""

    obj = marshmallow.fields.Nested(
        nested="commercetools.schemas._customer_group.CustomerGroupSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.CustomerGroupReference(**data)


class CustomerGroupResourceIdentifierSchema(ResourceIdentifierSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerGroupResourceIdentifier`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.CustomerGroupResourceIdentifier(**data)


class CustomerGroupSchema(BaseResourceSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerGroup`."""

    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True)
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, data_key="lastModifiedAt"
    )
    last_modified_by = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.LastModifiedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.CreatedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)
    name = marshmallow.fields.String(allow_none=True)
    custom = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerGroup(**data)


class CustomerGroupUpdateActionSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerGroupUpdateAction`."""

    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerGroupUpdateAction(**data)


class CustomerGroupUpdateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CustomerGroupUpdate`."""

    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeName": "commercetools.schemas._customer_group.CustomerGroupChangeNameActionSchema",
                "setCustomField": "commercetools.schemas._customer_group.CustomerGroupSetCustomFieldActionSchema",
                "setCustomType": "commercetools.schemas._customer_group.CustomerGroupSetCustomTypeActionSchema",
                "setKey": "commercetools.schemas._customer_group.CustomerGroupSetKeyActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CustomerGroupUpdate(**data)


class CustomerGroupChangeNameActionSchema(CustomerGroupUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerGroupChangeNameAction`."""

    name = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerGroupChangeNameAction(**data)


class CustomerGroupSetCustomFieldActionSchema(CustomerGroupUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerGroupSetCustomFieldAction`."""

    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerGroupSetCustomFieldAction(**data)


class CustomerGroupSetCustomTypeActionSchema(CustomerGroupUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerGroupSetCustomTypeAction`."""

    type = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.TypeResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerGroupSetCustomTypeAction(**data)


class CustomerGroupSetKeyActionSchema(CustomerGroupUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CustomerGroupSetKeyAction`."""

    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CustomerGroupSetKeyAction(**data)

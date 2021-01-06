# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from ..type import ResourceTypeId, TypeTextInputHint
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)


# Fields
class FieldContainerField(marshmallow.fields.Dict):
    def _deserialize(self, value, attr, data, **kwargs):
        result = super()._deserialize(value, attr, data)
        return models.FieldContainer(**result)


# Marshmallow Schemas
class CustomFieldEnumValueSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    label = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomFieldEnumValue(**data)


class CustomFieldLocalizedEnumValueSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    label = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomFieldLocalizedEnumValue(**data)


class CustomFieldsSchema(helpers.BaseSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TypeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomFields(**data)


class CustomFieldsDraftSchema(helpers.BaseSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = FieldContainerField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomFieldsDraft(**data)


class FieldDefinitionSchema(helpers.BaseSchema):
    type = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("name", "name"),
        discriminator_schemas={
            "Boolean": helpers.absmod(__name__, ".CustomFieldBooleanTypeSchema"),
            "DateTime": helpers.absmod(__name__, ".CustomFieldDateTimeTypeSchema"),
            "Date": helpers.absmod(__name__, ".CustomFieldDateTypeSchema"),
            "Enum": helpers.absmod(__name__, ".CustomFieldEnumTypeSchema"),
            "LocalizedEnum": helpers.absmod(
                __name__, ".CustomFieldLocalizedEnumTypeSchema"
            ),
            "LocalizedString": helpers.absmod(
                __name__, ".CustomFieldLocalizedStringTypeSchema"
            ),
            "Money": helpers.absmod(__name__, ".CustomFieldMoneyTypeSchema"),
            "Number": helpers.absmod(__name__, ".CustomFieldNumberTypeSchema"),
            "Reference": helpers.absmod(__name__, ".CustomFieldReferenceTypeSchema"),
            "Set": helpers.absmod(__name__, ".CustomFieldSetTypeSchema"),
            "String": helpers.absmod(__name__, ".CustomFieldStringTypeSchema"),
            "Time": helpers.absmod(__name__, ".CustomFieldTimeTypeSchema"),
        },
        missing=None,
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    label = LocalizedStringField(allow_none=True, missing=None)
    required = marshmallow.fields.Boolean(allow_none=True, missing=None)
    input_hint = marshmallow_enum.EnumField(
        TypeTextInputHint,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="inputHint",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.FieldDefinition(**data)


class FieldTypeSchema(helpers.BaseSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.FieldType(**data)


class CustomFieldBooleanTypeSchema(FieldTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.CustomFieldBooleanType(**data)


class CustomFieldDateTimeTypeSchema(FieldTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.CustomFieldDateTimeType(**data)


class CustomFieldDateTypeSchema(FieldTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.CustomFieldDateType(**data)


class CustomFieldEnumTypeSchema(FieldTypeSchema):
    values = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomFieldEnumValueSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.CustomFieldEnumType(**data)


class CustomFieldLocalizedEnumTypeSchema(FieldTypeSchema):
    values = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomFieldLocalizedEnumValueSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.CustomFieldLocalizedEnumType(**data)


class CustomFieldLocalizedStringTypeSchema(FieldTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.CustomFieldLocalizedStringType(**data)


class CustomFieldMoneyTypeSchema(FieldTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.CustomFieldMoneyType(**data)


class CustomFieldNumberTypeSchema(FieldTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.CustomFieldNumberType(**data)


class CustomFieldReferenceTypeSchema(FieldTypeSchema):
    reference_type_id = marshmallow_enum.EnumField(
        ReferenceTypeId,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="referenceTypeId",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.CustomFieldReferenceType(**data)


class CustomFieldSetTypeSchema(FieldTypeSchema):
    element_type = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("name", "name"),
        discriminator_schemas={
            "Boolean": helpers.absmod(__name__, ".CustomFieldBooleanTypeSchema"),
            "DateTime": helpers.absmod(__name__, ".CustomFieldDateTimeTypeSchema"),
            "Date": helpers.absmod(__name__, ".CustomFieldDateTypeSchema"),
            "Enum": helpers.absmod(__name__, ".CustomFieldEnumTypeSchema"),
            "LocalizedEnum": helpers.absmod(
                __name__, ".CustomFieldLocalizedEnumTypeSchema"
            ),
            "LocalizedString": helpers.absmod(
                __name__, ".CustomFieldLocalizedStringTypeSchema"
            ),
            "Money": helpers.absmod(__name__, ".CustomFieldMoneyTypeSchema"),
            "Number": helpers.absmod(__name__, ".CustomFieldNumberTypeSchema"),
            "Reference": helpers.absmod(__name__, ".CustomFieldReferenceTypeSchema"),
            "Set": helpers.absmod(__name__, ".CustomFieldSetTypeSchema"),
            "String": helpers.absmod(__name__, ".CustomFieldStringTypeSchema"),
            "Time": helpers.absmod(__name__, ".CustomFieldTimeTypeSchema"),
        },
        missing=None,
        data_key="elementType",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.CustomFieldSetType(**data)


class CustomFieldStringTypeSchema(FieldTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.CustomFieldStringType(**data)


class CustomFieldTimeTypeSchema(FieldTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.CustomFieldTimeType(**data)


class TypeSchema(BaseResourceSchema):
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
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    resource_type_ids = marshmallow.fields.List(
        marshmallow_enum.EnumField(ResourceTypeId, by_value=True, allow_none=True),
        allow_none=True,
        missing=None,
        data_key="resourceTypeIds",
    )
    field_definitions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".FieldDefinitionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="fieldDefinitions",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Type(**data)


class TypeDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    resource_type_ids = marshmallow.fields.List(
        marshmallow_enum.EnumField(ResourceTypeId, by_value=True, allow_none=True),
        allow_none=True,
        missing=None,
        data_key="resourceTypeIds",
    )
    field_definitions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".FieldDefinitionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="fieldDefinitions",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TypeDraft(**data)


class TypePagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TypeSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.TypePagedQueryResponse(**data)


class TypeReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".TypeSchema"),
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
        return models.TypeReference(**data)


class TypeResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.TypeResourceIdentifier(**data)


class TypeUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addEnumValue": helpers.absmod(
                    __name__, ".TypeAddEnumValueActionSchema"
                ),
                "addFieldDefinition": helpers.absmod(
                    __name__, ".TypeAddFieldDefinitionActionSchema"
                ),
                "addLocalizedEnumValue": helpers.absmod(
                    __name__, ".TypeAddLocalizedEnumValueActionSchema"
                ),
                "changeEnumValueLabel": helpers.absmod(
                    __name__, ".TypeChangeEnumValueLabelActionSchema"
                ),
                "changeEnumValueOrder": helpers.absmod(
                    __name__, ".TypeChangeEnumValueOrderActionSchema"
                ),
                "changeFieldDefinitionLabel": helpers.absmod(
                    __name__, ".TypeChangeFieldDefinitionLabelActionSchema"
                ),
                "changeFieldDefinitionOrder": helpers.absmod(
                    __name__, ".TypeChangeFieldDefinitionOrderActionSchema"
                ),
                "changeInputHint": helpers.absmod(
                    __name__, ".TypeChangeInputHintActionSchema"
                ),
                "changeKey": helpers.absmod(__name__, ".TypeChangeKeyActionSchema"),
                "changeLabel": helpers.absmod(__name__, ".TypeChangeLabelActionSchema"),
                "changeLocalizedEnumValueLabel": helpers.absmod(
                    __name__, ".TypeChangeLocalizedEnumValueLabelActionSchema"
                ),
                "changeLocalizedEnumValueOrder": helpers.absmod(
                    __name__, ".TypeChangeLocalizedEnumValueOrderActionSchema"
                ),
                "changeName": helpers.absmod(__name__, ".TypeChangeNameActionSchema"),
                "removeFieldDefinition": helpers.absmod(
                    __name__, ".TypeRemoveFieldDefinitionActionSchema"
                ),
                "setDescription": helpers.absmod(
                    __name__, ".TypeSetDescriptionActionSchema"
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

        return models.TypeUpdate(**data)


class TypeUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeUpdateAction(**data)


class TypeAddEnumValueActionSchema(TypeUpdateActionSchema):
    field_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="fieldName"
    )
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomFieldEnumValueSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeAddEnumValueAction(**data)


class TypeAddFieldDefinitionActionSchema(TypeUpdateActionSchema):
    field_definition = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".FieldDefinitionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="fieldDefinition",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeAddFieldDefinitionAction(**data)


class TypeAddLocalizedEnumValueActionSchema(TypeUpdateActionSchema):
    field_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="fieldName"
    )
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomFieldLocalizedEnumValueSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeAddLocalizedEnumValueAction(**data)


class TypeChangeEnumValueLabelActionSchema(TypeUpdateActionSchema):
    field_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="fieldName"
    )
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomFieldEnumValueSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeChangeEnumValueLabelAction(**data)


class TypeChangeEnumValueOrderActionSchema(TypeUpdateActionSchema):
    field_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="fieldName"
    )
    keys = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeChangeEnumValueOrderAction(**data)


class TypeChangeFieldDefinitionLabelActionSchema(TypeUpdateActionSchema):
    field_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="fieldName"
    )
    label = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeChangeFieldDefinitionLabelAction(**data)


class TypeChangeFieldDefinitionOrderActionSchema(TypeUpdateActionSchema):
    field_names = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="fieldNames",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeChangeFieldDefinitionOrderAction(**data)


class TypeChangeInputHintActionSchema(TypeUpdateActionSchema):
    field_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="fieldName"
    )
    input_hint = marshmallow_enum.EnumField(
        TypeTextInputHint,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="inputHint",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeChangeInputHintAction(**data)


class TypeChangeKeyActionSchema(TypeUpdateActionSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeChangeKeyAction(**data)


class TypeChangeLabelActionSchema(TypeUpdateActionSchema):
    field_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="fieldName"
    )
    label = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeChangeLabelAction(**data)


class TypeChangeLocalizedEnumValueLabelActionSchema(TypeUpdateActionSchema):
    field_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="fieldName"
    )
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomFieldLocalizedEnumValueSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeChangeLocalizedEnumValueLabelAction(**data)


class TypeChangeLocalizedEnumValueOrderActionSchema(TypeUpdateActionSchema):
    field_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="fieldName"
    )
    keys = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeChangeLocalizedEnumValueOrderAction(**data)


class TypeChangeNameActionSchema(TypeUpdateActionSchema):
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeChangeNameAction(**data)


class TypeRemoveFieldDefinitionActionSchema(TypeUpdateActionSchema):
    field_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="fieldName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeRemoveFieldDefinitionAction(**data)


class TypeSetDescriptionActionSchema(TypeUpdateActionSchema):
    description = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.TypeSetDescriptionAction(**data)

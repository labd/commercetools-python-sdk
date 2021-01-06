# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceType
from ..producttypes import AttributeConstraintEnum, TextInputHint
from .common import ImportResourceSchema, LocalizedStringField

# Fields


# Marshmallow Schemas
class AttributeDefinitionSchema(helpers.BaseSchema):
    type = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("name", "name"),
        discriminator_schemas={
            "boolean": helpers.absmod(__name__, ".AttributeBooleanTypeSchema"),
            "datetime": helpers.absmod(__name__, ".AttributeDateTimeTypeSchema"),
            "date": helpers.absmod(__name__, ".AttributeDateTypeSchema"),
            "enum": helpers.absmod(__name__, ".AttributeEnumTypeSchema"),
            "ltext": helpers.absmod(__name__, ".AttributeLocalizableTextTypeSchema"),
            "lenum": helpers.absmod(__name__, ".AttributeLocalizedEnumTypeSchema"),
            "money": helpers.absmod(__name__, ".AttributeMoneyTypeSchema"),
            "nested": helpers.absmod(__name__, ".AttributeNestedTypeSchema"),
            "number": helpers.absmod(__name__, ".AttributeNumberTypeSchema"),
            "reference": helpers.absmod(__name__, ".AttributeReferenceTypeSchema"),
            "set": helpers.absmod(__name__, ".AttributeSetTypeSchema"),
            "text": helpers.absmod(__name__, ".AttributeTextTypeSchema"),
            "time": helpers.absmod(__name__, ".AttributeTimeTypeSchema"),
        },
        missing=None,
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    label = LocalizedStringField(allow_none=True, missing=None)
    is_required = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isRequired"
    )
    attribute_constraint = marshmallow_enum.EnumField(
        AttributeConstraintEnum,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="attributeConstraint",
    )
    input_tip = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="inputTip",
    )
    input_hint = marshmallow_enum.EnumField(
        TextInputHint,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="inputHint",
    )
    is_searchable = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="isSearchable",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AttributeDefinition(**data)


class AttributeTypeSchema(helpers.BaseSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.AttributeType(**data)


class AttributeBooleanTypeSchema(AttributeTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.AttributeBooleanType(**data)


class AttributeDateTimeTypeSchema(AttributeTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.AttributeDateTimeType(**data)


class AttributeDateTypeSchema(AttributeTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.AttributeDateType(**data)


class AttributeEnumTypeSchema(AttributeTypeSchema):
    values = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributePlainEnumValueSchema"),
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
        return models.AttributeEnumType(**data)


class AttributePlainEnumValueSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    label = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AttributePlainEnumValue(**data)


class AttributeLocalizableTextTypeSchema(AttributeTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.AttributeLocalizableTextType(**data)


class AttributeLocalizedEnumTypeSchema(AttributeTypeSchema):
    values = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributeLocalizedEnumValueSchema"),
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
        return models.AttributeLocalizedEnumType(**data)


class AttributeLocalizedEnumValueSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    label = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AttributeLocalizedEnumValue(**data)


class AttributeMoneyTypeSchema(AttributeTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.AttributeMoneyType(**data)


class AttributeNestedTypeSchema(AttributeTypeSchema):
    type_reference = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductTypeKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="typeReference",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.AttributeNestedType(**data)


class AttributeNumberTypeSchema(AttributeTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.AttributeNumberType(**data)


class AttributeReferenceTypeSchema(AttributeTypeSchema):
    reference_type_id = marshmallow_enum.EnumField(
        ReferenceType,
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
        return models.AttributeReferenceType(**data)


class AttributeSetTypeSchema(AttributeTypeSchema):
    element_type = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("name", "name"),
        discriminator_schemas={
            "boolean": helpers.absmod(__name__, ".AttributeBooleanTypeSchema"),
            "datetime": helpers.absmod(__name__, ".AttributeDateTimeTypeSchema"),
            "date": helpers.absmod(__name__, ".AttributeDateTypeSchema"),
            "enum": helpers.absmod(__name__, ".AttributeEnumTypeSchema"),
            "ltext": helpers.absmod(__name__, ".AttributeLocalizableTextTypeSchema"),
            "lenum": helpers.absmod(__name__, ".AttributeLocalizedEnumTypeSchema"),
            "money": helpers.absmod(__name__, ".AttributeMoneyTypeSchema"),
            "nested": helpers.absmod(__name__, ".AttributeNestedTypeSchema"),
            "number": helpers.absmod(__name__, ".AttributeNumberTypeSchema"),
            "reference": helpers.absmod(__name__, ".AttributeReferenceTypeSchema"),
            "set": helpers.absmod(__name__, ".AttributeSetTypeSchema"),
            "text": helpers.absmod(__name__, ".AttributeTextTypeSchema"),
            "time": helpers.absmod(__name__, ".AttributeTimeTypeSchema"),
        },
        missing=None,
        data_key="elementType",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.AttributeSetType(**data)


class AttributeTextTypeSchema(AttributeTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.AttributeTextType(**data)


class AttributeTimeTypeSchema(AttributeTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.AttributeTimeType(**data)


class ProductTypeImportSchema(ImportResourceSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    description = marshmallow.fields.String(allow_none=True, missing=None)
    attributes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributeDefinitionSchema"),
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

        return models.ProductTypeImport(**data)

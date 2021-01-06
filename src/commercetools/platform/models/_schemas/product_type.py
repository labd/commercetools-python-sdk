# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from ..product_type import (
    AttributeConstraintEnum,
    AttributeConstraintEnumDraft,
    TextInputHint,
)
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)

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
        missing=None,
        data_key="inputHint",
    )
    is_searchable = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isSearchable"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AttributeDefinition(**data)


class AttributeDefinitionDraftSchema(helpers.BaseSchema):
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

        return models.AttributeDefinitionDraft(**data)


class AttributeLocalizedEnumValueSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    label = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AttributeLocalizedEnumValue(**data)


class AttributePlainEnumValueSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)
    label = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AttributePlainEnumValue(**data)


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


class AttributeMoneyTypeSchema(AttributeTypeSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return models.AttributeMoneyType(**data)


class AttributeNestedTypeSchema(AttributeTypeSchema):
    type_reference = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductTypeReferenceSchema"),
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


class ProductTypeSchema(BaseResourceSchema):
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
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
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

        return models.ProductType(**data)


class ProductTypeDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    description = marshmallow.fields.String(allow_none=True, missing=None)
    attributes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributeDefinitionDraftSchema"),
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

        return models.ProductTypeDraft(**data)


class ProductTypePagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductTypeSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductTypePagedQueryResponse(**data)


class ProductTypeReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductTypeSchema"),
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
        return models.ProductTypeReference(**data)


class ProductTypeResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductTypeResourceIdentifier(**data)


class ProductTypeUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addAttributeDefinition": helpers.absmod(
                    __name__, ".ProductTypeAddAttributeDefinitionActionSchema"
                ),
                "addLocalizedEnumValue": helpers.absmod(
                    __name__, ".ProductTypeAddLocalizedEnumValueActionSchema"
                ),
                "addPlainEnumValue": helpers.absmod(
                    __name__, ".ProductTypeAddPlainEnumValueActionSchema"
                ),
                "changeAttributeConstraint": helpers.absmod(
                    __name__, ".ProductTypeChangeAttributeConstraintActionSchema"
                ),
                "changeAttributeName": helpers.absmod(
                    __name__, ".ProductTypeChangeAttributeNameActionSchema"
                ),
                "changeAttributeOrder": helpers.absmod(
                    __name__, ".ProductTypeChangeAttributeOrderActionSchema"
                ),
                "changeAttributeOrderByName": helpers.absmod(
                    __name__, ".ProductTypeChangeAttributeOrderByNameActionSchema"
                ),
                "changeDescription": helpers.absmod(
                    __name__, ".ProductTypeChangeDescriptionActionSchema"
                ),
                "changeEnumKey": helpers.absmod(
                    __name__, ".ProductTypeChangeEnumKeyActionSchema"
                ),
                "changeInputHint": helpers.absmod(
                    __name__, ".ProductTypeChangeInputHintActionSchema"
                ),
                "changeIsSearchable": helpers.absmod(
                    __name__, ".ProductTypeChangeIsSearchableActionSchema"
                ),
                "changeLabel": helpers.absmod(
                    __name__, ".ProductTypeChangeLabelActionSchema"
                ),
                "changeLocalizedEnumValueLabel": helpers.absmod(
                    __name__, ".ProductTypeChangeLocalizedEnumValueLabelActionSchema"
                ),
                "changeLocalizedEnumValueOrder": helpers.absmod(
                    __name__, ".ProductTypeChangeLocalizedEnumValueOrderActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".ProductTypeChangeNameActionSchema"
                ),
                "changePlainEnumValueLabel": helpers.absmod(
                    __name__, ".ProductTypeChangePlainEnumValueLabelActionSchema"
                ),
                "changePlainEnumValueOrder": helpers.absmod(
                    __name__, ".ProductTypeChangePlainEnumValueOrderActionSchema"
                ),
                "removeAttributeDefinition": helpers.absmod(
                    __name__, ".ProductTypeRemoveAttributeDefinitionActionSchema"
                ),
                "removeEnumValues": helpers.absmod(
                    __name__, ".ProductTypeRemoveEnumValuesActionSchema"
                ),
                "setInputTip": helpers.absmod(
                    __name__, ".ProductTypeSetInputTipActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".ProductTypeSetKeyActionSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductTypeUpdate(**data)


class ProductTypeUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeUpdateAction(**data)


class ProductTypeAddAttributeDefinitionActionSchema(ProductTypeUpdateActionSchema):
    attribute = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributeDefinitionDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeAddAttributeDefinitionAction(**data)


class ProductTypeAddLocalizedEnumValueActionSchema(ProductTypeUpdateActionSchema):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributeLocalizedEnumValueSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeAddLocalizedEnumValueAction(**data)


class ProductTypeAddPlainEnumValueActionSchema(ProductTypeUpdateActionSchema):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributePlainEnumValueSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeAddPlainEnumValueAction(**data)


class ProductTypeChangeAttributeConstraintActionSchema(ProductTypeUpdateActionSchema):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
    new_value = marshmallow_enum.EnumField(
        AttributeConstraintEnumDraft,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="newValue",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeChangeAttributeConstraintAction(**data)


class ProductTypeChangeAttributeNameActionSchema(ProductTypeUpdateActionSchema):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
    new_attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="newAttributeName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeChangeAttributeNameAction(**data)


class ProductTypeChangeAttributeOrderActionSchema(ProductTypeUpdateActionSchema):
    attributes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributeDefinitionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeChangeAttributeOrderAction(**data)


class ProductTypeChangeAttributeOrderByNameActionSchema(ProductTypeUpdateActionSchema):
    attribute_names = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="attributeNames",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeChangeAttributeOrderByNameAction(**data)


class ProductTypeChangeDescriptionActionSchema(ProductTypeUpdateActionSchema):
    description = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeChangeDescriptionAction(**data)


class ProductTypeChangeEnumKeyActionSchema(ProductTypeUpdateActionSchema):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)
    new_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="newKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeChangeEnumKeyAction(**data)


class ProductTypeChangeInputHintActionSchema(ProductTypeUpdateActionSchema):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
    new_value = marshmallow_enum.EnumField(
        TextInputHint, by_value=True, allow_none=True, missing=None, data_key="newValue"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeChangeInputHintAction(**data)


class ProductTypeChangeIsSearchableActionSchema(ProductTypeUpdateActionSchema):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
    is_searchable = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isSearchable"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeChangeIsSearchableAction(**data)


class ProductTypeChangeLabelActionSchema(ProductTypeUpdateActionSchema):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
    label = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeChangeLabelAction(**data)


class ProductTypeChangeLocalizedEnumValueLabelActionSchema(
    ProductTypeUpdateActionSchema
):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
    new_value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributeLocalizedEnumValueSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="newValue",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeChangeLocalizedEnumValueLabelAction(**data)


class ProductTypeChangeLocalizedEnumValueOrderActionSchema(
    ProductTypeUpdateActionSchema
):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
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
        del data["action"]
        return models.ProductTypeChangeLocalizedEnumValueOrderAction(**data)


class ProductTypeChangeNameActionSchema(ProductTypeUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeChangeNameAction(**data)


class ProductTypeChangePlainEnumValueLabelActionSchema(ProductTypeUpdateActionSchema):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
    new_value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributePlainEnumValueSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="newValue",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeChangePlainEnumValueLabelAction(**data)


class ProductTypeChangePlainEnumValueOrderActionSchema(ProductTypeUpdateActionSchema):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
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
        del data["action"]
        return models.ProductTypeChangePlainEnumValueOrderAction(**data)


class ProductTypeRemoveAttributeDefinitionActionSchema(ProductTypeUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeRemoveAttributeDefinitionAction(**data)


class ProductTypeRemoveEnumValuesActionSchema(ProductTypeUpdateActionSchema):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
    keys = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeRemoveEnumValuesAction(**data)


class ProductTypeSetInputTipActionSchema(ProductTypeUpdateActionSchema):
    attribute_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="attributeName"
    )
    input_tip = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="inputTip",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeSetInputTipAction(**data)


class ProductTypeSetKeyActionSchema(ProductTypeUpdateActionSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTypeSetKeyAction(**data)

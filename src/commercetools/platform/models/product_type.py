# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, LocalizedString, ReferenceTypeId


class AttributeConstraintEnum(enum.Enum):
    NONE = "None"
    UNIQUE = "Unique"
    COMBINATION_UNIQUE = "CombinationUnique"
    SAME_FOR_ALL = "SameForAll"


class AttributeConstraintEnumDraft(enum.Enum):
    NONE = "None"


class AttributeDefinition(_BaseType):
    #: Describes the type of the attribute.
    type: "AttributeType"
    #: The unique name of the attribute used in the API.
    #: The name must be between two and 256 characters long and can contain the ASCII letters A to Z in lowercase or uppercase, digits, underscores (`_`) and the hyphen-minus (`-`).
    #: When using the same `name` for an attribute in two or more product types all fields of the AttributeDefinition of this attribute need to be the same across the product types, otherwise an AttributeDefinitionAlreadyExists error code will be returned.
    #: An exception to this are the values of an `enum` or `lenum` type and sets thereof.
    name: "str"
    #: A human-readable label for the attribute.
    label: "LocalizedString"
    #: Whether the attribute is required to have a value.
    is_required: "bool"
    #: Describes how an attribute or a set of attributes should be validated across all variants of a product.
    attribute_constraint: "AttributeConstraintEnum"
    #: Additional information about the attribute that aids content managers when setting product details.
    input_tip: typing.Optional["LocalizedString"]
    #: Provides a visual representation type for this attribute.
    #: only relevant for text-based attribute types
    #: like TextType and LocalizableTextType.
    input_hint: "TextInputHint"
    #: Whether the attribute's values should generally be enabled in product search.
    #: This determines whether the value is stored in products for matching terms in the context of full-text search queries  and can be used in facets & filters as part of product search queries.
    #: The exact features that are enabled/disabled with this flag depend on the concrete attribute type and are described there.
    #: The max size of a searchable field is **restricted to 10922 characters**.
    #: This constraint is enforced at both product creation and product update.
    #: If the length of the input exceeds the maximum size an InvalidField error is returned.
    is_searchable: "bool"

    def __init__(
        self,
        *,
        type: "AttributeType",
        name: "str",
        label: "LocalizedString",
        is_required: "bool",
        attribute_constraint: "AttributeConstraintEnum",
        input_tip: typing.Optional["LocalizedString"] = None,
        input_hint: "TextInputHint",
        is_searchable: "bool"
    ):
        self.type = type
        self.name = name
        self.label = label
        self.is_required = is_required
        self.attribute_constraint = attribute_constraint
        self.input_tip = input_tip
        self.input_hint = input_hint
        self.is_searchable = is_searchable
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeDefinition":
        from ._schemas.product_type import AttributeDefinitionSchema

        return AttributeDefinitionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeDefinitionSchema

        return AttributeDefinitionSchema().dump(self)


class AttributeDefinitionDraft(_BaseType):
    #: Describes the type of the attribute.
    type: "AttributeType"
    #: The unique name of the attribute used in the API.
    #: The name must be between two and 256 characters long and can contain the ASCII letters A to Z in lowercase or uppercase, digits, underscores (`_`) and the hyphen-minus (`-`).
    #: When using the same `name` for an attribute in two or more product types all fields of the AttributeDefinition of this attribute need to be the same across the product types.
    name: "str"
    #: A human-readable label for the attribute.
    label: "LocalizedString"
    #: Whether the attribute is required to have a value.
    is_required: "bool"
    #: Describes how an attribute or a set of attributes should be validated across all variants of a product.
    attribute_constraint: typing.Optional["AttributeConstraintEnum"]
    #: Additional information about the attribute that aids content managers when setting product details.
    input_tip: typing.Optional["LocalizedString"]
    #: Provides a visual representation type for this attribute.
    #: only relevant for text-based attribute types like TextType and LocalizableTextType.
    input_hint: typing.Optional["TextInputHint"]
    #: Whether the attribute's values should generally be enabled in product search.
    #: This determines whether the value is stored in products for matching terms in the context of full-text search queries and can be used in facets & filters as part of product search queries.
    #: The exact features that are enabled/disabled with this flag depend on the concrete attribute type and are described there.
    is_searchable: typing.Optional["bool"]

    def __init__(
        self,
        *,
        type: "AttributeType",
        name: "str",
        label: "LocalizedString",
        is_required: "bool",
        attribute_constraint: typing.Optional["AttributeConstraintEnum"] = None,
        input_tip: typing.Optional["LocalizedString"] = None,
        input_hint: typing.Optional["TextInputHint"] = None,
        is_searchable: typing.Optional["bool"] = None
    ):
        self.type = type
        self.name = name
        self.label = label
        self.is_required = is_required
        self.attribute_constraint = attribute_constraint
        self.input_tip = input_tip
        self.input_hint = input_hint
        self.is_searchable = is_searchable
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeDefinitionDraft":
        from ._schemas.product_type import AttributeDefinitionDraftSchema

        return AttributeDefinitionDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeDefinitionDraftSchema

        return AttributeDefinitionDraftSchema().dump(self)


class AttributeLocalizedEnumValue(_BaseType):
    key: "str"
    label: "LocalizedString"

    def __init__(self, *, key: "str", label: "LocalizedString"):
        self.key = key
        self.label = label
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeLocalizedEnumValue":
        from ._schemas.product_type import AttributeLocalizedEnumValueSchema

        return AttributeLocalizedEnumValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeLocalizedEnumValueSchema

        return AttributeLocalizedEnumValueSchema().dump(self)


class AttributePlainEnumValue(_BaseType):
    key: "str"
    label: "str"

    def __init__(self, *, key: "str", label: "str"):
        self.key = key
        self.label = label
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributePlainEnumValue":
        from ._schemas.product_type import AttributePlainEnumValueSchema

        return AttributePlainEnumValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributePlainEnumValueSchema

        return AttributePlainEnumValueSchema().dump(self)


class AttributeType(_BaseType):
    name: "str"

    def __init__(self, *, name: "str"):
        self.name = name
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeType":
        from ._schemas.product_type import AttributeTypeSchema

        return AttributeTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeTypeSchema

        return AttributeTypeSchema().dump(self)


class AttributeBooleanType(AttributeType):
    def __init__(self):

        super().__init__(name="boolean")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeBooleanType":
        from ._schemas.product_type import AttributeBooleanTypeSchema

        return AttributeBooleanTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeBooleanTypeSchema

        return AttributeBooleanTypeSchema().dump(self)


class AttributeDateTimeType(AttributeType):
    def __init__(self):

        super().__init__(name="datetime")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeDateTimeType":
        from ._schemas.product_type import AttributeDateTimeTypeSchema

        return AttributeDateTimeTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeDateTimeTypeSchema

        return AttributeDateTimeTypeSchema().dump(self)


class AttributeDateType(AttributeType):
    def __init__(self):

        super().__init__(name="date")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeDateType":
        from ._schemas.product_type import AttributeDateTypeSchema

        return AttributeDateTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeDateTypeSchema

        return AttributeDateTypeSchema().dump(self)


class AttributeEnumType(AttributeType):
    values: typing.List["AttributePlainEnumValue"]

    def __init__(self, *, values: typing.List["AttributePlainEnumValue"]):
        self.values = values
        super().__init__(name="enum")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeEnumType":
        from ._schemas.product_type import AttributeEnumTypeSchema

        return AttributeEnumTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeEnumTypeSchema

        return AttributeEnumTypeSchema().dump(self)


class AttributeLocalizableTextType(AttributeType):
    def __init__(self):

        super().__init__(name="ltext")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeLocalizableTextType":
        from ._schemas.product_type import AttributeLocalizableTextTypeSchema

        return AttributeLocalizableTextTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeLocalizableTextTypeSchema

        return AttributeLocalizableTextTypeSchema().dump(self)


class AttributeLocalizedEnumType(AttributeType):
    values: typing.List["AttributeLocalizedEnumValue"]

    def __init__(self, *, values: typing.List["AttributeLocalizedEnumValue"]):
        self.values = values
        super().__init__(name="lenum")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeLocalizedEnumType":
        from ._schemas.product_type import AttributeLocalizedEnumTypeSchema

        return AttributeLocalizedEnumTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeLocalizedEnumTypeSchema

        return AttributeLocalizedEnumTypeSchema().dump(self)


class AttributeMoneyType(AttributeType):
    def __init__(self):

        super().__init__(name="money")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeMoneyType":
        from ._schemas.product_type import AttributeMoneyTypeSchema

        return AttributeMoneyTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeMoneyTypeSchema

        return AttributeMoneyTypeSchema().dump(self)


class AttributeNestedType(AttributeType):
    type_reference: "ProductTypeReference"

    def __init__(self, *, type_reference: "ProductTypeReference"):
        self.type_reference = type_reference
        super().__init__(name="nested")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeNestedType":
        from ._schemas.product_type import AttributeNestedTypeSchema

        return AttributeNestedTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeNestedTypeSchema

        return AttributeNestedTypeSchema().dump(self)


class AttributeNumberType(AttributeType):
    def __init__(self):

        super().__init__(name="number")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeNumberType":
        from ._schemas.product_type import AttributeNumberTypeSchema

        return AttributeNumberTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeNumberTypeSchema

        return AttributeNumberTypeSchema().dump(self)


class AttributeReferenceType(AttributeType):
    reference_type_id: "ReferenceTypeId"

    def __init__(self, *, reference_type_id: "ReferenceTypeId"):
        self.reference_type_id = reference_type_id
        super().__init__(name="reference")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeReferenceType":
        from ._schemas.product_type import AttributeReferenceTypeSchema

        return AttributeReferenceTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeReferenceTypeSchema

        return AttributeReferenceTypeSchema().dump(self)


class AttributeSetType(AttributeType):
    element_type: "AttributeType"

    def __init__(self, *, element_type: "AttributeType"):
        self.element_type = element_type
        super().__init__(name="set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeSetType":
        from ._schemas.product_type import AttributeSetTypeSchema

        return AttributeSetTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeSetTypeSchema

        return AttributeSetTypeSchema().dump(self)


class AttributeTextType(AttributeType):
    def __init__(self):

        super().__init__(name="text")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeTextType":
        from ._schemas.product_type import AttributeTextTypeSchema

        return AttributeTextTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeTextTypeSchema

        return AttributeTextTypeSchema().dump(self)


class AttributeTimeType(AttributeType):
    def __init__(self):

        super().__init__(name="time")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeTimeType":
        from ._schemas.product_type import AttributeTimeTypeSchema

        return AttributeTimeTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import AttributeTimeTypeSchema

        return AttributeTimeTypeSchema().dump(self)


class ProductType(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    #: User-specific unique identifier for the product type (max.
    #: 256 characters).
    key: typing.Optional["str"]
    name: "str"
    description: "str"
    attributes: typing.Optional[typing.List["AttributeDefinition"]]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional["str"] = None,
        name: "str",
        description: "str",
        attributes: typing.Optional[typing.List["AttributeDefinition"]] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.description = description
        self.attributes = attributes
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductType":
        from ._schemas.product_type import ProductTypeSchema

        return ProductTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeSchema

        return ProductTypeSchema().dump(self)


class ProductTypeDraft(_BaseType):
    #: User-specific unique identifier for the product type (min.
    #: 2 and max.
    #: 256 characters).
    key: typing.Optional["str"]
    name: "str"
    description: "str"
    attributes: typing.Optional[typing.List["AttributeDefinitionDraft"]]

    def __init__(
        self,
        *,
        key: typing.Optional["str"] = None,
        name: "str",
        description: "str",
        attributes: typing.Optional[typing.List["AttributeDefinitionDraft"]] = None
    ):
        self.key = key
        self.name = name
        self.description = description
        self.attributes = attributes
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductTypeDraft":
        from ._schemas.product_type import ProductTypeDraftSchema

        return ProductTypeDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeDraftSchema

        return ProductTypeDraftSchema().dump(self)


class ProductTypePagedQueryResponse(_BaseType):
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["ProductType"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["ProductType"]
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
    ) -> "ProductTypePagedQueryResponse":
        from ._schemas.product_type import ProductTypePagedQueryResponseSchema

        return ProductTypePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypePagedQueryResponseSchema

        return ProductTypePagedQueryResponseSchema().dump(self)


class ProductTypeReference(Reference):
    obj: typing.Optional["ProductType"]

    def __init__(self, *, id: "str", obj: typing.Optional["ProductType"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.PRODUCT_TYPE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductTypeReference":
        from ._schemas.product_type import ProductTypeReferenceSchema

        return ProductTypeReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeReferenceSchema

        return ProductTypeReferenceSchema().dump(self)


class ProductTypeResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional["str"] = None, key: typing.Optional["str"] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.PRODUCT_TYPE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeResourceIdentifier":
        from ._schemas.product_type import ProductTypeResourceIdentifierSchema

        return ProductTypeResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeResourceIdentifierSchema

        return ProductTypeResourceIdentifierSchema().dump(self)


class ProductTypeUpdate(_BaseType):
    version: "int"
    actions: typing.List["ProductTypeUpdateAction"]

    def __init__(
        self, *, version: "int", actions: typing.List["ProductTypeUpdateAction"]
    ):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductTypeUpdate":
        from ._schemas.product_type import ProductTypeUpdateSchema

        return ProductTypeUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeUpdateSchema

        return ProductTypeUpdateSchema().dump(self)


class ProductTypeUpdateAction(_BaseType):
    action: "str"

    def __init__(self, *, action: "str"):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeUpdateAction":
        from ._schemas.product_type import ProductTypeUpdateActionSchema

        return ProductTypeUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeUpdateActionSchema

        return ProductTypeUpdateActionSchema().dump(self)


class TextInputHint(enum.Enum):
    SINGLE_LINE = "SingleLine"
    MULTI_LINE = "MultiLine"


class ProductTypeAddAttributeDefinitionAction(ProductTypeUpdateAction):
    attribute: "AttributeDefinitionDraft"

    def __init__(self, *, attribute: "AttributeDefinitionDraft"):
        self.attribute = attribute
        super().__init__(action="addAttributeDefinition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeAddAttributeDefinitionAction":
        from ._schemas.product_type import ProductTypeAddAttributeDefinitionActionSchema

        return ProductTypeAddAttributeDefinitionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeAddAttributeDefinitionActionSchema

        return ProductTypeAddAttributeDefinitionActionSchema().dump(self)


class ProductTypeAddLocalizedEnumValueAction(ProductTypeUpdateAction):
    attribute_name: "str"
    value: "AttributeLocalizedEnumValue"

    def __init__(self, *, attribute_name: "str", value: "AttributeLocalizedEnumValue"):
        self.attribute_name = attribute_name
        self.value = value
        super().__init__(action="addLocalizedEnumValue")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeAddLocalizedEnumValueAction":
        from ._schemas.product_type import ProductTypeAddLocalizedEnumValueActionSchema

        return ProductTypeAddLocalizedEnumValueActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeAddLocalizedEnumValueActionSchema

        return ProductTypeAddLocalizedEnumValueActionSchema().dump(self)


class ProductTypeAddPlainEnumValueAction(ProductTypeUpdateAction):
    attribute_name: "str"
    value: "AttributePlainEnumValue"

    def __init__(self, *, attribute_name: "str", value: "AttributePlainEnumValue"):
        self.attribute_name = attribute_name
        self.value = value
        super().__init__(action="addPlainEnumValue")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeAddPlainEnumValueAction":
        from ._schemas.product_type import ProductTypeAddPlainEnumValueActionSchema

        return ProductTypeAddPlainEnumValueActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeAddPlainEnumValueActionSchema

        return ProductTypeAddPlainEnumValueActionSchema().dump(self)


class ProductTypeChangeAttributeConstraintAction(ProductTypeUpdateAction):
    attribute_name: "str"
    new_value: "AttributeConstraintEnumDraft"

    def __init__(
        self, *, attribute_name: "str", new_value: "AttributeConstraintEnumDraft"
    ):
        self.attribute_name = attribute_name
        self.new_value = new_value
        super().__init__(action="changeAttributeConstraint")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangeAttributeConstraintAction":
        from ._schemas.product_type import (
            ProductTypeChangeAttributeConstraintActionSchema,
        )

        return ProductTypeChangeAttributeConstraintActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import (
            ProductTypeChangeAttributeConstraintActionSchema,
        )

        return ProductTypeChangeAttributeConstraintActionSchema().dump(self)


class ProductTypeChangeAttributeNameAction(ProductTypeUpdateAction):
    attribute_name: "str"
    new_attribute_name: "str"

    def __init__(self, *, attribute_name: "str", new_attribute_name: "str"):
        self.attribute_name = attribute_name
        self.new_attribute_name = new_attribute_name
        super().__init__(action="changeAttributeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangeAttributeNameAction":
        from ._schemas.product_type import ProductTypeChangeAttributeNameActionSchema

        return ProductTypeChangeAttributeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeChangeAttributeNameActionSchema

        return ProductTypeChangeAttributeNameActionSchema().dump(self)


class ProductTypeChangeAttributeOrderAction(ProductTypeUpdateAction):
    attributes: typing.List["AttributeDefinition"]

    def __init__(self, *, attributes: typing.List["AttributeDefinition"]):
        self.attributes = attributes
        super().__init__(action="changeAttributeOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangeAttributeOrderAction":
        from ._schemas.product_type import ProductTypeChangeAttributeOrderActionSchema

        return ProductTypeChangeAttributeOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeChangeAttributeOrderActionSchema

        return ProductTypeChangeAttributeOrderActionSchema().dump(self)


class ProductTypeChangeAttributeOrderByNameAction(ProductTypeUpdateAction):
    attribute_names: typing.List["str"]

    def __init__(self, *, attribute_names: typing.List["str"]):
        self.attribute_names = attribute_names
        super().__init__(action="changeAttributeOrderByName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangeAttributeOrderByNameAction":
        from ._schemas.product_type import (
            ProductTypeChangeAttributeOrderByNameActionSchema,
        )

        return ProductTypeChangeAttributeOrderByNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import (
            ProductTypeChangeAttributeOrderByNameActionSchema,
        )

        return ProductTypeChangeAttributeOrderByNameActionSchema().dump(self)


class ProductTypeChangeDescriptionAction(ProductTypeUpdateAction):
    description: "str"

    def __init__(self, *, description: "str"):
        self.description = description
        super().__init__(action="changeDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangeDescriptionAction":
        from ._schemas.product_type import ProductTypeChangeDescriptionActionSchema

        return ProductTypeChangeDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeChangeDescriptionActionSchema

        return ProductTypeChangeDescriptionActionSchema().dump(self)


class ProductTypeChangeEnumKeyAction(ProductTypeUpdateAction):
    attribute_name: "str"
    key: "str"
    new_key: "str"

    def __init__(self, *, attribute_name: "str", key: "str", new_key: "str"):
        self.attribute_name = attribute_name
        self.key = key
        self.new_key = new_key
        super().__init__(action="changeEnumKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangeEnumKeyAction":
        from ._schemas.product_type import ProductTypeChangeEnumKeyActionSchema

        return ProductTypeChangeEnumKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeChangeEnumKeyActionSchema

        return ProductTypeChangeEnumKeyActionSchema().dump(self)


class ProductTypeChangeInputHintAction(ProductTypeUpdateAction):
    attribute_name: "str"
    new_value: "TextInputHint"

    def __init__(self, *, attribute_name: "str", new_value: "TextInputHint"):
        self.attribute_name = attribute_name
        self.new_value = new_value
        super().__init__(action="changeInputHint")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangeInputHintAction":
        from ._schemas.product_type import ProductTypeChangeInputHintActionSchema

        return ProductTypeChangeInputHintActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeChangeInputHintActionSchema

        return ProductTypeChangeInputHintActionSchema().dump(self)


class ProductTypeChangeIsSearchableAction(ProductTypeUpdateAction):
    attribute_name: "str"
    is_searchable: "bool"

    def __init__(self, *, attribute_name: "str", is_searchable: "bool"):
        self.attribute_name = attribute_name
        self.is_searchable = is_searchable
        super().__init__(action="changeIsSearchable")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangeIsSearchableAction":
        from ._schemas.product_type import ProductTypeChangeIsSearchableActionSchema

        return ProductTypeChangeIsSearchableActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeChangeIsSearchableActionSchema

        return ProductTypeChangeIsSearchableActionSchema().dump(self)


class ProductTypeChangeLabelAction(ProductTypeUpdateAction):
    attribute_name: "str"
    label: "LocalizedString"

    def __init__(self, *, attribute_name: "str", label: "LocalizedString"):
        self.attribute_name = attribute_name
        self.label = label
        super().__init__(action="changeLabel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangeLabelAction":
        from ._schemas.product_type import ProductTypeChangeLabelActionSchema

        return ProductTypeChangeLabelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeChangeLabelActionSchema

        return ProductTypeChangeLabelActionSchema().dump(self)


class ProductTypeChangeLocalizedEnumValueLabelAction(ProductTypeUpdateAction):
    attribute_name: "str"
    new_value: "AttributeLocalizedEnumValue"

    def __init__(
        self, *, attribute_name: "str", new_value: "AttributeLocalizedEnumValue"
    ):
        self.attribute_name = attribute_name
        self.new_value = new_value
        super().__init__(action="changeLocalizedEnumValueLabel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangeLocalizedEnumValueLabelAction":
        from ._schemas.product_type import (
            ProductTypeChangeLocalizedEnumValueLabelActionSchema,
        )

        return ProductTypeChangeLocalizedEnumValueLabelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import (
            ProductTypeChangeLocalizedEnumValueLabelActionSchema,
        )

        return ProductTypeChangeLocalizedEnumValueLabelActionSchema().dump(self)


class ProductTypeChangeLocalizedEnumValueOrderAction(ProductTypeUpdateAction):
    attribute_name: "str"
    values: typing.List["AttributeLocalizedEnumValue"]

    def __init__(
        self,
        *,
        attribute_name: "str",
        values: typing.List["AttributeLocalizedEnumValue"]
    ):
        self.attribute_name = attribute_name
        self.values = values
        super().__init__(action="changeLocalizedEnumValueOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangeLocalizedEnumValueOrderAction":
        from ._schemas.product_type import (
            ProductTypeChangeLocalizedEnumValueOrderActionSchema,
        )

        return ProductTypeChangeLocalizedEnumValueOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import (
            ProductTypeChangeLocalizedEnumValueOrderActionSchema,
        )

        return ProductTypeChangeLocalizedEnumValueOrderActionSchema().dump(self)


class ProductTypeChangeNameAction(ProductTypeUpdateAction):
    name: "str"

    def __init__(self, *, name: "str"):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangeNameAction":
        from ._schemas.product_type import ProductTypeChangeNameActionSchema

        return ProductTypeChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeChangeNameActionSchema

        return ProductTypeChangeNameActionSchema().dump(self)


class ProductTypeChangePlainEnumValueLabelAction(ProductTypeUpdateAction):
    attribute_name: "str"
    new_value: "AttributePlainEnumValue"

    def __init__(self, *, attribute_name: "str", new_value: "AttributePlainEnumValue"):
        self.attribute_name = attribute_name
        self.new_value = new_value
        super().__init__(action="changePlainEnumValueLabel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangePlainEnumValueLabelAction":
        from ._schemas.product_type import (
            ProductTypeChangePlainEnumValueLabelActionSchema,
        )

        return ProductTypeChangePlainEnumValueLabelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import (
            ProductTypeChangePlainEnumValueLabelActionSchema,
        )

        return ProductTypeChangePlainEnumValueLabelActionSchema().dump(self)


class ProductTypeChangePlainEnumValueOrderAction(ProductTypeUpdateAction):
    attribute_name: "str"
    values: typing.List["AttributePlainEnumValue"]

    def __init__(
        self, *, attribute_name: "str", values: typing.List["AttributePlainEnumValue"]
    ):
        self.attribute_name = attribute_name
        self.values = values
        super().__init__(action="changePlainEnumValueOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeChangePlainEnumValueOrderAction":
        from ._schemas.product_type import (
            ProductTypeChangePlainEnumValueOrderActionSchema,
        )

        return ProductTypeChangePlainEnumValueOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import (
            ProductTypeChangePlainEnumValueOrderActionSchema,
        )

        return ProductTypeChangePlainEnumValueOrderActionSchema().dump(self)


class ProductTypeRemoveAttributeDefinitionAction(ProductTypeUpdateAction):
    #: The name of the attribute to remove.
    name: "str"

    def __init__(self, *, name: "str"):
        self.name = name
        super().__init__(action="removeAttributeDefinition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeRemoveAttributeDefinitionAction":
        from ._schemas.product_type import (
            ProductTypeRemoveAttributeDefinitionActionSchema,
        )

        return ProductTypeRemoveAttributeDefinitionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import (
            ProductTypeRemoveAttributeDefinitionActionSchema,
        )

        return ProductTypeRemoveAttributeDefinitionActionSchema().dump(self)


class ProductTypeRemoveEnumValuesAction(ProductTypeUpdateAction):
    attribute_name: "str"
    keys: typing.List["str"]

    def __init__(self, *, attribute_name: "str", keys: typing.List["str"]):
        self.attribute_name = attribute_name
        self.keys = keys
        super().__init__(action="removeEnumValues")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeRemoveEnumValuesAction":
        from ._schemas.product_type import ProductTypeRemoveEnumValuesActionSchema

        return ProductTypeRemoveEnumValuesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeRemoveEnumValuesActionSchema

        return ProductTypeRemoveEnumValuesActionSchema().dump(self)


class ProductTypeSetInputTipAction(ProductTypeUpdateAction):
    attribute_name: "str"
    input_tip: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        attribute_name: "str",
        input_tip: typing.Optional["LocalizedString"] = None
    ):
        self.attribute_name = attribute_name
        self.input_tip = input_tip
        super().__init__(action="setInputTip")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeSetInputTipAction":
        from ._schemas.product_type import ProductTypeSetInputTipActionSchema

        return ProductTypeSetInputTipActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeSetInputTipActionSchema

        return ProductTypeSetInputTipActionSchema().dump(self)


class ProductTypeSetKeyAction(ProductTypeUpdateAction):
    #: If `key` is absent or `null`, this field will be removed if it exists.
    key: typing.Optional["str"]

    def __init__(self, *, key: typing.Optional["str"] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeSetKeyAction":
        from ._schemas.product_type import ProductTypeSetKeyActionSchema

        return ProductTypeSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_type import ProductTypeSetKeyActionSchema

        return ProductTypeSetKeyActionSchema().dump(self)

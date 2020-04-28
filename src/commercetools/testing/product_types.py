import copy
import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import InternalUpdateError, update_attribute


class ProductTypesModel(BaseModel):
    _primary_type_name = "product-type"
    _resource_schema = schemas.ProductTypeSchema
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: types.ProductTypeDraft, id: typing.Optional[str] = None
    ) -> types.ProductType:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        attributes = (
            [_create_attribute_from_draft(attr) for attr in draft.attributes]
            if draft.attributes
            else []
        )

        return types.ProductType(
            id=str(object_id),
            version=1,
            name=draft.name,
            description=draft.description,
            key=draft.key,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            attributes=attributes,
        )


def _create_attribute_from_draft(
    draft: types.AttributeDefinitionDraft
) -> types.AttributeDefinition:
    return types.AttributeDefinition(
        type=draft.type,
        name=draft.name,
        label=draft.label,
        is_required=draft.is_required,
        attribute_constraint=draft.attribute_constraint,
        input_tip=draft.input_tip,
        input_hint=draft.input_hint or types.TextInputHint.SINGLE_LINE,
        is_searchable=draft.is_searchable,
    )


def change_label_action():
    def updater(self, obj: dict, action: types.ProductTypeChangeLabelAction):
        new = copy.deepcopy(obj)

        for attribute in new["attributes"]:
            if attribute["name"] == action.attribute_name:
                attribute["label"] = action.label
                return new

        raise InternalUpdateError(
            "No attribute found with name %r" % action.attribute_name
        )

    return updater


def change_localized_enum_value_label():
    def updater(
        self, obj: dict, action: types.ProductTypeChangeLocalizedEnumValueLabelAction
    ):
        new = copy.deepcopy(obj)

        def update_attribute_type(type_info: dict):
            if type_info["name"] == "lenum":
                for value in type_info["values"]:
                    if value["key"] == action.new_value.key:
                        value["label"] = action.new_value.label
                        return new

            if type_info["name"] == "set":
                return update_attribute_type(type_info["elementType"])

        for attribute in new["attributes"]:
            if attribute["name"] == action.attribute_name:
                result = update_attribute_type(attribute["type"])
                if result is not None:
                    return result

        raise InternalUpdateError(
            "No attribute found with name %r"
            " and local enum value key %r"
            % (action.attribute_name, action.new_value.key)
        )

    return updater


def add_attribute_definition_action():
    schema = schemas.AttributeDefinitionSchema()

    def updater(self, obj: dict, action: types.ProductTypeAddAttributeDefinitionAction):
        existing = [attr["name"] for attr in obj["attributes"]]

        if action.attribute.name in existing:
            raise InternalUpdateError(
                f"Attribute with name {action.attribute.name} already exists"
            )

        attr_json = schema.dump(_create_attribute_from_draft(action.attribute))
        obj["attributes"].append(attr_json)
        return obj

    return updater


class ProductTypesBackend(ServiceBackend):
    service_path = "product-types"
    model_class = ProductTypesModel

    _schema_draft = schemas.ProductTypeDraftSchema
    _schema_update = schemas.ProductTypeUpdateSchema
    _schema_query_response = schemas.ProductTypePagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
        ]

    _actions = {
        "changeDescription": update_attribute("description", "description"),
        "changeLabel": change_label_action(),
        "changeLocalizedEnumValueLabel": change_localized_enum_value_label(),
        "addAttributeDefinition": add_attribute_definition_action(),
    }

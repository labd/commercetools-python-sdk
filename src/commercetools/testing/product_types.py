import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ProductTypesModel(BaseModel):
    _primary_type_name = "product-type"
    _resource_schema = schemas.ProductTypeSchema

    def _create_from_draft(
        self, draft: types.ProductTypeDraft, id: typing.Optional[str] = None
    ) -> types.ProductType:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.ProductType(
            id=str(object_id),
            version=1,
            name=draft.name,
            description=draft.description,
            key=draft.key,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            attributes=self._create_attributes_from_draft(draft.attributes),
        )

    def _create_attributes_from_draft(
        self,
        draft_attributes: typing.Optional[typing.List[types.AttributeDefinitionDraft]],
    ) -> typing.List[types.AttributeDefinition]:

        result: typing.List[types.AttributeDefinition] = []
        if not draft_attributes:
            return result

        for draft in draft_attributes:
            ad = types.AttributeDefinition(
                type=draft.type,
                name=draft.name,
                label=draft.label,
                is_required=draft.is_required,
                attribute_constraint=draft.attribute_constraint,
                input_tip=draft.input_tip,
                input_hint=draft.input_hint,
                is_searchable=draft.is_searchable,
            )
            result.append(ad)
        return result


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

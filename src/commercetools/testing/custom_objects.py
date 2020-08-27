import datetime
import typing
import uuid

from commercetools import types
from commercetools._schemas._custom_object import (
    CustomObjectDraftSchema,
    CustomObjectPagedQueryResponseSchema,
    CustomObjectSchema,
)
from commercetools._schemas._error import ErrorResponseSchema
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import create_commercetools_response


class CustomObjectsModel(BaseModel):
    _primary_type_name = "custom-object"
    _resource_schema = CustomObjectSchema

    def _generate_key(self, obj):
        return obj.container, obj.key

    def _create_from_draft(
        self, obj: types.CustomObjectDraft, id: typing.Optional[str] = None
    ) -> types.CustomObject:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.CustomObject(
            id=str(object_id),
            version=1,
            key=obj.key,
            container=obj.container,
            value=obj.value,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
        )


class CustomObjectsBackend(ServiceBackend):
    service_path = "custom-objects"
    model_class = CustomObjectsModel
    _schema_draft = CustomObjectDraftSchema
    _schema_query_response = CustomObjectPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<container>[^/]+)/(?P<key>[^/]+)$", "GET", self.get_by_container_key),
        ]

    def get_by_id(self, request, id):
        item = next(
            (obj for obj in self.model.objects.values() if obj["id"] == id), None
        )
        if item:
            return create_commercetools_response(request, json=item)
        return create_commercetools_response(request, status_code=404)

    def get_by_container_key(self, request, container: str, key: str):
        id = (container, key)
        item = self.model.objects.get(id)
        if item:
            return create_commercetools_response(request, json=item)
        else:
            content = ErrorResponseSchema().dumps(
                types.ErrorResponse(
                    status_code=404,
                    message=f"The CustomObject with ID '({container},{key})'",
                    errors=[
                        types.InvalidSubjectError(
                            message=f"The CustomObject with ID '({container},{key}' was not found."  # noqa E501
                        )
                    ],
                )
            )
            return create_commercetools_response(request, text=content, status_code=404)

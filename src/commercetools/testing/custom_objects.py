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
            ("^(?P<container>[^/]+)/(?P<key>[^/]+)$", "GET", self.get_by_container_key),
            ("^(?P<container>[^/]+)$", "GET", self.query_by_container),
        ]

    def query_by_container(self, request, container: str):
        # container is not a valid predicate filter, but we can abuse it internally.
        if "where" not in request.qs:
            request.qs["where"] = f'container = "{container}"'
        else:
            request.qs["where"] = f'container = "{container}" AND {request.qs["where"]}'

        return self.query(request)

    def get_by_container_key(self, request, container: str, key: str):
        item = next(
            (
                obj
                for obj in self.model.objects.values()
                if obj["container"] == container and obj["key"] == key
            ),
            None,
        )
        if item:
            return create_commercetools_response(request, json=item)
        else:
            return create_commercetools_response(request, status_code=404)

import datetime
import typing
import uuid

from commercetools.platform import models
from commercetools.platform.models._schemas.custom_object import (
    CustomObjectDraftSchema,
    CustomObjectPagedQueryResponseSchema,
    CustomObjectSchema,
)
from commercetools.platform.models._schemas.error import ErrorResponseSchema
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import create_commercetools_response


class CustomObjectsModel(BaseModel):
    _primary_type_name = "custom-object"
    _resource_schema = CustomObjectSchema

    def _generate_key(self, obj):
        return obj.container, obj.key

    def add(self, draft, id=None):
        """Add a new object to the storage.

        If the container/key already exists we update the value as long as the
        version matches. otherwise create a new item
        """
        new_obj = self._create_from_draft(draft, id)
        current_obj = self._get_by_container_key(new_obj.container, new_obj.key)

        if current_obj:
            if current_obj["version"] != new_obj.version:
                raise ValueError(
                    "Version mismatch: got %d, expected %d"
                    % (new_obj.version, current_obj["version"])
                )
            current_obj["value"] = new_obj.value
            self.save(current_obj)
            return current_obj
        else:
            return self._store_obj(new_obj)

    def _create_from_draft(
        self, obj: models.CustomObjectDraft, id: typing.Optional[str] = None
    ) -> models.CustomObject:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return models.CustomObject(
            id=str(object_id),
            version=1,
            key=obj.key,
            container=obj.container,
            value=obj.value,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
        )

    def _get_by_container_key(
        self, container: str, key: str
    ) -> typing.Optional[typing.Dict]:
        return next(
            (
                obj
                for obj in self.objects.values()
                if obj["container"] == container and obj["key"] == key
            ),
            None,
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
        item = self.model._get_by_container_key(container, key)
        if item:
            return create_commercetools_response(request, json=item)
        else:
            return create_commercetools_response(request, status_code=404)

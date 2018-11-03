import datetime
import uuid

from requests_mock import create_response

from commercetools import abstract, schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class CustomObjectsModel(BaseModel):
    def add(self, obj):
        obj = self.create_custom_object(obj)
        self.objects[(obj.container, obj.key)] = obj
        return obj

    def create_custom_object(self, obj: types.CustomObjectDraft) -> types.CustomObject:
        return types.CustomObject(
            id=str(uuid.uuid4()),
            version=1,
            key=obj.key,
            container=obj.container,
            value=obj.value,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
        )


class CustomObjectsBackend(ServiceBackend):
    service_path = "custom-objects"
    model_class = CustomObjectsModel

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
        ]

    @property
    def path_prefix(self):
        return r"/(?P<project>[^/]+)/custom-objects/?(?P<path>.*)?"

    def query(self, request):
        obj = abstract.AbstractQuerySchema().load(request.qs)
        data = {
            "count": len(self.model.objects),
            "total": len(self.model.objects),
            "offset": 0,
            "results": self.model.objects.values(),
        }
        content = schemas.CustomObjectPagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def create(self, request):
        obj = schemas.CustomObjectDraftSchema().loads(request.body)
        data = self.model.add(obj)
        content = schemas.CustomObjectSchema().dumps(data)
        return create_response(request, text=content)

    def get_by_id(self, request, id):
        item = next((obj for obj in self.model.objects.values() if obj.id == id), None)
        if item:
            content = schemas.CustomObjectSchema().dumps(item)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

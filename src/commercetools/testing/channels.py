import datetime
import uuid

from requests_mock import create_response

from commercetools import abstract, schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ChannelsModel(BaseModel):
    def add(self, id, obj):
        obj = self.add_channel(obj)
        self.objects[obj.id] = obj
        return obj

    def add_channel(self, obj):
        return types.Channel(
            id=str(uuid.uuid4()),
            version=1,
            name=obj.name,
            description=obj.description,
            roles=obj.roles,
            key=obj.key,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
        )


class ChannelsBackend(ServiceBackend):
    service_path = "categories"
    model_class = ChannelsModel

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]

    @property
    def path_prefix(self):
        return r"/(?P<project>[^/]+)/channels/?(?P<path>.*)?"

    def query(self, request):
        obj = abstract.AbstractQuerySchema().load(request.qs)
        data = {
            "count": len(self.model.objects),
            "total": len(self.model.objects),
            "offset": 0,
            "results": self.model.objects.values(),
        }
        content = schemas.ChannelPagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def create(self, request):
        obj = schemas.ChannelDraftSchema().loads(request.body)
        data = self.model.add(id, obj)
        content = schemas.ChannelSchema().dumps(data)
        return create_response(request, text=content)

    def get_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            content = schemas.ChannelSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def update_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            schemas.ChannelUpdateSchema().loads(request.body)
            content = schemas.ChannelSchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

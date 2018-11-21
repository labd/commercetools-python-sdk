import datetime
import typing
import uuid

from requests_mock import create_response

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ChannelsModel(BaseModel):
    def _create_from_draft(
        self, obj: types.ChannelDraft, id: typing.Optional[str] = None
    ) -> types.CustomObject:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.Channel(
            id=str(object_id),
            version=1,
            name=obj.name,
            description=obj.description,
            roles=obj.roles,
            key=obj.key,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
            custom=utils.create_from_draft(obj.custom),
        )


class ChannelsBackend(ServiceBackend):
    service_path = "channels"
    model_class = ChannelsModel

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]

    def query(self, request):
        params = utils.parse_request_params(abstract.AbstractQuerySchema, request)
        results = list(self.model.objects.values())
        if params.get("limit"):
            results = results[: params["limit"]]

        data = {
            "count": len(results),
            "total": len(self.model.objects),
            "offset": 0,
            "results": results,
        }
        content = schemas.ChannelPagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def create(self, request):
        obj = schemas.ChannelDraftSchema().loads(request.body)
        data = self.model.add(obj)
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

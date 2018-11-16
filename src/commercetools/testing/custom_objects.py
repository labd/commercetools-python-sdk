import datetime
import typing
import uuid

from requests_mock import create_response

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class CustomObjectsModel(BaseModel):
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
            ("^(?P<container>[^/]+)/(?P<key>[^/]+)$", "GET", self.get_by_container_key),
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

    def get_by_container_key(self, request, container: str, key: str):
        id = (container, key)
        item = self.model.objects.get(id)
        if item:
            content = schemas.CustomObjectSchema().dumps(item)
            return create_response(request, text=content)
        else:
            content = schemas.ErrorResponseSchema().dumps(
                types.ErrorResponse(
                    status_code=404,
                    message=f"The CustomObject with ID '({container},{key})'",
                    errors=[
                        types.InvalidSubjectError(
                            code="InvalidSubject",
                            message=f"The CustomObject with ID '({container},{key}' was not found.",
                        )
                    ],
                )
            )
            return create_response(request, text=content, status_code=404)

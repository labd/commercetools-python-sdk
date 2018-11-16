import datetime
import typing
import uuid

from requests_mock import create_response

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class TaxCategoryModel(BaseModel):
    def _create_from_draft(
        self, obj: types.TaxCategoryDraft, id: typing.Optional[str] = None
    ) -> types.TaxCategory:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        obj = types.TaxCategory(
            id=str(object_id),
            key=obj.key,
            version=1,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
            name=obj.name,
            description=obj.description,
        )
        return obj


class TaxCategoryBackend(ServiceBackend):
    service_path = "tax-categories"
    model_class = TaxCategoryModel

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
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
        content = schemas.TaxCategoryPagedQueryResponseSchema().dumps(data)
        return create_response(request, text=content)

    def create(self, request):
        obj = schemas.TaxCategoryDraftSchema().loads(request.body)
        data = self.model.add(obj)
        content = schemas.TaxCategorySchema().dumps(data)
        return create_response(request, text=content)

    def get_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            content = schemas.TaxCategorySchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def get_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            content = schemas.TaxCategorySchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def update_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            schemas.TaxCategorySchema().loads(request.body)
            content = schemas.TaxCategorySchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

    def update_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            schemas.TaxCategorySchema().loads(request.body)
            content = schemas.TaxCategorySchema().dumps(obj)
            return create_response(request, text=content)
        return create_response(request, status_code=404)

import re
import typing
import uuid

import requests_mock
from requests_mock import create_response

from commercetools.services import abstract
from commercetools.testing import utils


class BaseModel:
    _resource_schema = None

    def __init__(self):
        self.objects: typing.Dict = {}

    def add(self, obj, id=None):
        obj = self._create_from_draft(obj, id)
        key = self._generate_key(obj)
        document = self._resource_schema().dump(obj)
        self.objects[key] = document
        return document

    def _generate_key(self, obj):
        return uuid.UUID(obj.id)

    def _create_from_draft(self, obj, id=None):
        raise NotImplementedError()

    def query(self, where):
        objects = list(self.objects.values())
        if not where:
            return objects
        return objects

    def get_by_id(self, id):
        try:
            return self.objects.get(uuid.UUID(id))
        except ValueError:
            return None

    def get_by_key(self, key):
        for obj in self.objects.values():
            if obj["key"] == key:
                return obj


class BaseBackend:
    path = None

    def __init__(self, model=None):
        self.model = model if model is not None else self.model_class()

    def register(self, adapter):
        adapter.add_matcher(self._matcher)

    def _matcher(self, request, skip_port_check=False):
        if not skip_port_check and request.port != 443:
            return

        if request.hostname not in self.hostnames:
            return
            if not request.route_kwargs["path"]:
                request.route_kwargs["path"] = "/"

        match = re.match(self.path_prefix, request.path)
        if match:
            try:
                request_path = match.groupdict()["path"]
            except KeyError:
                request_path = ""

            for path, method, callback in self.urls():
                path_match = re.match(path, request_path)

                # Call the view
                if path_match and request.method == method:
                    response = callback(request, **path_match.groupdict())
                    if response is None:
                        raise NotImplementedError(
                            "No response returned by %r" % callback
                        )
                    return response
            return requests_mock.create_response(request, status_code=404)


class ServiceBackend(BaseBackend):
    hostnames = ["api.sphere.io", "localhost"]
    model_class: typing.Any = None
    _schema_draft = None
    _schema_query_response = None

    @property
    def path_prefix(self):
        return f"/(?P<project>[^/]+)/{self.service_path}/?(?P<path>.*)?"

    def create(self, request):
        obj = self._schema_draft().loads(request.body)
        data = self.model.add(obj)
        return create_response(request, json=data)

    def get_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            return create_response(request, json=obj)
        return create_response(request, status_code=404)

    def get_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            return create_response(request, json=obj)
        return create_response(request, status_code=404)

    def query(self, request):
        params = utils.parse_request_params(abstract.AbstractQuerySchema, request)
        results = self.model.query(params.get("where"))
        total_count = len(results)
        if params.get("limit"):
            results = results[: params["limit"]]

        data = {
            "count": len(results),
            "total": total_count,
            "offset": 0,
            "results": self.model._resource_schema().load(results, many=True),
        }
        content = self._schema_query_response().dumps(data)
        return create_response(request, text=content)

    def update_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            return create_response(request, json=obj)
        return create_response(request, status_code=404)

    def update_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            return create_response(request, json=obj)
        return create_response(request, status_code=404)

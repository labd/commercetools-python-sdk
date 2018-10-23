import re
import typing

import requests_mock


class BaseModel:
    def __init__(self):
        self.objects: typing.Dict = {}

    def add(self, id, obj):
        self.objects[id] = obj

    def get_by_id(self, id):
        return self.objects.get(id)

    def get_by_key(self, key):
        for obj in self.objects.values():
            if obj.key == key:
                return obj


class BaseBackend:
    path = None

    def __init__(self, model=None):
        self.model = model if model is not None else self.model_class()

    def register(self, adapter):
        adapter.add_matcher(self._matcher)

    def _matcher(self, request):
        if request.hostname not in self.hostnames:
            return
            if not request.route_kwargs["path"]:
                request.route_kwargs["path"] = "/"

        match = re.match(self.path_prefix, request.path)
        if match:
            request_path = match.groupdict()["path"]

            for path, method, callback in self.urls():
                path_match = re.match(path, request_path)
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

    @property
    def path_prefix(self):
        return r"/(?P<project>[^/]+)/services/?(?P<path>.*)?"

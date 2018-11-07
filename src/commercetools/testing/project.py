from requests_mock import create_response

from commercetools import schemas
from commercetools.testing.abstract import ServiceBackend


class ProjectBackend(ServiceBackend):
    def __init__(self):
        self.project = {
            "key": "labdigital-sandbox",
            "name": "labdigital-sandbox",
            "countries": ["DE", "US"],
            "currencies": ["EUR"],
            "languages": ["en", "nl", "de", "nl-BE"],
            "createdAt": "2018-10-04T11:32:12.603Z",
            "trialUntil": "2018-12",
            "messages": {"enabled": False, "deleteDaysAfterCreation": 15},
            "version": 4,
        }

    def urls(self):
        return [("^$", "GET", self.get), ("^$", "POST", self.update)]

    @property
    def path_prefix(self):
        return r"/(?P<project>[^/]+)/$"

    def get(self, request):
        content = schemas.ProjectSchema().dumps(self.project)
        return create_response(request, text=content)

    def update(self, request):
        schemas.ProjectUpdateSchema().loads(request.body)

        # Return current
        content = schemas.ChannelSchema().dumps(self.project)
        return create_response(request, text=content)

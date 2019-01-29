import uuid

from commercetools import schemas
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import update_attribute


class ProjectsModel(BaseModel):
    _resource_schema = schemas.ChannelSchema
    _primary_type_name = "project"


class ProjectBackend(ServiceBackend):
    model_class = ProjectsModel
    _resource_schema = schemas.ProjectSchema
    _schema_update = schemas.ProjectUpdateSchema

    def __init__(self, storage):
        super().__init__(storage)

        project_id = uuid.uuid4()
        self.model.objects[project_id] = {
            "id": str(project_id),
            "key": "unittest",
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
        project_key = request.kwargs["project"]
        return self.get_by_key(request, project_key)

    def update(self, request):
        project_key = request.kwargs["project"]
        return self.update_by_key(request, project_key)

    # Fixme: use decorator for this
    _actions = {
        "changeCountries": update_attribute("countries", "countries"),
        "changeCurrencies": update_attribute("currencies", "currencies"),
        "changeName": update_attribute("name", "name"),
        "changeLanguages": update_attribute("languages", "languages"),
    }

import copy
import uuid

from commercetools import schemas
from commercetools.testing.abstract import BaseModel, ServiceBackend


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

    def _change_countries(self, obj, action):
        if obj['countries'] != action.countries:
            new = copy.deepcopy(obj)
            new['countries'] = action.countries
            return new
        return obj

    def _change_name(self, obj, action):
        if obj['name'] != action.name:
            new = copy.deepcopy(obj)
            new['name'] = action.name
            return new
        return obj

    def _change_languages(self, obj, action):
        if obj['languages'] != action.languages:
            new = copy.deepcopy(obj)
            new['languages'] = action.languages
            return new
        return obj

    # Fixme: use decorator for this
    _actions = {
        'changeCountries': _change_countries,
        'changeName': _change_name,
        'changeLanguages': _change_languages,
    }

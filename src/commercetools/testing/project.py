import copy
import uuid

from commercetools.platform import models
from commercetools.platform.models._schemas.project import (
    ProjectSchema,
    ProjectUpdateSchema,
)
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import update_attribute


class ProjectsModel(BaseModel):
    _resource_schema = ProjectSchema
    _primary_type_name = "project"


class ProjectBackend(ServiceBackend):
    model_class = ProjectsModel
    _resource_schema = ProjectSchema
    _schema_update = ProjectUpdateSchema

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
            "carts": {
                "countryTaxRateFallbackEnabled": False,
                "deleteDaysAfterLastModification": 90,
            },
            "messages": {"enabled": False, "deleteDaysAfterCreation": 15},
            "externalOAuth": None,
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

    def change_messages_enabled(
        self, obj, action: models.ProjectChangeMessagesEnabledAction
    ):
        # real API always increments version, so always apply new value.
        new = copy.deepcopy(obj)
        new["messages"]["enabled"] = action.messages_enabled
        return new

    def change_country_tax_rate_fallback_enabled(
        self, obj, action: models.ProjectChangeCountryTaxRateFallbackEnabledAction
    ):
        # real API always increments version, so always apply new value.
        new = copy.deepcopy(obj)
        new["carts"][
            "countryTaxRateFallbackEnabled"
        ] = action.country_tax_rate_fallback_enabled
        return new

    # Fixme: use decorator for this
    _actions = {
        "changeCountries": update_attribute("countries", "countries"),
        "changeCurrencies": update_attribute("currencies", "currencies"),
        "changeName": update_attribute("name", "name"),
        "changeLanguages": update_attribute("languages", "languages"),
        "setExternalOAuth": update_attribute("externalOAuth", "external_o_auth"),
        "changeMessagesEnabled": change_messages_enabled,
        "changeCountryTaxRateFallbackEnabled": change_country_tax_rate_fallback_enabled,
    }

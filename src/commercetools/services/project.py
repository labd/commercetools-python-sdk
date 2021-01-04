from typing import List

from commercetools.platform import models
from commercetools.platform.models._schemas.project import (
    ProjectSchema,
    ProjectUpdateSchema,
)
from commercetools.services import abstract

__all__ = ["ProjectService"]


class ProjectService(abstract.AbstractService):
    def get(self) -> models.Order:
        return self._client._get("", {}, ProjectSchema)

    def update(
        self,
        version: int,
        actions: List[models.OrderUpdateAction],
        *,
        force_update: bool = False,
    ) -> models.Order:
        update_action = models.ProjectUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint="",
            params={},
            data_object=update_action,
            request_schema_cls=ProjectUpdateSchema,
            response_schema_cls=ProjectSchema,
            force_update=force_update,
        )

from typing import List

from commercetools.platform import models
from commercetools.services import abstract

__all__ = ["ProjectService"]


class ProjectService(abstract.AbstractService):
    def get(self) -> models.Order:
        return self._client._get(endpoint="", params={}, response_class=models.Project)

    def update(
        self,
        version: int,
        actions: List[models.OrderUpdateAction],
        *,
        force_update: bool = False,
    ) -> models.Project:
        update_action = models.ProjectUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint="",
            params={},
            data_object=update_action,
            response_class=models.Project,
            force_update=force_update,
        )

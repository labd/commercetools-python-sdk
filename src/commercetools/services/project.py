from typing import List

from commercetools import schemas, types
from commercetools.services import abstract

__all__ = ["ProjectService"]


class ProjectService(abstract.AbstractService):
    def get(self) -> types.Order:
        return self._client._get("", {}, schemas.ProjectSchema)

    def update(
        self, version: int, actions: List[types.OrderUpdateAction]
    ) -> types.Order:
        update_action = types.ProjectUpdate(version=version, actions=actions)
        return self._client._post(
            "", {}, update_action, schemas.ProjectUpdateSchema, schemas.ProjectSchema
        )

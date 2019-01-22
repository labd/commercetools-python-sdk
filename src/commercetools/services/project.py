from typing import List

from commercetools import schemas, types
from commercetools.services import abstract

__all__ = ["ProjectService"]


class ProjectService(abstract.AbstractService):
    def get(self) -> types.Order:
        return self._client._get("", {}, schemas.ProjectSchema)

    def update(
        self,
        version: int,
        actions: List[types.OrderUpdateAction],
        *,
        force_update: bool = False,
    ) -> types.Order:
        update_action = types.ProjectUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint="",
            params={},
            data_object=update_action,
            request_schema_cls=schemas.ProjectUpdateSchema,
            response_schema_cls=schemas.ProjectSchema,
            force_update=force_update,
        )

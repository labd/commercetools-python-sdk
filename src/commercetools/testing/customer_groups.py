import datetime
import uuid
from typing import Optional

from commercetools.platform import models
from commercetools.platform.models._schemas.customer_group import (
    CustomerGroupDraftSchema,
    CustomerGroupPagedQueryResponseSchema,
    CustomerGroupSchema,
    CustomerGroupUpdateSchema,
)
from commercetools.platform.models._schemas.review import ReviewUpdateSchema
from commercetools.testing import abstract, utils
from commercetools.testing.utils import update_attribute


class CustomerGroupModel(abstract.BaseModel):
    _resource_schema = CustomerGroupSchema
    _primary_type_name = "customer-group"
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: models.CustomerGroupDraft, id: Optional[str] = None
    ) -> models.CustomerGroup:
        object_id = uuid.UUID(id) if id is not None else uuid.uuid4()
        return models.CustomerGroup(
            id=str(object_id),
            key=draft.key,
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            name=draft.group_name,
            custom=utils.create_from_draft(draft.custom),
        )


class CustomerGroupBackend(abstract.ServiceBackend):
    service_path = "customer-groups"
    model_class = CustomerGroupModel

    _schema_draft = CustomerGroupDraftSchema
    _schema_update = CustomerGroupUpdateSchema
    _schema_query_response = CustomerGroupPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]

    _actions = {
        "changeName": update_attribute("name", "name"),
        "setKey": update_attribute("key", "key"),
    }

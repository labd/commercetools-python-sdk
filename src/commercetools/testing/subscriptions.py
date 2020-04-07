import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import create_commercetools_response


class SubscriptionsModel(BaseModel):
    _primary_type_name = "subscription"
    _resource_schema = schemas.SubscriptionSchema
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: types.SubscriptionDraft, id: typing.Optional[str] = None
    ) -> types.Subscription:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return types.Subscription(
            id=str(object_id),
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            key=draft.key,
            changes=draft.changes,
            destination=draft.destination,
            messages=draft.messages,
        )


class SubscriptionsBackend(ServiceBackend):
    service_path = "subscriptions"
    model_class = SubscriptionsModel
    _schema_draft = schemas.SubscriptionDraftSchema
    _schema_update = schemas.SubscriptionUpdateSchema
    _schema_query_response = schemas.SubscriptionPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
        ]

    def create(self, request):
        obj = self._schema_draft().loads(request.body)

        if isinstance(obj.destination, types.SqsDestination):
            dest = obj.destination
            message = (
                "A test message could not be delivered to this destination: "
                "SQS %r in %r for %r. "
                "Please make sure your destination is correctly configured."
            ) % (dest.queue_url, dest.region, dest.access_key)
            error = types.ErrorResponse(
                status_code=400,
                message=message,
                errors=[types.InvalidInputError(message=message)],
            )
            error_data = schemas.ErrorResponseSchema().dumps(error).encode("utf-8")
            return create_commercetools_response(
                request, content=error_data, status_code=400
            )

        data = self.model.add(obj)
        return create_commercetools_response(request, json=data)

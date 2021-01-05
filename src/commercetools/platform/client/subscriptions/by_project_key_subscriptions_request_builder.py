# Generated file, please do not change!!!
import typing

from ...models.subscription import (
    Subscription,
    SubscriptionDraft,
    SubscriptionPagedQueryResponse,
)
from .by_project_key_subscriptions_by_id_request_builder import (
    ByProjectKeySubscriptionsByIDRequestBuilder,
)
from .by_project_key_subscriptions_key_by_key_request_builder import (
    ByProjectKeySubscriptionsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeySubscriptionsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeySubscriptionsKeyByKeyRequestBuilder:
        return ByProjectKeySubscriptionsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeySubscriptionsByIDRequestBuilder:
        return ByProjectKeySubscriptionsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: str = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: str = None,
        predicate_var: typing.Dict[str, str] = None,
        headers: typing.Dict[str, str] = None,
    ) -> "SubscriptionPagedQueryResponse":
        """Query subscriptions"""
        params = {
            "expand": expand,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "where": where,
        }
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/subscriptions",
            params=params,
            response_class=SubscriptionPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "SubscriptionDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Subscription":
        """The creation of a Subscription is eventually consistent, it may take up to a minute before it becomes fully active.
        In order to test that the destination is correctly configured, a test message will be put into the queue.
        If the message could not be delivered, the subscription will not be created.
        The payload of the test message is a notification of type ResourceCreated for the resourceTypeId subscription.
        Currently, a maximum of 25 subscriptions can be created per project.

        """
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/subscriptions",
            params={"expand": expand},
            data_object=body,
            response_class=Subscription,
            headers={"Content-Type": "application/json", **headers},
        )

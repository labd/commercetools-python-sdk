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


class ByProjectKeySubscriptionsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeySubscriptionsKeyByKeyRequestBuilder:
        return ByProjectKeySubscriptionsKeyByKeyRequestBuilder(
            key=key, projectKey=self._project_key, client=self._client
        )

    def withId(self, ID: str) -> ByProjectKeySubscriptionsByIDRequestBuilder:
        return ByProjectKeySubscriptionsByIDRequestBuilder(
            ID=ID, projectKey=self._project_key, client=self._client
        )

    def get(
        self,
        *,
        expand: "str" = None,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        where: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "SubscriptionPagedQueryResponse":
        """Query subscriptions
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/subscriptions",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=SubscriptionPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "SubscriptionDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Subscription":
        """The creation of a Subscription is eventually consistent, it may take up to a minute before it becomes fully active.
        In order to test that the destination is correctly configured, a test message will be put into the queue.
        If the message could not be delivered, the subscription will not be created.
        The payload of the test message is a notification of type ResourceCreated for the resourceTypeId subscription.
        Currently, a maximum of 25 subscriptions can be created per project.
        
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/subscriptions",
            params={"expand": expand},
            data_object=body,
            response_object=Subscription,
            headers={"Content-Type": "application/json", **headers},
        )

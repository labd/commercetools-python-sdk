# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.error import ErrorResponse
from ...models.subscription import Subscription, SubscriptionUpdate
from ..health.by_project_key_subscriptions_by_id_health_request_builder import (
    ByProjectKeySubscriptionsByIDHealthRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeySubscriptionsByIDRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _id: str

    def __init__(
        self,
        project_key: str,
        id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._id = id
        self._client = client

    def with_id_health(self) -> ByProjectKeySubscriptionsByIDHealthRequestBuilder:
        return ByProjectKeySubscriptionsByIDHealthRequestBuilder(
            project_key=self._project_key,
            id=self._id,
            client=self._client,
        )

    def get(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Subscription"]:
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/subscriptions/{self._id}",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Subscription.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

    def head(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional[None]:
        """Checks if a Subscription exists for a given `id`. Returns a `200 OK` status if the Subscription exists or a `404 Not Found` otherwise."""
        headers = {} if headers is None else headers
        response = self._client._head(
            endpoint=f"/{self._project_key}/subscriptions/{self._id}",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        elif response.status_code == 200:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def post(
        self,
        body: "SubscriptionUpdate",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Subscription"]:
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/subscriptions/{self._id}",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 200:
            return Subscription.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

    def delete(
        self,
        *,
        version: int,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Subscription"]:
        headers = {} if headers is None else headers
        response = self._client._delete(
            endpoint=f"/{self._project_key}/subscriptions/{self._id}",
            params={"version": version},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Subscription.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

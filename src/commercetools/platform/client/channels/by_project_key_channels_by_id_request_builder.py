# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.channel import Channel, ChannelUpdate
from ...models.error import ErrorResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyChannelsByIDRequestBuilder:

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

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Channel"]:
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/channels/{self._id}",
            params={"expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Channel.deserialize(response.json())
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
        """Checks if a Channel exists for a given `id`. Returns a `200 OK` status if the Channel exists or a `404 Not Found` otherwise."""
        headers = {} if headers is None else headers
        response = self._client._head(
            endpoint=f"/{self._project_key}/channels/{self._id}",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return None
        elif response.status_code == 404:
            return None
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

    def post(
        self,
        body: "ChannelUpdate",
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Channel"]:
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/channels/{self._id}",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 200:
            return Channel.deserialize(response.json())
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
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Channel"]:
        headers = {} if headers is None else headers
        response = self._client._delete(
            endpoint=f"/{self._project_key}/channels/{self._id}",
            params={"version": version, "expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Channel.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            raise self._client._create_exception(None, response)
        warnings.warn("Unhandled status code %d" % response.status_code)

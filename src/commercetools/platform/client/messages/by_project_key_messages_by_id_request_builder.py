# Generated file, please do not change!!!
import typing

from ...models.message import Message


class ByProjectKeyMessagesByIDRequestBuilder:

    _client: "Client"
    _project_key: str
    _id: str

    def __init__(self, projectKey: str, ID: str, client: "Client"):
        self._project_key = projectKey
        self._id = ID
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "Message":
        """Get Message by ID
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/messages/{self._id}",
            params={"expand": expand},
            response_object=Message,
            headers=headers,
        )

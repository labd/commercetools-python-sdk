# Generated file, please do not change!!!
import typing

from ...models.custom_object import CustomObject


class ByProjectKeyCustomObjectsByContainerRequestBuilder:

    _client: "Client"
    _project_key: str
    _container: str

    def __init__(self, projectKey: str, container: str, client: "Client"):
        self._project_key = projectKey
        self._container = container
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "CustomObject":
        """Get CustomObject by container
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/custom-objects/{self._container}",
            params={"expand": expand},
            response_object=CustomObject,
            headers=headers,
        )

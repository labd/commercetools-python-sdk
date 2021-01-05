# Generated file, please do not change!!!
import typing

from ...models.custom_object import CustomObject

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCustomObjectsByContainerByKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _container: str
    _key: str

    def __init__(
        self,
        project_key: str,
        container: str,
        key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._container = container
        self._key = key
        self._client = client

    def get(
        self, *, expand: str = None, headers: typing.Dict[str, str] = None
    ) -> "CustomObject":
        """Get CustomObject by container and key"""
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/custom-objects/{self._container}/{self._key}",
            params={"expand": expand},
            response_class=CustomObject,
            headers=headers,
        )

    def delete(
        self,
        *,
        version: int = None,
        data_erasure: bool = None,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "CustomObject":
        """Delete CustomObject by container and key"""
        headers = {} if headers is None else headers
        return self._client._delete(
            endpoint=f"/{self._project_key}/custom-objects/{self._container}/{self._key}",
            params={"version": version, "dataErasure": data_erasure, "expand": expand},
            response_class=CustomObject,
            headers=headers,
        )

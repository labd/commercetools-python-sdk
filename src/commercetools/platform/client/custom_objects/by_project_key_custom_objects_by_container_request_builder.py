# Generated file, please do not change!!!
import typing
import warnings

from ...models.custom_object import CustomObjectPagedQueryResponse
from ...models.error import ErrorResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCustomObjectsByContainerRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _container: str

    def __init__(
        self,
        project_key: str,
        container: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._container = container
        self._client = client

    def get(
        self,
        *,
        where: typing.List["str"] = None,
        predicate_var: typing.Dict[str, typing.List["str"]] = None,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["CustomObjectPagedQueryResponse"]:
        """Get CustomObjectPagedQueryResponse by container"""
        params = {"where": where, "expand": expand}
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/custom-objects/{self._container}",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return CustomObjectPagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

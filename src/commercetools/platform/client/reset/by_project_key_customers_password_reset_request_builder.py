# Generated file, please do not change!!!
import typing

from ...models.customer import Customer, CustomerResetPassword

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyCustomersPasswordResetRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def post(
        self, body: "CustomerResetPassword", *, headers: typing.Dict[str, str] = None
    ) -> "Customer":
        """Set a new password using a token."""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/customers/password/reset",
            params={},
            data_object=body,
            response_class=Customer,
            headers={"Content-Type": "application/json", **headers},
        )

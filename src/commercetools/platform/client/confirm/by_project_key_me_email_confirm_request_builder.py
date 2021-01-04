# Generated file, please do not change!!!
import typing


class ByProjectKeyMeEmailConfirmRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def post(self, *, headers: typing.Dict[str, str] = None) -> None:
        return self._client._post(
            endpoint=f"/{self._project_key}/me/email/confirm",
            params={},
            response_object=None,
            headers=headers,
        )

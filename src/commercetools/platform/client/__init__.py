# Generated file, please do not change!!!
from commercetools.client import BaseClient

from .by_project_key_request_builder import ByProjectKeyRequestBuilder


class Client(BaseClient):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("url", "https://api.europe-west1.gcp.commercetools.com")
        super().__init__(self, **kwargs)

    def withProjectKey(self, projectKey: str) -> ByProjectKeyRequestBuilder:
        """The Project endpoint is used to retrieve certain information from a project.
            """
        return ByProjectKeyRequestBuilder(projectKey=projectKey, client=self)

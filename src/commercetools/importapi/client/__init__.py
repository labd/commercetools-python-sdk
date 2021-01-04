# Generated file, please do not change!!!
from commercetools.client import BaseClient

from .by_project_key_request_builder import ByProjectKeyRequestBuilder


class Client(BaseClient):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("url", "https://import.europe-west1.gcp.commercetools.com")
        super().__init__(self, **kwargs)

    def withProjectKeyValue(self, projectKey: str) -> ByProjectKeyRequestBuilder:
        return ByProjectKeyRequestBuilder(projectKey=projectKey, client=self)

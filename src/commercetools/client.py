from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from commercetools.services.products import ProductService


class Client:
    def __init__(self, project_key, client_id, client_secret, scope, url, token_url):
        self._url = url
        client = BackendApplicationClient(client_id=client_id)
        self._http_client = OAuth2Session(client=client)
        self._http_client.fetch_token(
            token_url=token_url, client_id=client_id, client_secret=client_secret
        )
        self._base_url = url + "/" + project_key + "/"

    def _get(self, endpoint, params, schema_cls):
        """Retrieve a single object from the commercetools platform"""
        response = self._http_client.get(self._base_url + endpoint)

        if response.status_code == 200:
            return schema_cls().load(response.json())

    @property
    def products(self) -> ProductService:
        return ProductService(self)

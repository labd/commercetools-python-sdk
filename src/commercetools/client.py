from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from commercetools import schemas
from commercetools.services.products import ProductService


class CommercetoolsError(Exception):
    def __init__(self, message, response):
        super().__init__(message)
        self.response = response


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
        else:
            obj = schemas.ErrorResponseSchema().loads(response.content)
            raise CommercetoolsError(obj.message, obj)

    def _create(
        self, endpoint, params, data_object, request_schema_cls, response_schema_cls
    ):
        """Create an object in the commercetools platform"""
        data = request_schema_cls().dump(data_object)
        response = self._http_client.post(self._base_url + endpoint, json=data)
        if response.status_code in (200, 201):
            return response_schema_cls().load(response.json())
        else:
            obj = schemas.ErrorResponseSchema().loads(response.content)
            raise CommercetoolsError(obj.message, obj)

    def _update(
        self, endpoint, params, data_object, request_schema_cls, response_schema_cls
    ):
        """Retrieve a single object from the commercetools platform"""
        data = request_schema_cls().dump(data_object)
        response = self._http_client.post(self._base_url + endpoint, json=data)
        if response.status_code == 200:
            return response_schema_cls().load(response.json())
        else:
            obj = schemas.ErrorResponseSchema().loads(response.content)
            raise CommercetoolsError(obj.message, obj)

    @property
    def products(self) -> ProductService:
        return ProductService(self)

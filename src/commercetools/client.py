import os
import typing

import requests
from marshmallow.base import SchemaABC
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from commercetools import schemas
from commercetools.services.carts import CartService
from commercetools.services.categories import CategoriesService
from commercetools.services.orders import OrderService
from commercetools.services.payments import PaymentService
from commercetools.services.product_projections import ProductProjectionService
from commercetools.services.products import ProductService

env = os.environ.get


class CommercetoolsError(Exception):
    def __init__(self, message, response) -> None:
        super().__init__(message)
        self.response = response


class Client:
    def __init__(self, project_key: str=None, client_id: str=None, client_secret: str=None,
                 scope: typing.List[str]=None, url: str=None, token_url: str=None) -> None:
        project_key = project_key or env('CTP_PROJECT_KEY')
        client_id = client_id or env('CTP_CLIENT_ID')
        client_secret = client_secret or env('CTP_CLIENT_SECRET')
        scope = scope or env('CTP_SCOPES', '').split(',')
        url = url or env('CTP_API_URL')
        token_url = token_url or env('CTP_AUTH_URL', '') + '/oauth/token'

        self._url = url
        client = BackendApplicationClient(client_id=client_id)
        self._http_client = OAuth2Session(client=client)
        self._http_client.fetch_token(
            token_url=token_url, client_id=client_id, client_secret=client_secret
        )
        self._base_url = f"{url}/{project_key}/"

    def _get(
        self, endpoint: str, params: typing.Dict[str, typing.Any], schema_cls: SchemaABC
    ) -> typing.Any:
        """Retrieve a single object from the commercetools platform"""
        response = self._http_client.get(self._base_url + endpoint, params=params)

        if response.status_code == 200:
            return schema_cls().load(response.json())
        return self._process_error(response)

    def _post(
        self,
        endpoint: str,
        params: typing.Dict[str, str],
        data_object: typing.Any,
        request_schema_cls: SchemaABC,
        response_schema_cls: SchemaABC,
        form_encoded: bool = False,
    ) -> typing.Any:
        """Retrieve a single object from the commercetools platform"""
        data = request_schema_cls().dump(data_object)
        if form_encoded:
            kwargs = {"data": data}
        else:
            kwargs = {"json": data}
        response = self._http_client.post(self._base_url + endpoint, **kwargs)

        if response.status_code in (200, 201):
            return response_schema_cls().load(response.json())
        return self._process_error(response)

    def _delete(
        self,
        endpoint: str,
        params: typing.Dict[str, str],
        response_schema_cls: SchemaABC,
    ) -> typing.Any:
        """Delete an object from the commercetools platform"""
        response = self._http_client.delete(self._base_url + endpoint, params=params)

        if response.status_code == 200:
            return response_schema_cls().load(response.json())
        return self._process_error(response)

    def _process_error(self, response: requests.Response) -> None:
        if not response.content:
            response.raise_for_status()
        obj = schemas.ErrorResponseSchema().loads(response.content)
        raise CommercetoolsError(obj.message, obj)

    @property
    def categories(self) -> CategoriesService:
        return CategoriesService(self)

    @property
    def products(self) -> ProductService:
        return ProductService(self)

    @property
    def carts(self) -> CartService:
        return CartService(self)

    @property
    def orders(self) -> OrderService:
        return OrderService(self)

    @property
    def payments(self) -> PaymentService:
        return PaymentService(self)

    @property
    def product_projections(self) -> ProductProjectionService:
        return ProductProjectionService(self)

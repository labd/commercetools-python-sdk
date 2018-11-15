import os
import typing

import requests
from marshmallow.base import SchemaABC
from oauthlib.oauth2 import BackendApplicationClient
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests_oauthlib import OAuth2Session

from commercetools import schemas
from commercetools.services.carts import CartService
from commercetools.services.categories import CategoryService
from commercetools.services.channels import ChannelService
from commercetools.services.custom_objects import CustomObjectService
from commercetools.services.inventory import InventoryService
from commercetools.services.orders import OrderService
from commercetools.services.payments import PaymentService
from commercetools.services.product_projections import ProductProjectionService
from commercetools.services.product_types import ProductTypeService
from commercetools.services.products import ProductService
from commercetools.services.project import ProjectService
from commercetools.services.tax_categories import TaxCategoryService
from commercetools.services.types import TypeService
from commercetools.utils import BaseTokenSaver, DefaultTokenSaver


class CommercetoolsError(Exception):
    def __init__(self, message, response) -> None:
        super().__init__(message)
        self.response = response


class Client:
    def __init__(
        self,
        project_key: str = None,
        client_id: str = None,
        client_secret: str = None,
        scope: typing.List[str] = None,
        url: str = None,
        token_url: str = None,
        token_saver: BaseTokenSaver = None,
    ) -> None:

        # Use environment variables as fallback
        config = {
            "project_key": project_key,
            "client_id": client_id,
            "client_secret": client_secret,
            "url": url,
            "token_url": token_url,
            "scope": scope,
        }
        # Make sure we use the config vars
        del project_key, client_id, client_secret, url, token_url, scope

        self._config = self._prepare_config(config)
        self._token_saver = token_saver or DefaultTokenSaver()
        self._url = self._config["url"]
        self._base_url = f"{self._config['url']}/{self._config['project_key']}/"

        # Fetch token from the token saver
        token = self._token_saver.get_token(
            self._config["client_id"], self._config["scope"]
        )
        token_oauth_url = f"{self._config['token_url']}/oauth/token"

        client = BackendApplicationClient(
            client_id=self._config["client_id"], scope=self._config["scope"]
        )
        self._http_client = OAuth2Session(
            client=client,
            scope=self._config["scope"],
            auto_refresh_url=token_oauth_url,
            auto_refresh_kwargs={
                "client_id": self._config["client_id"],
                "client_secret": self._config["client_secret"],
            },
            token_updater=self._save_token,
        )

        # Register retry handling for Connection errors and 502, 503, 504.
        retry = Retry(status=3, connect=3, status_forcelist=[502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        self._http_client.mount("http://", adapter)
        self._http_client.mount("https://", adapter)

        if token:
            self._http_client.token = token
        else:
            token = self._http_client.fetch_token(
                token_url=token_oauth_url,
                scope=self._config["scope"],
                client_id=self._config["client_id"],
                client_secret=self._config["client_secret"],
            )
            self._save_token(token)

    def _save_token(self, token):
        self._token_saver.add_token(
            self._config["client_id"], self._config["scope"], token
        )

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

    def _upload(
        self,
        endpoint: str,
        params: typing.Dict[str, str],
        file: typing.IO,
        response_schema_cls: SchemaABC,
    ) -> typing.Any:
        """Retrieve a single object from the commercetools platform"""
        response = self._http_client.post(
            self._base_url + endpoint, data=file.read(), params=params
        )

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

    def _prepare_config(self, config: dict) -> dict:
        if not config.get("project_key"):
            config["project_key"] = os.environ.get("CTP_PROJECT_KEY")

        if not config.get("client_id"):
            config["client_id"] = os.environ.get("CTP_CLIENT_ID")

        if not config.get("client_secret"):
            config["client_secret"] = os.environ.get("CTP_CLIENT_SECRET")

        if not config.get("url"):
            config["url"] = os.environ.get("CTP_API_URL")

        if not config.get("token_url"):
            config["token_url"] = os.environ.get("CTP_AUTH_URL")

        if not config["scope"]:
            config["scope"] = os.environ.get("CTP_SCOPES")
            if config["scope"]:
                config["scope"] = config["scope"].split(",")
            else:
                config["scope"] = ["manage_project:%s" % config["project_key"]]

        for key, value in config.items():
            if value is None:
                raise ValueError(f"No value set for {key}")

        return config

    @property
    def categories(self) -> CategoryService:
        return CategoryService(self)

    @property
    def custom_objects(self) -> CustomObjectService:
        return CustomObjectService(self)

    @property
    def carts(self) -> CartService:
        return CartService(self)

    @property
    def cart_discounts(self):
        raise NotImplementedError()

    @property
    def channels(self) -> ChannelService:
        return ChannelService(self)

    @property
    def discount_codes(self):
        raise NotImplementedError()

    @property
    def inventory(self):
        return InventoryService(self)

    @property
    def orders(self) -> OrderService:
        return OrderService(self)

    @property
    def products(self) -> ProductService:
        return ProductService(self)

    @property
    def product_discounts(self):
        raise NotImplementedError()

    @property
    def project(self) -> ProjectService:
        return ProjectService(self)

    @property
    def payments(self) -> PaymentService:
        return PaymentService(self)

    @property
    def product_projections(self) -> ProductProjectionService:
        return ProductProjectionService(self)

    @property
    def product_types(self) -> ProductTypeService:
        return ProductTypeService(self)

    @property
    def reviews(self):
        raise NotImplementedError()

    @property
    def tax_categories(self) -> TaxCategoryService:
        return TaxCategoryService(self)

    @property
    def types(self) -> TypeService:
        return TypeService(self)

import os
import typing
import urllib.parse

import requests
from marshmallow.base import SchemaABC
from oauthlib.oauth2 import BackendApplicationClient
from requests.adapters import HTTPAdapter
from requests_oauthlib import OAuth2Session
from urllib3.util.retry import Retry

from commercetools._schemas._error import ErrorResponseSchema
from commercetools.constants import HEADER_CORRELATION_ID
from commercetools.exceptions import CommercetoolsError
from commercetools.helpers import _concurrent_retry
from commercetools.services import ServicesMixin
from commercetools.services_async import AsyncServicesMixin
from commercetools.utils import BaseTokenSaver, DefaultTokenSaver, fix_token_url


class RefreshingOAuth2Session(OAuth2Session):
    def refresh_token(self, token_url, **kwargs):
        kwargs.update(self.auto_refresh_kwargs)
        kwargs["scope"] = self.scope
        return self.fetch_token(token_url, **kwargs)


class BaseClient:
    def _process_error(self, response: requests.Response) -> None:
        correlation_id = response.headers.get(HEADER_CORRELATION_ID)
        if not response.content:
            response.raise_for_status()
        obj = schemas.ErrorResponseSchema().loads(response.content)

        # We'll fetch the 'raw' errors from the response because some of the
        # attributes are not included in the schemas.
        # With the raw errors in the CommercetoolsError object we can use that
        # information later to render more detailed error messages
        errors_raw = []
        try:
            response_json = response.json()
        except ValueError:
            pass
        else:
            errors_raw = response_json.get("errors", [])

        raise CommercetoolsError(obj.message, errors_raw, obj, correlation_id)

    def _read_env_vars(self, config: dict) -> dict:
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


class Client(BaseClient, ServicesMixin):
    """The Commercetools Client, used to interact with the Commercetools API.

    :param project_key: the key for the project with which you want to interact
    :param client_id: the oauth2 client id
    :param client_secret: the oauth2 client secret
    :param scope: the oauth2 scope. If None then 'manage_project:{project_key}'
    :param url: the api endpoint
    :param token_url: the oauth2 token url endpoint. This should be the full
     path to the token url.
    :param token_saver: optional custom token saver to store and retrieve the
     oauth2 tokens.

    """

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

        self._config = self._read_env_vars(config)
        self._config["token_url"] = fix_token_url(self._config["token_url"])
        self._token_saver = token_saver or DefaultTokenSaver()
        self._url = self._config["url"]
        self._base_url = f"{self._config['url']}/{self._config['project_key']}/"

        # Fetch token from the token saver
        token = self._token_saver.get_token(
            self._config["client_id"], self._config["scope"]
        )

        client = BackendApplicationClient(
            client_id=self._config["client_id"], scope=self._config["scope"]
        )
        self._http_client = RefreshingOAuth2Session(
            client=client,
            scope=self._config["scope"],
            auto_refresh_url=self._config["token_url"],
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
                token_url=self._config["token_url"],
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
        force_update: bool = False,
    ) -> typing.Any:
        """Retrieve a single object from the commercetools platform"""

        @_concurrent_retry(3 if force_update else 0)
        def remote_http_call(data):
            if form_encoded:
                kwargs = {"data": data}
            else:
                kwargs = {"json": data}
            if params:
                kwargs["params"] = params

            response = self._http_client.post(self._base_url + endpoint, **kwargs)
            if response.status_code in (200, 201):
                return response_schema_cls().load(response.json())
            return self._process_error(response)

        data = request_schema_cls().dump(data_object)
        return remote_http_call(data)

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
        force_delete: bool = False,
    ) -> typing.Any:
        """Delete an object from the commercetools platform"""

        @_concurrent_retry(3 if force_delete else 0)
        def remote_http_call(data):
            response = self._http_client.delete(
                self._base_url + endpoint, params=params
            )
            if response.status_code == 200:
                return response_schema_cls().load(response.json())
            return self._process_error(response)

        return remote_http_call(params)

class AsyncClient(BaseClient, AsyncServicesMixin):

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

        self._config = self._read_env_vars(config)

        self._url = self._config["url"]
        self._base_url = f"{self._config['url']}/{self._config['project_key']}/"
        self._http_client = None
        self.register_services()

    async def _get_client(self):
        if self._http_client is None:
            from authlib.integrations.httpx_client import AsyncOAuth2Client

            self._http_client = AsyncOAuth2Client(
                self._config['client_id'],
                self._config['client_secret'],
                grant_type='client_credentials',
                scope=self._config["scope"],
                audience='auth',
                token_endpoint=self._config['token_url'],
                token_endpoint_auth_method='client_secret_basic',
                update_token=self.update_token,
            )
            await self._http_client.fetch_token(self._config['token_url'])
        return self._http_client

    async def update_token(token, refresh_token=None, access_token=None):
        if refresh_token:
            item = await OAuth2Token.find(name=name, refresh_token=refresh_token)
        elif access_token:
            item = await OAuth2Token.find(name=name, access_token=access_token)
        else:
            return

        # update old token
        item.access_token = token['access_token']
        item.refresh_token = token.get('refresh_token')
        item.expires_at = token['expires_at']
        await item.save()

    async def _get(
        self, endpoint: str, params: typing.Dict[str, typing.Any], schema_cls: SchemaABC
    ) -> typing.Any:
        """Retrieve a single object from the commercetools platform"""

        client = await self._get_client()
        response = await client.get(self._base_url + endpoint, params=params)

        if response.status_code == 200:
            return schema_cls().load(response.json())
        return self._process_error(response)

    async def _post(
        self,
        endpoint: str,
        params: typing.Dict[str, str],
        data_object: typing.Any,
        request_schema_cls: SchemaABC,
        response_schema_cls: SchemaABC,
        form_encoded: bool = False,
        force_update: bool = False,
    ) -> typing.Any:
        """Retrieve a single object from the commercetools platform"""

        @_concurrent_retry(3 if force_update else 0)
        async def remote_http_call(data):
            if form_encoded:
                kwargs = {"data": data}
            else:
                kwargs = {"json": data}
            if params:
                kwargs["params"] = params

            client = await self._get_client()
            response = await client.post(self._base_url + endpoint, **kwargs)
            if response.status_code in (200, 201):
                return response_schema_cls().load(response.json())
            return self._process_error(response)

        data = request_schema_cls().dump(data_object)
        return remote_http_call(data)

    async def _upload(
        self,
        endpoint: str,
        params: typing.Dict[str, str],
        file: typing.IO,
        response_schema_cls: SchemaABC,
    ) -> typing.Any:
        """Retrieve a single object from the commercetools platform"""

        client = await self._get_client()
        response = await client.post(
            self._base_url + endpoint, data=file.read(), params=params
        )

        if response.status_code in (200, 201):
            return response_schema_cls().load(response.json())
        return self._process_error(response)

    async def _delete(
        self,
        endpoint: str,
        params: typing.Dict[str, str],
        response_schema_cls: SchemaABC,
        force_delete: bool = False,
    ) -> typing.Any:
        """Delete an object from the commercetools platform"""

        @_concurrent_retry(3 if force_delete else 0)
        async def remote_http_call(data):
            client = await self._get_client()
            response = client.delete(
                self._base_url + endpoint, params=params
            )
            if response.status_code == 200:
                return response_schema_cls().load(response.json())
            return self._process_error(response)

        return await remote_http_call(params)

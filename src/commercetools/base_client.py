import os
import platform
import sys
import typing

from oauthlib.oauth2 import BackendApplicationClient
from requests.adapters import HTTPAdapter
from requests_oauthlib import OAuth2Session
from urllib3 import Retry

from commercetools.constants import HEADER_CORRELATION_ID
from commercetools.exceptions import CommercetoolsError
from commercetools.helpers import _concurrent_retry
from commercetools.utils import BaseTokenSaver, DefaultTokenSaver, fix_token_url
from commercetools.version import __version__


class RefreshingOAuth2Session(OAuth2Session):
    def refresh_token(self, token_url, **kwargs):
        kwargs.update(self.auto_refresh_kwargs)
        kwargs["scope"] = self.scope
        return self.fetch_token(token_url, **kwargs)


class BaseClient:
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
    :param http_adapter: optional custom http adapter, useful for settings
     custom timeouts, custom retries, or for testing.

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
        http_adapter: HTTPAdapter = None,
    ) -> None:

        # Use environment variables as fallback
        config = {
            "project_key": project_key or "example-project",
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
        self._base_url = f"{self._config['url']}"

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
        self._http_client.headers.update({"User-Agent": self._get_user_agent()})

        if not http_adapter:
            # Register retry handling for Connection errors and 502, 503, 504.
            retry = Retry(status=3, connect=3, status_forcelist=[502, 503, 504])
            http_adapter = HTTPAdapter(max_retries=retry)
        self._http_client.mount("http://", http_adapter)
        self._http_client.mount("https://", http_adapter)

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
        self,
        endpoint: str,
        params: typing.Dict[str, typing.Any],
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Any:
        """Retrieve a single object from the commercetools platform"""
        return self._http_client.get(self._base_url + endpoint, params=params)

    def _post(
        self,
        endpoint: str,
        params: typing.Dict[str, typing.Any],
        data: typing.Any = None,
        json: typing.Dict[str, typing.Any] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Any:
        """Retrieve a single object from the commercetools platform"""
        if options and options.get("force_version"):

            @_concurrent_retry(3, "json")
            def post(**kwargs):
                return self._http_client.post(**kwargs)

            return post(
                url=self._base_url + endpoint,
                params=params,
                data=data,
                json=json,
                headers=headers,
            )
        else:
            return self._http_client.post(
                self._base_url + endpoint,
                params=params,
                data=data,
                json=json,
                headers=headers,
            )

    def _delete(
        self,
        endpoint: str,
        params: typing.Dict[str, typing.Any],
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Any:
        """Delete an object from the commercetools platform"""

        if options and options.get("force_version"):

            @_concurrent_retry(3, "params")
            def delete(**kwargs):
                return self._http_client.delete(**kwargs)

            return delete(url=self._base_url + endpoint, params=params)
        else:
            return self._http_client.delete(self._base_url + endpoint, params=params)

    def _create_exception(self, obj, response) -> CommercetoolsError:
        correlation_id = response.headers.get(HEADER_CORRELATION_ID)
        if not response.content:
            response.raise_for_status()

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

        return CommercetoolsError(obj.message, errors_raw, obj, correlation_id)

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

    def _get_user_agent(self):
        py_version = "%d.%d" % sys.version_info[0:2]
        arch = platform.machine()
        return "commercetools-python-sdk/%s Python/%s (%s; %s; %s)" % (
            __version__,
            py_version,
            sys.implementation.name,
            sys.platform,
            arch,
        )

import io
import typing
import warnings

import requests
from marshmallow.exceptions import ValidationError

from commercetools.helpers import _concurrent_retry

from .base_client import BaseClient
from .constants import HEADER_CORRELATION_ID
from .exceptions import CommercetoolsError
from .protocols import Model


class Client(BaseClient):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            "This client interface will be removed in the near future, "
            + "use the new request builder client "
            + "`commercetools.platform.client.Client()`",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)
        self._base_url = f"{self._config['url']}/{self._config['project_key']}/"

    def _get(
        self,
        endpoint: str,
        params: typing.Dict[str, typing.Any],
        response_class: typing.Type[Model] = None,
        headers: typing.Dict[str, str] = None,
    ) -> typing.Any:
        """Retrieve a single object from the commercetools platform"""
        response = self._http_client.get(self._base_url + endpoint, params=params)

        if response.status_code == 200:
            if response_class:
                return response_class.deserialize(response.json())
        return self._process_error(response)

    def _post(
        self,
        endpoint: str,
        params: typing.Dict[str, typing.Any],
        data_object: typing.Any = None,
        response_class: typing.Type[Model] = None,
        headers: typing.Dict[str, str] = None,
        form_encoded: bool = False,
        force_update: bool = False,
    ) -> typing.Any:
        """Retrieve a single object from the commercetools platform"""

        @_concurrent_retry(3 if force_update else 0, "json")
        def remote_http_call(**kwargs):
            return self._http_client.post(self._base_url + endpoint, **kwargs)

        if isinstance(data_object, io.IOBase):
            data = data_object.read()
        elif data_object is not None:
            data = data_object.serialize()
        else:
            data = None

        if form_encoded and data is not None:
            kwargs = {"data": data}
        else:
            kwargs = {"json": data}
        if params:
            kwargs["params"] = params

        response = remote_http_call(**kwargs)
        if response.status_code in (200, 201):
            return response_class.deserialize(response.json())
        return self._process_error(response)

    def _delete(
        self,
        endpoint: str,
        params: typing.Dict[str, typing.Any],
        response_class: typing.Type[Model] = None,
        headers: typing.Dict[str, str] = None,
        force_delete: bool = False,
    ) -> typing.Any:
        """Delete an object from the commercetools platform"""

        @_concurrent_retry(3 if force_delete else 0, "params")
        def remote_http_call(**kwargs):
            return self._http_client.delete(self._base_url + endpoint, **kwargs)

        response = remote_http_call(params=params)
        if response.status_code == 200:
            if response_class:
                return response_class.deserialize(response.json())
        return self._process_error(response)

    def _process_error(self, response: requests.Response) -> None:
        correlation_id = response.headers.get(HEADER_CORRELATION_ID)
        if not response.content:
            response.raise_for_status()

        # FIXME: The error response defined in the RAML should be used
        from commercetools.platform.models._schemas.error import ErrorResponseSchema

        try:
            obj = ErrorResponseSchema().loads(response.content)
        except ValidationError:
            raise Exception(f"Could not parse error response: {response.content}")

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

    def _upload(
        self,
        endpoint: str,
        params: typing.Dict[str, typing.Any],
        file: typing.IO,
        response_class: Model = None,
    ) -> typing.Any:
        """Retrieve a single object from the commercetools platform"""
        response = self._http_client.post(
            self._base_url + endpoint, data=file.read(), params=params
        )

        if response.status_code in (200, 201):
            if response_class:
                return response_class.deserialize(response.json())
        return self._process_error(response)

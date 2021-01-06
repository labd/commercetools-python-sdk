
import typing
from .protocols import Model
from .base_client import BaseClient
from .services import ServicesMixin


class Client(BaseClient, ServicesMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._base_url = f"{self._config['url']}/{self._config['project_key']}/"

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

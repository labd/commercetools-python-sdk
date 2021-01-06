from .base_client import BaseClient
from .services import ServicesMixin


class Client(BaseClient, ServicesMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._base_url = f"{self._config['url']}/{self._config['project_key']}/"

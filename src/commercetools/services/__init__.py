from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from commercetools.client import Client


class AbstractService:
    def __init__(self, client: "Client") -> None:
        self._client = client

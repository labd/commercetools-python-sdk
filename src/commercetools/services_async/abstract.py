import typing

if typing.TYPE_CHECKING:
    from commercetools import Client


class AbstractService:
    def __init__(self, client: "Client") -> None:
        self._client = client
        self._schemas = {}

    def _serialize_params(self, params, schema):
        if schema not in self._schemas:
            self._schemas[schema] = schema()
        return self._schemas[schema].dump(params)

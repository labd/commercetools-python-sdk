import typing

from marshmallow.base import SchemaABC

if typing.TYPE_CHECKING:
    from commercetools.protocols import ClientProtocol


class AbstractService:
    def __init__(self, client: "ClientProtocol") -> None:
        self._client = client
        self._schemas: typing.Dict[str, SchemaABC] = {}

    def _serialize_params(self, params, schema) -> typing.Dict[str, str]:
        if schema not in self._schemas:
            self._schemas[schema] = schema()
        return self._schemas[schema].dump(params)

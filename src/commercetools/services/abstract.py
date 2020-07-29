import typing

from marshmallow import Schema, fields, post_dump

from commercetools.helpers import OptionalList

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


class RemoveEmptyValuesMixin:
    @post_dump
    def remove_empty_values(self, data, **kwargs):
        """Remove the key, value pairs for which the value is None.

        This doesn't work if allow_none is set. And in the future we might also
        want to remove values which are already the default to minimise the
        params.

        """
        result = {}
        for k, v in data.items():
            if v is not None:
                result[k] = v
        return result


class AbstractDeleteSchema(Schema, RemoveEmptyValuesMixin):
    version = fields.Integer()
    expand = OptionalList(fields.String())


class AbstractQuerySchema(Schema, RemoveEmptyValuesMixin):
    where = OptionalList(fields.String())
    sort = OptionalList(fields.String())
    expand = OptionalList(fields.String())
    limit = fields.Int()
    offset = fields.Int()

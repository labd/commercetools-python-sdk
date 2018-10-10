from marshmallow import Schema, fields, post_dump


class RemoveEmptyValuesMixin:
    @post_dump
    def remove_empty_values(self, data):
        """Remove the key, value pairs for which the value is None.continue

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


class AbstractQuerySchema(Schema, RemoveEmptyValuesMixin):
    where = fields.List(fields.String(required=False))
    sort = fields.List(fields.String(required=False))
    expand = fields.List(fields.String())
    limit = fields.Int(required=False)
    offset = fields.Int(required=False)

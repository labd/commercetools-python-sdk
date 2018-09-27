from marshmallow import Schema, fields


class AbstractDeleteSchema(Schema):
    version = fields.Integer()


class AbstractQuerySchema(Schema):
    where = fields.List(fields.String(required=False))
    sort = fields.List(fields.String(required=False))
    expand = fields.List(fields.String(required=False))
    limit = fields.Int(required=False)
    offset = fields.Int(required=False)

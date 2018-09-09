from typing import Dict, List

import attr

from marshmallow import Schema, fields, post_load


@attr.s(auto_attribs=True)
class Money:
    currency_code: str
    cent_amount: int
    fraction_digits: int


class MoneySchema(Schema):
    currency_code = fields.String(data_key="currencyCode")
    cent_amount = fields.Integer(data_key="centAmount")
    fraction_digits = fields.Integer(data_key="fractionDigits")

    @post_load
    def make(self, data):
        return Money(**data)


@attr.s(auto_attribs=True)
class ResourceIdentifier:
    id: str = None
    key: str = None
    type_id: str = None


class ResourceIdentifierSchema(Schema):
    id = fields.Str()
    key = fields.Str()
    type_id = fields.Str(data_key="typeId")

    @post_load
    def make(self, data):
        return ResourceIdentifier(**data)


class LocalizedString(dict):
    def __repr__(self):
        value = ", ".join("%s=%r" % (k, v) for k, v in self.items())
        return "LocalizedString(%s)" % value

    def __getattr__(self, key):
        if key in self:
            return self[key]
        raise AttributeError("No such attribute")


class LocalizedStringField(fields.Dict):
    def _deserialize(self, value, attr, data):
        result = super()._deserialize(value, attr, data)
        return LocalizedString(**result)


@attr.s(auto_attribs=True)
class AssetSource:
    url: str
    key: str
    dimensions: Dict[str, int]
    content_type: str


class AssetSourceSchema(Schema):
    url = fields.String()
    key = fields.String()
    dimensions = fields.Dict()
    content_type = fields.String(data_key="contentType")

    @post_load
    def make(self, data):
        return AssetSource(**data)


@attr.s(auto_attribs=True)
class AssetDraft:
    key: str
    sources: List[AssetSource]
    name: LocalizedString
    description: LocalizedString
    tags: List[str]
    # custom: CustomFieldsDraft TODO


class AssetDraftSchema(Schema):
    key = fields.String()
    sources = fields.Nested(AssetSourceSchema, many=True)
    name = LocalizedStringField()
    descriptiojn = LocalizedStringField()
    tags = fields.String(many=True)

    @post_load
    def make(self, data):
        return AssetDraft(**data)

@attr.s(auto_attribs=True)
class Asset:
    key: str
    sources: List[AssetSource]
    name: LocalizedString
    description: LocalizedString
    tags: List[str]
    # custom: CustomFieldsDraft TODO


class AssetSchema(Schema):
    key = fields.String()
    sources = fields.Nested(AssetSourceSchema, many=True)
    name = LocalizedStringField()
    descriptiojn = LocalizedStringField()
    tags = fields.String(many=True)

    @post_load
    def make(self, data):
        return Asset(**data)

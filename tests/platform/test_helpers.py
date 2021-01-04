from marshmallow import Schema, fields

from commercetools import helpers


class Dummy(Schema):
    items = helpers.OptionalList(fields.String())


def test_optional_list_str():
    data = Dummy().dump({"items": "foobar"})
    assert data["items"] == ["foobar"]


def test_optional_list_items():
    data = Dummy().dump({"items": ["foobar"]})
    assert data["items"] == ["foobar"]

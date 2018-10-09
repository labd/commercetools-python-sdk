from marshmallow import fields, Schema

from commercetools.fields import PredicateList


class TestPredicateList:
    class MySchema(Schema):
        sort = PredicateList(fields.String(required=False))

    def test_predicate_list_serialize_none(self):
        result = self.MySchema().dump({})
        assert result == {}

    def test_predicate_list_serialize_empty(self):
        result = self.MySchema().dump({"sort": None})
        assert result == {"sort": None}

    def test_predicate_list_serialize_single(self):
        result = self.MySchema().dump({"sort": "id asc"})
        assert result == {"sort": "id asc"}

    def test_predicate_list_serialize_multiple(self):
        result = self.MySchema().dump({"sort": ["id asc", "name desc"]})
        assert result == {"sort": "id asc and name desc"}

    def test_predicate_list_serialize_multiple_three(self):
        result = self.MySchema().dump({"sort": ("id asc", "name desc", "date asc")})
        assert result == {"sort": "id asc and name desc and date asc"}

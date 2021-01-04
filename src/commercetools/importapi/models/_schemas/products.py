# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from .common import ImportResourceSchema, LocalizedStringField

# Fields


# Marshmallow Schemas
class SearchKeywordsSchema(marshmallow.Schema):
    _regex = helpers.RegexField(
        unknown=marshmallow.EXCLUDE,
        pattern=re.compile("^[a-z]{2}(-[A-Z]{2})?$"),
        type=helpers.LazyNestedField(
            nested=helpers.absmod(__name__, ".SearchKeywordSchema"),
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
            many=True,
        ),
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        data = typing.cast(helpers.RegexField, self.fields["_regex"]).postprocess(data)
        return models.SearchKeywords(**data)

    @marshmallow.pre_load
    def pre_load(self, data, **kwargs):
        data = typing.cast(helpers.RegexField, self.fields["_regex"]).preprocess(data)
        return data

    @marshmallow.pre_dump
    def pre_dump(self, data, **kwargs):
        data = typing.cast(helpers.RegexField, self.fields["_regex"]).preprocess(data)
        return data

    @marshmallow.post_dump
    def post_dump(self, data, **kwargs):
        data = typing.cast(helpers.RegexField, self.fields["_regex"]).postprocess(data)
        return data


class SearchKeywordSchema(marshmallow.Schema):
    text = marshmallow.fields.String(allow_none=True, missing=None)
    suggest_tokenizer = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "custom": helpers.absmod(__name__, ".CustomTokenizerSchema"),
            "whitespace": helpers.absmod(__name__, ".WhitespaceTokenizerSchema"),
        },
        missing=None,
        data_key="suggestTokenizer",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SearchKeyword(**data)


class SuggestTokenizerSchema(marshmallow.Schema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.SuggestTokenizer(**data)


class CustomTokenizerSchema(SuggestTokenizerSchema):
    inputs = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CustomTokenizer(**data)


class WhitespaceTokenizerSchema(SuggestTokenizerSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.WhitespaceTokenizer(**data)


class ProductImportSchema(ImportResourceSchema):
    name = LocalizedStringField(allow_none=True, missing=None)
    product_type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ProductTypeKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productType",
    )
    slug = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    categories = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CategoryKeyReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    meta_title = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaTitle"
    )
    meta_description = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaDescription"
    )
    meta_keywords = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaKeywords"
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.TaxCategoryKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxCategory",
    )
    search_keywords = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SearchKeywordsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="searchKeywords",
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.StateKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    publish = marshmallow.fields.Boolean(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductImport(**data)

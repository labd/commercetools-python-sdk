# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResource

if typing.TYPE_CHECKING:
    from .common import (
        CategoryKeyReference,
        LocalizedString,
        ProductTypeKeyReference,
        StateKeyReference,
        TaxCategoryKeyReference,
    )

__all__ = [
    "CustomTokenizer",
    "ProductImport",
    "SearchKeyword",
    "SearchKeywords",
    "SuggestTokenizer",
    "WhitespaceTokenizer",
]


class SearchKeywords(typing.Dict[str, typing.List["SearchKeyword"]]):
    pass


class SearchKeyword(_BaseType):
    text: str
    #: The tokenizer defines the tokens that are used to match against the [Suggest Query](/../products-suggestions#suggest-query) input.
    suggest_tokenizer: typing.Optional["SuggestTokenizer"]

    def __init__(
        self,
        *,
        text: str,
        suggest_tokenizer: typing.Optional["SuggestTokenizer"] = None
    ):
        self.text = text
        self.suggest_tokenizer = suggest_tokenizer
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SearchKeyword":
        from ._schemas.products import SearchKeywordSchema

        return SearchKeywordSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.products import SearchKeywordSchema

        return SearchKeywordSchema().dump(self)


class SuggestTokenizer(_BaseType):
    """The tokenizer defines the tokens that are used to match against the [Suggest Query](/../products-suggestions#suggest-query) input."""

    type: str

    def __init__(self, *, type: str):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SuggestTokenizer":
        if data["type"] == "custom":
            from ._schemas.products import CustomTokenizerSchema

            return CustomTokenizerSchema().load(data)
        if data["type"] == "whitespace":
            from ._schemas.products import WhitespaceTokenizerSchema

            return WhitespaceTokenizerSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.products import SuggestTokenizerSchema

        return SuggestTokenizerSchema().dump(self)


class CustomTokenizer(SuggestTokenizer):
    inputs: typing.List["str"]

    def __init__(self, *, inputs: typing.List["str"]):
        self.inputs = inputs
        super().__init__(type="custom")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomTokenizer":
        from ._schemas.products import CustomTokenizerSchema

        return CustomTokenizerSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.products import CustomTokenizerSchema

        return CustomTokenizerSchema().dump(self)


class WhitespaceTokenizer(SuggestTokenizer):
    def __init__(self):

        super().__init__(type="whitespace")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "WhitespaceTokenizer":
        from ._schemas.products import WhitespaceTokenizerSchema

        return WhitespaceTokenizerSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.products import WhitespaceTokenizerSchema

        return WhitespaceTokenizerSchema().dump(self)


class ProductImport(ImportResource):
    """Import representation for a prduct.

    The import representation for a product is the most minimal representation required
    for creating a product in commercetools.

    """

    #: Maps to `Product.name`.
    name: "LocalizedString"
    #: The product's product type. Maps to `Product.productType`.
    #:
    #: The product type referenced
    #: must already exist in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    product_type: "ProductTypeKeyReference"
    #: Human-readable identifiers usually used as deep-link URL to the related product. Each slug must be unique across a project,
    #: but a product can have the same slug for different languages. Allowed are alphabetic, numeric, underscore (_) and hyphen (-) characters.
    slug: "LocalizedString"
    #: Maps to `Product.description`.
    description: typing.Optional["LocalizedString"]
    #: An array of references to a categories by their keys. Maps to `Product.categories`.
    #:
    #: The categories referenced
    #: must already exist in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    categories: typing.Optional[typing.List["CategoryKeyReference"]]
    #: A localized string is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag), and the values the corresponding strings used for that language.
    #: ```json
    #: {
    #:   "de": "Hundefutter",
    #:   "en": "dog food"
    #: }
    #: ```
    meta_title: typing.Optional["LocalizedString"]
    #: A localized string is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag), and the values the corresponding strings used for that language.
    #: ```json
    #: {
    #:   "de": "Hundefutter",
    #:   "en": "dog food"
    #: }
    #: ```
    meta_description: typing.Optional["LocalizedString"]
    #: A localized string is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag), and the values the corresponding strings used for that language.
    #: ```json
    #: {
    #:   "de": "Hundefutter",
    #:   "en": "dog food"
    #: }
    #: ```
    meta_keywords: typing.Optional["LocalizedString"]
    #: References a tax category by its key.
    #:
    #: The tax category referenced must already exist
    #: in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    tax_category: typing.Optional["TaxCategoryKeyReference"]
    #: Search keywords are primarily used by the suggester but are also considered for the full-text search. SearchKeywords is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag). The value to a language tag key is an array of SearchKeyword for the specific language.
    #: ```json
    #: {
    #:   "en": [
    #:     { "text": "Multi tool" },
    #:     { "text": "Swiss Army Knife", "suggestTokenizer": { "type": "whitespace" } }
    #:   ],
    #:   "de": [
    #:     {
    #:       "text": "Schweizer Messer",
    #:       "suggestTokenizer": {
    #:         "type": "custom",
    #:         "inputs": ["schweizer messer", "offiziersmesser", "sackmesser"]
    #:       }
    #:     }
    #:   ]
    #: }
    #: ```
    search_keywords: typing.Optional["SearchKeywords"]
    #: References a state by its key.
    #:
    #: The tax category referenced must already exist
    #: in the commercetools project, or the
    #: import operation state is set to `Unresolved`.
    state: typing.Optional["StateKeyReference"]
    #: If there were updates, only the updates will be published to `staged` and `current` projection.
    publish: typing.Optional[bool]

    def __init__(
        self,
        *,
        key: str,
        name: "LocalizedString",
        product_type: "ProductTypeKeyReference",
        slug: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        categories: typing.Optional[typing.List["CategoryKeyReference"]] = None,
        meta_title: typing.Optional["LocalizedString"] = None,
        meta_description: typing.Optional["LocalizedString"] = None,
        meta_keywords: typing.Optional["LocalizedString"] = None,
        tax_category: typing.Optional["TaxCategoryKeyReference"] = None,
        search_keywords: typing.Optional["SearchKeywords"] = None,
        state: typing.Optional["StateKeyReference"] = None,
        publish: typing.Optional[bool] = None
    ):
        self.name = name
        self.product_type = product_type
        self.slug = slug
        self.description = description
        self.categories = categories
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords
        self.tax_category = tax_category
        self.search_keywords = search_keywords
        self.state = state
        self.publish = publish
        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductImport":
        from ._schemas.products import ProductImportSchema

        return ProductImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.products import ProductImportSchema

        return ProductImportSchema().dump(self)

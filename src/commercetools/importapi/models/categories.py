# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResource

if typing.TYPE_CHECKING:
    from .common import Asset, CategoryKeyReference, LocalizedString
    from .customfields import Custom


class CategoryImport(ImportResource):
    """Import representation for a category.
    
    """

    #: Maps to `Category.name`.
    name: "LocalizedString"
    #: Maps to `Category.slug`.
    #: Must match the pattern `[-a-zA-Z0-9_]{2,256}`.
    slug: "LocalizedString"
    #: Maps to `Category.description`.
    description: typing.Optional["LocalizedString"]
    #: Maps to `Category.parent`.
    #: The parent category referenced must already exist
    #: in the commercetools project, or the import operation
    #: will have an `Unresolved` state.
    parent: typing.Optional["CategoryKeyReference"]
    #: Maps to `Category.orderHint`.
    order_hint: typing.Optional["str"]
    #: Maps to `Category.externalId`.
    external_id: typing.Optional["str"]
    #: Maps to `Category.metaTitle`.
    meta_title: typing.Optional["LocalizedString"]
    #: Maps to `Category.metaDescription`.
    meta_description: typing.Optional["LocalizedString"]
    #: Maps to `Category.metaKeywords`.
    meta_keywords: typing.Optional["LocalizedString"]
    assets: typing.Optional[typing.List["Asset"]]
    #: The custom fields for this category.
    custom: typing.Optional["Custom"]

    def __init__(
        self,
        *,
        key: "str",
        name: "LocalizedString",
        slug: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        parent: typing.Optional["CategoryKeyReference"] = None,
        order_hint: typing.Optional["str"] = None,
        external_id: typing.Optional["str"] = None,
        meta_title: typing.Optional["LocalizedString"] = None,
        meta_description: typing.Optional["LocalizedString"] = None,
        meta_keywords: typing.Optional["LocalizedString"] = None,
        assets: typing.Optional[typing.List["Asset"]] = None,
        custom: typing.Optional["Custom"] = None
    ):
        self.name = name
        self.slug = slug
        self.description = description
        self.parent = parent
        self.order_hint = order_hint
        self.external_id = external_id
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords
        self.assets = assets
        self.custom = custom
        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CategoryImport":
        from ._schemas.categories import CategoryImportSchema

        return CategoryImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.categories import CategoryImportSchema

        return CategoryImportSchema().dump(self)

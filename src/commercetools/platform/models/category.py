# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import (
        Asset,
        AssetDraft,
        AssetSource,
        CreatedBy,
        LastModifiedBy,
        LocalizedString,
        ReferenceTypeId,
    )
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "Category",
    "CategoryAddAssetAction",
    "CategoryChangeAssetNameAction",
    "CategoryChangeAssetOrderAction",
    "CategoryChangeNameAction",
    "CategoryChangeOrderHintAction",
    "CategoryChangeParentAction",
    "CategoryChangeSlugAction",
    "CategoryDraft",
    "CategoryPagedQueryResponse",
    "CategoryReference",
    "CategoryRemoveAssetAction",
    "CategoryResourceIdentifier",
    "CategorySetAssetCustomFieldAction",
    "CategorySetAssetCustomTypeAction",
    "CategorySetAssetDescriptionAction",
    "CategorySetAssetKeyAction",
    "CategorySetAssetSourcesAction",
    "CategorySetAssetTagsAction",
    "CategorySetCustomFieldAction",
    "CategorySetCustomTypeAction",
    "CategorySetDescriptionAction",
    "CategorySetExternalIdAction",
    "CategorySetKeyAction",
    "CategorySetMetaDescriptionAction",
    "CategorySetMetaKeywordsAction",
    "CategorySetMetaTitleAction",
    "CategoryUpdate",
    "CategoryUpdateAction",
]


class Category(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    name: "LocalizedString"
    #: human-readable identifiers usually used as deep-link URL to the related category.
    #: Each slug is unique across a project, but a category can have the same slug for different languages.
    slug: "LocalizedString"
    description: typing.Optional["LocalizedString"]
    #: Contains the parent path towards the root category.
    ancestors: typing.List["CategoryReference"]
    #: A category that is the parent of this category in the category tree.
    parent: typing.Optional["CategoryReference"]
    #: An attribute as base for a custom category order in one level.
    order_hint: str
    external_id: typing.Optional[str]
    meta_title: typing.Optional["LocalizedString"]
    meta_description: typing.Optional["LocalizedString"]
    meta_keywords: typing.Optional["LocalizedString"]
    custom: typing.Optional["CustomFields"]
    #: Can be used to store images, icons or movies related to this category.
    assets: typing.Optional[typing.List["Asset"]]
    #: User-specific unique identifier for the category.
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        name: "LocalizedString",
        slug: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        ancestors: typing.List["CategoryReference"],
        parent: typing.Optional["CategoryReference"] = None,
        order_hint: str,
        external_id: typing.Optional[str] = None,
        meta_title: typing.Optional["LocalizedString"] = None,
        meta_description: typing.Optional["LocalizedString"] = None,
        meta_keywords: typing.Optional["LocalizedString"] = None,
        custom: typing.Optional["CustomFields"] = None,
        assets: typing.Optional[typing.List["Asset"]] = None,
        key: typing.Optional[str] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.name = name
        self.slug = slug
        self.description = description
        self.ancestors = ancestors
        self.parent = parent
        self.order_hint = order_hint
        self.external_id = external_id
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords
        self.custom = custom
        self.assets = assets
        self.key = key
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Category":
        from ._schemas.category import CategorySchema

        return CategorySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySchema

        return CategorySchema().dump(self)


class CategoryDraft(_BaseType):
    name: "LocalizedString"
    #: human-readable identifier usually used as deep-link URL to the related category.
    #: Allowed are alphabetic, numeric, underscore (`_`) and hyphen (`-`) characters.
    #: Maximum size is 256.
    #: **Must be unique across a project!** The same category can have the same slug for different languages.
    slug: "LocalizedString"
    description: typing.Optional["LocalizedString"]
    #: A category that is the parent of this category in the category tree.
    #: The parent can be set by its ID or by its key.
    parent: typing.Optional["CategoryResourceIdentifier"]
    #: An attribute as base for a custom category order in one level.
    #: A random value will be assigned by API if not set.
    order_hint: typing.Optional[str]
    external_id: typing.Optional[str]
    meta_title: typing.Optional["LocalizedString"]
    meta_description: typing.Optional["LocalizedString"]
    meta_keywords: typing.Optional["LocalizedString"]
    #: The custom fields.
    custom: typing.Optional["CustomFieldsDraft"]
    assets: typing.Optional[typing.List["AssetDraft"]]
    #: User-defined unique identifier for the category.
    #: Keys can only contain alphanumeric characters (`a-Z, 0-9`), underscores and hyphens (`-, _`) and be between 2 and 256 characters.
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        name: "LocalizedString",
        slug: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        parent: typing.Optional["CategoryResourceIdentifier"] = None,
        order_hint: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        meta_title: typing.Optional["LocalizedString"] = None,
        meta_description: typing.Optional["LocalizedString"] = None,
        meta_keywords: typing.Optional["LocalizedString"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        assets: typing.Optional[typing.List["AssetDraft"]] = None,
        key: typing.Optional[str] = None
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
        self.custom = custom
        self.assets = assets
        self.key = key
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CategoryDraft":
        from ._schemas.category import CategoryDraftSchema

        return CategoryDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryDraftSchema

        return CategoryDraftSchema().dump(self)


class CategoryPagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["Category"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["Category"]
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategoryPagedQueryResponse":
        from ._schemas.category import CategoryPagedQueryResponseSchema

        return CategoryPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryPagedQueryResponseSchema

        return CategoryPagedQueryResponseSchema().dump(self)


class CategoryReference(Reference):
    obj: typing.Optional["Category"]

    def __init__(self, *, id: str, obj: typing.Optional["Category"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.CATEGORY)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CategoryReference":
        from ._schemas.category import CategoryReferenceSchema

        return CategoryReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryReferenceSchema

        return CategoryReferenceSchema().dump(self)


class CategoryResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.CATEGORY)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategoryResourceIdentifier":
        from ._schemas.category import CategoryResourceIdentifierSchema

        return CategoryResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryResourceIdentifierSchema

        return CategoryResourceIdentifierSchema().dump(self)


class CategoryUpdate(_BaseType):
    version: int
    actions: typing.List["CategoryUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["CategoryUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CategoryUpdate":
        from ._schemas.category import CategoryUpdateSchema

        return CategoryUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryUpdateSchema

        return CategoryUpdateSchema().dump(self)


class CategoryUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CategoryUpdateAction":
        if data["action"] == "addAsset":
            from ._schemas.category import CategoryAddAssetActionSchema

            return CategoryAddAssetActionSchema().load(data)
        if data["action"] == "changeAssetName":
            from ._schemas.category import CategoryChangeAssetNameActionSchema

            return CategoryChangeAssetNameActionSchema().load(data)
        if data["action"] == "changeAssetOrder":
            from ._schemas.category import CategoryChangeAssetOrderActionSchema

            return CategoryChangeAssetOrderActionSchema().load(data)
        if data["action"] == "changeName":
            from ._schemas.category import CategoryChangeNameActionSchema

            return CategoryChangeNameActionSchema().load(data)
        if data["action"] == "changeOrderHint":
            from ._schemas.category import CategoryChangeOrderHintActionSchema

            return CategoryChangeOrderHintActionSchema().load(data)
        if data["action"] == "changeParent":
            from ._schemas.category import CategoryChangeParentActionSchema

            return CategoryChangeParentActionSchema().load(data)
        if data["action"] == "changeSlug":
            from ._schemas.category import CategoryChangeSlugActionSchema

            return CategoryChangeSlugActionSchema().load(data)
        if data["action"] == "removeAsset":
            from ._schemas.category import CategoryRemoveAssetActionSchema

            return CategoryRemoveAssetActionSchema().load(data)
        if data["action"] == "setAssetCustomField":
            from ._schemas.category import CategorySetAssetCustomFieldActionSchema

            return CategorySetAssetCustomFieldActionSchema().load(data)
        if data["action"] == "setAssetCustomType":
            from ._schemas.category import CategorySetAssetCustomTypeActionSchema

            return CategorySetAssetCustomTypeActionSchema().load(data)
        if data["action"] == "setAssetDescription":
            from ._schemas.category import CategorySetAssetDescriptionActionSchema

            return CategorySetAssetDescriptionActionSchema().load(data)
        if data["action"] == "setAssetKey":
            from ._schemas.category import CategorySetAssetKeyActionSchema

            return CategorySetAssetKeyActionSchema().load(data)
        if data["action"] == "setAssetSources":
            from ._schemas.category import CategorySetAssetSourcesActionSchema

            return CategorySetAssetSourcesActionSchema().load(data)
        if data["action"] == "setAssetTags":
            from ._schemas.category import CategorySetAssetTagsActionSchema

            return CategorySetAssetTagsActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.category import CategorySetCustomFieldActionSchema

            return CategorySetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.category import CategorySetCustomTypeActionSchema

            return CategorySetCustomTypeActionSchema().load(data)
        if data["action"] == "setDescription":
            from ._schemas.category import CategorySetDescriptionActionSchema

            return CategorySetDescriptionActionSchema().load(data)
        if data["action"] == "setExternalId":
            from ._schemas.category import CategorySetExternalIdActionSchema

            return CategorySetExternalIdActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.category import CategorySetKeyActionSchema

            return CategorySetKeyActionSchema().load(data)
        if data["action"] == "setMetaDescription":
            from ._schemas.category import CategorySetMetaDescriptionActionSchema

            return CategorySetMetaDescriptionActionSchema().load(data)
        if data["action"] == "setMetaKeywords":
            from ._schemas.category import CategorySetMetaKeywordsActionSchema

            return CategorySetMetaKeywordsActionSchema().load(data)
        if data["action"] == "setMetaTitle":
            from ._schemas.category import CategorySetMetaTitleActionSchema

            return CategorySetMetaTitleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryUpdateActionSchema

        return CategoryUpdateActionSchema().dump(self)


class CategoryAddAssetAction(CategoryUpdateAction):
    asset: "AssetDraft"
    #: When specified, the value might be `0` and should be lower than the total of the assets list.
    position: typing.Optional[int]

    def __init__(self, *, asset: "AssetDraft", position: typing.Optional[int] = None):
        self.asset = asset
        self.position = position
        super().__init__(action="addAsset")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategoryAddAssetAction":
        from ._schemas.category import CategoryAddAssetActionSchema

        return CategoryAddAssetActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryAddAssetActionSchema

        return CategoryAddAssetActionSchema().dump(self)


class CategoryChangeAssetNameAction(CategoryUpdateAction):
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]
    name: "LocalizedString"

    def __init__(
        self,
        *,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        name: "LocalizedString"
    ):
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.name = name
        super().__init__(action="changeAssetName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategoryChangeAssetNameAction":
        from ._schemas.category import CategoryChangeAssetNameActionSchema

        return CategoryChangeAssetNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryChangeAssetNameActionSchema

        return CategoryChangeAssetNameActionSchema().dump(self)


class CategoryChangeAssetOrderAction(CategoryUpdateAction):
    asset_order: typing.List["str"]

    def __init__(self, *, asset_order: typing.List["str"]):
        self.asset_order = asset_order
        super().__init__(action="changeAssetOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategoryChangeAssetOrderAction":
        from ._schemas.category import CategoryChangeAssetOrderActionSchema

        return CategoryChangeAssetOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryChangeAssetOrderActionSchema

        return CategoryChangeAssetOrderActionSchema().dump(self)


class CategoryChangeNameAction(CategoryUpdateAction):
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString"):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategoryChangeNameAction":
        from ._schemas.category import CategoryChangeNameActionSchema

        return CategoryChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryChangeNameActionSchema

        return CategoryChangeNameActionSchema().dump(self)


class CategoryChangeOrderHintAction(CategoryUpdateAction):
    order_hint: str

    def __init__(self, *, order_hint: str):
        self.order_hint = order_hint
        super().__init__(action="changeOrderHint")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategoryChangeOrderHintAction":
        from ._schemas.category import CategoryChangeOrderHintActionSchema

        return CategoryChangeOrderHintActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryChangeOrderHintActionSchema

        return CategoryChangeOrderHintActionSchema().dump(self)


class CategoryChangeParentAction(CategoryUpdateAction):
    parent: "CategoryResourceIdentifier"

    def __init__(self, *, parent: "CategoryResourceIdentifier"):
        self.parent = parent
        super().__init__(action="changeParent")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategoryChangeParentAction":
        from ._schemas.category import CategoryChangeParentActionSchema

        return CategoryChangeParentActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryChangeParentActionSchema

        return CategoryChangeParentActionSchema().dump(self)


class CategoryChangeSlugAction(CategoryUpdateAction):
    #: Allowed are alphabetic, numeric, underscore (&#95;) and hyphen (&#45;) characters.
    #: Maximum size is {{ site.data.api-limits.slugLength }}.
    slug: "LocalizedString"

    def __init__(self, *, slug: "LocalizedString"):
        self.slug = slug
        super().__init__(action="changeSlug")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategoryChangeSlugAction":
        from ._schemas.category import CategoryChangeSlugActionSchema

        return CategoryChangeSlugActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryChangeSlugActionSchema

        return CategoryChangeSlugActionSchema().dump(self)


class CategoryRemoveAssetAction(CategoryUpdateAction):
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]

    def __init__(
        self,
        *,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None
    ):
        self.asset_id = asset_id
        self.asset_key = asset_key
        super().__init__(action="removeAsset")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategoryRemoveAssetAction":
        from ._schemas.category import CategoryRemoveAssetActionSchema

        return CategoryRemoveAssetActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategoryRemoveAssetActionSchema

        return CategoryRemoveAssetActionSchema().dump(self)


class CategorySetAssetCustomFieldAction(CategoryUpdateAction):
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]
    name: str
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        name: str,
        value: typing.Optional[typing.Any] = None
    ):
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.name = name
        self.value = value
        super().__init__(action="setAssetCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetAssetCustomFieldAction":
        from ._schemas.category import CategorySetAssetCustomFieldActionSchema

        return CategorySetAssetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetAssetCustomFieldActionSchema

        return CategorySetAssetCustomFieldActionSchema().dump(self)


class CategorySetAssetCustomTypeAction(CategoryUpdateAction):
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]
    #: If set, the custom type is set to this new value.
    #: If absent, the custom type and any existing custom fields are removed.
    type: typing.Optional["TypeResourceIdentifier"]
    #: If set, the custom fields are set to this new value.
    fields: typing.Optional[object]

    def __init__(
        self,
        *,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional[object] = None
    ):
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.type = type
        self.fields = fields
        super().__init__(action="setAssetCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetAssetCustomTypeAction":
        from ._schemas.category import CategorySetAssetCustomTypeActionSchema

        return CategorySetAssetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetAssetCustomTypeActionSchema

        return CategorySetAssetCustomTypeActionSchema().dump(self)


class CategorySetAssetDescriptionAction(CategoryUpdateAction):
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]
    description: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None
    ):
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.description = description
        super().__init__(action="setAssetDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetAssetDescriptionAction":
        from ._schemas.category import CategorySetAssetDescriptionActionSchema

        return CategorySetAssetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetAssetDescriptionActionSchema

        return CategorySetAssetDescriptionActionSchema().dump(self)


class CategorySetAssetKeyAction(CategoryUpdateAction):
    asset_id: str
    #: User-defined identifier for the asset.
    #: If left blank or set to `null`, the asset key is unset/removed.
    asset_key: typing.Optional[str]

    def __init__(self, *, asset_id: str, asset_key: typing.Optional[str] = None):
        self.asset_id = asset_id
        self.asset_key = asset_key
        super().__init__(action="setAssetKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetAssetKeyAction":
        from ._schemas.category import CategorySetAssetKeyActionSchema

        return CategorySetAssetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetAssetKeyActionSchema

        return CategorySetAssetKeyActionSchema().dump(self)


class CategorySetAssetSourcesAction(CategoryUpdateAction):
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]
    sources: typing.List["AssetSource"]

    def __init__(
        self,
        *,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        sources: typing.List["AssetSource"]
    ):
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.sources = sources
        super().__init__(action="setAssetSources")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetAssetSourcesAction":
        from ._schemas.category import CategorySetAssetSourcesActionSchema

        return CategorySetAssetSourcesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetAssetSourcesActionSchema

        return CategorySetAssetSourcesActionSchema().dump(self)


class CategorySetAssetTagsAction(CategoryUpdateAction):
    asset_id: typing.Optional[str]
    asset_key: typing.Optional[str]
    tags: typing.Optional[typing.List["str"]]

    def __init__(
        self,
        *,
        asset_id: typing.Optional[str] = None,
        asset_key: typing.Optional[str] = None,
        tags: typing.Optional[typing.List["str"]] = None
    ):
        self.asset_id = asset_id
        self.asset_key = asset_key
        self.tags = tags
        super().__init__(action="setAssetTags")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetAssetTagsAction":
        from ._schemas.category import CategorySetAssetTagsActionSchema

        return CategorySetAssetTagsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetAssetTagsActionSchema

        return CategorySetAssetTagsActionSchema().dump(self)


class CategorySetCustomFieldAction(CategoryUpdateAction):
    name: str
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetCustomFieldAction":
        from ._schemas.category import CategorySetCustomFieldActionSchema

        return CategorySetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetCustomFieldActionSchema

        return CategorySetCustomFieldActionSchema().dump(self)


class CategorySetCustomTypeAction(CategoryUpdateAction):
    #: If absent, the custom type and any existing CustomFields are removed.
    type: typing.Optional["TypeResourceIdentifier"]
    #: A valid JSON object, based on the FieldDefinitions of the Type. Sets the custom fields to this value.
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetCustomTypeAction":
        from ._schemas.category import CategorySetCustomTypeActionSchema

        return CategorySetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetCustomTypeActionSchema

        return CategorySetCustomTypeActionSchema().dump(self)


class CategorySetDescriptionAction(CategoryUpdateAction):
    description: typing.Optional["LocalizedString"]

    def __init__(self, *, description: typing.Optional["LocalizedString"] = None):
        self.description = description
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetDescriptionAction":
        from ._schemas.category import CategorySetDescriptionActionSchema

        return CategorySetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetDescriptionActionSchema

        return CategorySetDescriptionActionSchema().dump(self)


class CategorySetExternalIdAction(CategoryUpdateAction):
    #: If not defined, the external ID is unset.
    external_id: typing.Optional[str]

    def __init__(self, *, external_id: typing.Optional[str] = None):
        self.external_id = external_id
        super().__init__(action="setExternalId")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetExternalIdAction":
        from ._schemas.category import CategorySetExternalIdActionSchema

        return CategorySetExternalIdActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetExternalIdActionSchema

        return CategorySetExternalIdActionSchema().dump(self)


class CategorySetKeyAction(CategoryUpdateAction):
    #: User-defined unique identifier for the category.
    #: Keys can only contain alphanumeric characters (`a-Z, 0-9`), underscores and hyphens (`-, _`) and be between 2 and 256 characters.
    #: If `key` is absent or `null`, this field will be removed if it exists.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CategorySetKeyAction":
        from ._schemas.category import CategorySetKeyActionSchema

        return CategorySetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetKeyActionSchema

        return CategorySetKeyActionSchema().dump(self)


class CategorySetMetaDescriptionAction(CategoryUpdateAction):
    meta_description: typing.Optional["LocalizedString"]

    def __init__(self, *, meta_description: typing.Optional["LocalizedString"] = None):
        self.meta_description = meta_description
        super().__init__(action="setMetaDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetMetaDescriptionAction":
        from ._schemas.category import CategorySetMetaDescriptionActionSchema

        return CategorySetMetaDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetMetaDescriptionActionSchema

        return CategorySetMetaDescriptionActionSchema().dump(self)


class CategorySetMetaKeywordsAction(CategoryUpdateAction):
    meta_keywords: typing.Optional["LocalizedString"]

    def __init__(self, *, meta_keywords: typing.Optional["LocalizedString"] = None):
        self.meta_keywords = meta_keywords
        super().__init__(action="setMetaKeywords")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetMetaKeywordsAction":
        from ._schemas.category import CategorySetMetaKeywordsActionSchema

        return CategorySetMetaKeywordsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetMetaKeywordsActionSchema

        return CategorySetMetaKeywordsActionSchema().dump(self)


class CategorySetMetaTitleAction(CategoryUpdateAction):
    meta_title: typing.Optional["LocalizedString"]

    def __init__(self, *, meta_title: typing.Optional["LocalizedString"] = None):
        self.meta_title = meta_title
        super().__init__(action="setMetaTitle")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CategorySetMetaTitleAction":
        from ._schemas.category import CategorySetMetaTitleActionSchema

        return CategorySetMetaTitleActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.category import CategorySetMetaTitleActionSchema

        return CategorySetMetaTitleActionSchema().dump(self)

# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class CategorySchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="createdBy",
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    slug = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    ancestors = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CategoryReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    parent = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    order_hint = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="orderHint"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
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
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    assets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AssetSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Category(**data)


class CategoryDraftSchema(marshmallow.Schema):
    name = LocalizedStringField(allow_none=True, missing=None)
    slug = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    parent = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CategoryResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    order_hint = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="orderHint"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
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
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    assets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AssetDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CategoryDraft(**data)


class CategoryPagedQueryResponseSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CategorySchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CategoryPagedQueryResponse(**data)


class CategoryReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CategorySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CategoryReference(**data)


class CategoryResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CategoryResourceIdentifier(**data)


class CategoryUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addAsset": helpers.absmod(__name__, ".CategoryAddAssetActionSchema"),
                "changeAssetName": helpers.absmod(
                    __name__, ".CategoryChangeAssetNameActionSchema"
                ),
                "changeAssetOrder": helpers.absmod(
                    __name__, ".CategoryChangeAssetOrderActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".CategoryChangeNameActionSchema"
                ),
                "changeOrderHint": helpers.absmod(
                    __name__, ".CategoryChangeOrderHintActionSchema"
                ),
                "changeParent": helpers.absmod(
                    __name__, ".CategoryChangeParentActionSchema"
                ),
                "changeSlug": helpers.absmod(
                    __name__, ".CategoryChangeSlugActionSchema"
                ),
                "removeAsset": helpers.absmod(
                    __name__, ".CategoryRemoveAssetActionSchema"
                ),
                "setAssetCustomField": helpers.absmod(
                    __name__, ".CategorySetAssetCustomFieldActionSchema"
                ),
                "setAssetCustomType": helpers.absmod(
                    __name__, ".CategorySetAssetCustomTypeActionSchema"
                ),
                "setAssetDescription": helpers.absmod(
                    __name__, ".CategorySetAssetDescriptionActionSchema"
                ),
                "setAssetKey": helpers.absmod(
                    __name__, ".CategorySetAssetKeyActionSchema"
                ),
                "setAssetSources": helpers.absmod(
                    __name__, ".CategorySetAssetSourcesActionSchema"
                ),
                "setAssetTags": helpers.absmod(
                    __name__, ".CategorySetAssetTagsActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".CategorySetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".CategorySetCustomTypeActionSchema"
                ),
                "setDescription": helpers.absmod(
                    __name__, ".CategorySetDescriptionActionSchema"
                ),
                "setExternalId": helpers.absmod(
                    __name__, ".CategorySetExternalIdActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".CategorySetKeyActionSchema"),
                "setMetaDescription": helpers.absmod(
                    __name__, ".CategorySetMetaDescriptionActionSchema"
                ),
                "setMetaKeywords": helpers.absmod(
                    __name__, ".CategorySetMetaKeywordsActionSchema"
                ),
                "setMetaTitle": helpers.absmod(
                    __name__, ".CategorySetMetaTitleActionSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CategoryUpdate(**data)


class CategoryUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategoryUpdateAction(**data)


class CategoryAddAssetActionSchema(CategoryUpdateActionSchema):
    asset = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AssetDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    position = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategoryAddAssetAction(**data)


class CategoryChangeAssetNameActionSchema(CategoryUpdateActionSchema):
    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategoryChangeAssetNameAction(**data)


class CategoryChangeAssetOrderActionSchema(CategoryUpdateActionSchema):
    asset_order = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="assetOrder",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategoryChangeAssetOrderAction(**data)


class CategoryChangeNameActionSchema(CategoryUpdateActionSchema):
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategoryChangeNameAction(**data)


class CategoryChangeOrderHintActionSchema(CategoryUpdateActionSchema):
    order_hint = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="orderHint"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategoryChangeOrderHintAction(**data)


class CategoryChangeParentActionSchema(CategoryUpdateActionSchema):
    parent = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CategoryResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategoryChangeParentAction(**data)


class CategoryChangeSlugActionSchema(CategoryUpdateActionSchema):
    slug = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategoryChangeSlugAction(**data)


class CategoryRemoveAssetActionSchema(CategoryUpdateActionSchema):
    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategoryRemoveAssetAction(**data)


class CategorySetAssetCustomFieldActionSchema(CategoryUpdateActionSchema):
    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetAssetCustomFieldAction(**data)


class CategorySetAssetCustomTypeActionSchema(CategoryUpdateActionSchema):
    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetAssetCustomTypeAction(**data)


class CategorySetAssetDescriptionActionSchema(CategoryUpdateActionSchema):
    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetAssetDescriptionAction(**data)


class CategorySetAssetKeyActionSchema(CategoryUpdateActionSchema):
    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetAssetKeyAction(**data)


class CategorySetAssetSourcesActionSchema(CategoryUpdateActionSchema):
    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )
    sources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AssetSourceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetAssetSourcesAction(**data)


class CategorySetAssetTagsActionSchema(CategoryUpdateActionSchema):
    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )
    tags = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetAssetTagsAction(**data)


class CategorySetCustomFieldActionSchema(CategoryUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetCustomFieldAction(**data)


class CategorySetCustomTypeActionSchema(CategoryUpdateActionSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetCustomTypeAction(**data)


class CategorySetDescriptionActionSchema(CategoryUpdateActionSchema):
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetDescriptionAction(**data)


class CategorySetExternalIdActionSchema(CategoryUpdateActionSchema):
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetExternalIdAction(**data)


class CategorySetKeyActionSchema(CategoryUpdateActionSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetKeyAction(**data)


class CategorySetMetaDescriptionActionSchema(CategoryUpdateActionSchema):
    meta_description = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaDescription"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetMetaDescriptionAction(**data)


class CategorySetMetaKeywordsActionSchema(CategoryUpdateActionSchema):
    meta_keywords = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaKeywords"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetMetaKeywordsAction(**data)


class CategorySetMetaTitleActionSchema(CategoryUpdateActionSchema):
    meta_title = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaTitle"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CategorySetMetaTitleAction(**data)

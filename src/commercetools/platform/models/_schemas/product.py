# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..cart import ProductPublishScope
from ..common import ReferenceTypeId
from ..product import FacetTypes, TermFacetResultType
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from .type import FieldContainerField


# Fields
class CategoryOrderHintsField(marshmallow.fields.Dict):
    def _deserialize(self, value, attr, data, **kwargs):
        result = super()._deserialize(value, attr, data)
        return models.CategoryOrderHints(**result)


# Marshmallow Schemas
class AttributeSchema(helpers.BaseSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Attribute(**data)


class FacetResultSchema(helpers.BaseSchema):
    type = marshmallow_enum.EnumField(
        FacetTypes, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.FacetResult(**data)


class FacetResultRangeSchema(helpers.BaseSchema):
    from_ = marshmallow.fields.Float(allow_none=True, missing=None, data_key="from")
    from_str = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="fromStr"
    )
    to = marshmallow.fields.Float(allow_none=True, missing=None)
    to_str = marshmallow.fields.String(allow_none=True, missing=None, data_key="toStr")
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    product_count = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="productCount",
    )
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    min = marshmallow.fields.Float(allow_none=True, missing=None)
    max = marshmallow.fields.Float(allow_none=True, missing=None)
    mean = marshmallow.fields.Float(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.FacetResultRange(**data)


class FacetResultTermSchema(helpers.BaseSchema):
    term = marshmallow.fields.Raw(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    product_count = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="productCount",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.FacetResultTerm(**data)


class FacetResultsSchema(helpers.BaseSchema):
    _regex = helpers.RegexField(
        unknown=marshmallow.EXCLUDE,
        pattern=re.compile("^[a-z].*$"),
        type=helpers.LazyNestedField(
            nested=helpers.absmod(__name__, "...marshmallow.fields.Raw"),
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
        return models.FacetResults(**data)

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


class FilteredFacetResultSchema(FacetResultSchema):
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    product_count = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="productCount",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.FilteredFacetResult(**data)


class ProductSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    product_type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product_type.ProductTypeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productType",
    )
    master_data = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductCatalogDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="masterData",
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".tax_category.TaxCategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxCategory",
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    review_rating_statistics = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".review.ReviewRatingStatisticsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="reviewRatingStatistics",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Product(**data)


class ProductCatalogDataSchema(helpers.BaseSchema):
    published = marshmallow.fields.Boolean(allow_none=True, missing=None)
    current = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductDataSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    has_staged_changes = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="hasStagedChanges"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductCatalogData(**data)


class ProductDataSchema(helpers.BaseSchema):
    name = LocalizedStringField(allow_none=True, missing=None)
    categories = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    category_order_hints = CategoryOrderHintsField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="categoryOrderHints",
    )
    description = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    slug = LocalizedStringField(allow_none=True, missing=None)
    meta_title = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="metaTitle",
    )
    meta_description = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="metaDescription",
    )
    meta_keywords = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="metaKeywords",
    )
    master_variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductVariantSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="masterVariant",
    )
    variants = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductVariantSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    search_keywords = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SearchKeywordsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="searchKeywords",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductData(**data)


class ProductDraftSchema(helpers.BaseSchema):
    product_type = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".product_type.ProductTypeResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productType",
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    slug = LocalizedStringField(allow_none=True, missing=None)
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    description = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    categories = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".category.CategoryResourceIdentifierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    category_order_hints = CategoryOrderHintsField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="categoryOrderHints",
    )
    meta_title = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="metaTitle",
    )
    meta_description = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="metaDescription",
    )
    meta_keywords = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="metaKeywords",
    )
    master_variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductVariantDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="masterVariant",
    )
    variants = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductVariantDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxCategory",
    )
    search_keywords = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SearchKeywordsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="searchKeywords",
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    publish = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductDraft(**data)


class ProductPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductPagedQueryResponse(**data)


class ProductProjectionSchema(BaseResourceSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    product_type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product_type.ProductTypeReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productType",
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    slug = LocalizedStringField(allow_none=True, missing=None)
    categories = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    category_order_hints = CategoryOrderHintsField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="categoryOrderHints",
    )
    meta_title = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="metaTitle",
    )
    meta_description = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="metaDescription",
    )
    meta_keywords = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="metaKeywords",
    )
    search_keywords = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SearchKeywordsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="searchKeywords",
    )
    has_staged_changes = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="hasStagedChanges",
    )
    published = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    master_variant = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductVariantSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="masterVariant",
    )
    variants = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductVariantSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".tax_category.TaxCategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxCategory",
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    review_rating_statistics = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".review.ReviewRatingStatisticsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="reviewRatingStatistics",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductProjection(**data)


class ProductProjectionPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductProjectionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    facets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".FacetResultsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductProjectionPagedQueryResponse(**data)


class ProductProjectionPagedSearchResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductProjectionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    facets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".FacetResultsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductProjectionPagedSearchResponse(**data)


class ProductReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductReference(**data)


class ProductResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductResourceIdentifier(**data)


class ProductUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addAsset": helpers.absmod(__name__, ".ProductAddAssetActionSchema"),
                "addExternalImage": helpers.absmod(
                    __name__, ".ProductAddExternalImageActionSchema"
                ),
                "addPrice": helpers.absmod(__name__, ".ProductAddPriceActionSchema"),
                "addToCategory": helpers.absmod(
                    __name__, ".ProductAddToCategoryActionSchema"
                ),
                "addVariant": helpers.absmod(
                    __name__, ".ProductAddVariantActionSchema"
                ),
                "changeAssetName": helpers.absmod(
                    __name__, ".ProductChangeAssetNameActionSchema"
                ),
                "changeAssetOrder": helpers.absmod(
                    __name__, ".ProductChangeAssetOrderActionSchema"
                ),
                "changeMasterVariant": helpers.absmod(
                    __name__, ".ProductChangeMasterVariantActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".ProductChangeNameActionSchema"
                ),
                "changePrice": helpers.absmod(
                    __name__, ".ProductChangePriceActionSchema"
                ),
                "changeSlug": helpers.absmod(
                    __name__, ".ProductChangeSlugActionSchema"
                ),
                "legacySetSku": helpers.absmod(
                    __name__, ".ProductLegacySetSkuActionSchema"
                ),
                "moveImageToPosition": helpers.absmod(
                    __name__, ".ProductMoveImageToPositionActionSchema"
                ),
                "publish": helpers.absmod(__name__, ".ProductPublishActionSchema"),
                "removeAsset": helpers.absmod(
                    __name__, ".ProductRemoveAssetActionSchema"
                ),
                "removeFromCategory": helpers.absmod(
                    __name__, ".ProductRemoveFromCategoryActionSchema"
                ),
                "removeImage": helpers.absmod(
                    __name__, ".ProductRemoveImageActionSchema"
                ),
                "removePrice": helpers.absmod(
                    __name__, ".ProductRemovePriceActionSchema"
                ),
                "removeVariant": helpers.absmod(
                    __name__, ".ProductRemoveVariantActionSchema"
                ),
                "revertStagedChanges": helpers.absmod(
                    __name__, ".ProductRevertStagedChangesActionSchema"
                ),
                "revertStagedVariantChanges": helpers.absmod(
                    __name__, ".ProductRevertStagedVariantChangesActionSchema"
                ),
                "setAssetCustomField": helpers.absmod(
                    __name__, ".ProductSetAssetCustomFieldActionSchema"
                ),
                "setAssetCustomType": helpers.absmod(
                    __name__, ".ProductSetAssetCustomTypeActionSchema"
                ),
                "setAssetDescription": helpers.absmod(
                    __name__, ".ProductSetAssetDescriptionActionSchema"
                ),
                "setAssetKey": helpers.absmod(
                    __name__, ".ProductSetAssetKeyActionSchema"
                ),
                "setAssetSources": helpers.absmod(
                    __name__, ".ProductSetAssetSourcesActionSchema"
                ),
                "setAssetTags": helpers.absmod(
                    __name__, ".ProductSetAssetTagsActionSchema"
                ),
                "setAttribute": helpers.absmod(
                    __name__, ".ProductSetAttributeActionSchema"
                ),
                "setAttributeInAllVariants": helpers.absmod(
                    __name__, ".ProductSetAttributeInAllVariantsActionSchema"
                ),
                "setCategoryOrderHint": helpers.absmod(
                    __name__, ".ProductSetCategoryOrderHintActionSchema"
                ),
                "setDescription": helpers.absmod(
                    __name__, ".ProductSetDescriptionActionSchema"
                ),
                "setDiscountedPrice": helpers.absmod(
                    __name__, ".ProductSetDiscountedPriceActionSchema"
                ),
                "setImageLabel": helpers.absmod(
                    __name__, ".ProductSetImageLabelActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".ProductSetKeyActionSchema"),
                "setMetaDescription": helpers.absmod(
                    __name__, ".ProductSetMetaDescriptionActionSchema"
                ),
                "setMetaKeywords": helpers.absmod(
                    __name__, ".ProductSetMetaKeywordsActionSchema"
                ),
                "setMetaTitle": helpers.absmod(
                    __name__, ".ProductSetMetaTitleActionSchema"
                ),
                "setPrices": helpers.absmod(__name__, ".ProductSetPricesActionSchema"),
                "setProductPriceCustomField": helpers.absmod(
                    __name__, ".ProductSetProductPriceCustomFieldActionSchema"
                ),
                "setProductPriceCustomType": helpers.absmod(
                    __name__, ".ProductSetProductPriceCustomTypeActionSchema"
                ),
                "setProductVariantKey": helpers.absmod(
                    __name__, ".ProductSetProductVariantKeyActionSchema"
                ),
                "setSearchKeywords": helpers.absmod(
                    __name__, ".ProductSetSearchKeywordsActionSchema"
                ),
                "setSku": helpers.absmod(__name__, ".ProductSetSkuActionSchema"),
                "setTaxCategory": helpers.absmod(
                    __name__, ".ProductSetTaxCategoryActionSchema"
                ),
                "transitionState": helpers.absmod(
                    __name__, ".ProductTransitionStateActionSchema"
                ),
                "unpublish": helpers.absmod(__name__, ".ProductUnpublishActionSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductUpdate(**data)


class ProductUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductUpdateAction(**data)


class ProductVariantSchema(helpers.BaseSchema):
    id = marshmallow.fields.Integer(allow_none=True, missing=None)
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    prices = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    attributes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributeSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    images = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ImageSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    assets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AssetSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    availability = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductVariantAvailabilitySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    is_matching_variant = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="isMatchingVariant",
    )
    scoped_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ScopedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="scopedPrice",
    )
    scoped_price_discounted = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="scopedPriceDiscounted",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductVariant(**data)


class ProductVariantAvailabilitySchema(helpers.BaseSchema):
    is_on_stock = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="isOnStock",
    )
    restockable_in_days = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="restockableInDays",
    )
    available_quantity = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="availableQuantity",
    )
    channels = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductVariantChannelAvailabilityMapSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductVariantAvailability(**data)


class ProductVariantChannelAvailabilitySchema(helpers.BaseSchema):
    is_on_stock = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="isOnStock",
    )
    restockable_in_days = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="restockableInDays",
    )
    available_quantity = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="availableQuantity",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductVariantChannelAvailability(**data)


class ProductVariantChannelAvailabilityMapSchema(helpers.BaseSchema):
    _regex = helpers.RegexField(
        unknown=marshmallow.EXCLUDE,
        pattern=re.compile(""),
        type=helpers.LazyNestedField(
            nested=helpers.absmod(__name__, ".ProductVariantChannelAvailabilitySchema"),
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
        return models.ProductVariantChannelAvailabilityMap(**data)

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


class ProductVariantDraftSchema(helpers.BaseSchema):
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    prices = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    attributes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributeSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    images = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ImageSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    assets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AssetDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductVariantDraft(**data)


class RangeFacetResultSchema(FacetResultSchema):
    ranges = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".FacetResultRangeSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.RangeFacetResult(**data)


class SearchKeywordSchema(helpers.BaseSchema):
    text = marshmallow.fields.String(allow_none=True, missing=None)
    suggest_tokenizer = marshmallow.fields.Raw(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="suggestTokenizer",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SearchKeyword(**data)


class SearchKeywordsSchema(helpers.BaseSchema):
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


class SuggestTokenizerSchema(helpers.BaseSchema):
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


class SuggestionSchema(helpers.BaseSchema):
    text = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Suggestion(**data)


class SuggestionResultSchema(helpers.BaseSchema):
    _regex = helpers.RegexField(
        unknown=marshmallow.EXCLUDE,
        pattern=re.compile("searchKeywords.[a-z]{2}(-[A-Z]{2})?"),
        type=helpers.LazyNestedField(
            nested=helpers.absmod(__name__, ".SuggestionSchema"),
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
        return models.SuggestionResult(**data)

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


class TermFacetResultSchema(FacetResultSchema):
    data_type = marshmallow_enum.EnumField(
        TermFacetResultType,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="dataType",
    )
    missing = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    other = marshmallow.fields.Integer(allow_none=True, missing=None)
    terms = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".FacetResultTermSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.TermFacetResult(**data)


class WhitespaceTokenizerSchema(SuggestTokenizerSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.WhitespaceTokenizer(**data)


class ProductAddAssetActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    asset = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AssetDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    position = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductAddAssetAction(**data)


class ProductAddExternalImageActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    image = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ImageSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductAddExternalImageAction(**data)


class ProductAddPriceActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductAddPriceAction(**data)


class ProductAddToCategoryActionSchema(ProductUpdateActionSchema):
    category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".category.CategoryResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    order_hint = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="orderHint",
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductAddToCategoryAction(**data)


class ProductAddVariantActionSchema(ProductUpdateActionSchema):
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    prices = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    images = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.ImageSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    attributes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributeSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    assets = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AssetSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductAddVariantAction(**data)


class ProductChangeAssetNameActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    asset_id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="assetKey",
    )
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductChangeAssetNameAction(**data)


class ProductChangeAssetOrderActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
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
        return models.ProductChangeAssetOrderAction(**data)


class ProductChangeMasterVariantActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductChangeMasterVariantAction(**data)


class ProductChangeNameActionSchema(ProductUpdateActionSchema):
    name = LocalizedStringField(allow_none=True, missing=None)
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductChangeNameAction(**data)


class ProductChangePriceActionSchema(ProductUpdateActionSchema):
    price_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="priceId"
    )
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductChangePriceAction(**data)


class ProductChangeSlugActionSchema(ProductUpdateActionSchema):
    slug = LocalizedStringField(allow_none=True, missing=None)
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductChangeSlugAction(**data)


class ProductLegacySetSkuActionSchema(ProductUpdateActionSchema):
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductLegacySetSkuAction(**data)


class ProductMoveImageToPositionActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    image_url = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="imageUrl"
    )
    position = marshmallow.fields.Integer(allow_none=True, missing=None)
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductMoveImageToPositionAction(**data)


class ProductPublishActionSchema(ProductUpdateActionSchema):
    scope = marshmallow_enum.EnumField(
        ProductPublishScope,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductPublishAction(**data)


class ProductRemoveAssetActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    asset_id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="assetKey",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductRemoveAssetAction(**data)


class ProductRemoveFromCategoryActionSchema(ProductUpdateActionSchema):
    category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".category.CategoryResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductRemoveFromCategoryAction(**data)


class ProductRemoveImageActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    image_url = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="imageUrl"
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductRemoveImageAction(**data)


class ProductRemovePriceActionSchema(ProductUpdateActionSchema):
    price_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="priceId"
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductRemovePriceAction(**data)


class ProductRemoveVariantActionSchema(ProductUpdateActionSchema):
    id = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductRemoveVariantAction(**data)


class ProductRevertStagedChangesActionSchema(ProductUpdateActionSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductRevertStagedChangesAction(**data)


class ProductRevertStagedVariantChangesActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductRevertStagedVariantChangesAction(**data)


class ProductSetAssetCustomFieldActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    asset_id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="assetKey",
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetAssetCustomFieldAction(**data)


class ProductSetAssetCustomTypeActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    asset_id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="assetKey",
    )
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    fields = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetAssetCustomTypeAction(**data)


class ProductSetAssetDescriptionActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    asset_id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="assetKey",
    )
    description = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetAssetDescriptionAction(**data)


class ProductSetAssetKeyActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="assetKey",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetAssetKeyAction(**data)


class ProductSetAssetSourcesActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    asset_id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="assetKey",
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
        return models.ProductSetAssetSourcesAction(**data)


class ProductSetAssetTagsActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    asset_id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="assetKey",
    )
    tags = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetAssetTagsAction(**data)


class ProductSetAttributeActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetAttributeAction(**data)


class ProductSetAttributeInAllVariantsActionSchema(ProductUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetAttributeInAllVariantsAction(**data)


class ProductSetCategoryOrderHintActionSchema(ProductUpdateActionSchema):
    category_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="categoryId"
    )
    order_hint = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="orderHint",
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetCategoryOrderHintAction(**data)


class ProductSetDescriptionActionSchema(ProductUpdateActionSchema):
    description = LocalizedStringField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetDescriptionAction(**data)


class ProductSetDiscountedPriceActionSchema(ProductUpdateActionSchema):
    price_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="priceId"
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.DiscountedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetDiscountedPriceAction(**data)


class ProductSetImageLabelActionSchema(ProductUpdateActionSchema):
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    image_url = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="imageUrl"
    )
    label = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetImageLabelAction(**data)


class ProductSetKeyActionSchema(ProductUpdateActionSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetKeyAction(**data)


class ProductSetMetaDescriptionActionSchema(ProductUpdateActionSchema):
    meta_description = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="metaDescription",
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetMetaDescriptionAction(**data)


class ProductSetMetaKeywordsActionSchema(ProductUpdateActionSchema):
    meta_keywords = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="metaKeywords",
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetMetaKeywordsAction(**data)


class ProductSetMetaTitleActionSchema(ProductUpdateActionSchema):
    meta_title = LocalizedStringField(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="metaTitle",
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetMetaTitleAction(**data)


class ProductSetPricesActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    prices = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.PriceDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetPricesAction(**data)


class ProductSetProductPriceCustomFieldActionSchema(ProductUpdateActionSchema):
    price_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="priceId"
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetProductPriceCustomFieldAction(**data)


class ProductSetProductPriceCustomTypeActionSchema(ProductUpdateActionSchema):
    price_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="priceId"
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    fields = FieldContainerField(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetProductPriceCustomTypeAction(**data)


class ProductSetProductVariantKeyActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="variantId",
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetProductVariantKeyAction(**data)


class ProductSetSearchKeywordsActionSchema(ProductUpdateActionSchema):
    search_keywords = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SearchKeywordsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="searchKeywords",
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetSearchKeywordsAction(**data)


class ProductSetSkuActionSchema(ProductUpdateActionSchema):
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    staged = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetSkuAction(**data)


class ProductSetTaxCategoryActionSchema(ProductUpdateActionSchema):
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxCategory",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSetTaxCategoryAction(**data)


class ProductTransitionStateActionSchema(ProductUpdateActionSchema):
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    force = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductTransitionStateAction(**data)


class ProductUnpublishActionSchema(ProductUpdateActionSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductUnpublishAction(**data)

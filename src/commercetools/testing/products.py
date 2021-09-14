import copy
import datetime
import uuid
from typing import Dict, List, Optional, Union

from marshmallow import Schema
from marshmallow import fields as schema_fields

from commercetools.platform import models
from commercetools.platform.models._schemas.common import ImageSchema, PriceSchema
from commercetools.platform.models._schemas.product import (
    AttributeSchema,
    ProductDraftSchema,
    ProductPagedQueryResponseSchema,
    ProductSchema,
    ProductUpdateSchema,
    ProductVariantSchema,
)
from commercetools.services.products import _ProductQuerySchema
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import (
    create_commercetools_response,
    custom_fields_from_draft,
    get_product_variants,
    parse_request_params,
)


class ProductsModel(BaseModel):
    _primary_type_name = "product"
    _resource_schema = ProductSchema
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: models.ProductDraft, id: Optional[str] = None
    ) -> models.Product:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())

        master_variant = None
        if draft.master_variant:
            master_variant = self._create_variant_from_draft(draft.master_variant)

        product_data = models.ProductData(
            name=draft.name,
            categories=draft.categories,
            category_order_hints=draft.category_order_hints,
            description=draft.description,
            master_variant=master_variant,
            variants=[self._create_variant_from_draft(vd) for vd in draft.variants]
            if draft.variants
            else [],
            slug=draft.slug or models.LocalizedString(),
            search_keywords=models.SearchKeywords(),
        )

        if draft.publish:
            master_data = models.ProductCatalogData(
                staged=None,
                current=product_data,
                published=True,
                has_staged_changes=False,
            )
        else:
            master_data = models.ProductCatalogData(
                staged=product_data,
                current=None,
                published=False,
                has_staged_changes=True,
            )

        product = models.Product(
            id=str(object_id),
            key=draft.key,
            product_type=draft.product_type,
            master_data=master_data,
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
        )

        return product

    def _create_variant_from_draft(
        self, draft: models.ProductVariantDraft
    ) -> models.ProductVariant:

        assets: Optional[List[models.Asset]] = None
        if draft.assets:
            assets = self._create_assets_from_draft(draft.assets)

        prices: Optional[List[models.Price]] = None
        if draft.prices:
            prices = self._create_prices_from_draft(draft.prices)

        return models.ProductVariant(
            id=1,
            sku=draft.sku,
            key=draft.key,
            prices=prices,
            attributes=draft.attributes,
            price=None,
            images=draft.images,
            assets=assets,
            availability=None,
            is_matching_variant=None,
            scoped_price=None,
            scoped_price_discounted=None,
        )

    def _create_assets_from_draft(
        self, drafts: List[models.AssetDraft]
    ) -> List[models.Asset]:
        assets: List[models.Asset] = []
        for draft in drafts:
            custom: Optional[models.CustomFields] = None
            if draft.custom:
                custom = custom_fields_from_draft(self._storage, draft.custom)

            asset = models.Asset(
                id=str(uuid.uuid4()),
                sources=draft.sources,
                name=draft.name,
                description=draft.description,
                tags=draft.tags,
                custom=custom,
                key=draft.key,
            )
            assets.append(asset)
        return assets

    def _create_prices_from_draft(
        self, drafts: List[models.PriceDraft]
    ) -> List[models.Price]:
        prices: List[models.Price] = []
        for draft in drafts:
            custom = None
            if draft.custom:
                custom = custom_fields_from_draft(self._storage, draft.custom)

            price = models.Price(
                id=str(uuid.uuid4()),
                value=self._create_price_from_draft(draft.value),
                country=draft.country,
                customer_group=draft.customer_group,
                channel=draft.channel,
                valid_from=draft.valid_from,
                valid_until=draft.valid_until,
                discounted=None,
                custom=custom,
                tiers=draft.tiers,
            )
            prices.append(price)
        return prices

    def _create_price_from_draft(
        self, draft: Union[models.Money, Optional[models.TypedMoneyDraft]]
    ) -> Optional[models.TypedMoney]:
        if draft is None:
            return None

        if isinstance(draft, models.CentPrecisionMoneyDraft):
            return models.CentPrecisionMoney(
                cent_amount=draft.cent_amount, currency_code=draft.currency_code
            )
        elif isinstance(draft, models.HighPrecisionMoneyDraft):
            return models.HighPrecisionMoney(
                cent_amount=draft.cent_amount,
                currency_code=draft.currency_code,
                precise_amount=draft.precise_amount,
            )
        elif isinstance(draft, models.Money):
            return models.CentPrecisionMoney(
                cent_amount=draft.cent_amount,
                currency_code=draft.currency_code,
                fraction_digits=2,
            )
        else:
            return models.TypedMoney(
                cent_amount=draft.cent_amount,
                currency_code=draft.currency_code,
                type=draft.type,
            )


def _get_target_obj(obj: dict, staged: bool):
    if not staged and obj["masterData"]["current"]:
        return obj["masterData"]["current"]
    return obj["masterData"]["staged"]


def _get_variant(data_object: dict, *, id: int = "", sku: str = "") -> Optional[dict]:
    if not data_object:
        return None

    variants = [data_object["masterVariant"]]
    if data_object["variants"]:
        variants += data_object["variants"]

    for variant in variants:
        if id and id == variant["id"]:
            return variant
        if sku and sku == variant["sku"]:
            return variant

    return None


def _update_productdata_attr(dst: str, src: str):
    def updater(self, obj: dict, action: models.ProductUpdateAction):
        value = getattr(action, src)
        target_obj = _get_target_obj(obj, getattr(action, "staged", False))

        if target_obj[dst] != value:
            new = copy.deepcopy(obj)
            new[dst] = value
            return new
        return obj

    return updater


def _set_attribute_action():
    def updater(self, obj: dict, action: models.ProductSetAttributeAction):
        staged = getattr(action, "staged", False)
        new = copy.deepcopy(obj)

        target_obj = _get_target_obj(new, staged)
        variant = _get_variant(target_obj, id=action.variant_id)
        if variant:
            for attr in variant["attributes"]:
                if attr["name"] == action.name:
                    attr["value"] = action.value
                    return new

            # Attribute not found, will add it
            attr_schema = AttributeSchema()
            variant["attributes"].append(
                attr_schema.dump(models.Attribute(name=action.name, value=action.value))
            )

        return new

    return updater


def _add_variant_action():
    def updater(self, obj: dict, action: models.ProductAddVariantAction):
        variant = self.model._create_variant_from_draft(
            models.ProductVariantDraft(
                sku=action.sku,
                key=action.key,
                prices=action.prices,
                attributes=action.attributes,
                images=action.images,
                assets=action.assets,
            )
        )
        schema = ProductVariantSchema()

        new = copy.deepcopy(obj)
        target_obj = _get_target_obj(new, staged=getattr(action, "staged", True))
        if not target_obj["variants"]:
            target_obj["variants"] = []
        target_obj["variants"].append(schema.dump(variant))

        return new

    return updater


def _publish_product_action():
    def updater(self, obj: dict, action: models.ProductPublishAction):
        new = copy.deepcopy(obj)
        # not implemented scopes right now.
        if new["masterData"].get("staged"):
            new["masterData"]["current"] = new["masterData"]["staged"]
            new["masterData"]["staged"] = None
        new["masterData"]["hasStagedChanges"] = False
        new["masterData"]["published"] = True
        return new

    return updater


def convert_draft_price(
    price_draft: models.PriceDraft, price_id: str = None
) -> models.Price:
    tiers: Optional[List[models.PriceTier]] = None
    if price_draft.tiers:
        tiers = [utils.create_from_draft(tier) for tier in price_draft.tiers]
    return models.Price(
        id=price_id or str(uuid.uuid4()),
        country=price_draft.country,
        channel=price_draft.channel,
        value=utils.money_to_typed(price_draft.value),
        valid_from=price_draft.valid_from,
        valid_until=price_draft.valid_until,
        discounted=price_draft.discounted,
        custom=utils.create_from_draft(price_draft.custom),
        tiers=tiers,
    )


def _set_product_prices():
    def updater(self, obj: dict, action: models.ProductSetPricesAction):
        new = copy.deepcopy(obj)
        target_obj = _get_target_obj(new, getattr(action, "staged", True))
        prices = []
        for price_draft in action.prices:
            price = convert_draft_price(price_draft)
            prices.append(price)

        schema = PriceSchema()
        for variant in get_product_variants(target_obj):
            if variant["sku"] == action.sku:
                variant["prices"] = schema.dump(prices, many=True)
        if action.staged:
            new["masterData"]["hasStagedChanges"] = True
        return new

    return updater


def _change_price():
    def updater(self, obj: dict, action: models.ProductChangePriceAction):
        new = copy.deepcopy(obj)
        staged = action.staged
        if staged is None:
            staged = True
        target_obj = _get_target_obj(new, staged)
        changed_price = convert_draft_price(action.price, action.price_id)
        schema = PriceSchema()

        found_price = True
        for variant in get_product_variants(target_obj):
            if not variant["prices"]:
                continue
            for index, price in enumerate(variant["prices"]):
                if price["id"] == action.price_id:
                    variant["prices"][index] = schema.dump(changed_price)
                    found_price = True
                    break
        if not found_price:
            raise ValueError("Could not find price with id %s" % action.price_id)
        if staged:
            new["masterData"]["hasStagedChanges"] = True
        return new

    return updater


def _add_price():
    def updater(self, obj: dict, action: models.ProductAddPriceAction):
        new = copy.deepcopy(obj)
        staged = action.staged
        if staged is None:
            staged = True
        target_obj = _get_target_obj(new, staged)
        new_price = convert_draft_price(action.price)
        schema = PriceSchema()

        found_sku = False
        for variant in get_product_variants(target_obj):
            if variant["sku"] == action.sku:
                if "prices" not in variant:
                    variant["prices"] = []
                elif not variant["prices"]:
                    variant["prices"] = []
                variant["prices"].append(schema.dump(new_price))
                found_sku = True
                break
        if not found_sku:
            raise ValueError("Could not find sku %s" % action.sku)
        if staged:
            new["masterData"]["hasStagedChanges"] = True
        return new

    return updater


def _change_master_variant():
    def updater(self, obj: Dict, action: models.ProductChangeMasterVariantAction):
        new = copy.deepcopy(obj)
        staged = action.staged
        if staged is None:
            staged = True
        target_obj = _get_target_obj(new, staged)
        master_variant = target_obj["masterVariant"]
        if master_variant and master_variant["sku"] == action.sku:
            return obj
        found_sku = False
        for variant in get_product_variants(target_obj):
            if variant["sku"] == action.sku:
                target_obj["variants"].append(target_obj["masterVariant"])
                target_obj["masterVariant"] = variant
                target_obj["variants"].remove(variant)
                found_sku = True
                break
        if not found_sku:
            raise ValueError("Could not find sku %s" % action.sku)
        if staged:
            new["masterData"]["hasStagedChanges"] = True
        return new

    return updater


class UploadImageQuerySchema(Schema):
    staged = schema_fields.Bool()
    filename = schema_fields.Field()
    sku = schema_fields.Field()


class ProductsBackend(ServiceBackend):
    service_path = "products"
    model_class = ProductsModel
    _schema_draft = ProductDraftSchema
    _schema_update = ProductUpdateSchema
    _schema_query_params = _ProductQuerySchema
    _schema_query_response = ProductPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
            ("^(?P<id>[^/]+)\/images$", "POST", self.upload_image),
        ]

    # Fixme: use decorator for this
    _actions = {
        "changeSlug": _update_productdata_attr("slug", "slug"),
        "setAttribute": _set_attribute_action(),
        "addVariant": _add_variant_action(),
        "setPrices": _set_product_prices(),
        "changePrice": _change_price(),
        "addPrice": _add_price(),
        "changeMasterVariant": _change_master_variant(),
        "publish": _publish_product_action(),
    }

    def upload_image(self, request, id):
        obj = self.model.get_by_id(id)
        if not obj:
            return create_commercetools_response(request, status_code=404)

        obj = copy.deepcopy(obj)

        params = parse_request_params(UploadImageQuerySchema, request)
        target = _get_target_obj(obj, staged=params["staged"])
        filename = params["filename"]

        variant = _get_variant(target, sku=params["sku"])
        if not variant["images"]:
            variant["images"] = []
        image_schema = ImageSchema()
        variant["images"].append(
            image_schema.dump(
                models.Image(
                    url=f"cdn.commercetools.local/detail-{filename}",
                    dimensions=models.ImageDimensions(w=500, h=500),
                )
            )
        )
        self.model.save(obj)
        return create_commercetools_response(request, json=obj)

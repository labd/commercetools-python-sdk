import copy
import datetime
import typing
import uuid

from marshmallow import Schema
from marshmallow import fields as schema_fields

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import (
    create_commercetools_response,
    custom_fields_from_draft,
    get_product_variants,
    parse_request_params,
)


class ProductsModel(BaseModel):
    _primary_type_name = "product"
    _resource_schema = schemas.ProductSchema
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: types.ProductDraft, id: typing.Optional[str] = None
    ) -> types.Product:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())

        product = types.Product(
            id=str(object_id),
            key=draft.key,
            product_type=draft.product_type,
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
        )

        master_variant = None
        if draft.master_variant:
            master_variant = self._create_variant_from_draft(draft.master_variant)

        product_data = types.ProductData(
            name=draft.name,
            categories=draft.categories,
            category_order_hints=draft.category_order_hints,
            description=draft.description,
            master_variant=master_variant,
            slug=draft.slug or types.LocalizedString(),
        )

        if draft.publish:
            product.master_data = types.ProductCatalogData(
                staged=None, current=product_data, published=True
            )
        else:
            product.master_data = types.ProductCatalogData(
                staged=product_data, current=None, published=False
            )

        return product

    def _create_variant_from_draft(
        self, draft: types.ProductVariantDraft
    ) -> types.ProductVariant:

        assets: typing.Optional[typing.List[types.Asset]] = None
        if draft.assets:
            assets = self._create_assets_from_draft(draft.assets)

        prices: typing.Optional[typing.List[types.Price]] = None
        if draft.prices:
            prices = self._create_prices_from_draft(draft.prices)

        return types.ProductVariant(
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
        self, drafts: typing.List[types.AssetDraft]
    ) -> typing.List[types.Asset]:
        assets: typing.List[types.Asset] = []
        for draft in drafts:
            custom: typing.Optional[types.CustomFields] = None
            if draft.custom:
                custom = custom_fields_from_draft(self._storage, draft.custom)

            asset = types.Asset(
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
        self, drafts: typing.List[types.PriceDraft]
    ) -> typing.List[types.Price]:
        prices: typing.List[types.Price] = []
        for draft in drafts:
            custom = None
            if draft.custom:
                custom = custom_fields_from_draft(self._storage, draft.custom)

            price = types.Price(
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
        self, draft: typing.Optional[types.TypedMoneyDraft]
    ) -> typing.Optional[types.TypedMoney]:
        if draft is None:
            return None

        if isinstance(draft, types.CentPrecisionMoneyDraft):
            return types.CentPrecisionMoney(
                cent_amount=draft.cent_amount, currency_code=draft.currency_code
            )
        elif isinstance(draft, types.HighPrecisionMoneyDraft):
            return types.HighPrecisionMoney(
                cent_amount=draft.cent_amount,
                currency_code=draft.currency_code,
                precise_amount=draft.precise_amount,
            )
        elif isinstance(draft, types.Money):
            return types.CentPrecisionMoney(
                cent_amount=draft.cent_amount, currency_code=draft.currency_code
            )
        else:
            return types.TypedMoney(
                cent_amount=draft.cent_amount,
                currency_code=draft.currency_code,
                type=draft.type,
            )


def _get_target_obj(obj: dict, staged: bool):
    if not staged and obj["masterData"]["current"]:
        return obj["masterData"]["current"]
    return obj["masterData"]["staged"]


def _get_variant(
    data_object: dict, *, id: str = "", sku: str = ""
) -> typing.Optional[dict]:
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
    def updater(self, obj: dict, action: types.ProductUpdateAction):
        value = getattr(action, src)
        target_obj = _get_target_obj(obj, getattr(action, "staged", False))

        if target_obj[dst] != value:
            new = copy.deepcopy(obj)
            new[dst] = value
            return new
        return obj

    return updater


def _set_attribute_action():
    def updater(self, obj: dict, action: types.ProductSetAttributeAction):
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
            attr_schema = schemas.AttributeSchema()
            variant["attributes"].append(
                attr_schema.dump(types.Attribute(name=action.name, value=action.value))
            )

        return new

    return updater


def _add_variant_action():
    def updater(self, obj: dict, action: types.ProductAddVariantAction):
        variant = self.model._create_variant_from_draft(
            types.ProductVariantDraft(
                sku=action.sku,
                key=action.key,
                prices=action.prices,
                attributes=action.attributes,
                images=action.images,
                assets=action.assets,
            )
        )
        schema = schemas.ProductVariantSchema()

        new = copy.deepcopy(obj)
        target_obj = _get_target_obj(new, staged=getattr(action, "staged", True))
        if not target_obj["variants"]:
            target_obj["variants"] = []
        target_obj["variants"].append(schema.dump(variant))

        return new

    return updater


def _publish_product_action():
    def updater(self, obj: dict, action: types.ProductPublishAction):
        new = copy.deepcopy(obj)
        # not implemented scopes right now.
        if new["masterData"].get("staged"):
            new["masterData"]["current"] = new["masterData"]["staged"]
        new["masterData"]["hasStagedChanges"] = False
        new["masterData"]["published"] = True
        return new

    return updater


def _set_product_prices():
    def updater(self, obj: dict, action: types.ProductSetPricesAction):
        new = copy.deepcopy(obj)
        target_obj = _get_target_obj(new, getattr(action, "staged", True))
        prices = []
        for price_draft in action.prices:
            price = types.Price(
                id=str(uuid.uuid4()),
                country=price_draft.country,
                channel=price_draft.channel,
                value=types.TypedMoney(
                    fraction_digits=2,
                    cent_amount=price_draft.value.cent_amount,
                    currency_code=price_draft.value.currency_code,
                    type=types.MoneyType.CENT_PRECISION,
                ),
                valid_from=price_draft.valid_from,
                valid_until=price_draft.valid_until,
                discounted=price_draft.discounted,
                custom=price_draft.custom,
                tiers=price_draft.tiers,
            )
            prices.append(price)

        schema = schemas.PriceSchema()
        for variant in get_product_variants(target_obj):
            if variant["sku"] == action.sku:
                variant["prices"] = schema.dump(prices, many=True)
        if action.staged:
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
    _schema_draft = schemas.ProductDraftSchema
    _schema_update = schemas.ProductUpdateSchema
    _schema_query_response = schemas.ProductPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
            ("^(?P<id>[^/]+)\/images$", "POST", self.upload_image),
        ]

    # Fixme: use decorator for this
    _actions = {
        "changeSlug": _update_productdata_attr("slug", "slug"),
        "setAttribute": _set_attribute_action(),
        "addVariant": _add_variant_action(),
        "setPrices": _set_product_prices(),
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
        image_schema = schemas.ImageSchema()
        variant["images"].append(
            image_schema.dump(
                types.Image(url=f"cdn.commercetools.local/detail-{filename}")
            )
        )
        self.model.save(obj)
        return create_commercetools_response(request, json=obj)

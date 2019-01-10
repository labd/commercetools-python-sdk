import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import custom_fields_from_draft


class ProductsModel(BaseModel):
    _primary_type_name = "product"
    _resource_schema = schemas.ProductSchema

    def _create_from_draft(
        self, obj: types.ProductDraft, id: typing.Optional[str] = None
    ) -> types.Product:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())

        product = types.Product(
            id=str(object_id),
            key=obj.key,
            product_type=obj.product_type,
            version=1,
            created_at=datetime.datetime.now(),
            last_modified_at=datetime.datetime.now(),
        )

        master_variant = None
        if obj.master_variant:
            master_variant = self._create_variant_from_draft(obj.master_variant)

        product_data = types.ProductData(
            name=obj.name,
            categories=obj.categories,
            category_order_hints=obj.category_order_hints,
            description=obj.description,
            master_variant=master_variant,
            slug=obj.slug or types.LocalizedString(),
        )

        if obj.publish:
            product.master_data = types.ProductCatalogData(
                staged=None, current=product_data, published=True
            )
        else:
            product.master_data = types.ProductCatalogData(
                staged=product_data, current=None, published=False
            )

        return product

    def _create_variant_from_draft(
        self, obj: types.ProductVariantDraft
    ) -> types.ProductVariant:

        assets: typing.Optional[typing.List[types.Asset]] = None
        if obj.assets:
            assets = self._create_assets_from_draft(obj.assets)

        prices: typing.Optional[typing.List[types.Price]] = None
        if obj.prices:
            prices = self._create_prices_from_draft(obj.prices)

        return types.ProductVariant(
            id=1,
            sku=obj.sku,
            key=obj.key,
            prices=prices,
            attributes=obj.attributes,
            price=None,
            images=obj.images,
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
                value=draft.value,
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


class ProductsBackend(ServiceBackend):
    service_path = "products"
    model_class = ProductsModel
    _schema_draft = schemas.ProductDraftSchema
    _schema_query_response = schemas.ProductPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]

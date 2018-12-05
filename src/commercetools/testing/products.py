import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ProductsModel(BaseModel):
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

        product_data = types.ProductData(
            name=obj.name,
            categories=obj.categories,
            category_order_hints=obj.category_order_hints,
            description=obj.description,
            master_variant=obj.master_variant,
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

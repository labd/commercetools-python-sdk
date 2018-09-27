from typing import List, Optional
from commercetools import types, schemas

__all__ = ["ProductService"]


class ProductService:
    def __init__(self, client):
        self._client = client

    def get_by_id(self, id: str) -> Optional[types.Product]:
        return self._client._get(f"products/{id}", [], schemas.ProductSchema)

    def get_by_key(self, key: str) -> types.Product:
        return self._client._get(f"products/key={key}", [], schemas.ProductSchema)

    def query(self) -> List[types.Product]:
        pass

    def create(self, draft: types.ProductDraft) -> types.Product:
        return self._client._create(
            "products", [], draft, schemas.ProductUpdateSchema, schemas.ProductSchema
        )

    def update_by_id(
        self, id: str, version: int, actions: List[types.ProductUpdateAction]
    ) -> types.Product:
        update_action = types.ProductUpdate(version=version, actions=actions)
        return self._client._update(
            f"products/{id}",
            [],
            update_action,
            schemas.ProductUpdateSchema,
            schemas.ProductSchema,
        )

    def update_by_key(
        self, key: str, version: int, actions: List[types.ProductUpdateAction]
    ) -> types.Product:
        update_action = types.ProductUpdate(version=version, actions=actions)
        return self._client._update(
            f"products/key={key}",
            [],
            update_action,
            schemas.ProductUpdateSchema,
            schemas.ProductSchema,
        )

    def delete_by_id(self, id: str) -> types.Product:
        pass

    def delete_by_key(self, key: str) -> types.Product:
        pass

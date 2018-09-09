from typing import List, Optional
from . import types

__all__ = ["ProductService"]


class ProductService:
    def __init__(self, client):
        self._client = client

    def get_by_id(self, id: str) -> Optional[types.Product]:
        return self._client._get(f"products/{id}", [], types.ProductSchema)

    def get_by_key(self, key: str) -> types.Product:
        ...

    def query(self) -> List[types.Product]:
        pass

    def create(self, draft: types.ProductDraft) -> types.Product:
        print(types.ProductDraftSchema().dump(draft))

    def update_by_id(self, id: str, actions) -> types.Product:
        pass

    def update_by_key(self, key: str, actions) -> types.Product:
        pass

    def delete_by_id(self, id: str) -> types.Product:
        pass

    def delete_by_key(self, key: str) -> types.Product:
        pass

# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ..product_tailoring.by_project_key_in_store_key_by_store_key_products_key_by_product_key_product_tailoring_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyProductsKeyByProductKeyProductTailoringRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyProductsKeyByProductKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str
    _product_key: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        product_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._product_key = product_key
        self._client = client

    def product_tailoring(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyProductsKeyByProductKeyProductTailoringRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyProductsKeyByProductKeyProductTailoringRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            product_key=self._product_key,
            client=self._client,
        )

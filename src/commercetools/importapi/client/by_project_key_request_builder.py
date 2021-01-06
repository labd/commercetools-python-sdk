# Generated file, please do not change!!!
import typing

from .categories.by_project_key_categories_request_builder import (
    ByProjectKeyCategoriesRequestBuilder,
)
from .customers.by_project_key_customers_request_builder import (
    ByProjectKeyCustomersRequestBuilder,
)
from .import_sinks.by_project_key_import_sinks_request_builder import (
    ByProjectKeyImportSinksRequestBuilder,
)
from .import_summaries.by_project_key_import_summaries_request_builder import (
    ByProjectKeyImportSummariesRequestBuilder,
)
from .inventories.by_project_key_inventories_request_builder import (
    ByProjectKeyInventoriesRequestBuilder,
)
from .orders.by_project_key_orders_request_builder import (
    ByProjectKeyOrdersRequestBuilder,
)
from .prices.by_project_key_prices_request_builder import (
    ByProjectKeyPricesRequestBuilder,
)
from .product_drafts.by_project_key_product_drafts_request_builder import (
    ByProjectKeyProductDraftsRequestBuilder,
)
from .product_types.by_project_key_product_types_request_builder import (
    ByProjectKeyProductTypesRequestBuilder,
)
from .product_variant_patches.by_project_key_product_variant_patches_request_builder import (
    ByProjectKeyProductVariantPatchesRequestBuilder,
)
from .product_variants.by_project_key_product_variants_request_builder import (
    ByProjectKeyProductVariantsRequestBuilder,
)
from .products.by_project_key_products_request_builder import (
    ByProjectKeyProductsRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ..base_client import BaseClient


class ByProjectKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def import_sinks(self) -> ByProjectKeyImportSinksRequestBuilder:
        return ByProjectKeyImportSinksRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def import_summaries(self) -> ByProjectKeyImportSummariesRequestBuilder:
        return ByProjectKeyImportSummariesRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def categories(self) -> ByProjectKeyCategoriesRequestBuilder:
        return ByProjectKeyCategoriesRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def prices(self) -> ByProjectKeyPricesRequestBuilder:
        return ByProjectKeyPricesRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def products(self) -> ByProjectKeyProductsRequestBuilder:
        return ByProjectKeyProductsRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def product_drafts(self) -> ByProjectKeyProductDraftsRequestBuilder:
        return ByProjectKeyProductDraftsRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def product_types(self) -> ByProjectKeyProductTypesRequestBuilder:
        return ByProjectKeyProductTypesRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def product_variants(self) -> ByProjectKeyProductVariantsRequestBuilder:
        return ByProjectKeyProductVariantsRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def product_variant_patches(
        self,
    ) -> ByProjectKeyProductVariantPatchesRequestBuilder:
        return ByProjectKeyProductVariantPatchesRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def orders(self) -> ByProjectKeyOrdersRequestBuilder:
        return ByProjectKeyOrdersRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def customers(self) -> ByProjectKeyCustomersRequestBuilder:
        return ByProjectKeyCustomersRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def inventories(self) -> ByProjectKeyInventoriesRequestBuilder:
        return ByProjectKeyInventoriesRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

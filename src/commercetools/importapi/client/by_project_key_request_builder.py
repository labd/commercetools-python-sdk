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


class ByProjectKeyRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def importSinks(self) -> ByProjectKeyImportSinksRequestBuilder:
        return ByProjectKeyImportSinksRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def importSummaries(self) -> ByProjectKeyImportSummariesRequestBuilder:
        return ByProjectKeyImportSummariesRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def categories(self) -> ByProjectKeyCategoriesRequestBuilder:
        return ByProjectKeyCategoriesRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def prices(self) -> ByProjectKeyPricesRequestBuilder:
        return ByProjectKeyPricesRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def products(self) -> ByProjectKeyProductsRequestBuilder:
        return ByProjectKeyProductsRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def productDrafts(self) -> ByProjectKeyProductDraftsRequestBuilder:
        return ByProjectKeyProductDraftsRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def productTypes(self) -> ByProjectKeyProductTypesRequestBuilder:
        return ByProjectKeyProductTypesRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def productVariants(self) -> ByProjectKeyProductVariantsRequestBuilder:
        return ByProjectKeyProductVariantsRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def productVariantPatches(self) -> ByProjectKeyProductVariantPatchesRequestBuilder:
        return ByProjectKeyProductVariantPatchesRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def orders(self) -> ByProjectKeyOrdersRequestBuilder:
        return ByProjectKeyOrdersRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def customers(self) -> ByProjectKeyCustomersRequestBuilder:
        return ByProjectKeyCustomersRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def inventories(self) -> ByProjectKeyInventoriesRequestBuilder:
        return ByProjectKeyInventoriesRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

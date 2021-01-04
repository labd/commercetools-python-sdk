# Generated file, please do not change!!!
import typing

from ...models.shipping_method import (
    ShippingMethod,
    ShippingMethodDraft,
    ShippingMethodPagedQueryResponse,
)
from ..matching_cart.by_project_key_shipping_methods_matching_cart_request_builder import (
    ByProjectKeyShippingMethodsMatchingCartRequestBuilder,
)
from ..matching_location.by_project_key_shipping_methods_matching_location_request_builder import (
    ByProjectKeyShippingMethodsMatchingLocationRequestBuilder,
)
from ..matching_orderedit.by_project_key_shipping_methods_matching_orderedit_request_builder import (
    ByProjectKeyShippingMethodsMatchingOrdereditRequestBuilder,
)
from .by_project_key_shipping_methods_by_id_request_builder import (
    ByProjectKeyShippingMethodsByIDRequestBuilder,
)
from .by_project_key_shipping_methods_key_by_key_request_builder import (
    ByProjectKeyShippingMethodsKeyByKeyRequestBuilder,
)


class ByProjectKeyShippingMethodsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyShippingMethodsKeyByKeyRequestBuilder:
        return ByProjectKeyShippingMethodsKeyByKeyRequestBuilder(
            key=key, projectKey=self._project_key, client=self._client
        )

    def matchingCart(self) -> ByProjectKeyShippingMethodsMatchingCartRequestBuilder:
        """Get ShippingMethods for a cart
        """
        return ByProjectKeyShippingMethodsMatchingCartRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def matchingOrderedit(
        self
    ) -> ByProjectKeyShippingMethodsMatchingOrdereditRequestBuilder:
        """Get ShippingMethods for an order edit
        """
        return ByProjectKeyShippingMethodsMatchingOrdereditRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def matchingLocation(
        self
    ) -> ByProjectKeyShippingMethodsMatchingLocationRequestBuilder:
        """Get ShippingMethods for a location
        """
        return ByProjectKeyShippingMethodsMatchingLocationRequestBuilder(
            projectKey=self._project_key, client=self._client
        )

    def withId(self, ID: str) -> ByProjectKeyShippingMethodsByIDRequestBuilder:
        return ByProjectKeyShippingMethodsByIDRequestBuilder(
            ID=ID, projectKey=self._project_key, client=self._client
        )

    def get(
        self,
        *,
        expand: "str" = None,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        where: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShippingMethodPagedQueryResponse":
        """Query shipping-methods
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/shipping-methods",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=ShippingMethodPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "ShippingMethodDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShippingMethod":
        """Create ShippingMethod
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/shipping-methods",
            params={"expand": expand},
            data_object=body,
            response_object=ShippingMethod,
            headers={"Content-Type": "application/json", **headers},
        )

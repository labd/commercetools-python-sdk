# Generated file, please do not change!!!
import typing

from ...models.shipping_method import ShippingMethodPagedQueryResponse


class ByProjectKeyShippingMethodsMatchingLocationRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def get(
        self,
        *,
        country: "str",
        state: "str" = None,
        currency: "str" = None,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShippingMethodPagedQueryResponse":
        return self._client._get(
            endpoint=f"/{self._project_key}/shipping-methods/matching-location",
            params={
                "country": country,
                "state": state,
                "currency": currency,
                "expand": expand,
            },
            response_object=ShippingMethodPagedQueryResponse,
            headers=headers,
        )

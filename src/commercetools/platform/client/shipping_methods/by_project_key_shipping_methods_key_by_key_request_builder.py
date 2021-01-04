# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.shipping_method import ShippingMethod


class ByProjectKeyShippingMethodsKeyByKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _key: str

    def __init__(self, projectKey: str, key: str, client: "Client"):
        self._project_key = projectKey
        self._key = key
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "ShippingMethod":
        """Get ShippingMethod by key
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/shipping-methods/key={self._key}",
            params={"expand": expand},
            response_object=ShippingMethod,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShippingMethod":
        """Update ShippingMethod by key
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/shipping-methods/key={self._key}",
            params={"expand": expand},
            data_object=body,
            response_object=ShippingMethod,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShippingMethod":
        """Delete ShippingMethod by key
        """
        return self._client._delete(
            endpoint=f"/{self._project_key}/shipping-methods/key={self._key}",
            params={"version": version, "expand": expand},
            response_object=ShippingMethod,
            headers=headers,
        )

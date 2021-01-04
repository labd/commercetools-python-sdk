# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.tax_category import TaxCategory


class ByProjectKeyTaxCategoriesKeyByKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _key: str

    def __init__(self, projectKey: str, key: str, client: "Client"):
        self._project_key = projectKey
        self._key = key
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "TaxCategory":
        """Get TaxCategory by key
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/tax-categories/key={self._key}",
            params={"expand": expand},
            response_object=TaxCategory,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "TaxCategory":
        """Update TaxCategory by key
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/tax-categories/key={self._key}",
            params={"expand": expand},
            data_object=body,
            response_object=TaxCategory,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "TaxCategory":
        """Delete TaxCategory by key
        """
        return self._client._delete(
            endpoint=f"/{self._project_key}/tax-categories/key={self._key}",
            params={"version": version, "expand": expand},
            response_object=TaxCategory,
            headers=headers,
        )

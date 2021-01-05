# Generated file, please do not change!!!
import typing

from ...models.product import Product


class ByProjectKeyProductsByIDImagesRequestBuilder:

    _client: "Client"
    _project_key: str
    _id: str

    def __init__(
        self,
        projectKey: str,
        ID: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._id = ID
        self._client = client

    def post(
        self,
        body: "Buffer",
        *,
        filename: "str" = None,
        variant: "float" = None,
        sku: "str" = None,
        staged: "bool" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Product":
        """Uploads a binary image file to a given product variant. The supported image formats are JPEG, PNG and GIF."""
        return self._client._post(
            endpoint=f"/{self._project_key}/products/{self._id}/images",
            params={
                "filename": filename,
                "variant": variant,
                "sku": sku,
                "staged": staged,
            },
            data_object=body,
            response_class=Product,
            headers=headers,
        )

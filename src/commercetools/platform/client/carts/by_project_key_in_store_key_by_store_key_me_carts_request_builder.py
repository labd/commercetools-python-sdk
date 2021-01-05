# Generated file, please do not change!!!
import typing

from ...models.cart import Cart, CartPagedQueryResponse
from ...models.me import MyCartDraft
from .by_project_key_in_store_key_by_store_key_me_carts_by_id_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyMeCartsByIDRequestBuilder,
)


class ByProjectKeyInStoreKeyByStoreKeyMeCartsRequestBuilder:

    _client: "Client"
    _project_key: str
    _store_key: str

    def __init__(
        self,
        projectKey: str,
        storeKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._store_key = storeKey
        self._client = client

    def withId(
        self, ID: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyMeCartsByIDRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyMeCartsByIDRequestBuilder(
            ID=ID,
            projectKey=self._project_key,
            storeKey=self._store_key,
            client=self._client,
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
    ) -> "CartPagedQueryResponse":
        """Query carts"""
        return self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/me/carts",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_class=CartPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "MyCartDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Cart":
        """Create Cart"""
        return self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/me/carts",
            params={"expand": expand},
            data_object=body,
            response_class=Cart,
            headers={"Content-Type": "application/json", **headers},
        )

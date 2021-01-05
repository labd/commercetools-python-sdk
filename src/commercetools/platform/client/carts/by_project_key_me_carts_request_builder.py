# Generated file, please do not change!!!
import typing

from ...models.cart import CartPagedQueryResponse
from ...models.me import MyCart, MyCartDraft
from .by_project_key_me_carts_by_id_request_builder import (
    ByProjectKeyMeCartsByIDRequestBuilder,
)


class ByProjectKeyMeCartsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def withId(self, ID: str) -> ByProjectKeyMeCartsByIDRequestBuilder:
        return ByProjectKeyMeCartsByIDRequestBuilder(
            ID=ID,
            projectKey=self._project_key,
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
            endpoint=f"/{self._project_key}/me/carts",
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
    ) -> "MyCart":
        """Create MyCart"""
        return self._client._post(
            endpoint=f"/{self._project_key}/me/carts",
            params={"expand": expand},
            data_object=body,
            response_class=MyCart,
            headers={"Content-Type": "application/json", **headers},
        )

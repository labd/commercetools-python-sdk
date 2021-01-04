# Generated file, please do not change!!!
import typing

from ...models.me import MyPayment, MyPaymentDraft, MyPaymentPagedQueryResponse
from .by_project_key_me_payments_by_id_request_builder import (
    ByProjectKeyMePaymentsByIDRequestBuilder,
)
from .by_project_key_me_payments_key_by_key_request_builder import (
    ByProjectKeyMePaymentsKeyByKeyRequestBuilder,
)


class ByProjectKeyMePaymentsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyMePaymentsKeyByKeyRequestBuilder:
        return ByProjectKeyMePaymentsKeyByKeyRequestBuilder(
            key=key, projectKey=self._project_key, client=self._client
        )

    def withId(self, ID: str) -> ByProjectKeyMePaymentsByIDRequestBuilder:
        return ByProjectKeyMePaymentsByIDRequestBuilder(
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
    ) -> "MyPaymentPagedQueryResponse":
        """Query payments
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/me/payments",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=MyPaymentPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "MyPaymentDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "MyPayment":
        """Create MyPayment
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/me/payments",
            params={"expand": expand},
            data_object=body,
            response_object=MyPayment,
            headers={"Content-Type": "application/json", **headers},
        )

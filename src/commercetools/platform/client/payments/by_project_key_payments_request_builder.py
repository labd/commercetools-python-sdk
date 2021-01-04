# Generated file, please do not change!!!
import typing

from ...models.payment import Payment, PaymentDraft, PaymentPagedQueryResponse
from .by_project_key_payments_by_id_request_builder import (
    ByProjectKeyPaymentsByIDRequestBuilder,
)
from .by_project_key_payments_key_by_key_request_builder import (
    ByProjectKeyPaymentsKeyByKeyRequestBuilder,
)


class ByProjectKeyPaymentsRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def withKey(self, key: str) -> ByProjectKeyPaymentsKeyByKeyRequestBuilder:
        return ByProjectKeyPaymentsKeyByKeyRequestBuilder(
            key=key, projectKey=self._project_key, client=self._client
        )

    def withId(self, ID: str) -> ByProjectKeyPaymentsByIDRequestBuilder:
        return ByProjectKeyPaymentsByIDRequestBuilder(
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
    ) -> "PaymentPagedQueryResponse":
        """Query payments
        """
        return self._client._get(
            endpoint=f"/{self._project_key}/payments",
            params={
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
            },
            response_object=PaymentPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "PaymentDraft",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Payment":
        """To create a payment object a payment draft object has to be given with the request.
        """
        return self._client._post(
            endpoint=f"/{self._project_key}/payments",
            params={"expand": expand},
            data_object=body,
            response_object=Payment,
            headers={"Content-Type": "application/json", **headers},
        )

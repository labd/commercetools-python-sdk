# Generated file, please do not change!!!
import typing

from ...models.payment import Payment, PaymentDraft, PaymentPagedQueryResponse
from .by_project_key_payments_by_id_request_builder import (
    ByProjectKeyPaymentsByIDRequestBuilder,
)
from .by_project_key_payments_key_by_key_request_builder import (
    ByProjectKeyPaymentsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyPaymentsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeyPaymentsKeyByKeyRequestBuilder:
        return ByProjectKeyPaymentsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeyPaymentsByIDRequestBuilder:
        return ByProjectKeyPaymentsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: str = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: str = None,
        predicate_var: typing.Dict[str, str] = None,
        headers: typing.Dict[str, str] = None,
    ) -> "PaymentPagedQueryResponse":
        """Query payments"""
        params = {
            "expand": expand,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "where": where,
        }
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/payments",
            params=params,
            response_class=PaymentPagedQueryResponse,
            headers=headers,
        )

    def post(
        self,
        body: "PaymentDraft",
        *,
        expand: str = None,
        headers: typing.Dict[str, str] = None,
    ) -> "Payment":
        """To create a payment object a payment draft object has to be given with the request."""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/payments",
            params={"expand": expand},
            data_object=body,
            response_class=Payment,
            headers={"Content-Type": "application/json", **headers},
        )

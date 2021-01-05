import datetime
import uuid
from typing import Optional

from commercetools.platform import models
from commercetools.platform.models._schemas.customer import (
    CustomerDraftSchema,
    CustomerPagedQueryResponseSchema,
    CustomerSchema,
    CustomerUpdateSchema,
)
from commercetools.testing import abstract, utils
from commercetools.testing.utils import create_commercetools_response


class CustomerModel(abstract.BaseModel):
    _resource_schema = CustomerSchema
    _primary_type_name = "customer"
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: models.CustomerDraft, id: Optional[str] = None
    ) -> models.Customer:
        object_id = uuid.UUID(id) if id is not None else uuid.uuid4()
        now = datetime.datetime.now(datetime.timezone.utc)

        return models.Customer(
            id=str(object_id),
            version=1,
            created_at=now,
            last_modified_at=now,
            customer_number=draft.customer_number,
            email=draft.email,
            password=draft.password,
            first_name=draft.first_name,
            last_name=draft.last_name,
            middle_name=draft.middle_name,
            title=draft.title,
            date_of_birth=draft.date_of_birth,
            company_name=draft.company_name,
            vat_id=draft.vat_id,
            addresses=draft.addresses,
            default_shipping_address_id=(
                str(draft.default_shipping_address)
                if draft.default_shipping_address
                else None
            ),
            shipping_address_ids=(
                [str(address_id) for address_id in draft.shipping_addresses]
                if draft.shipping_addresses
                else None
            ),
            default_billing_address_id=(
                str(draft.default_billing_address)
                if draft.default_billing_address
                else None
            ),
            billing_address_ids=(
                [str(address_id) for address_id in draft.billing_addresses]
                if draft.billing_addresses
                else None
            ),
            is_email_verified=draft.is_email_verified,
            external_id=draft.external_id,
            customer_group=draft.customer_group,
            custom=utils.create_from_draft(draft.custom),
            locale=draft.locale,
            salutation=draft.salutation,
            key=draft.key,
        )


class CustomerBackend(abstract.ServiceBackend):
    service_path = "customers"
    model_class = CustomerModel
    _schema_draft = CustomerDraftSchema
    _schema_update = CustomerUpdateSchema
    _schema_query_response = CustomerPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]

    def create(self, request):
        obj = self._schema_draft().loads(request.body)
        data = self.model.add(obj)

        # Convert to CustomerSignInResult
        data = {"customer": data, "cart": None}

        expanded_data = self._expand(request, data)
        return create_commercetools_response(request, json=expanded_data)

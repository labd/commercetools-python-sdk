import copy
import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class ShippingMethodsModel(BaseModel):
    _primary_type_name = "shipping-method"
    _resource_schema = schemas.ShippingMethodSchema
    _schema_update = schemas.ProjectUpdateSchema

    def _create_from_draft(
        self, draft: types.ShippingMethodDraft, id: typing.Optional[str] = None
    ) -> types.ShippingMethod:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())

        zone_rates: typing.List[types.ZoneRate] = []
        for rate_draft in draft.zone_rates or []:
            shipping_rates: typing.List[types.ShippingRate] = []
            for shipping_rate_draft in rate_draft.shipping_rates or []:
                shipping_rate = types.ShippingRate(
                    price=utils._money_to_typed(shipping_rate_draft.price),
                    free_above=utils._money_to_typed(shipping_rate_draft.free_above),
                    tiers=copy.deepcopy(shipping_rate_draft.tiers),
                )
                shipping_rates.append(shipping_rate)

            zone_rate = types.ZoneRate(
                zone=rate_draft.zone, shipping_rates=shipping_rates
            )
            zone_rates.append(zone_rate)

        return types.ShippingMethod(
            id=str(object_id),
            key=draft.key,
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            name=draft.name,
            description=draft.description,
            tax_category=draft.tax_category,
            zone_rates=zone_rates,
            is_default=draft.is_default,
            predicate=draft.predicate,
        )


class ShippingMethodsBackend(ServiceBackend):
    service_path = "shipping-methods"
    model_class = ShippingMethodsModel
    _schema_draft = schemas.ShippingMethodDraftSchema
    _schema_update = schemas.ShippingMethodUpdateSchema
    _schema_query_response = schemas.ShippingMethodPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
        ]

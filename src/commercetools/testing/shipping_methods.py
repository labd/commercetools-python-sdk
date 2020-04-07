import copy
import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import InternalUpdateError, update_attribute


class ShippingMethodsModel(BaseModel):
    _primary_type_name = "shipping-method"
    _resource_schema = schemas.ShippingMethodSchema
    _schema_update = schemas.ShippingMethodUpdateSchema
    _unique_values = ["key"]

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


def create_shipping_rate_from_draft(
    draft: types.ShippingRateDraft,
) -> types.ShippingRate:
    free_above = None
    if draft.free_above:
        free_above = types.CentPrecisionMoney(
            cent_amount=draft.free_above.cent_amount,
            currency_code=draft.free_above.currency_code,
            type=types.MoneyType.CENT_PRECISION,
            fraction_digits=2,
        )
    shipping_rate = types.ShippingRate(
        price=types.CentPrecisionMoney(
            cent_amount=draft.price.cent_amount,
            currency_code=draft.price.currency_code,
            type=types.MoneyType.CENT_PRECISION,
            fraction_digits=2,
        ),
        free_above=free_above,
        tiers=draft.tiers if draft.tiers else [],
    )
    return shipping_rate


def change_is_default(
    backend: "ShippingMethodsBackend",
    obj: dict,
    action: types.ShippingMethodChangeIsDefaultAction,
):
    if action.is_default:
        for shipping_method in backend.model._storage._stores[
            "shipping-method"
        ].values():
            shipping_method["isDefault"] = False
            backend.model.save(shipping_method)
    new = copy.deepcopy(obj)
    new["isDefault"] = action.is_default
    return new


def change_tax_category(
    backend: "ShippingMethodsBackend",
    obj: dict,
    action: types.ShippingMethodChangeTaxCategoryAction,
):
    for tax_category in backend.model._storage._stores["tax-category"].values():
        if action.tax_category.id and tax_category["id"] == action.tax_category.id:
            break
        if action.tax_category.key and tax_category["key"] == action.tax_category.key:
            break
    else:
        raise InternalUpdateError("Tax Category does not exist")
    new = copy.deepcopy(obj)
    new["taxCategory"] = schemas.TaxCategoryResourceIdentifierSchema().dump(
        action.tax_category
    )
    return new


def add_shipping_zone(
    backend: "ShippingMethodsBackend",
    obj: dict,
    action: types.ShippingMethodAddZoneAction,
):
    new = copy.deepcopy(obj)
    if not new.get("zoneRates"):
        new["zoneRates"] = []
    for zone_rate in new["zoneRates"]:
        if zone_rate["zone"]["id"] == action.zone.id:
            raise InternalUpdateError("Zone already exists")
    new["zoneRates"].append(
        schemas.ZoneRateSchema().dump(types.ZoneRate(zone=action.zone))
    )
    return new


def remove_shipping_zone(
    backend: "ShippingMethodsBackend",
    obj: dict,
    action: types.ShippingMethodRemoveZoneAction,
):
    new = copy.deepcopy(obj)
    for zone_rate in new["zoneRates"]:
        if zone_rate["zone"]["id"] == action.zone.id:
            new["zoneRates"].remove(zone_rate)
            break
    else:
        raise InternalUpdateError("Zone rate not found")

    return new


def add_shipping_rate(
    backend: "ShippingMethodsBackend",
    obj: dict,
    action: types.ShippingMethodAddShippingRateAction,
):
    new = copy.deepcopy(obj)
    draft = action.shipping_rate
    shipping_rate = create_shipping_rate_from_draft(draft)
    target_zone_rate = None
    for zone_rate in new["zoneRates"]:
        if zone_rate["zone"]["id"] == action.zone.id:
            target_zone_rate = zone_rate
            break
    if not target_zone_rate:
        new["zoneRates"].append(
            schemas.ZoneRateSchema().dump(
                types.ZoneRate(zone=action.zone, shipping_rates=[shipping_rate])
            )
        )
    else:
        if not target_zone_rate.get("shippingRates"):
            target_zone_rate["shippingRates"] = []
        target_zone_rate["shippingRates"].append(
            schemas.ShippingRateSchema().dump(shipping_rate)
        )

    return new


def remove_shipping_rate(
    backend: "ShippingMethodsBackend",
    obj: dict,
    action: types.ShippingMethodRemoveShippingRateAction,
):
    target_zone_rate = None
    for zone_rate in obj["zoneRates"]:
        if zone_rate["zone"]["id"] == action.zone.id:
            target_zone_rate = zone_rate
            break

    if not target_zone_rate:
        raise InternalUpdateError("Zone does not exist")

    rate_to_delete = create_shipping_rate_from_draft(action.shipping_rate)
    for shipping_rate in target_zone_rate["shippingRates"]:
        existing_rate = schemas.ShippingRateSchema().load(shipping_rate)
        if existing_rate == rate_to_delete:
            target_zone_rate["shippingRates"].remove(shipping_rate)
            return copy.deepcopy(obj)

    raise InternalUpdateError("Shipping rate does not exist")


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
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
        ]

    _actions = {
        "addShippingRate": add_shipping_rate,
        "addZone": add_shipping_zone,
        "changeIsDefault": change_is_default,
        "changeName": update_attribute("name", "name"),
        "changeTaxCategory": change_tax_category,
        "removeShippingRate": remove_shipping_rate,
        "removeZone": remove_shipping_zone,
        "setDescription": update_attribute("description", "description"),
        "setKey": update_attribute("key", "key"),
        "setPredicate": update_attribute("predicate", "predicate"),
    }

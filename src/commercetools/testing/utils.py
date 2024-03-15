import copy
import json
import typing
import uuid
from datetime import datetime

from marshmallow import Schema
from requests_mock import create_response
from requests_mock.request import _RequestObjectProxy

from commercetools.constants import HEADER_CORRELATION_ID
from commercetools.platform import models
from commercetools.platform.models import (
    CartSetCustomFieldAction,
    OrderSetCustomFieldAction,
)
from commercetools.platform.models._abstract import _BaseType
from commercetools.platform.models._schemas.product import ProductSchema
from commercetools.platform.models.cart import CartSetLineItemCustomFieldAction
from commercetools.platform.models.order import OrderSetLineItemCustomFieldAction

if typing.TYPE_CHECKING:
    from commercetools.testing import Storage  # NOQA


class InternalUpdateError(ValueError):
    pass


def parse_request_params(schema: Schema, request: _RequestObjectProxy) -> dict:
    params = flatten_multivaluedict(request.qs)
    obj = schema().load(params)
    return obj


def flatten_multivaluedict(data: dict) -> dict:
    result = {}
    for key, value in data.items():
        if isinstance(value, list) and len(value) == 1:
            value = value[0]
        result[key] = value
    return result


def get_product_variants(product_catalog_data: dict) -> typing.List[dict]:
    variants = []
    if product_catalog_data.get("masterVariant"):
        variants.append(product_catalog_data["masterVariant"])
    if product_catalog_data.get("variants"):
        variants += product_catalog_data["variants"]
    return variants


def create_from_draft(draft: typing.Optional[_BaseType]):
    """Utility method to create normal objects out of draft objects.

    This is used for non-resource objects. For the resources themselves (which contain)
    an id, we have the specific implementations of the `BaseModel`.
    """
    if not draft:
        return None

    if isinstance(draft, models.CustomFieldsDraft):
        return models.CustomFields(
            type=models.TypeReference(id=draft.type.id), fields=draft.fields
        )
    if isinstance(draft, models.PriceTierDraft):
        return models.PriceTier(
            minimum_quantity=draft.minimum_quantity,
            value=money_to_typed(
                models.Money(
                    cent_amount=draft.value.cent_amount,
                    currency_code=draft.value.currency_code,
                )
            ),
        )
    if isinstance(draft, models.TaxedPriceDraft):
        return models.TaxedPrice(
            total_net=money_to_typed(draft.total_net),
            total_gross=money_to_typed(draft.total_gross),
            tax_portions=[
                models.TaxPortion(
                    name=portion.name,
                    rate=portion.rate,
                    amount=money_to_typed(portion.amount),
                )
                for portion in draft.tax_portions
            ],
        )
    if isinstance(draft, models.ExternalTaxRateDraft):
        return models.TaxRate(
            id=str(uuid.uuid4()),
            name=draft.name,
            amount=draft.amount,
            included_in_price=draft.included_in_price,
            country=draft.country,
            state=draft.state,
            sub_rates=draft.sub_rates,
        )
    if isinstance(draft, models.PriceDraft):
        return models.Price(
            id=str(uuid.uuid4()),
            value=money_to_typed(draft.value),
            country=draft.country,
            customer_group=draft.customer_group,
            channel=draft.channel,
            valid_from=draft.valid_from,
            valid_until=draft.valid_until,
            discounted=draft.discounted,
            custom=create_from_draft(draft.custom),
            tiers=(
                None
                if draft.tiers is None
                else [create_from_draft(t) for t in draft.tiers]
            ),
        )

    raise ValueError(f"Unsupported type {draft.__class__}")


def custom_fields_from_draft(
    storage, draft: models.CustomFieldsDraft
) -> models.CustomFields:
    return models.CustomFields(
        type=models.TypeReference(
            id=storage.get_by_resource_identifier(draft.type)["id"]
        ),
        fields=draft.fields,
    )


def money_to_typed(
    money: typing.Optional[models.Money],
) -> typing.Optional[models.TypedMoney]:
    if money is None:
        return None

    return models.TypedMoney(
        cent_amount=money.cent_amount,
        currency_code=money.currency_code,
        type=models.MoneyType.CENT_PRECISION,
        fraction_digits=2,
    )


def update_attribute(dst: str, src: str):
    def updater(self, obj, action):
        value = getattr(action, src)

        if isinstance(value, _BaseType):
            value = value.serialize()

        if obj.get(dst) != value:
            new = copy.deepcopy(obj)
            new[dst] = value
            return new
        return obj

    return updater


def update_datetime_attribute(dst: str, src: str):
    def updater(self, obj, action):
        value = getattr(action, src)

        # value should be either None or datetime
        if isinstance(value, datetime):
            value = value.isoformat()

        if obj.get(dst) != value:
            new = copy.deepcopy(obj)
            new[dst] = value
            return new
        return obj

    return updater


def update_nested_object_attribute(dst: str, src: str):
    def updater(self, obj, action):
        values = getattr(action, src)

        # values should be either None or a list
        if isinstance(values, list):
            values = [item.serialize() for item in values]

        if values != obj.get(dst):
            new = copy.deepcopy(obj)
            new[dst] = values
            return new

        return obj

    return updater


def update_enum_attribute(dst: str, src: str):
    def updater(self, obj, action):
        value = getattr(action, src).value
        if obj.get(dst) != value:
            new = copy.deepcopy(obj)
            new[dst] = value
            return new
        return obj

    return updater


def update_attribute_add_item(
    dst: str,
    src: str,
    schema: Schema,
    id_generator: typing.Optional[typing.Callable] = None,
):
    def updater(self, obj, action):
        value = getattr(action, src)
        if id_generator:
            value.id = id_generator()
        value = schema().dump(value)
        if value not in obj[dst]:
            new = copy.deepcopy(obj)
            new[dst].append(value)
            return new
        else:
            raise InternalUpdateError(
                "Duplicate value %r exists for field %s on %r"
                % (json.dumps(value), dst, obj["id"])
            )
        return obj

    return updater


def update_attribute_delete_item(dst: str, src: str, schema: Schema):
    def updater(self, obj, action):
        value = getattr(action, src)
        value = schema().dump(value)
        if value in obj[dst]:
            new = copy.deepcopy(obj)
            new[dst].remove(value)
            return new
        else:
            raise InternalUpdateError("No item found with id %r" % (obj["id"]))

    return updater


def update_attribute_delete_item_by_id(dst: str, src: str):
    def updater(self, obj, action):
        value = getattr(action, src)

        new = copy.deepcopy(obj)
        for i, item in enumerate(obj[dst]):
            if item["id"] == value:
                del new[dst][i]
                return new

        raise InternalUpdateError("No item found with id %r" % value)

    return updater


def set_custom_field():
    """Set custom field. Note it always sets the type now, instead of type checking the custom field type!"""

    def updater(
        self,
        obj,
        action: typing.Union[OrderSetCustomFieldAction, CartSetCustomFieldAction],
    ):
        if not obj["custom"]:
            raise ValueError(
                "This resource has no custom type set - please use "
                "setCustomType first to set the type of the custom fields"
            )

        name = action.name
        value = action.value

        # real API always increments version, so always apply new value.
        new = copy.deepcopy(obj)
        if not new["custom"]:
            new["custom"] = {"fields": {}}
        new["custom"]["fields"][name] = value
        return new

    return updater


def set_line_item_custom_field():
    """Set custom field of a line item.
    Note it always sets the type now, instead of type checking the custom field type!
    """

    def updater(
        self,
        obj,
        action: typing.Union[
            OrderSetLineItemCustomFieldAction, CartSetLineItemCustomFieldAction
        ],
    ):
        line_item_id = action.line_item_id
        name = action.name
        value = action.value

        # real API always increments version, so always apply new value.
        new = copy.deepcopy(obj)
        for line in new["lineItems"]:
            if line["id"] != line_item_id:
                continue

            if not line["custom"]:
                line["custom"] = {"fields": {}}
            line["custom"]["fields"][name] = value
        return new

    return updater


def get_product_from_storage(
    storage: "Storage",
    product_id: typing.Union[str, uuid.UUID] = None,
    sku: str = None,
) -> typing.Optional[models.Product]:
    product = None
    product_store = storage._stores["product"]

    if product_id:
        if isinstance(product_id, str):
            product_id = uuid.UUID(product_id)
        product = ProductSchema().load(product_store[product_id])
    elif sku:
        for product_data in product_store.values():
            try:
                master_data = product_data["masterData"]["current"]
            except KeyError:
                continue

            if master_data and master_data["masterVariant"]["sku"] == sku:
                product = ProductSchema().load(product_data)
    else:
        raise ValueError("SKU or productId is required")

    return product


def create_commercetools_response(request, **kwargs):
    correlation_id = request.headers.get(
        HEADER_CORRELATION_ID, f"projects-{str(uuid.uuid4())}"
    )
    headers = kwargs.pop("headers", {})
    headers.update({HEADER_CORRELATION_ID: correlation_id})
    return create_response(request, headers=headers, **kwargs)

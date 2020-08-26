import copy
import importlib
import json
import typing
import uuid

from marshmallow import Schema
from requests_mock import create_response
from requests_mock.request import _RequestObjectProxy

from commercetools import types
from commercetools._schemas._product import ProductSchema
from commercetools.constants import HEADER_CORRELATION_ID
from commercetools.types import CartSetCustomFieldAction, OrderSetCustomFieldAction
from commercetools.types._abstract import _BaseType


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


def create_from_draft(draft):
    """Utility method to create normal objects out of draft objects.

    This is used for non-resource objects. For the resources themselves (which contain)
    an id, we have the specific implementations of the `BaseModel`.
    """
    if not draft:
        return None

    if isinstance(draft, types.CustomFieldsDraft):
        return types.CustomFields(
            type=types.TypeReference(id=draft.type.id), fields=draft.fields
        )
    if isinstance(draft, types.PriceTierDraft):
        return types.PriceTier(
            minimum_quantity=draft.minimum_quantity,
            value=_money_to_typed(
                types.Money(
                    cent_amount=draft.value.cent_amount,
                    currency_code=draft.value.currency_code,
                )
            ),
        )

    raise ValueError(f"Unsupported type {draft.__class__}")


def custom_fields_from_draft(
    storage, draft: types.CustomFieldsDraft
) -> types.CustomFields:
    return types.CustomFields(
        type=types.TypeReference(
            id=storage.get_by_resource_identifier(draft.type)["id"]
        ),
        fields=draft.fields,
    )


def _money_to_typed(
    money: typing.Optional[types.Money],
) -> typing.Optional[types.TypedMoney]:
    if money is not None:
        return types.TypedMoney(
            cent_amount=money.cent_amount,
            currency_code=money.currency_code,
            type=types.MoneyType.CENT_PRECISION,
            fraction_digits=2,
        )
    return None


def update_attribute(dst: str, src: str):
    def updater(self, obj, action):
        value = getattr(action, src)

        if isinstance(value, _BaseType):
            # FIXME: this stupidly assumes the types and schemas module names
            # are in sync. which might be the case since we auto-generate both,
            # but still...
            pkg_name = value.__class__.__module__.replace(".types.", "._schemas.")
            module = importlib.import_module(pkg_name)
            schema = getattr(module, value.__class__.__name__ + "Schema", None)
            if schema:
                value = schema().dump(value)
        if obj[dst] != value:
            new = copy.deepcopy(obj)
            new[dst] = value
            return new
        return obj

    return updater


def update_enum_attribute(dst: str, src: str):
    def updater(self, obj, action):
        value = getattr(action, src).value
        if obj[dst] != value:
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
        name = action.name
        value = action.value

        # real API always increments version, so always apply new value.
        new = copy.deepcopy(obj)
        if not new["custom"]:
            new["custom"] = {"fields": {}}
        new["custom"]["fields"][name] = value
        return new

    return updater


def get_product_from_storage(
    storage: "commercetools.testing.Storage",
    product_id: uuid.UUID = None,
    sku: str = None,
) -> typing.Optional[types.Product]:
    product = None
    product_store = storage._stores["product"]

    if product_id:
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

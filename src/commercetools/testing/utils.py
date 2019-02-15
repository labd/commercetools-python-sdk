import copy
import typing

from marshmallow import Schema
from requests_mock.request import _RequestObjectProxy

from commercetools import types


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


def create_from_draft(draft):
    """Utility method to create normal objects out of draft objects.

    This is used for non-resource objects. For the resources themselves (which contain)
    an id, we have the specific implementations of the `BaseModel`.
    """
    if not draft:
        return None

    if isinstance(draft, types.CustomFieldsDraft):
        return types.CustomFields(type=draft.type, fields=draft.fields)

    raise ValueError(f"Unsupported type {draft.__class__}")


def custom_fields_from_draft(
    storage, draft: types.CustomFieldsDraft
) -> types.CustomFields:
    return types.CustomFields(
        type=storage.get_by_resource_identifier(draft.type), fields=draft.fields
    )


def _money_to_typed(
    money: typing.Optional[types.Money]
) -> typing.Optional[types.TypedMoney]:
    if money is not None:
        return types.TypedMoney(
            cent_amount=money.cent_amount,
            currency_code=money.currency_code,
            type=types.MoneyType.CENT_PRECISION,
            fraction_digits=2,
        )


def update_attribute(dst: str, src: str):
    def updater(self, obj, action):
        value = getattr(action, src)
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


def update_attribute_add_item(dst: str, src: str, schema: Schema):
    def updater(self, obj, action):
        value = getattr(action, src)
        value = schema().dump(value)
        if value not in obj[dst]:
            new = copy.deepcopy(obj)
            new[dst].append(value)
            return new
        return obj

    return updater

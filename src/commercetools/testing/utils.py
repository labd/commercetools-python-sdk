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


def create_from_draft(draft_obj):
    """Utility method to create normal objects out of draft objects.

    This is used for non-resource objects. For the resources themselves (which contain)
    an id, we have the specific implementations of the `BaseModel`.
    """
    if not draft_obj:
        return None

    if isinstance(draft_obj, types.CustomFieldsDraft):
        return types.CustomFields(type=draft_obj.type, fields=draft_obj.fields)

    raise ValueError(f"Unsupported type {draft_obj.__class__}")


def custom_fields_from_draft(
    storage, draft: types.CustomFieldsDraft
) -> types.CustomFields:
    return types.CustomFields(
        type=storage.get_by_resource_identifier(draft.type), fields=draft.fields
    )

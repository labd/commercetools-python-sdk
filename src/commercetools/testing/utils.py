from marshmallow import Schema
from requests_mock.request import _RequestObjectProxy


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

from commercetools.platform.models import ExtensionNoResponseError, QueryTimedOutError
from commercetools.platform.models._schemas.error import ErrorResponseSchema


def test_extension_no_response_error():
    error_response = {
        "errors": [
            {
                "code": "ExtensionNoResponse",
                "extensionId": "eff671fb-d6e9-4fac-85b3-0b39af542762",
                "extensionKey": "create-cart",
                "message": "Extension did not respond in time.",
            }
        ],
        "message": "Extension did not respond in time.",
        "statusCode": 504,
    }

    obj = ErrorResponseSchema().load(error_response)
    error = obj.errors[0]

    assert isinstance(error, ExtensionNoResponseError)


def test_query_timeout_error():
    error_response = {
        "errors": [{"code": "QueryTimedOut", "message": "The query timed out."}],
        "message": "The query timed out.",
        "statusCode": 400,
    }
    obj = ErrorResponseSchema().load(error_response)
    error = obj.errors[0]

    assert isinstance(error, QueryTimedOutError)

import typing

from commercetools.types import ErrorResponse


class CommercetoolsError(Exception):
    response: ErrorResponse
    correlation_id: typing.Optional[str]

    def __init__(
        self, message: typing.Any, response: ErrorResponse, correlation_id: str = None
    ) -> None:
        super().__init__(message)
        self.response = response
        self.correlation_id = correlation_id

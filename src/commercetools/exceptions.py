import typing

from commercetools.types import ErrorResponse


class CommercetoolsError(Exception):
    response: ErrorResponse
    correlation_id: typing.Optional[str]

    def __init__(
        self,
        message: typing.Any,
        errors: typing.List[dict],
        response: ErrorResponse,
        correlation_id: str = None,
    ) -> None:
        super().__init__(message)
        self.response = response
        self.errors = errors
        self.correlation_id = correlation_id

    def __str__(self):
        result = super().__str__()
        if self.details:
            return f"{result} ({', '.join(self.details)})"
        return result

    @property
    def details(self) -> typing.List[str]:
        return [
            e["detailedErrorMessage"]
            for e in self.errors
            if "detailedErrorMessage" in e
        ]

    @property
    def codes(self) -> typing.List[str]:
        try:
            return [e.code for e in self.response.errors]
        except AttributeError:
            return []

    @property
    def code(self) -> str:
        """Convenience property to easily get the error code.
        
        Returns the code of the first error, just as
        'message' is always the message of the first error.
        """
        try:
            return self.codes[0]
        except KeyError:
            return ""

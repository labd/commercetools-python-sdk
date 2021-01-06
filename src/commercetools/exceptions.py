import typing

from commercetools.protocols import Model


class CommercetoolsError(Exception):
    response: Model
    correlation_id: typing.Optional[str]

    def __init__(
        self,
        message: typing.Any,
        errors: typing.List[dict],
        response: Model,
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
            if self.response.errors is not None:
                return [e.code for e in self.response.errors]
            else:
                return []
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

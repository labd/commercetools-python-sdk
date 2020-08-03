# DO NOT EDIT! This file is automatically generated
import datetime
import typing

from commercetools.types._abstract import _BaseType

__all__ = [
    "GraphQLError",
    "GraphQLErrorLocation",
    "GraphQLRequest",
    "GraphQLResponse",
    "GraphQLVariablesMap",
]


class GraphQLError(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.GraphQLErrorSchema`."""

    #: :class:`str`
    message: str
    #: :class:`list`
    locations: list
    #: :class:`list`
    path: list

    def __init__(
        self, *, message: str = None, locations: list = None, path: list = None
    ) -> None:
        self.message = message
        self.locations = locations
        self.path = path
        super().__init__()

    def __repr__(self) -> str:
        return "GraphQLError(message=%r, locations=%r, path=%r)" % (
            self.message,
            self.locations,
            self.path,
        )


class GraphQLErrorLocation(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.GraphQLErrorLocationSchema`."""

    #: :class:`int`
    line: int
    #: :class:`int`
    column: int

    def __init__(self, *, line: int = None, column: int = None) -> None:
        self.line = line
        self.column = column
        super().__init__()

    def __repr__(self) -> str:
        return "GraphQLErrorLocation(line=%r, column=%r)" % (self.line, self.column)


class GraphQLRequest(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.GraphQLRequestSchema`."""

    #: :class:`str`
    query: str
    #: Optional :class:`str` `(Named` ``operationName`` `in Commercetools)`
    operation_name: typing.Optional[str]
    #: Optional :class:`commercetools.types.GraphQLVariablesMap`
    variables: typing.Optional["GraphQLVariablesMap"]

    def __init__(
        self,
        *,
        query: str = None,
        operation_name: typing.Optional[str] = None,
        variables: typing.Optional["GraphQLVariablesMap"] = None,
    ) -> None:
        self.query = query
        self.operation_name = operation_name
        self.variables = variables
        super().__init__()

    def __repr__(self) -> str:
        return "GraphQLRequest(query=%r, operation_name=%r, variables=%r)" % (
            self.query,
            self.operation_name,
            self.variables,
        )


class GraphQLResponse(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.GraphQLResponseSchema`."""

    #: Optional :class:`typing.Any`
    data: typing.Optional[typing.Any]
    #: Optional :class:`list`
    errors: typing.Optional[list]

    def __init__(
        self,
        *,
        data: typing.Optional[typing.Any] = None,
        errors: typing.Optional[list] = None,
    ) -> None:
        self.data = data
        self.errors = errors
        super().__init__()

    def __repr__(self) -> str:
        return "GraphQLResponse(data=%r, errors=%r)" % (self.data, self.errors)


class GraphQLVariablesMap(typing.Dict[str, typing.Any]):
    def __repr__(self) -> str:
        return "GraphQLVariablesMap(%s)" % (
            ", ".join(f"{k}={v!r}" for k, v in self.items())
        )

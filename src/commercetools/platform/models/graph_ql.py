# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType

__all__ = [
    "GraphQLError",
    "GraphQLErrorLocation",
    "GraphQLRequest",
    "GraphQLResponse",
    "GraphQLVariablesMap",
]


class GraphQLError(_BaseType):
    message: str
    locations: typing.List["GraphQLErrorLocation"]
    path: typing.List["typing.Any"]

    def __init__(
        self,
        *,
        message: str,
        locations: typing.List["GraphQLErrorLocation"],
        path: typing.List["typing.Any"]
    ):
        self.message = message
        self.locations = locations
        self.path = path
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "GraphQLError":
        from ._schemas.graph_ql import GraphQLErrorSchema

        return GraphQLErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.graph_ql import GraphQLErrorSchema

        return GraphQLErrorSchema().dump(self)


class GraphQLErrorLocation(_BaseType):
    line: int
    column: int

    def __init__(self, *, line: int, column: int):
        self.line = line
        self.column = column
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "GraphQLErrorLocation":
        from ._schemas.graph_ql import GraphQLErrorLocationSchema

        return GraphQLErrorLocationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.graph_ql import GraphQLErrorLocationSchema

        return GraphQLErrorLocationSchema().dump(self)


class GraphQLRequest(_BaseType):
    query: str
    operation_name: typing.Optional[str]
    variables: typing.Optional["GraphQLVariablesMap"]

    def __init__(
        self,
        *,
        query: str,
        operation_name: typing.Optional[str] = None,
        variables: typing.Optional["GraphQLVariablesMap"] = None
    ):
        self.query = query
        self.operation_name = operation_name
        self.variables = variables
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "GraphQLRequest":
        from ._schemas.graph_ql import GraphQLRequestSchema

        return GraphQLRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.graph_ql import GraphQLRequestSchema

        return GraphQLRequestSchema().dump(self)


class GraphQLResponse(_BaseType):
    data: typing.Optional[typing.Any]
    errors: typing.Optional[typing.List["GraphQLError"]]

    def __init__(
        self,
        *,
        data: typing.Optional[typing.Any] = None,
        errors: typing.Optional[typing.List["GraphQLError"]] = None
    ):
        self.data = data
        self.errors = errors
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "GraphQLResponse":
        from ._schemas.graph_ql import GraphQLResponseSchema

        return GraphQLResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.graph_ql import GraphQLResponseSchema

        return GraphQLResponseSchema().dump(self)


class GraphQLVariablesMap(typing.Dict[str, str]):
    pass

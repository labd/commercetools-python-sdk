import typing

from marshmallow.base import SchemaABC


class Model(typing.Protocol[T]):
    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> T:
        ...

    def serialize(self) -> typing.Dict[str, typing.Any]:
        ...

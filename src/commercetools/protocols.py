import typing

try:
    from typing import Protocol
except ImportError:  # Python < 3.8
    Protocol = object


class Model(Protocol):
    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Model": ...

    def serialize(self) -> typing.Dict[str, typing.Any]: ...

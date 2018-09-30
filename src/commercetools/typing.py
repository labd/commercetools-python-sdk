import typing
from uuid import UUID

OptionalListStr = typing.Union[typing.List[str], str, None]
OptionalListInt = typing.Union[typing.List[str], str, None]
OptionalListUUID = typing.Union[typing.List[UUID], UUID, None]

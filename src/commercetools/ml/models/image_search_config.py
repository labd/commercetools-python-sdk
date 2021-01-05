# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType

__all__ = [
    "ChangeStatusUpdateAction",
    "ImageSearchConfigRequest",
    "ImageSearchConfigResponse",
    "ImageSearchConfigStatus",
    "ImageSearchConfigUpdateAction",
]


class ImageSearchConfigStatus(enum.Enum):
    ON = "on"
    OFF = "off"


class ImageSearchConfigUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ImageSearchConfigUpdateAction":
        if data["action"] == "changeStatus":
            from ._schemas.image_search_config import ChangeStatusUpdateActionSchema

            return ChangeStatusUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.image_search_config import ImageSearchConfigUpdateActionSchema

        return ImageSearchConfigUpdateActionSchema().dump(self)


class ChangeStatusUpdateAction(ImageSearchConfigUpdateAction):
    status: "ImageSearchConfigStatus"

    def __init__(self, *, status: "ImageSearchConfigStatus"):
        self.status = status
        super().__init__(action="changeStatus")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ChangeStatusUpdateAction":
        from ._schemas.image_search_config import ChangeStatusUpdateActionSchema

        return ChangeStatusUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.image_search_config import ChangeStatusUpdateActionSchema

        return ChangeStatusUpdateActionSchema().dump(self)


class ImageSearchConfigRequest(_BaseType):
    #: The list of update actions to be performed on the project.
    actions: typing.List["ImageSearchConfigUpdateAction"]

    def __init__(self, *, actions: typing.List["ImageSearchConfigUpdateAction"]):
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ImageSearchConfigRequest":
        from ._schemas.image_search_config import ImageSearchConfigRequestSchema

        return ImageSearchConfigRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.image_search_config import ImageSearchConfigRequestSchema

        return ImageSearchConfigRequestSchema().dump(self)


class ImageSearchConfigResponse(_BaseType):
    #: The image search activation status.
    status: "ImageSearchConfigStatus"
    last_modified_at: datetime.datetime

    def __init__(
        self, *, status: "ImageSearchConfigStatus", last_modified_at: datetime.datetime
    ):
        self.status = status
        self.last_modified_at = last_modified_at
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ImageSearchConfigResponse":
        from ._schemas.image_search_config import ImageSearchConfigResponseSchema

        return ImageSearchConfigResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.image_search_config import ImageSearchConfigResponseSchema

        return ImageSearchConfigResponseSchema().dump(self)

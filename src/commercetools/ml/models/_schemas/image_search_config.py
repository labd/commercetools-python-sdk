# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..image_search_config import ImageSearchConfigStatus

# Fields


# Marshmallow Schemas


class ImageSearchConfigUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ImageSearchConfigUpdateAction(**data)


class ChangeStatusUpdateActionSchema(ImageSearchConfigUpdateActionSchema):
    status = marshmallow_enum.EnumField(
        ImageSearchConfigStatus, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChangeStatusUpdateAction(**data)


class ImageSearchConfigRequestSchema(marshmallow.Schema):
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeStatus": helpers.absmod(
                    __name__, ".ChangeStatusUpdateActionSchema"
                )
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImageSearchConfigRequest(**data)


class ImageSearchConfigResponseSchema(marshmallow.Schema):
    status = marshmallow_enum.EnumField(
        ImageSearchConfigStatus, by_value=True, allow_none=True, missing=None
    )
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="lastModifiedAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImageSearchConfigResponse(**data)

# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ProcessingState
from ..importoperations import ImportOperationState

# Fields


# Marshmallow Schemas
class ImportOperationSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    import_sink_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="importSinkKey"
    )
    resource_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="resourceKey"
    )
    id = marshmallow.fields.String(allow_none=True, missing=None)
    state = marshmallow_enum.EnumField(
        ProcessingState, by_value=True, allow_none=True, missing=None
    )
    resource_version = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="resourceVersion"
    )
    retry_count = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="retryCount"
    )
    errors = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("code", "code"),
            discriminator_schemas={
                "access_denied": helpers.absmod(
                    __name__, ".errors.AccessDeniedErrorSchema"
                ),
                "invalid_scope": helpers.absmod(
                    __name__, ".errors.InvalidScopeErrorSchema"
                ),
                "InvalidOperation": helpers.absmod(
                    __name__, ".errors.InvalidOperationSchema"
                ),
                "DuplicateAttributeValue": helpers.absmod(
                    __name__, ".errors.DuplicateAttributeValueErrorSchema"
                ),
                "DuplicateAttributeValues": helpers.absmod(
                    __name__, ".errors.DuplicateAttributeValuesErrorSchema"
                ),
                "DuplicateField": helpers.absmod(
                    __name__, ".errors.DuplicateFieldErrorSchema"
                ),
                "DuplicateVariantValues": helpers.absmod(
                    __name__, ".errors.DuplicateVariantValuesErrorSchema"
                ),
                "insufficient_scope": helpers.absmod(
                    __name__, ".errors.InsufficientScopeErrorSchema"
                ),
                "InvalidCredentials": helpers.absmod(
                    __name__, ".errors.InvalidCredentialsErrorSchema"
                ),
                "invalid_token": helpers.absmod(
                    __name__, ".errors.InvalidTokenErrorSchema"
                ),
                "InvalidField": helpers.absmod(
                    __name__, ".errors.InvalidFieldErrorSchema"
                ),
                "InvalidJsonInput": helpers.absmod(
                    __name__, ".errors.InvalidJsonInputSchema"
                ),
                "InvalidInput": helpers.absmod(__name__, ".errors.InvalidInputSchema"),
                "ResourceNotFound": helpers.absmod(
                    __name__, ".errors.ResourceNotFoundErrorSchema"
                ),
                "ResourceCreation": helpers.absmod(
                    __name__, ".errors.ResourceCreationErrorSchema"
                ),
                "ResourceUpdate": helpers.absmod(
                    __name__, ".errors.ResourceUpdateErrorSchema"
                ),
                "ResourceDeletion": helpers.absmod(
                    __name__, ".errors.ResourceDeletionErrorSchema"
                ),
                "RequiredField": helpers.absmod(
                    __name__, ".errors.RequiredFieldErrorSchema"
                ),
                "InvalidTransition": helpers.absmod(
                    __name__, ".errors.InvalidStateTransitionErrorSchema"
                ),
                "ConcurrentModification": helpers.absmod(
                    __name__, ".errors.ConcurrentModificationErrorSchema"
                ),
                "Contention": helpers.absmod(__name__, ".errors.ContentionErrorSchema"),
                "Generic": helpers.absmod(__name__, ".errors.GenericErrorSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )
    created_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="createdAt"
    )
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="lastModifiedAt"
    )
    expires_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="expiresAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImportOperation(**data)


class ImportOperationPagedResponseSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ImportOperationSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImportOperationPagedResponse(**data)


class ImportOperationStatusSchema(marshmallow.Schema):
    operation_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="operationId"
    )
    state = marshmallow_enum.EnumField(
        ImportOperationState, by_value=True, allow_none=True, missing=None
    )
    errors = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("code", "code"),
            discriminator_schemas={
                "access_denied": helpers.absmod(
                    __name__, ".errors.AccessDeniedErrorSchema"
                ),
                "invalid_scope": helpers.absmod(
                    __name__, ".errors.InvalidScopeErrorSchema"
                ),
                "InvalidOperation": helpers.absmod(
                    __name__, ".errors.InvalidOperationSchema"
                ),
                "DuplicateAttributeValue": helpers.absmod(
                    __name__, ".errors.DuplicateAttributeValueErrorSchema"
                ),
                "DuplicateAttributeValues": helpers.absmod(
                    __name__, ".errors.DuplicateAttributeValuesErrorSchema"
                ),
                "DuplicateField": helpers.absmod(
                    __name__, ".errors.DuplicateFieldErrorSchema"
                ),
                "DuplicateVariantValues": helpers.absmod(
                    __name__, ".errors.DuplicateVariantValuesErrorSchema"
                ),
                "insufficient_scope": helpers.absmod(
                    __name__, ".errors.InsufficientScopeErrorSchema"
                ),
                "InvalidCredentials": helpers.absmod(
                    __name__, ".errors.InvalidCredentialsErrorSchema"
                ),
                "invalid_token": helpers.absmod(
                    __name__, ".errors.InvalidTokenErrorSchema"
                ),
                "InvalidField": helpers.absmod(
                    __name__, ".errors.InvalidFieldErrorSchema"
                ),
                "InvalidJsonInput": helpers.absmod(
                    __name__, ".errors.InvalidJsonInputSchema"
                ),
                "InvalidInput": helpers.absmod(__name__, ".errors.InvalidInputSchema"),
                "ResourceNotFound": helpers.absmod(
                    __name__, ".errors.ResourceNotFoundErrorSchema"
                ),
                "ResourceCreation": helpers.absmod(
                    __name__, ".errors.ResourceCreationErrorSchema"
                ),
                "ResourceUpdate": helpers.absmod(
                    __name__, ".errors.ResourceUpdateErrorSchema"
                ),
                "ResourceDeletion": helpers.absmod(
                    __name__, ".errors.ResourceDeletionErrorSchema"
                ),
                "RequiredField": helpers.absmod(
                    __name__, ".errors.RequiredFieldErrorSchema"
                ),
                "InvalidTransition": helpers.absmod(
                    __name__, ".errors.InvalidStateTransitionErrorSchema"
                ),
                "ConcurrentModification": helpers.absmod(
                    __name__, ".errors.ConcurrentModificationErrorSchema"
                ),
                "Contention": helpers.absmod(__name__, ".errors.ContentionErrorSchema"),
                "Generic": helpers.absmod(__name__, ".errors.GenericErrorSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImportOperationStatus(**data)

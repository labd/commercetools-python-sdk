# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, Reference

__all__ = [
    "Extension",
    "ExtensionAWSLambdaDestination",
    "ExtensionAction",
    "ExtensionAuthorizationHeaderAuthentication",
    "ExtensionAzureFunctionsAuthentication",
    "ExtensionChangeDestinationAction",
    "ExtensionChangeTriggersAction",
    "ExtensionDestination",
    "ExtensionDraft",
    "ExtensionHttpDestination",
    "ExtensionHttpDestinationAuthentication",
    "ExtensionInput",
    "ExtensionPagedQueryResponse",
    "ExtensionResourceTypeId",
    "ExtensionSetKeyAction",
    "ExtensionSetTimeoutInMsAction",
    "ExtensionTrigger",
    "ExtensionUpdate",
    "ExtensionUpdateAction",
]


class Extension(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    key: typing.Optional[str]
    destination: "ExtensionDestination"
    triggers: typing.List["ExtensionTrigger"]
    #: The maximum time the commercetools platform waits for a response from the extension.
    #: If not present, `2000` (2 seconds) is used.
    timeout_in_ms: typing.Optional[int]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional[str] = None,
        destination: "ExtensionDestination",
        triggers: typing.List["ExtensionTrigger"],
        timeout_in_ms: typing.Optional[int] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.destination = destination
        self.triggers = triggers
        self.timeout_in_ms = timeout_in_ms
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Extension":
        from ._schemas.extension import ExtensionSchema

        return ExtensionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionSchema

        return ExtensionSchema().dump(self)


class ExtensionAction(enum.Enum):
    CREATE = "Create"
    UPDATE = "Update"


class ExtensionDestination(_BaseType):
    type: str

    def __init__(self, *, type: str):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ExtensionDestination":
        if data["type"] == "AWSLambda":
            from ._schemas.extension import ExtensionAWSLambdaDestinationSchema

            return ExtensionAWSLambdaDestinationSchema().load(data)
        if data["type"] == "HTTP":
            from ._schemas.extension import ExtensionHttpDestinationSchema

            return ExtensionHttpDestinationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionDestinationSchema

        return ExtensionDestinationSchema().dump(self)


class ExtensionAWSLambdaDestination(ExtensionDestination):
    arn: str
    access_key: str
    access_secret: str

    def __init__(self, *, arn: str, access_key: str, access_secret: str):
        self.arn = arn
        self.access_key = access_key
        self.access_secret = access_secret
        super().__init__(type="AWSLambda")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExtensionAWSLambdaDestination":
        from ._schemas.extension import ExtensionAWSLambdaDestinationSchema

        return ExtensionAWSLambdaDestinationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionAWSLambdaDestinationSchema

        return ExtensionAWSLambdaDestinationSchema().dump(self)


class ExtensionDraft(_BaseType):
    #: User-specific unique identifier for the extension
    key: typing.Optional[str]
    #: Details where the extension can be reached
    destination: "ExtensionDestination"
    #: Describes what triggers the extension
    triggers: typing.List["ExtensionTrigger"]
    #: The maximum time the commercetools platform waits for a response from the extension.
    #: The maximum value is 2000 ms (2 seconds).
    #: This limit can be increased per project after we review the performance impact.
    #: Please contact Support via the [Support Portal](https://support.commercetools.com) and provide the region, project key and use case.
    timeout_in_ms: typing.Optional[int]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        destination: "ExtensionDestination",
        triggers: typing.List["ExtensionTrigger"],
        timeout_in_ms: typing.Optional[int] = None
    ):
        self.key = key
        self.destination = destination
        self.triggers = triggers
        self.timeout_in_ms = timeout_in_ms
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ExtensionDraft":
        from ._schemas.extension import ExtensionDraftSchema

        return ExtensionDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionDraftSchema

        return ExtensionDraftSchema().dump(self)


class ExtensionHttpDestination(ExtensionDestination):
    url: str
    authentication: typing.Optional["ExtensionHttpDestinationAuthentication"]

    def __init__(
        self,
        *,
        url: str,
        authentication: typing.Optional["ExtensionHttpDestinationAuthentication"] = None
    ):
        self.url = url
        self.authentication = authentication
        super().__init__(type="HTTP")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExtensionHttpDestination":
        from ._schemas.extension import ExtensionHttpDestinationSchema

        return ExtensionHttpDestinationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionHttpDestinationSchema

        return ExtensionHttpDestinationSchema().dump(self)


class ExtensionHttpDestinationAuthentication(_BaseType):
    type: str

    def __init__(self, *, type: str):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExtensionHttpDestinationAuthentication":
        if data["type"] == "AuthorizationHeader":
            from ._schemas.extension import (
                ExtensionAuthorizationHeaderAuthenticationSchema,
            )

            return ExtensionAuthorizationHeaderAuthenticationSchema().load(data)
        if data["type"] == "AzureFunctions":
            from ._schemas.extension import ExtensionAzureFunctionsAuthenticationSchema

            return ExtensionAzureFunctionsAuthenticationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionHttpDestinationAuthenticationSchema

        return ExtensionHttpDestinationAuthenticationSchema().dump(self)


class ExtensionAuthorizationHeaderAuthentication(
    ExtensionHttpDestinationAuthentication
):
    header_value: str

    def __init__(self, *, header_value: str):
        self.header_value = header_value
        super().__init__(type="AuthorizationHeader")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExtensionAuthorizationHeaderAuthentication":
        from ._schemas.extension import ExtensionAuthorizationHeaderAuthenticationSchema

        return ExtensionAuthorizationHeaderAuthenticationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionAuthorizationHeaderAuthenticationSchema

        return ExtensionAuthorizationHeaderAuthenticationSchema().dump(self)


class ExtensionAzureFunctionsAuthentication(ExtensionHttpDestinationAuthentication):
    key: str

    def __init__(self, *, key: str):
        self.key = key
        super().__init__(type="AzureFunctions")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExtensionAzureFunctionsAuthentication":
        from ._schemas.extension import ExtensionAzureFunctionsAuthenticationSchema

        return ExtensionAzureFunctionsAuthenticationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionAzureFunctionsAuthenticationSchema

        return ExtensionAzureFunctionsAuthenticationSchema().dump(self)


class ExtensionInput(_BaseType):
    action: "ExtensionAction"
    resource: "Reference"

    def __init__(self, *, action: "ExtensionAction", resource: "Reference"):
        self.action = action
        self.resource = resource
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ExtensionInput":
        from ._schemas.extension import ExtensionInputSchema

        return ExtensionInputSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionInputSchema

        return ExtensionInputSchema().dump(self)


class ExtensionPagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["Extension"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["Extension"]
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExtensionPagedQueryResponse":
        from ._schemas.extension import ExtensionPagedQueryResponseSchema

        return ExtensionPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionPagedQueryResponseSchema

        return ExtensionPagedQueryResponseSchema().dump(self)


class ExtensionResourceTypeId(enum.Enum):
    CART = "cart"
    ORDER = "order"
    PAYMENT = "payment"
    CUSTOMER = "customer"


class ExtensionTrigger(_BaseType):
    resource_type_id: "ExtensionResourceTypeId"
    actions: typing.List["ExtensionAction"]

    def __init__(
        self,
        *,
        resource_type_id: "ExtensionResourceTypeId",
        actions: typing.List["ExtensionAction"]
    ):
        self.resource_type_id = resource_type_id
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ExtensionTrigger":
        from ._schemas.extension import ExtensionTriggerSchema

        return ExtensionTriggerSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionTriggerSchema

        return ExtensionTriggerSchema().dump(self)


class ExtensionUpdate(_BaseType):
    version: int
    actions: typing.List["ExtensionUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["ExtensionUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ExtensionUpdate":
        from ._schemas.extension import ExtensionUpdateSchema

        return ExtensionUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionUpdateSchema

        return ExtensionUpdateSchema().dump(self)


class ExtensionUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ExtensionUpdateAction":
        if data["action"] == "changeDestination":
            from ._schemas.extension import ExtensionChangeDestinationActionSchema

            return ExtensionChangeDestinationActionSchema().load(data)
        if data["action"] == "changeTriggers":
            from ._schemas.extension import ExtensionChangeTriggersActionSchema

            return ExtensionChangeTriggersActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.extension import ExtensionSetKeyActionSchema

            return ExtensionSetKeyActionSchema().load(data)
        if data["action"] == "setTimeoutInMs":
            from ._schemas.extension import ExtensionSetTimeoutInMsActionSchema

            return ExtensionSetTimeoutInMsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionUpdateActionSchema

        return ExtensionUpdateActionSchema().dump(self)


class ExtensionChangeDestinationAction(ExtensionUpdateAction):
    destination: "ExtensionDestination"

    def __init__(self, *, destination: "ExtensionDestination"):
        self.destination = destination
        super().__init__(action="changeDestination")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExtensionChangeDestinationAction":
        from ._schemas.extension import ExtensionChangeDestinationActionSchema

        return ExtensionChangeDestinationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionChangeDestinationActionSchema

        return ExtensionChangeDestinationActionSchema().dump(self)


class ExtensionChangeTriggersAction(ExtensionUpdateAction):
    triggers: typing.List["ExtensionTrigger"]

    def __init__(self, *, triggers: typing.List["ExtensionTrigger"]):
        self.triggers = triggers
        super().__init__(action="changeTriggers")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExtensionChangeTriggersAction":
        from ._schemas.extension import ExtensionChangeTriggersActionSchema

        return ExtensionChangeTriggersActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionChangeTriggersActionSchema

        return ExtensionChangeTriggersActionSchema().dump(self)


class ExtensionSetKeyAction(ExtensionUpdateAction):
    #: If `key` is absent or `null`, this field will be removed if it exists.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ExtensionSetKeyAction":
        from ._schemas.extension import ExtensionSetKeyActionSchema

        return ExtensionSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionSetKeyActionSchema

        return ExtensionSetKeyActionSchema().dump(self)


class ExtensionSetTimeoutInMsAction(ExtensionUpdateAction):
    #: The maximum time the commercetools platform waits for a response from the extension.
    #: The maximum value is 2000 ms (2 seconds).
    #: This limit can be increased per project after we review the performance impact.
    #: Please contact Support via the support and provide the region, project key and use case.
    timeout_in_ms: typing.Optional[int]

    def __init__(self, *, timeout_in_ms: typing.Optional[int] = None):
        self.timeout_in_ms = timeout_in_ms
        super().__init__(action="setTimeoutInMs")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ExtensionSetTimeoutInMsAction":
        from ._schemas.extension import ExtensionSetTimeoutInMsActionSchema

        return ExtensionSetTimeoutInMsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.extension import ExtensionSetTimeoutInMsActionSchema

        return ExtensionSetTimeoutInMsActionSchema().dump(self)

# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, Reference
    from .message import UserProvidedIdentifiers


class ChangeSubscription(_BaseType):
    resource_type_id: "str"

    def __init__(self, *, resource_type_id: "str"):
        self.resource_type_id = resource_type_id
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ChangeSubscription":
        from ._schemas.subscription import ChangeSubscriptionSchema

        return ChangeSubscriptionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import ChangeSubscriptionSchema

        return ChangeSubscriptionSchema().dump(self)


class DeliveryFormat(_BaseType):
    type: "str"

    def __init__(self, *, type: "str"):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DeliveryFormat":
        from ._schemas.subscription import DeliveryFormatSchema

        return DeliveryFormatSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import DeliveryFormatSchema

        return DeliveryFormatSchema().dump(self)


class DeliveryCloudEventsFormat(DeliveryFormat):
    cloud_events_version: "str"

    def __init__(self, *, cloud_events_version: "str"):
        self.cloud_events_version = cloud_events_version
        super().__init__(type="CloudEvents")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DeliveryCloudEventsFormat":
        from ._schemas.subscription import DeliveryCloudEventsFormatSchema

        return DeliveryCloudEventsFormatSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import DeliveryCloudEventsFormatSchema

        return DeliveryCloudEventsFormatSchema().dump(self)


class DeliveryPlatformFormat(DeliveryFormat):
    def __init__(self):

        super().__init__(type="Platform")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DeliveryPlatformFormat":
        from ._schemas.subscription import DeliveryPlatformFormatSchema

        return DeliveryPlatformFormatSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import DeliveryPlatformFormatSchema

        return DeliveryPlatformFormatSchema().dump(self)


class Destination(_BaseType):
    type: "str"

    def __init__(self, *, type: "str"):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Destination":
        from ._schemas.subscription import DestinationSchema

        return DestinationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import DestinationSchema

        return DestinationSchema().dump(self)


class AzureEventGridDestination(Destination):
    uri: "str"
    access_key: "str"

    def __init__(self, *, uri: "str", access_key: "str"):
        self.uri = uri
        self.access_key = access_key
        super().__init__(type="EventGrid")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AzureEventGridDestination":
        from ._schemas.subscription import AzureEventGridDestinationSchema

        return AzureEventGridDestinationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import AzureEventGridDestinationSchema

        return AzureEventGridDestinationSchema().dump(self)


class AzureServiceBusDestination(Destination):
    connection_string: "str"

    def __init__(self, *, connection_string: "str"):
        self.connection_string = connection_string
        super().__init__(type="AzureServiceBus")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AzureServiceBusDestination":
        from ._schemas.subscription import AzureServiceBusDestinationSchema

        return AzureServiceBusDestinationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import AzureServiceBusDestinationSchema

        return AzureServiceBusDestinationSchema().dump(self)


class GoogleCloudPubSubDestination(Destination):
    project_id: "str"
    topic: "str"

    def __init__(self, *, project_id: "str", topic: "str"):
        self.project_id = project_id
        self.topic = topic
        super().__init__(type="GoogleCloudPubSub")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "GoogleCloudPubSubDestination":
        from ._schemas.subscription import GoogleCloudPubSubDestinationSchema

        return GoogleCloudPubSubDestinationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import GoogleCloudPubSubDestinationSchema

        return GoogleCloudPubSubDestinationSchema().dump(self)


class IronMqDestination(Destination):
    uri: "str"

    def __init__(self, *, uri: "str"):
        self.uri = uri
        super().__init__(type="IronMQ")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "IronMqDestination":
        from ._schemas.subscription import IronMqDestinationSchema

        return IronMqDestinationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import IronMqDestinationSchema

        return IronMqDestinationSchema().dump(self)


class MessageSubscription(_BaseType):
    resource_type_id: "str"
    types: typing.Optional[typing.List["str"]]

    def __init__(
        self,
        *,
        resource_type_id: "str",
        types: typing.Optional[typing.List["str"]] = None
    ):
        self.resource_type_id = resource_type_id
        self.types = types
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MessageSubscription":
        from ._schemas.subscription import MessageSubscriptionSchema

        return MessageSubscriptionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import MessageSubscriptionSchema

        return MessageSubscriptionSchema().dump(self)


class PayloadNotIncluded(_BaseType):
    reason: "str"
    payload_type: "str"

    def __init__(self, *, reason: "str", payload_type: "str"):
        self.reason = reason
        self.payload_type = payload_type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PayloadNotIncluded":
        from ._schemas.subscription import PayloadNotIncludedSchema

        return PayloadNotIncludedSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import PayloadNotIncludedSchema

        return PayloadNotIncludedSchema().dump(self)


class SnsDestination(Destination):
    access_key: "str"
    access_secret: "str"
    topic_arn: "str"

    def __init__(self, *, access_key: "str", access_secret: "str", topic_arn: "str"):
        self.access_key = access_key
        self.access_secret = access_secret
        self.topic_arn = topic_arn
        super().__init__(type="SNS")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SnsDestination":
        from ._schemas.subscription import SnsDestinationSchema

        return SnsDestinationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import SnsDestinationSchema

        return SnsDestinationSchema().dump(self)


class SqsDestination(Destination):
    access_key: "str"
    access_secret: "str"
    queue_url: "str"
    region: "str"

    def __init__(
        self,
        *,
        access_key: "str",
        access_secret: "str",
        queue_url: "str",
        region: "str"
    ):
        self.access_key = access_key
        self.access_secret = access_secret
        self.queue_url = queue_url
        self.region = region
        super().__init__(type="SQS")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SqsDestination":
        from ._schemas.subscription import SqsDestinationSchema

        return SqsDestinationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import SqsDestinationSchema

        return SqsDestinationSchema().dump(self)


class Subscription(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    changes: typing.List["ChangeSubscription"]
    destination: "Destination"
    key: typing.Optional["str"]
    messages: typing.List["MessageSubscription"]
    format: "DeliveryFormat"
    status: "SubscriptionHealthStatus"

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        changes: typing.List["ChangeSubscription"],
        destination: "Destination",
        key: typing.Optional["str"] = None,
        messages: typing.List["MessageSubscription"],
        format: "DeliveryFormat",
        status: "SubscriptionHealthStatus"
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.changes = changes
        self.destination = destination
        self.key = key
        self.messages = messages
        self.format = format
        self.status = status
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Subscription":
        from ._schemas.subscription import SubscriptionSchema

        return SubscriptionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import SubscriptionSchema

        return SubscriptionSchema().dump(self)


class SubscriptionDelivery(_BaseType):
    project_key: "str"
    notification_type: "str"
    resource: "Reference"
    resource_user_provided_identifiers: typing.Optional["UserProvidedIdentifiers"]

    def __init__(
        self,
        *,
        project_key: "str",
        notification_type: "str",
        resource: "Reference",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None
    ):
        self.project_key = project_key
        self.notification_type = notification_type
        self.resource = resource
        self.resource_user_provided_identifiers = resource_user_provided_identifiers
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SubscriptionDelivery":
        from ._schemas.subscription import SubscriptionDeliverySchema

        return SubscriptionDeliverySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import SubscriptionDeliverySchema

        return SubscriptionDeliverySchema().dump(self)


class MessageDelivery(SubscriptionDelivery):
    id: "str"
    version: "int"
    created_at: "datetime.datetime"
    last_modified_at: "datetime.datetime"
    sequence_number: "int"
    resource_version: "int"
    payload_not_included: "PayloadNotIncluded"

    def __init__(
        self,
        *,
        project_key: "str",
        resource: "Reference",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        sequence_number: "int",
        resource_version: "int",
        payload_not_included: "PayloadNotIncluded"
    ):
        self.id = id
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        self.sequence_number = sequence_number
        self.resource_version = resource_version
        self.payload_not_included = payload_not_included
        super().__init__(
            project_key=project_key,
            resource=resource,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            notification_type="Message",
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "MessageDelivery":
        from ._schemas.subscription import MessageDeliverySchema

        return MessageDeliverySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import MessageDeliverySchema

        return MessageDeliverySchema().dump(self)


class ResourceCreatedDelivery(SubscriptionDelivery):
    version: "int"
    modified_at: "datetime.datetime"

    def __init__(
        self,
        *,
        project_key: "str",
        resource: "Reference",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        version: "int",
        modified_at: "datetime.datetime"
    ):
        self.version = version
        self.modified_at = modified_at
        super().__init__(
            project_key=project_key,
            resource=resource,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            notification_type="ResourceCreated",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ResourceCreatedDelivery":
        from ._schemas.subscription import ResourceCreatedDeliverySchema

        return ResourceCreatedDeliverySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import ResourceCreatedDeliverySchema

        return ResourceCreatedDeliverySchema().dump(self)


class ResourceDeletedDelivery(SubscriptionDelivery):
    version: "int"
    modified_at: "datetime.datetime"
    data_erasure: typing.Optional["bool"]

    def __init__(
        self,
        *,
        project_key: "str",
        resource: "Reference",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        version: "int",
        modified_at: "datetime.datetime",
        data_erasure: typing.Optional["bool"] = None
    ):
        self.version = version
        self.modified_at = modified_at
        self.data_erasure = data_erasure
        super().__init__(
            project_key=project_key,
            resource=resource,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            notification_type="ResourceDeleted",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ResourceDeletedDelivery":
        from ._schemas.subscription import ResourceDeletedDeliverySchema

        return ResourceDeletedDeliverySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import ResourceDeletedDeliverySchema

        return ResourceDeletedDeliverySchema().dump(self)


class ResourceUpdatedDelivery(SubscriptionDelivery):
    version: "int"
    old_version: "int"
    modified_at: "datetime.datetime"

    def __init__(
        self,
        *,
        project_key: "str",
        resource: "Reference",
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        version: "int",
        old_version: "int",
        modified_at: "datetime.datetime"
    ):
        self.version = version
        self.old_version = old_version
        self.modified_at = modified_at
        super().__init__(
            project_key=project_key,
            resource=resource,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
            notification_type="ResourceUpdated",
        )

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ResourceUpdatedDelivery":
        from ._schemas.subscription import ResourceUpdatedDeliverySchema

        return ResourceUpdatedDeliverySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import ResourceUpdatedDeliverySchema

        return ResourceUpdatedDeliverySchema().dump(self)


class SubscriptionDraft(_BaseType):
    changes: typing.Optional[typing.List["ChangeSubscription"]]
    destination: "Destination"
    key: typing.Optional["str"]
    messages: typing.Optional[typing.List["MessageSubscription"]]
    format: typing.Optional["DeliveryFormat"]

    def __init__(
        self,
        *,
        changes: typing.Optional[typing.List["ChangeSubscription"]] = None,
        destination: "Destination",
        key: typing.Optional["str"] = None,
        messages: typing.Optional[typing.List["MessageSubscription"]] = None,
        format: typing.Optional["DeliveryFormat"] = None
    ):
        self.changes = changes
        self.destination = destination
        self.key = key
        self.messages = messages
        self.format = format
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SubscriptionDraft":
        from ._schemas.subscription import SubscriptionDraftSchema

        return SubscriptionDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import SubscriptionDraftSchema

        return SubscriptionDraftSchema().dump(self)


class SubscriptionHealthStatus(enum.Enum):
    HEALTHY = "Healthy"
    CONFIGURATION_ERROR = "ConfigurationError"
    CONFIGURATION_ERROR_DELIVERY_STOPPED = "ConfigurationErrorDeliveryStopped"
    TEMPORARY_ERROR = "TemporaryError"


class SubscriptionPagedQueryResponse(_BaseType):
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["Subscription"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["Subscription"]
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
    ) -> "SubscriptionPagedQueryResponse":
        from ._schemas.subscription import SubscriptionPagedQueryResponseSchema

        return SubscriptionPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import SubscriptionPagedQueryResponseSchema

        return SubscriptionPagedQueryResponseSchema().dump(self)


class SubscriptionUpdate(_BaseType):
    version: "int"
    actions: typing.List["SubscriptionUpdateAction"]

    def __init__(
        self, *, version: "int", actions: typing.List["SubscriptionUpdateAction"]
    ):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SubscriptionUpdate":
        from ._schemas.subscription import SubscriptionUpdateSchema

        return SubscriptionUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import SubscriptionUpdateSchema

        return SubscriptionUpdateSchema().dump(self)


class SubscriptionUpdateAction(_BaseType):
    action: "str"

    def __init__(self, *, action: "str"):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SubscriptionUpdateAction":
        from ._schemas.subscription import SubscriptionUpdateActionSchema

        return SubscriptionUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import SubscriptionUpdateActionSchema

        return SubscriptionUpdateActionSchema().dump(self)


class SubscriptionChangeDestinationAction(SubscriptionUpdateAction):
    destination: "Destination"

    def __init__(self, *, destination: "Destination"):
        self.destination = destination
        super().__init__(action="changeDestination")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SubscriptionChangeDestinationAction":
        from ._schemas.subscription import SubscriptionChangeDestinationActionSchema

        return SubscriptionChangeDestinationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import SubscriptionChangeDestinationActionSchema

        return SubscriptionChangeDestinationActionSchema().dump(self)


class SubscriptionSetChangesAction(SubscriptionUpdateAction):
    changes: typing.Optional[typing.List["ChangeSubscription"]]

    def __init__(
        self, *, changes: typing.Optional[typing.List["ChangeSubscription"]] = None
    ):
        self.changes = changes
        super().__init__(action="setChanges")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SubscriptionSetChangesAction":
        from ._schemas.subscription import SubscriptionSetChangesActionSchema

        return SubscriptionSetChangesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import SubscriptionSetChangesActionSchema

        return SubscriptionSetChangesActionSchema().dump(self)


class SubscriptionSetKeyAction(SubscriptionUpdateAction):
    #: If `key` is absent or `null`, this field will be removed if it exists.
    key: typing.Optional["str"]

    def __init__(self, *, key: typing.Optional["str"] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SubscriptionSetKeyAction":
        from ._schemas.subscription import SubscriptionSetKeyActionSchema

        return SubscriptionSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import SubscriptionSetKeyActionSchema

        return SubscriptionSetKeyActionSchema().dump(self)


class SubscriptionSetMessagesAction(SubscriptionUpdateAction):
    messages: typing.Optional[typing.List["MessageSubscription"]]

    def __init__(
        self, *, messages: typing.Optional[typing.List["MessageSubscription"]] = None
    ):
        self.messages = messages
        super().__init__(action="setMessages")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SubscriptionSetMessagesAction":
        from ._schemas.subscription import SubscriptionSetMessagesActionSchema

        return SubscriptionSetMessagesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.subscription import SubscriptionSetMessagesActionSchema

        return SubscriptionSetMessagesActionSchema().dump(self)

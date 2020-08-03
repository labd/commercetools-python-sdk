# DO NOT EDIT! This file is automatically generated
import datetime
import enum
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import BaseResource

if typing.TYPE_CHECKING:
    from ._common import CreatedBy, LastModifiedBy, Reference
    from ._message import UserProvidedIdentifiers
__all__ = [
    "AzureEventGridDestination",
    "AzureServiceBusDestination",
    "ChangeSubscription",
    "DeliveryCloudEventsFormat",
    "DeliveryFormat",
    "DeliveryPlatformFormat",
    "Destination",
    "GoogleCloudPubSubDestination",
    "IronMqDestination",
    "MessageDelivery",
    "MessageSubscription",
    "PayloadNotIncluded",
    "ResourceCreatedDelivery",
    "ResourceDeletedDelivery",
    "ResourceUpdatedDelivery",
    "SnsDestination",
    "SqsDestination",
    "Subscription",
    "SubscriptionChangeDestinationAction",
    "SubscriptionDelivery",
    "SubscriptionDraft",
    "SubscriptionHealthStatus",
    "SubscriptionPagedQueryResponse",
    "SubscriptionSetChangesAction",
    "SubscriptionSetKeyAction",
    "SubscriptionSetMessagesAction",
    "SubscriptionUpdate",
    "SubscriptionUpdateAction",
]


class ChangeSubscription(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.ChangeSubscriptionSchema`."""

    #: :class:`str` `(Named` ``resourceTypeId`` `in Commercetools)`
    resource_type_id: str

    def __init__(self, *, resource_type_id: str = None) -> None:
        self.resource_type_id = resource_type_id
        super().__init__()

    def __repr__(self) -> str:
        return "ChangeSubscription(resource_type_id=%r)" % (self.resource_type_id,)


class DeliveryFormat(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.DeliveryFormatSchema`."""

    #: :class:`str`
    type: str

    def __init__(self, *, type: str = None) -> None:
        self.type = type
        super().__init__()

    def __repr__(self) -> str:
        return "DeliveryFormat(type=%r)" % (self.type,)


class Destination(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.DestinationSchema`."""

    #: :class:`str`
    type: str

    def __init__(self, *, type: str = None) -> None:
        self.type = type
        super().__init__()

    def __repr__(self) -> str:
        return "Destination(type=%r)" % (self.type,)


class MessageSubscription(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.MessageSubscriptionSchema`."""

    #: :class:`str` `(Named` ``resourceTypeId`` `in Commercetools)`
    resource_type_id: str
    #: Optional list of :class:`str`
    types: typing.Optional[typing.List[str]]

    def __init__(
        self,
        *,
        resource_type_id: str = None,
        types: typing.Optional[typing.List[str]] = None
    ) -> None:
        self.resource_type_id = resource_type_id
        self.types = types
        super().__init__()

    def __repr__(self) -> str:
        return "MessageSubscription(resource_type_id=%r, types=%r)" % (
            self.resource_type_id,
            self.types,
        )


class PayloadNotIncluded(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.PayloadNotIncludedSchema`."""

    #: :class:`str`
    reason: str
    #: :class:`str` `(Named` ``payloadType`` `in Commercetools)`
    payload_type: str

    def __init__(self, *, reason: str = None, payload_type: str = None) -> None:
        self.reason = reason
        self.payload_type = payload_type
        super().__init__()

    def __repr__(self) -> str:
        return "PayloadNotIncluded(reason=%r, payload_type=%r)" % (
            self.reason,
            self.payload_type,
        )


class Subscription(BaseResource):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.SubscriptionSchema`."""

    #: :class:`str`
    id: str
    #: :class:`int`
    version: int
    #: :class:`datetime.datetime` `(Named` ``createdAt`` `in Commercetools)`
    created_at: datetime.datetime
    #: :class:`datetime.datetime` `(Named` ``lastModifiedAt`` `in Commercetools)`
    last_modified_at: datetime.datetime
    #: Optional :class:`commercetools.types.LastModifiedBy` `(Named` ``lastModifiedBy`` `in Commercetools)`
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Optional :class:`commercetools.types.CreatedBy` `(Named` ``createdBy`` `in Commercetools)`
    created_by: typing.Optional["CreatedBy"]
    #: List of :class:`commercetools.types.ChangeSubscription`
    changes: typing.List["ChangeSubscription"]
    #: :class:`commercetools.types.Destination`
    destination: "Destination"
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: List of :class:`commercetools.types.MessageSubscription`
    messages: typing.List["MessageSubscription"]
    #: :class:`commercetools.types.DeliveryFormat`
    format: "DeliveryFormat"
    #: :class:`commercetools.types.SubscriptionHealthStatus`
    status: "SubscriptionHealthStatus"

    def __init__(
        self,
        *,
        id: str = None,
        version: int = None,
        created_at: datetime.datetime = None,
        last_modified_at: datetime.datetime = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        changes: typing.List["ChangeSubscription"] = None,
        destination: "Destination" = None,
        key: typing.Optional[str] = None,
        messages: typing.List["MessageSubscription"] = None,
        format: "DeliveryFormat" = None,
        status: "SubscriptionHealthStatus" = None
    ) -> None:
        self.id = id
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
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

    def __repr__(self) -> str:
        return (
            "Subscription(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, changes=%r, destination=%r, key=%r, messages=%r, format=%r, status=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.changes,
                self.destination,
                self.key,
                self.messages,
                self.format,
                self.status,
            )
        )


class SubscriptionDelivery(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.SubscriptionDeliverySchema`."""

    #: :class:`str` `(Named` ``projectKey`` `in Commercetools)`
    project_key: str
    #: :class:`str` `(Named` ``notificationType`` `in Commercetools)`
    notification_type: str
    #: :class:`commercetools.types.Reference`
    resource: "Reference"
    #: Optional :class:`commercetools.types.UserProvidedIdentifiers` `(Named` ``resourceUserProvidedIdentifiers`` `in Commercetools)`
    resource_user_provided_identifiers: typing.Optional["UserProvidedIdentifiers"]

    def __init__(
        self,
        *,
        project_key: str = None,
        notification_type: str = None,
        resource: "Reference" = None,
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None
    ) -> None:
        self.project_key = project_key
        self.notification_type = notification_type
        self.resource = resource
        self.resource_user_provided_identifiers = resource_user_provided_identifiers
        super().__init__()

    def __repr__(self) -> str:
        return (
            "SubscriptionDelivery(project_key=%r, notification_type=%r, resource=%r, resource_user_provided_identifiers=%r)"
            % (
                self.project_key,
                self.notification_type,
                self.resource,
                self.resource_user_provided_identifiers,
            )
        )


class SubscriptionDraft(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.SubscriptionDraftSchema`."""

    #: Optional list of :class:`commercetools.types.ChangeSubscription`
    changes: typing.Optional[typing.List["ChangeSubscription"]]
    #: :class:`commercetools.types.Destination`
    destination: "Destination"
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: Optional list of :class:`commercetools.types.MessageSubscription`
    messages: typing.Optional[typing.List["MessageSubscription"]]
    #: Optional :class:`commercetools.types.DeliveryFormat`
    format: typing.Optional["DeliveryFormat"]

    def __init__(
        self,
        *,
        changes: typing.Optional[typing.List["ChangeSubscription"]] = None,
        destination: "Destination" = None,
        key: typing.Optional[str] = None,
        messages: typing.Optional[typing.List["MessageSubscription"]] = None,
        format: typing.Optional["DeliveryFormat"] = None
    ) -> None:
        self.changes = changes
        self.destination = destination
        self.key = key
        self.messages = messages
        self.format = format
        super().__init__()

    def __repr__(self) -> str:
        return (
            "SubscriptionDraft(changes=%r, destination=%r, key=%r, messages=%r, format=%r)"
            % (self.changes, self.destination, self.key, self.messages, self.format)
        )


class SubscriptionHealthStatus(enum.Enum):
    HEALTHY = "Healthy"
    CONFIGURATION_ERROR = "ConfigurationError"
    CONFIGURATION_ERROR_DELIVERY_STOPPED = "ConfigurationErrorDeliveryStopped"
    TEMPORARY_ERROR = "TemporaryError"


class SubscriptionPagedQueryResponse(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.SubscriptionPagedQueryResponseSchema`."""

    #: :class:`int`
    limit: int
    #: :class:`int`
    count: int
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: int
    #: List of :class:`commercetools.types.Subscription`
    results: typing.Sequence["Subscription"]

    def __init__(
        self,
        *,
        limit: int = None,
        count: int = None,
        total: typing.Optional[int] = None,
        offset: int = None,
        results: typing.Sequence["Subscription"] = None
    ) -> None:
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "SubscriptionPagedQueryResponse(limit=%r, count=%r, total=%r, offset=%r, results=%r)"
            % (self.limit, self.count, self.total, self.offset, self.results)
        )


class SubscriptionUpdate(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.SubscriptionUpdateSchema`."""

    #: :class:`int`
    version: int
    #: :class:`list`
    actions: list

    def __init__(self, *, version: int = None, actions: list = None) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "SubscriptionUpdate(version=%r, actions=%r)" % (
            self.version,
            self.actions,
        )


class SubscriptionUpdateAction(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.SubscriptionUpdateActionSchema`."""

    #: :class:`str`
    action: str

    def __init__(self, *, action: str = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "SubscriptionUpdateAction(action=%r)" % (self.action,)


class AzureEventGridDestination(Destination):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.AzureEventGridDestinationSchema`."""

    #: :class:`str`
    uri: str
    #: :class:`str` `(Named` ``accessKey`` `in Commercetools)`
    access_key: str

    def __init__(
        self, *, type: str = None, uri: str = None, access_key: str = None
    ) -> None:
        self.uri = uri
        self.access_key = access_key
        super().__init__(type="EventGrid")

    def __repr__(self) -> str:
        return "AzureEventGridDestination(type=%r, uri=%r, access_key=%r)" % (
            self.type,
            self.uri,
            self.access_key,
        )


class AzureServiceBusDestination(Destination):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.AzureServiceBusDestinationSchema`."""

    #: :class:`str` `(Named` ``connectionString`` `in Commercetools)`
    connection_string: str

    def __init__(self, *, type: str = None, connection_string: str = None) -> None:
        self.connection_string = connection_string
        super().__init__(type="AzureServiceBus")

    def __repr__(self) -> str:
        return "AzureServiceBusDestination(type=%r, connection_string=%r)" % (
            self.type,
            self.connection_string,
        )


class DeliveryCloudEventsFormat(DeliveryFormat):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.DeliveryCloudEventsFormatSchema`."""

    #: :class:`str` `(Named` ``cloudEventsVersion`` `in Commercetools)`
    cloud_events_version: str

    def __init__(self, *, type: str = None, cloud_events_version: str = None) -> None:
        self.cloud_events_version = cloud_events_version
        super().__init__(type="CloudEvents")

    def __repr__(self) -> str:
        return "DeliveryCloudEventsFormat(type=%r, cloud_events_version=%r)" % (
            self.type,
            self.cloud_events_version,
        )


class DeliveryPlatformFormat(DeliveryFormat):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.DeliveryPlatformFormatSchema`."""

    def __init__(self, *, type: str = None) -> None:
        super().__init__(type="Platform")

    def __repr__(self) -> str:
        return "DeliveryPlatformFormat(type=%r)" % (self.type,)


class GoogleCloudPubSubDestination(Destination):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.GoogleCloudPubSubDestinationSchema`."""

    #: :class:`str` `(Named` ``projectId`` `in Commercetools)`
    project_id: str
    #: :class:`str`
    topic: str

    def __init__(
        self, *, type: str = None, project_id: str = None, topic: str = None
    ) -> None:
        self.project_id = project_id
        self.topic = topic
        super().__init__(type="GoogleCloudPubSub")

    def __repr__(self) -> str:
        return "GoogleCloudPubSubDestination(type=%r, project_id=%r, topic=%r)" % (
            self.type,
            self.project_id,
            self.topic,
        )


class IronMqDestination(Destination):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.IronMqDestinationSchema`."""

    #: :class:`str`
    uri: str

    def __init__(self, *, type: str = None, uri: str = None) -> None:
        self.uri = uri
        super().__init__(type="IronMQ")

    def __repr__(self) -> str:
        return "IronMqDestination(type=%r, uri=%r)" % (self.type, self.uri)


class MessageDelivery(SubscriptionDelivery):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.MessageDeliverySchema`."""

    #: :class:`str`
    id: str
    #: :class:`int`
    version: int
    #: :class:`datetime.datetime` `(Named` ``createdAt`` `in Commercetools)`
    created_at: datetime.datetime
    #: :class:`datetime.datetime` `(Named` ``lastModifiedAt`` `in Commercetools)`
    last_modified_at: datetime.datetime
    #: :class:`int` `(Named` ``sequenceNumber`` `in Commercetools)`
    sequence_number: int
    #: :class:`int` `(Named` ``resourceVersion`` `in Commercetools)`
    resource_version: int
    #: :class:`commercetools.types.PayloadNotIncluded` `(Named` ``payloadNotIncluded`` `in Commercetools)`
    payload_not_included: "PayloadNotIncluded"

    def __init__(
        self,
        *,
        project_key: str = None,
        notification_type: str = None,
        resource: "Reference" = None,
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        id: str = None,
        version: int = None,
        created_at: datetime.datetime = None,
        last_modified_at: datetime.datetime = None,
        sequence_number: int = None,
        resource_version: int = None,
        payload_not_included: "PayloadNotIncluded" = None
    ) -> None:
        self.id = id
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        self.sequence_number = sequence_number
        self.resource_version = resource_version
        self.payload_not_included = payload_not_included
        super().__init__(
            project_key=project_key,
            notification_type="Message",
            resource=resource,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
        )

    def __repr__(self) -> str:
        return (
            "MessageDelivery(project_key=%r, notification_type=%r, resource=%r, resource_user_provided_identifiers=%r, id=%r, version=%r, created_at=%r, last_modified_at=%r, sequence_number=%r, resource_version=%r, payload_not_included=%r)"
            % (
                self.project_key,
                self.notification_type,
                self.resource,
                self.resource_user_provided_identifiers,
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.sequence_number,
                self.resource_version,
                self.payload_not_included,
            )
        )


class ResourceCreatedDelivery(SubscriptionDelivery):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.ResourceCreatedDeliverySchema`."""

    #: :class:`int`
    version: int
    #: :class:`datetime.datetime` `(Named` ``modifiedAt`` `in Commercetools)`
    modified_at: datetime.datetime

    def __init__(
        self,
        *,
        project_key: str = None,
        notification_type: str = None,
        resource: "Reference" = None,
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        version: int = None,
        modified_at: datetime.datetime = None
    ) -> None:
        self.version = version
        self.modified_at = modified_at
        super().__init__(
            project_key=project_key,
            notification_type="ResourceCreated",
            resource=resource,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
        )

    def __repr__(self) -> str:
        return (
            "ResourceCreatedDelivery(project_key=%r, notification_type=%r, resource=%r, resource_user_provided_identifiers=%r, version=%r, modified_at=%r)"
            % (
                self.project_key,
                self.notification_type,
                self.resource,
                self.resource_user_provided_identifiers,
                self.version,
                self.modified_at,
            )
        )


class ResourceDeletedDelivery(SubscriptionDelivery):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.ResourceDeletedDeliverySchema`."""

    #: :class:`int`
    version: int
    #: :class:`datetime.datetime` `(Named` ``modifiedAt`` `in Commercetools)`
    modified_at: datetime.datetime

    def __init__(
        self,
        *,
        project_key: str = None,
        notification_type: str = None,
        resource: "Reference" = None,
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        version: int = None,
        modified_at: datetime.datetime = None
    ) -> None:
        self.version = version
        self.modified_at = modified_at
        super().__init__(
            project_key=project_key,
            notification_type="ResourceDeleted",
            resource=resource,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
        )

    def __repr__(self) -> str:
        return (
            "ResourceDeletedDelivery(project_key=%r, notification_type=%r, resource=%r, resource_user_provided_identifiers=%r, version=%r, modified_at=%r)"
            % (
                self.project_key,
                self.notification_type,
                self.resource,
                self.resource_user_provided_identifiers,
                self.version,
                self.modified_at,
            )
        )


class ResourceUpdatedDelivery(SubscriptionDelivery):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.ResourceUpdatedDeliverySchema`."""

    #: :class:`int`
    version: int
    #: :class:`int` `(Named` ``oldVersion`` `in Commercetools)`
    old_version: int
    #: :class:`datetime.datetime` `(Named` ``modifiedAt`` `in Commercetools)`
    modified_at: datetime.datetime

    def __init__(
        self,
        *,
        project_key: str = None,
        notification_type: str = None,
        resource: "Reference" = None,
        resource_user_provided_identifiers: typing.Optional[
            "UserProvidedIdentifiers"
        ] = None,
        version: int = None,
        old_version: int = None,
        modified_at: datetime.datetime = None
    ) -> None:
        self.version = version
        self.old_version = old_version
        self.modified_at = modified_at
        super().__init__(
            project_key=project_key,
            notification_type="ResourceUpdated",
            resource=resource,
            resource_user_provided_identifiers=resource_user_provided_identifiers,
        )

    def __repr__(self) -> str:
        return (
            "ResourceUpdatedDelivery(project_key=%r, notification_type=%r, resource=%r, resource_user_provided_identifiers=%r, version=%r, old_version=%r, modified_at=%r)"
            % (
                self.project_key,
                self.notification_type,
                self.resource,
                self.resource_user_provided_identifiers,
                self.version,
                self.old_version,
                self.modified_at,
            )
        )


class SnsDestination(Destination):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.SnsDestinationSchema`."""

    #: :class:`str` `(Named` ``accessKey`` `in Commercetools)`
    access_key: str
    #: :class:`str` `(Named` ``accessSecret`` `in Commercetools)`
    access_secret: str
    #: :class:`str` `(Named` ``topicArn`` `in Commercetools)`
    topic_arn: str

    def __init__(
        self,
        *,
        type: str = None,
        access_key: str = None,
        access_secret: str = None,
        topic_arn: str = None
    ) -> None:
        self.access_key = access_key
        self.access_secret = access_secret
        self.topic_arn = topic_arn
        super().__init__(type="SNS")

    def __repr__(self) -> str:
        return (
            "SnsDestination(type=%r, access_key=%r, access_secret=%r, topic_arn=%r)"
            % (self.type, self.access_key, self.access_secret, self.topic_arn)
        )


class SqsDestination(Destination):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.SqsDestinationSchema`."""

    #: :class:`str` `(Named` ``accessKey`` `in Commercetools)`
    access_key: str
    #: :class:`str` `(Named` ``accessSecret`` `in Commercetools)`
    access_secret: str
    #: :class:`str` `(Named` ``queueUrl`` `in Commercetools)`
    queue_url: str
    #: :class:`str`
    region: str

    def __init__(
        self,
        *,
        type: str = None,
        access_key: str = None,
        access_secret: str = None,
        queue_url: str = None,
        region: str = None
    ) -> None:
        self.access_key = access_key
        self.access_secret = access_secret
        self.queue_url = queue_url
        self.region = region
        super().__init__(type="SQS")

    def __repr__(self) -> str:
        return (
            "SqsDestination(type=%r, access_key=%r, access_secret=%r, queue_url=%r, region=%r)"
            % (
                self.type,
                self.access_key,
                self.access_secret,
                self.queue_url,
                self.region,
            )
        )


class SubscriptionChangeDestinationAction(SubscriptionUpdateAction):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.SubscriptionChangeDestinationActionSchema`."""

    #: :class:`commercetools.types.Destination`
    destination: "Destination"

    def __init__(
        self, *, action: str = None, destination: "Destination" = None
    ) -> None:
        self.destination = destination
        super().__init__(action="changeDestination")

    def __repr__(self) -> str:
        return "SubscriptionChangeDestinationAction(action=%r, destination=%r)" % (
            self.action,
            self.destination,
        )


class SubscriptionSetChangesAction(SubscriptionUpdateAction):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.SubscriptionSetChangesActionSchema`."""

    #: Optional list of :class:`commercetools.types.ChangeSubscription`
    changes: typing.Optional[typing.List["ChangeSubscription"]]

    def __init__(
        self,
        *,
        action: str = None,
        changes: typing.Optional[typing.List["ChangeSubscription"]] = None
    ) -> None:
        self.changes = changes
        super().__init__(action="setChanges")

    def __repr__(self) -> str:
        return "SubscriptionSetChangesAction(action=%r, changes=%r)" % (
            self.action,
            self.changes,
        )


class SubscriptionSetKeyAction(SubscriptionUpdateAction):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.SubscriptionSetKeyActionSchema`."""

    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(self, *, action: str = None, key: typing.Optional[str] = None) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "SubscriptionSetKeyAction(action=%r, key=%r)" % (self.action, self.key)


class SubscriptionSetMessagesAction(SubscriptionUpdateAction):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.SubscriptionSetMessagesActionSchema`."""

    #: Optional list of :class:`commercetools.types.MessageSubscription`
    messages: typing.Optional[typing.List["MessageSubscription"]]

    def __init__(
        self,
        *,
        action: str = None,
        messages: typing.Optional[typing.List["MessageSubscription"]] = None
    ) -> None:
        self.messages = messages
        super().__init__(action="setMessages")

    def __repr__(self) -> str:
        return "SubscriptionSetMessagesAction(action=%r, messages=%r)" % (
            self.action,
            self.messages,
        )

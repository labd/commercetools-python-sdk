from commercetools.platform.models import message


def test_deserialize_order_created():
    result = message.OrderCreatedMessage.deserialize(
        {
            "createdAt": "2021-01-30T16:34:06.907Z",
            "id": "cb093b59-045d-47eb-8c6e-0a7fbf15b14b",
            "notificationType": "Message",
            "payloadNotIncluded": {
                "payloadType": "OrderCreated",
                "reason": "Payload too large",
            },
            "projectKey": "some-project",
            "resource": {
                "id": "a41e26ce-8801-4795-bc93-b1507e1d925f",
                "typeId": "order",
            },
            "resourceUserProvidedIdentifiers": {"orderNumber": "ORDER00001"},
            "resourceVersion": 1,
            "sequenceNumber": 1,
            "version": 1,
        }
    )
    assert result.id == "cb093b59-045d-47eb-8c6e-0a7fbf15b14b"
    assert result.resource

from commercetools.platform import models
from commercetools.platform.client import Client


def test_extension_create(ct_platform_client: Client):
    extension = (
        ct_platform_client.with_project_key("unittest")
        .extensions()
        .post(
            models.ExtensionDraft(
                destination=models.AWSLambdaDestination(
                    arn="arn:", access_key="access", access_secret="secret"
                ),
                triggers=[],
            )
        )
    )
    assert extension.id


def test_extension_with_id_get(ct_platform_client: Client):
    extension = (
        ct_platform_client.with_project_key("unittest")
        .extensions()
        .post(
            models.ExtensionDraft(
                destination=models.AWSLambdaDestination(
                    arn="arn:", access_key="access", access_secret="secret"
                ),
                triggers=[],
            )
        )
    )
    assert extension.id

    extension = (
        ct_platform_client.with_project_key("unittest")
        .extensions()
        .with_id(extension.id)
        .get()
    )
    assert extension.id


def test_extension_update_change_triggers(ct_platform_client: Client):
    extension = (
        ct_platform_client.with_project_key("unittest")
        .extensions()
        .post(
            models.ExtensionDraft(
                destination=models.AWSLambdaDestination(
                    arn="arn:", access_key="access", access_secret="secret"
                ),
                triggers=[],
            )
        )
    )
    assert extension.id
    assert extension.triggers == []

    extension = (
        ct_platform_client.with_project_key("unittest")
        .extensions()
        .with_id(extension.id)
        .post(
            models.ExtensionUpdate(
                version=extension.version,
                actions=[
                    models.ExtensionChangeTriggersAction(
                        triggers=[
                            models.ExtensionTrigger(
                                resource_type_id=models.ExtensionResourceTypeId.CART,
                                actions=[
                                    models.ExtensionAction.CREATE,
                                    models.ExtensionAction.UPDATE,
                                ],
                            )
                        ]
                    )
                ],
            )
        )
    )
    assert extension.triggers == [
        models.ExtensionTrigger(
            resource_type_id=models.ExtensionResourceTypeId.CART,
            actions=[models.ExtensionAction.CREATE, models.ExtensionAction.UPDATE],
        )
    ]

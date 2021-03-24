from commercetools.platform import models


def test_extension_create(old_client):
    extension = old_client.extensions.create(
        models.ExtensionDraft(
            destination=models.ExtensionAWSLambdaDestination(
                arn="arn:", access_key="access", access_secret="secret"
            ),
            triggers=[],
        )
    )
    assert extension.id


def test_extension_get_by_id(old_client):
    extension = old_client.extensions.create(
        models.ExtensionDraft(
            destination=models.ExtensionAWSLambdaDestination(
                arn="arn:", access_key="access", access_secret="secret"
            ),
            triggers=[],
        )
    )
    assert extension.id

    extension = old_client.extensions.get_by_id(extension.id)
    assert extension.id


def test_extension_update_change_triggers(old_client):
    extension = old_client.extensions.create(
        models.ExtensionDraft(
            destination=models.ExtensionAWSLambdaDestination(
                arn="arn:", access_key="access", access_secret="secret"
            ),
            triggers=[],
        )
    )
    assert extension.id
    assert extension.triggers == []

    extension = old_client.extensions.update_by_id(
        id=extension.id,
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
    assert extension.triggers == [
        models.ExtensionTrigger(
            resource_type_id=models.ExtensionResourceTypeId.CART,
            actions=[models.ExtensionAction.CREATE, models.ExtensionAction.UPDATE],
        )
    ]

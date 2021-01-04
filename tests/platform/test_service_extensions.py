from commercetools.platform import models


def test_extension_create(client):
    extension = client.extensions.create(
        models.ExtensionDraft(
            destination=models.ExtensionAWSLambdaDestination(
                arn="arn:", access_key="access", access_secret="secret"
            ),
            triggers=[],
        )
    )
    assert extension.id


def test_extension_get_by_id(client):
    extension = client.extensions.create(
        models.ExtensionDraft(
            destination=models.ExtensionAWSLambdaDestination(
                arn="arn:", access_key="access", access_secret="secret"
            ),
            triggers=[],
        )
    )
    assert extension.id

    extension = client.extensions.get_by_id(extension.id)
    assert extension.id

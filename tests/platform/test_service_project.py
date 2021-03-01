from commercetools.platform import models


def test_project_update_countries(old_client):
    project = old_client.project.get()
    project = old_client.project.update(
        actions=[models.ProjectChangeCountriesAction(countries=["AT", "NL"])],
        version=project.version,
    )
    assert project.countries == ["AT", "NL"]


def test_project_update_change_messages_enabled(old_client):
    project = old_client.project.get()
    project = old_client.project.update(
        actions=[models.ProjectChangeMessagesEnabledAction(messages_enabled=True)],
        version=project.version,
    )
    assert project.messages.enabled is True


def test_project_update_change_country_tax_rate_fallback_enabled(old_client):
    project = old_client.project.get()
    project = old_client.project.update(
        actions=[
            models.ProjectChangeCountryTaxRateFallbackEnabledAction(
                country_tax_rate_fallback_enabled=True
            )
        ],
        version=project.version,
    )
    assert project.carts.country_tax_rate_fallback_enabled is True

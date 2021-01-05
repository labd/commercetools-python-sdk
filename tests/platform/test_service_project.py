from commercetools.platform import models


def test_project_update(old_client):
    project = old_client.project.get()
    project = old_client.project.update(
        actions=[models.ProjectChangeCountriesAction(countries=["AT", "NL"])],
        version=project.version,
    )
    assert project.countries == ["AT", "NL"]

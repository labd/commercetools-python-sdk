from commercetools.platform import models


def test_project_update(client):
    project = client.project.get()
    project = client.project.update(
        actions=[models.ProjectChangeCountriesAction(countries=["AT", "NL"])],
        version=project.version,
    )
    assert project.countries == ["AT", "NL"]

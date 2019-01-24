from commercetools import types


def test_project_update(client):
    project = client.project.get()
    project = client.project.update(
        actions=[types.ProjectChangeCountriesAction(countries=["AT", "NL"])],
        version=project.version,
    )
    assert project.countries == ["AT", "NL"]

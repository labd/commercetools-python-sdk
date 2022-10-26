import pytest

from commercetools.platform import models
from commercetools.platform.client import Client


def test_state_flow(ct_platform_client: Client, state_draft):
    state = ct_platform_client.with_project_key("unittest").states().post(state_draft)
    assert state
    assert state.id

    new_name = models.LocalizedString({"en": "new_name"})
    new_description = models.LocalizedString({"en": "new_description"})
    update_actions = [
        models.StateSetNameAction(name=new_name),
        models.StateSetDescriptionAction(description=new_description),
        models.StateChangeInitialAction(initial=True),
        models.StateSetRolesAction(
            roles=[models.StateRoleEnum.REVIEW_INCLUDED_IN_STATISTICS]
        ),
    ]
    state = (
        ct_platform_client.with_project_key("unittest")
        .states()
        .with_id(state.id)
        .post(models.StateUpdate(version=state.version, actions=update_actions))
    )
    assert state
    assert state.name == new_name
    assert state.description == new_description
    assert state.initial is True
    assert state.roles and len(state.roles) == 1

    state = (
        ct_platform_client.with_project_key("unittest")
        .states()
        .with_id(state.id)
        .post(
            models.StateUpdate(
                version=state.version, actions=[models.StateSetRolesAction(roles=[])]
            )
        )
    )
    assert len(state.roles) == 0

    deleted_state = (
        ct_platform_client.with_project_key("unittest")
        .states()
        .with_id(state.id)
        .delete(version=state.version)
    )
    assert state.id == deleted_state.id


@pytest.fixture
def state_draft():
    return models.StateDraft(
        key="test state",
        name=models.LocalizedString({"en": "test store"}),
        description=models.LocalizedString({"en": "test store"}),
        initial=False,
        type=models.StateTypeEnum.REVIEW_STATE,
    )

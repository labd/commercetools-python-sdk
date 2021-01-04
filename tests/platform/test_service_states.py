import pytest

from commercetools.platform import models


def test_state_flow(client, state_draft):
    state = client.states.create(state_draft)
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
    state = client.states.update_by_id(state.id, state.version, update_actions)
    assert state.name == new_name
    assert state.description == new_description
    assert state.initial is True
    assert len(state.roles) == 1

    state = client.states.update_by_id(
        state.id, state.version, [models.StateSetRolesAction(roles=[])]
    )
    assert len(state.roles) == 0

    deleted_state = client.states.delete_by_id(state.id, state.version)
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

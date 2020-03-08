import pytest

from commercetools import types


def test_state_flow(client, state_draft):
    state = client.states.create(state_draft)
    assert state.id

    new_name = types.LocalizedString({"en": "new_name"})
    new_description = types.LocalizedString({"en": "new_description"})
    update_actions = [
        types.StateSetNameAction(name=new_name),
        types.StateSetDescriptionAction(description=new_description),
        types.StateChangeInitialAction(initial=True),
        types.StateSetRolesAction(
            roles=[types.StateRoleEnum.REVIEW_INCLUDED_IN_STATISTICS]
        ),
    ]
    state = client.states.update_by_id(state.id, state.version, update_actions)
    assert state.name == new_name
    assert state.description == new_description
    assert state.initial is True
    assert len(state.roles) == 1

    state = client.states.update_by_id(
        state.id, state.version, [types.StateSetRolesAction(roles=[])]
    )
    assert len(state.roles) == 0

    deleted_state = client.states.delete_by_id(state.id, state.version)
    assert state.id == deleted_state.id


@pytest.fixture
def state_draft():
    return types.StateDraft(
        key="test state",
        name=types.LocalizedString({"en": "test store"}),
        description=types.LocalizedString({"en": "test store"}),
        initial=False,
        type=types.StateTypeEnum.REVIEW_STATE,
    )

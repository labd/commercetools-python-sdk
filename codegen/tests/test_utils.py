import utils

import pytest


@pytest.mark.parametrize("test_input,test_output", [
    ('fooBar', 'foo_bar'),
    ('externalOAuth', 'external_oauth')
])
def test_snakit(test_input, test_output):
    assert utils.snakeit(test_input) == test_output

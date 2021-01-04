import pytest

from commercetools.utils import fix_token_url


@pytest.mark.parametrize(
    "token_url,expected_url",
    [
        ("https://auth.sphere.io", "https://auth.sphere.io/oauth/token"),
        ("https://auth.sphere.io/oauth/token", "https://auth.sphere.io/oauth/token"),
        ("https://auth.commercetools.co", "https://auth.commercetools.co/oauth/token"),
        (
            "https://auth.sphere.io?test=123",
            "https://auth.sphere.io/oauth/token?test=123",
        ),
    ],
)
def test_fix_token_url(token_url, expected_url):
    assert fix_token_url(token_url) == expected_url

import pytest

from commercetools.utils import fix_token_url


@pytest.mark.parametrize(
    "token_url,expected_url",
    [
        (
            "https://auth.europe-west1.gcp.commercetools.com",
            "https://auth.europe-west1.gcp.commercetools.com/oauth/token",
        ),
        (
            "https://auth.europe-west1.gcp.commercetools.com/oauth/token",
            "https://auth.europe-west1.gcp.commercetools.com/oauth/token",
        ),
        ("https://auth.commercetools.co", "https://auth.commercetools.co/oauth/token"),
        (
            "https://auth.europe-west1.gcp.commercetools.com?test=123",
            "https://auth.europe-west1.gcp.commercetools.com/oauth/token?test=123",
        ),
    ],
)
def test_fix_token_url(token_url, expected_url):
    assert fix_token_url(token_url) == expected_url

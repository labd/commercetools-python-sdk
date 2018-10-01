from commercetools.contrib.pytest import mock_backend

# Tricks flake8 into silencing redefining fixtures warnings.
__all__ = (
    'mock_backend',
)

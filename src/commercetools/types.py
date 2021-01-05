import warnings

from commercetools.platform.models import *  # noqa

warnings.warn(
    "This `commercetools.types` module will be removed in the near future, "
    "use the compatible `commercetools.platform.models`",
    DeprecationWarning,
)

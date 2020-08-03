# DO NOT EDIT! This file is automatically generated
import typing

from commercetools import schemas, types
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.typing import OptionalListStr

from . import abstract, traits


class LoginService(abstract.AbstractService):
    """Retrieves the authenticated customer."""

    def create(self) -> typing.Awaitable[types.CustomerSignInResult]:
        """Authenticate Customer (Sign In).

        Retrieves the authenticated customer (a customer that matches the given
        email/password pair). If used with an access token for Anonymous
        Sessions, all orders and carts belonging to the anonymousId will be
        assigned to the newly created customer. If a cart is is returned as part
        of the CustomerSignInResult, it has been recalculated (It will have up-
        to-date prices, taxes and discounts, and invalid line items have been
        removed.).   Retrieves the authenticated customer.
        """
        params = {}
        return self._client._post(
            endpoint="login",
            params=params,
            response_schema_cls=schemas.CustomerSignInResultSchema,
        )

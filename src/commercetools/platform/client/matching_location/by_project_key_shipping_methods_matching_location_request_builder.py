# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.error import ErrorResponse
from ...models.shipping_method import ShippingMethodPagedQueryResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyShippingMethodsMatchingLocationRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def get(
        self,
        *,
        country: str,
        state: str = None,
        currency: str = None,
        expand: typing.List["str"] = None,
        sort: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["ShippingMethodPagedQueryResponse"]:
        """Retrieves all the ShippingMethods that can ship to the given [Location](/projects/zones#location).
        ShippingMethods that have a `predicate` defined are automatically disqualified.
        If the `currency` parameter is given, then the ShippingMethods must also have a rate defined in the specified currency.
        Each ShippingMethod contains at least one ShippingRate with the flag `isMatching` set to `true`.
        If the `currency` parameter is given, exactly one ShippingRate will contain it.

        """
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/shipping-methods/matching-location",
            params={
                "country": country,
                "state": state,
                "currency": currency,
                "expand": expand,
                "sort": sort,
            },
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ShippingMethodPagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def head(
        self,
        *,
        country: str,
        state: str = None,
        currency: str = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional[None]:
        """Checks if a ShippingMethod that can ship to the given [Location](ctp:api:type:Location) exists. Returns a `200 OK` status if the ShippingMethod exists or a `404 Not Found` otherwise."""
        headers = {} if headers is None else headers
        response = self._client._head(
            endpoint=f"/{self._project_key}/shipping-methods/matching-location",
            params={"country": country, "state": state, "currency": currency},
            headers=headers,
            options=options,
        )
        if response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        elif response.status_code == 200:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

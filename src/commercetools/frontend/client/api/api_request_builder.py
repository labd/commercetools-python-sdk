# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ..build.api_build_request_builder import ApiBuildRequestBuilder

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ApiRequestBuilder:

    _client: "BaseClient"

    def __init__(
        self,
        client: "BaseClient",
    ):
        self._client = client

    def build(self) -> ApiBuildRequestBuilder:
        return ApiBuildRequestBuilder(
            client=self._client,
        )

# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from .frontastic_action_by_namespace_by_action_request_builder import (
    FrontasticActionByNamespaceByActionRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class FrontasticActionRequestBuilder:

    _client: "BaseClient"

    def __init__(
        self,
        client: "BaseClient",
    ):
        self._client = client

    def with_namespace_value_with_action_value(
        self, namespace: str, action: str
    ) -> FrontasticActionByNamespaceByActionRequestBuilder:
        return FrontasticActionByNamespaceByActionRequestBuilder(
            namespace=namespace,
            action=action,
            client=self._client,
        )

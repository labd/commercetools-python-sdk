# Generated file, please do not change!!!
import typing

from ...models.graph_ql import GraphQLRequest, GraphQLResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyGraphqlRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def post(
        self, body: "GraphQLRequest", *, headers: typing.Dict[str, str] = None
    ) -> "GraphQLResponse":
        """Execute a GraphQL query"""
        headers = {} if headers is None else headers
        return self._client._post(
            endpoint=f"/{self._project_key}/graphql",
            params={},
            data_object=body,
            response_class=GraphQLResponse,
            headers={"Content-Type": "application/graphql", **headers},
        )

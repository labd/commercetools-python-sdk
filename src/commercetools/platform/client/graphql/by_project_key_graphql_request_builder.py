# Generated file, please do not change!!!
import typing

from ...models.graph_ql import GraphQLRequest, GraphQLResponse


class ByProjectKeyGraphqlRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(
        self,
        projectKey: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._client = client

    def post(
        self, body: "GraphQLRequest", *, headers: typing.Dict[str, str] = None
    ) -> "GraphQLResponse":
        """Execute a GraphQL query"""
        return self._client._post(
            endpoint=f"/{self._project_key}/graphql",
            params={},
            data_object=body,
            response_class=GraphQLResponse,
            headers={"Content-Type": "application/graphql", **headers},
        )

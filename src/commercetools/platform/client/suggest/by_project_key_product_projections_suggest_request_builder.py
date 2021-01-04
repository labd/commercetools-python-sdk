# Generated file, please do not change!!!
import typing


class ByProjectKeyProductProjectionsSuggestRequestBuilder:

    _client: "Client"
    _project_key: str

    def __init__(self, projectKey: str, client: "Client"):
        self._project_key = projectKey
        self._client = client

    def get(
        self,
        *,
        fuzzy: "bool" = None,
        staged: "bool" = None,
        sort: "str" = None,
        limit: "int" = None,
        offset: "int" = None,
        with_total: "bool" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "any":
        return self._client._get(
            endpoint=f"/{self._project_key}/product-projections/suggest",
            params={
                "fuzzy": fuzzy,
                "staged": staged,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
            },
            response_object=any,
            headers=headers,
        )

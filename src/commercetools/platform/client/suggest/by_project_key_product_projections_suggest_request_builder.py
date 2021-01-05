# Generated file, please do not change!!!
import typing

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyProductProjectionsSuggestRequestBuilder:

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
        fuzzy: bool = None,
        staged: bool = None,
        search_keywords: typing.Dict[str, str] = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        headers: typing.Dict[str, str] = None,
    ) -> typing.Any:
        params = {
            "fuzzy": fuzzy,
            "staged": staged,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
        }
        search_keywords and params.update(
            {f"searchKeywords.{k}": v for k, v in search_keywords.items()}
        )
        headers = {} if headers is None else headers
        return self._client._get(
            endpoint=f"/{self._project_key}/product-projections/suggest",
            params=params,
            response_class=typing.Any,
            headers=headers,
        )

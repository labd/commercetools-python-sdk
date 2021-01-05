# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType


class ApiClient(_BaseType):
    #: The unique ID of the API client.
    #: This is the OAuth2 `client_id` and can be used to obtain a token.
    id: "str"
    name: "str"
    #: A whitespace separated list of the OAuth scopes.
    #: This is the OAuth2 `scope` and can be used to obtain a token.
    scope: "str"
    created_at: typing.Optional["datetime.datetime"]
    #: The last day this API Client was used to obtain a token.
    last_used_at: typing.Optional["datetime.date"]
    #: If set, the client will be deleted on (or shortly after) this point in time.
    delete_at: typing.Optional["datetime.datetime"]
    #: The secret is only shown once in the response of creating the API Client.
    #: This is the OAuth2 `client_secret` and can be used to obtain a token.
    secret: typing.Optional["str"]

    def __init__(
        self,
        *,
        id: "str",
        name: "str",
        scope: "str",
        created_at: typing.Optional["datetime.datetime"] = None,
        last_used_at: typing.Optional["datetime.date"] = None,
        delete_at: typing.Optional["datetime.datetime"] = None,
        secret: typing.Optional["str"] = None
    ):
        self.id = id
        self.name = name
        self.scope = scope
        self.created_at = created_at
        self.last_used_at = last_used_at
        self.delete_at = delete_at
        self.secret = secret
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ApiClient":
        from ._schemas.api_client import ApiClientSchema

        return ApiClientSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.api_client import ApiClientSchema

        return ApiClientSchema().dump(self)


class ApiClientDraft(_BaseType):
    name: "str"
    scope: "str"
    #: If set, the client will be deleted after the specified amount of days.
    delete_days_after_creation: typing.Optional["int"]

    def __init__(
        self,
        *,
        name: "str",
        scope: "str",
        delete_days_after_creation: typing.Optional["int"] = None
    ):
        self.name = name
        self.scope = scope
        self.delete_days_after_creation = delete_days_after_creation
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ApiClientDraft":
        from ._schemas.api_client import ApiClientDraftSchema

        return ApiClientDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.api_client import ApiClientDraftSchema

        return ApiClientDraftSchema().dump(self)


class ApiClientPagedQueryResponse(_BaseType):
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["ApiClient"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["ApiClient"]
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ApiClientPagedQueryResponse":
        from ._schemas.api_client import ApiClientPagedQueryResponseSchema

        return ApiClientPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.api_client import ApiClientPagedQueryResponseSchema

        return ApiClientPagedQueryResponseSchema().dump(self)

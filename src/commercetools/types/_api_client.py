# DO NOT EDIT! This file is automatically generated

import datetime
import typing

import attr

__all__ = ["ApiClient", "ApiClientDraft", "ApiClientPagedQueryResponse"]


@attr.s(auto_attribs=True, init=False, repr=False)
class ApiClient:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ApiClientSchema`."
    #: :class:`str`
    id: typing.Optional[str]
    #: :class:`str`
    name: typing.Optional[str]
    #: :class:`str`
    scope: typing.Optional[str]
    #: :class:`datetime.datetime` `(Named` ``createdAt`` `in Commercetools)`
    created_at: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.date` `(Named` ``lastUsedAt`` `in Commercetools)`
    last_used_at: typing.Optional[datetime.date]
    #: Optional :class:`str`
    secret: typing.Optional[str]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_used_at: typing.Optional[datetime.date] = None,
        secret: typing.Optional[str] = None
    ) -> None:
        self.id = id
        self.name = name
        self.scope = scope
        self.created_at = created_at
        self.last_used_at = last_used_at
        self.secret = secret

    def __repr__(self) -> str:
        return (
            "ApiClient(id=%r, name=%r, scope=%r, created_at=%r, last_used_at=%r, secret=%r)"
            % (
                self.id,
                self.name,
                self.scope,
                self.created_at,
                self.last_used_at,
                self.secret,
            )
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class ApiClientDraft:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ApiClientDraftSchema`."
    #: :class:`str`
    name: typing.Optional[str]
    #: :class:`str`
    scope: typing.Optional[str]

    def __init__(
        self, *, name: typing.Optional[str] = None, scope: typing.Optional[str] = None
    ) -> None:
        self.name = name
        self.scope = scope

    def __repr__(self) -> str:
        return "ApiClientDraft(name=%r, scope=%r)" % (self.name, self.scope)


@attr.s(auto_attribs=True, init=False, repr=False)
class ApiClientPagedQueryResponse:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ApiClientPagedQueryResponseSchema`."
    #: :class:`int`
    count: typing.Optional[int]
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: typing.Optional[int]
    #: List of :class:`commercetools.types.ApiClient`
    results: typing.Optional[typing.Sequence["ApiClient"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["ApiClient"]] = None
    ) -> None:
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results

    def __repr__(self) -> str:
        return (
            "ApiClientPagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)"
            % (self.count, self.total, self.offset, self.results)
        )

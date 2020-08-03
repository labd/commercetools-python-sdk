# DO NOT EDIT! This file is automatically generated
import datetime
import typing

from commercetools.types._abstract import _BaseType

__all__ = ["ApiClient", "ApiClientDraft", "ApiClientPagedQueryResponse"]


class ApiClient(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.ApiClientSchema`."""

    #: :class:`str`
    id: str
    #: :class:`str`
    name: str
    #: :class:`str`
    scope: str
    #: Optional :class:`datetime.datetime` `(Named` ``createdAt`` `in Commercetools)`
    created_at: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.date` `(Named` ``lastUsedAt`` `in Commercetools)`
    last_used_at: typing.Optional[datetime.date]
    #: Optional :class:`datetime.datetime` `(Named` ``deleteAt`` `in Commercetools)`
    delete_at: typing.Optional[datetime.datetime]
    #: Optional :class:`str`
    secret: typing.Optional[str]

    def __init__(
        self,
        *,
        id: str = None,
        name: str = None,
        scope: str = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_used_at: typing.Optional[datetime.date] = None,
        delete_at: typing.Optional[datetime.datetime] = None,
        secret: typing.Optional[str] = None
    ) -> None:
        self.id = id
        self.name = name
        self.scope = scope
        self.created_at = created_at
        self.last_used_at = last_used_at
        self.delete_at = delete_at
        self.secret = secret
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ApiClient(id=%r, name=%r, scope=%r, created_at=%r, last_used_at=%r, delete_at=%r, secret=%r)"
            % (
                self.id,
                self.name,
                self.scope,
                self.created_at,
                self.last_used_at,
                self.delete_at,
                self.secret,
            )
        )


class ApiClientDraft(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.ApiClientDraftSchema`."""

    #: :class:`str`
    name: str
    #: :class:`str`
    scope: str
    #: Optional :class:`int` `(Named` ``deleteDaysAfterCreation`` `in Commercetools)`
    delete_days_after_creation: typing.Optional[int]

    def __init__(
        self,
        *,
        name: str = None,
        scope: str = None,
        delete_days_after_creation: typing.Optional[int] = None
    ) -> None:
        self.name = name
        self.scope = scope
        self.delete_days_after_creation = delete_days_after_creation
        super().__init__()

    def __repr__(self) -> str:
        return "ApiClientDraft(name=%r, scope=%r, delete_days_after_creation=%r)" % (
            self.name,
            self.scope,
            self.delete_days_after_creation,
        )


class ApiClientPagedQueryResponse(_BaseType):
    """Corresponding marshmallow schema is :class:`commercetools.schemas.ApiClientPagedQueryResponseSchema`."""

    #: :class:`int`
    limit: int
    #: :class:`int`
    count: int
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: int
    #: List of :class:`commercetools.types.ApiClient`
    results: typing.Sequence["ApiClient"]

    def __init__(
        self,
        *,
        limit: int = None,
        count: int = None,
        total: typing.Optional[int] = None,
        offset: int = None,
        results: typing.Sequence["ApiClient"] = None
    ) -> None:
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ApiClientPagedQueryResponse(limit=%r, count=%r, total=%r, offset=%r, results=%r)"
            % (self.limit, self.count, self.total, self.offset, self.results)
        )

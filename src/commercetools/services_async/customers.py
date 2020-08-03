# DO NOT EDIT! This file is automatically generated
import typing

from commercetools import schemas, types
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _CustomerQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _CustomerUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _CustomerDeleteSchema(
    traits.VersionedSchema, traits.ExpandableSchema, traits.DataErasureSchema
):
    pass


class CustomerService(abstract.AbstractService):
    """A customer is a person purchasing products.

    customers, Orders, Comments and Reviews can be associated to a customer.
    """

    def get_by_email_token(
        self, email_token: str, *, expand: OptionalListStr = None
    ) -> typing.Awaitable[types.Customer]:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"customers/email-token={email_token}",
            params=params,
            schema_cls=schemas.CustomerSchema,
        )

    def get_by_id(
        self, id: str, *, expand: OptionalListStr = None
    ) -> typing.Awaitable[types.Customer]:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"customers/{id}", params=params, schema_cls=schemas.CustomerSchema
        )

    def get_by_key(
        self, key: str, *, expand: OptionalListStr = None
    ) -> typing.Awaitable[types.Customer]:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"customers/key={key}",
            params=params,
            schema_cls=schemas.CustomerSchema,
        )

    def get_by_password_token(
        self, password_token: str, *, expand: OptionalListStr = None
    ) -> typing.Awaitable[types.Customer]:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"customers/password-token={password_token}",
            params=params,
            schema_cls=schemas.CustomerSchema,
        )

    def query(
        self,
        *,
        expand: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: OptionalListStr = None,
        predicate_var: typing.Dict[str, str] = None,
    ) -> typing.Awaitable[types.CustomerPagedQueryResponse]:
        """A customer is a person purchasing products. customers, Orders, Comments
        and Reviews can be associated to a customer.
        """
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
                "predicate_var": predicate_var,
            },
            _CustomerQuerySchema,
        )
        return self._client._get(
            endpoint="customers",
            params=params,
            schema_cls=schemas.CustomerPagedQueryResponseSchema,
        )

    def create(
        self, draft: types.CustomerDraft, *, expand: OptionalListStr = None
    ) -> typing.Awaitable[types.CustomerSignInResult]:
        """Creates a customer.

        If an anonymous cart is passed in, then the cart is assigned to the
        created customer and the version number of the Cart will increase. If the
        ID of an anonymous session is given, all carts and orders will be
        assigned to the created customer.   A customer is a person purchasing
        products. customers, Orders, Comments and Reviews can be associated to a
        customer.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="customers",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.CustomerDraftSchema,
            response_schema_cls=schemas.CustomerSignInResultSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.CustomerUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> typing.Awaitable[types.Customer]:
        params = self._serialize_params({"expand": expand}, _CustomerUpdateSchema)
        update_action = types.CustomerUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"customers/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.CustomerUpdateSchema,
            response_schema_cls=schemas.CustomerSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[types.CustomerUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> typing.Awaitable[types.Customer]:
        params = self._serialize_params({"expand": expand}, _CustomerUpdateSchema)
        update_action = types.CustomerUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"customers/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.CustomerUpdateSchema,
            response_schema_cls=schemas.CustomerSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> typing.Awaitable[types.Customer]:
        params = self._serialize_params(
            {"version": version, "expand": expand, "dataErasure": data_erasure},
            _CustomerDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"customers/{id}",
            params=params,
            response_schema_cls=schemas.CustomerSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> typing.Awaitable[types.Customer]:
        params = self._serialize_params(
            {"version": version, "expand": expand, "dataErasure": data_erasure},
            _CustomerDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"customers/key={key}",
            params=params,
            response_schema_cls=schemas.CustomerSchema,
            force_delete=force_delete,
        )

    def email_confirm(
        self, action: types.CustomerEmailVerify
    ) -> typing.Awaitable[types.Customer]:
        """Verifies customer's email using a token."""
        params = {}
        return self._client._post(
            endpoint="customers/email/confirm",
            params=params,
            data_object=action,
            request_schema_cls=schemas.CustomerEmailVerifySchema,
            response_schema_cls=schemas.CustomerSchema,
        )

    def email_token(
        self, action: types.CustomerCreateEmailToken
    ) -> typing.Awaitable[types.CustomerToken]:
        """Create a Token for verifying the Customer's Email

        To verify a customer's email, an email token can be created. This should
        be embedded in a link and sent to the customer via email. When the
        customer clicks on the link, the "verify customer's email" endpoint
        should be called, which sets customer's isVerifiedEmail field to true.
        """
        params = {}
        return self._client._post(
            endpoint="customers/email-token",
            params=params,
            data_object=action,
            request_schema_cls=schemas.CustomerCreateEmailTokenSchema,
            response_schema_cls=schemas.CustomerTokenSchema,
        )

    def password(
        self, action: types.CustomerChangePassword
    ) -> typing.Awaitable[types.Customer]:
        """Change a customers password"""
        params = {}
        return self._client._post(
            endpoint="customers/password",
            params=params,
            data_object=action,
            request_schema_cls=schemas.CustomerChangePasswordSchema,
            response_schema_cls=schemas.CustomerSchema,
        )

    def password_reset(
        self, action: types.CustomerResetPassword
    ) -> typing.Awaitable[types.Customer]:
        """Set a new password using a token."""
        params = {}
        return self._client._post(
            endpoint="customers/password/reset",
            params=params,
            data_object=action,
            request_schema_cls=schemas.CustomerResetPasswordSchema,
            response_schema_cls=schemas.CustomerSchema,
        )

    def password_token(
        self, action: types.CustomerCreatePasswordResetToken
    ) -> typing.Awaitable[types.CustomerToken]:
        """The token value is used to reset the password of the customer with the
        given email.

        The token is valid only for 10 minutes.   The following workflow can be
        used to reset the customer's password:  * Create a password reset token
        and send it embedded in a link to the customer. * When the customer
        clicks on the link, the customer is retrieved with the token. * The
        customer enters a new password and the "reset customer's password"
        endpoint is called.
        """
        params = {}
        return self._client._post(
            endpoint="customers/password-token",
            params=params,
            data_object=action,
            request_schema_cls=schemas.CustomerCreatePasswordResetTokenSchema,
            response_schema_cls=schemas.CustomerTokenSchema,
        )

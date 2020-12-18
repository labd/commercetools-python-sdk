# DO NOT EDIT! This file is automatically generated
import typing

from marshmallow import fields

from commercetools._schemas._cart import (
    CartDraftSchema,
    CartPagedQueryResponseSchema,
    CartSchema,
    CartUpdateSchema,
)
from commercetools._schemas._customer import (
    CustomerChangePasswordSchema,
    CustomerCreateEmailTokenSchema,
    CustomerCreatePasswordResetTokenSchema,
    CustomerDraftSchema,
    CustomerEmailVerifySchema,
    CustomerPagedQueryResponseSchema,
    CustomerResetPasswordSchema,
    CustomerSchema,
    CustomerSignInResultSchema,
    CustomerSigninSchema,
    CustomerTokenSchema,
    CustomerUpdateSchema,
)
from commercetools._schemas._order import (
    OrderFromCartDraftSchema,
    OrderPagedQueryResponseSchema,
    OrderSchema,
    OrderUpdateSchema,
)
from commercetools.helpers import OptionalList, RemoveEmptyValuesMixin
from commercetools.types._cart import (
    Cart,
    CartDraft,
    CartPagedQueryResponse,
    CartUpdate,
    CartUpdateAction,
)
from commercetools.types._customer import (
    Customer,
    CustomerChangePassword,
    CustomerCreateEmailToken,
    CustomerCreatePasswordResetToken,
    CustomerDraft,
    CustomerEmailVerify,
    CustomerPagedQueryResponse,
    CustomerResetPassword,
    CustomerSignin,
    CustomerSignInResult,
    CustomerToken,
    CustomerUpdate,
    CustomerUpdateAction,
)
from commercetools.types._order import (
    Order,
    OrderFromCartDraft,
    OrderPagedQueryResponse,
    OrderUpdate,
    OrderUpdateAction,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _In_StoreQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _In_StoreUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _In_StoreDeleteSchema(
    traits.VersionedSchema, traits.ExpandableSchema, traits.DataErasureSchema
):
    pass


class In_StoreService(abstract.AbstractService):
    def cart_get_by_customer_id(
        self, store_key, customer_id: str, *, expand: OptionalListStr = None
    ) -> Cart:
        """Retrieves the active cart of the customer that has been modified most
        recently in a specific Store.

        The {storeKey} path parameter maps to a Store's key.  If the cart exists
        in the commercetools project but does not have the store field, or the
        store field references a different store, this method returns a
        ResourceNotFound error.  The cart may not contain up-to-date prices,
        discounts etc. If you want to ensure they're up-to-date, send an Update
        request with the Recalculate update action instead.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"in-store/key={store_key}/carts/customer-id={customer_id}",
            params=params,
            schema_cls=CartSchema,
        )

    def cart_get_by_id(
        self, store_key, id: str, *, expand: OptionalListStr = None
    ) -> Cart:
        """Returns a cart by its ID from a specific Store.

        The {storeKey} path parameter maps to a Store's key. If the cart exists
        in the commercetools project but does not have the store field, or the
        store field references a different store, this method returns a
        ResourceNotFound error. The cart may not contain up-to-date prices,
        discounts etc. If you want to ensure they're up-to-date, send an Update
        request with the Recalculate update action instead.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"in-store/key={store_key}/carts/{id}",
            params=params,
            schema_cls=CartSchema,
        )

    def customer_get_by_email_token(
        self, store_key, email_token: str, *, expand: OptionalListStr = None
    ) -> Customer:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"in-store/key={store_key}/customers/email-token={email_token}",
            params=params,
            schema_cls=CustomerSchema,
        )

    def customer_get_by_id(
        self, store_key, id: str, *, expand: OptionalListStr = None
    ) -> Customer:
        """Returns a customer by its ID from a specific Store.

        The {storeKey} path parameter maps to a Store's key. It also considers
        customers that do not have the stores field. If the customer exists in
        the commercetools project but the stores field references different
        stores, this method returns a ResourceNotFound error.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"in-store/key={store_key}/customers/{id}",
            params=params,
            schema_cls=CustomerSchema,
        )

    def customer_get_by_key(
        self, store_key, key: str, *, expand: OptionalListStr = None
    ) -> Customer:
        """Returns a customer by its Key from a specific Store.

        The {storeKey} path parameter maps to a Store's key. It also considers
        customers that do not have the stores field. If the customer exists in
        the commercetools project but the stores field references different
        stores, this method returns a ResourceNotFound error.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"in-store/key={store_key}/customers/key={key}",
            params=params,
            schema_cls=CustomerSchema,
        )

    def customer_get_by_password_token(
        self, store_key, password_token: str, *, expand: OptionalListStr = None
    ) -> Customer:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"in-store/key={store_key}/customers/password-token={password_token}",
            params=params,
            schema_cls=CustomerSchema,
        )

    def order_get_by_id(
        self, store_key, id: str, *, expand: OptionalListStr = None
    ) -> Order:
        """Returns an order by its ID from a specific Store.

        The {storeKey} path parameter maps to a Store's key. If the order exists
        in the commercetools project but does not have the store field, or the
        store field references a different store, this method returns a
        ResourceNotFound error.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"in-store/key={store_key}/orders/{id}",
            params=params,
            schema_cls=OrderSchema,
        )

    def order_get_by_order_number(
        self, store_key, order_number: str, *, expand: OptionalListStr = None
    ) -> Order:
        """Returns an order by its order number from a specific Store.

        The {storeKey} path parameter maps to a Store's key. If the order exists
        in the commercetools project but does not have the store field, or the
        store field references a different store, this method returns a
        ResourceNotFound error. In case the orderNumber does not match the
        regular expression [a-zA-Z0-9_\\-]+, it should be provided in URL-encoded
        format.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"in-store/key={store_key}/orders/order-number={order_number}",
            params=params,
            schema_cls=OrderSchema,
        )

    def cart_query(
        self,
        store_key,
        *,
        expand: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: OptionalListStr = None,
        predicate_var: typing.Dict[str, str] = None,
        customer_id: str = None,
    ) -> CartPagedQueryResponse:
        """Queries carts in a specific Store.

        The {storeKey} path parameter maps to a Store's key.  A shopping cart
        holds product variants and can be ordered.
        """
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "with_total": with_total,
                "where": where,
                "predicate_var": predicate_var,
                "customer_id": customer_id,
            },
            _In_StoreQuerySchema,
        )
        return self._client._get(
            endpoint=f"in-store/key={store_key}/carts",
            params=params,
            schema_cls=CartPagedQueryResponseSchema,
        )

    def customer_query(
        self,
        store_key,
        *,
        expand: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: OptionalListStr = None,
        predicate_var: typing.Dict[str, str] = None,
    ) -> CustomerPagedQueryResponse:
        """A customer is a person purchasing products. customers, Orders, Comments
        and Reviews can be associated to a customer.
        """
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "with_total": with_total,
                "where": where,
                "predicate_var": predicate_var,
            },
            _In_StoreQuerySchema,
        )
        return self._client._get(
            endpoint=f"in-store/key={store_key}/customers",
            params=params,
            schema_cls=CustomerPagedQueryResponseSchema,
        )

    def order_query(
        self,
        store_key,
        *,
        expand: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: OptionalListStr = None,
        predicate_var: typing.Dict[str, str] = None,
    ) -> OrderPagedQueryResponse:
        """Queries orders in a specific Store.

        The {storeKey} path parameter maps to a Store's key.  An order can be
        created from a cart, usually after a checkout process has been completed.
        """
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "with_total": with_total,
                "where": where,
                "predicate_var": predicate_var,
            },
            _In_StoreQuerySchema,
        )
        return self._client._get(
            endpoint=f"in-store/key={store_key}/orders",
            params=params,
            schema_cls=OrderPagedQueryResponseSchema,
        )

    def cart_create(
        self, store_key, draft: CartDraft, *, expand: OptionalListStr = None
    ) -> Cart:
        """Creates a cart in the store specified by {storeKey}.

        The {storeKey} path parameter maps to a Store's key. When using this
        endpoint the cart's store field is always set to the store specified in
        the path parameter. Creating a cart can fail with an InvalidOperation if
        the referenced shipping method in the CartDraft has a predicate which
        does not match the cart.   A shopping cart holds product variants and can
        be ordered.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint=f"in-store/key={store_key}/carts",
            params=params,
            data_object=draft,
            request_schema_cls=CartDraftSchema,
            response_schema_cls=CartSchema,
        )

    def customer_create(
        self, store_key, draft: CustomerDraft, *, expand: OptionalListStr = None
    ) -> CustomerSignInResult:
        """Creates a customer in a specific Store.

        The {storeKey} path parameter maps to a Store's key. When using this
        endpoint, if omitted, the customer's stores field is set to the store
        specified in the path parameter. If an anonymous cart is passed in as
        when using this method, then the cart is assigned to the created customer
        and the version number of the Cart increases. If the ID of an anonymous
        session is given, all carts and orders will be assigned to the created
        customer and the store specified. If you pass in a cart with a store
        field specified, the store field must reference the same store specified
        in the {storeKey} path parameter.   A customer is a person purchasing
        products. customers, Orders, Comments and Reviews can be associated to a
        customer.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint=f"in-store/key={store_key}/customers",
            params=params,
            data_object=draft,
            request_schema_cls=CustomerDraftSchema,
            response_schema_cls=CustomerSignInResultSchema,
        )

    def order_create(
        self, store_key, draft: OrderFromCartDraft, *, expand: OptionalListStr = None
    ) -> Order:
        """Creates an order from a Cart from a specific Store.

        The {storeKey} path parameter maps to a Store's key. When using this
        endpoint the orders's store field is always set to the store specified in
        the path parameter. The cart must have a shipping address set before
        creating an order. When using the Platform TaxMode, the shipping address
        is used for tax calculation.   An order can be created from a cart,
        usually after a checkout process has been completed.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint=f"in-store/key={store_key}/orders",
            params=params,
            data_object=draft,
            request_schema_cls=OrderFromCartDraftSchema,
            response_schema_cls=OrderSchema,
        )

    def cart_update_by_id(
        self,
        store_key,
        id: str,
        version: int,
        actions: typing.List[CartUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Cart:
        """Updates a cart in the store specified by {storeKey}.

        The {storeKey} path parameter maps to a Store's key. If the cart exists
        in the commercetools project but does not have the store field, or the
        store field references a different store, this method returns a
        ResourceNotFound error.
        """
        params = self._serialize_params({"expand": expand}, _In_StoreUpdateSchema)
        update_action = CartUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"in-store/key={store_key}/carts/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=CartUpdateSchema,
            response_schema_cls=CartSchema,
            force_update=force_update,
        )

    def customer_update_by_id(
        self,
        store_key,
        id: str,
        version: int,
        actions: typing.List[CustomerUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Customer:
        """Updates a customer in the store specified by {storeKey}.

        The {storeKey} path parameter maps to a Store's key. If the customer
        exists in the commercetools project but the stores field references a
        different store, this method returns a ResourceNotFound error.
        """
        params = self._serialize_params({"expand": expand}, _In_StoreUpdateSchema)
        update_action = CustomerUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"in-store/key={store_key}/customers/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=CustomerUpdateSchema,
            response_schema_cls=CustomerSchema,
            force_update=force_update,
        )

    def customer_update_by_key(
        self,
        store_key,
        key: str,
        version: int,
        actions: typing.List[CustomerUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Customer:
        """If the customer exists in the commercetools project but the stores
        field references a different store,

        this method returns a ResourceNotFound error.
        """
        params = self._serialize_params({"expand": expand}, _In_StoreUpdateSchema)
        update_action = CustomerUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"in-store/key={store_key}/customers/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=CustomerUpdateSchema,
            response_schema_cls=CustomerSchema,
            force_update=force_update,
        )

    def order_update_by_id(
        self,
        store_key,
        id: str,
        version: int,
        actions: typing.List[OrderUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Order:
        """Updates an order in the store specified by {storeKey}.

        The {storeKey} path parameter maps to a Store's key. If the order exists
        in the commercetools project but does not have the store field, or the
        store field references a different store, this method returns a
        ResourceNotFound error.
        """
        params = self._serialize_params({"expand": expand}, _In_StoreUpdateSchema)
        update_action = OrderUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"in-store/key={store_key}/orders/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=OrderUpdateSchema,
            response_schema_cls=OrderSchema,
            force_update=force_update,
        )

    def order_update_by_order_number(
        self,
        store_key,
        order_number: str,
        version: int,
        actions: typing.List[OrderUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Order:
        """Updates an order in the store specified by {storeKey}.

        The {storeKey} path parameter maps to a Store's key. If the order exists
        in the commercetools project but does not have the store field, or the
        store field references a different store, this method returns a
        ResourceNotFound error. In case the orderNumber does not match the
        regular expression [a-zA-Z0-9_\\-]+, it should be provided in URL-encoded
        format.
        """
        params = self._serialize_params({"expand": expand}, _In_StoreUpdateSchema)
        update_action = OrderUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"in-store/key={store_key}/orders/order-number={order_number}",
            params=params,
            data_object=update_action,
            request_schema_cls=OrderUpdateSchema,
            response_schema_cls=OrderSchema,
            force_update=force_update,
        )

    def cart_delete_by_id(
        self,
        store_key,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> Cart:
        params = self._serialize_params(
            {"version": version, "expand": expand, "data_erasure": data_erasure},
            _In_StoreDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"in-store/key={store_key}/carts/{id}",
            params=params,
            response_schema_cls=CartSchema,
            force_delete=force_delete,
        )

    def customer_delete_by_id(
        self,
        store_key,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> Customer:
        params = self._serialize_params(
            {"version": version, "expand": expand, "data_erasure": data_erasure},
            _In_StoreDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"in-store/key={store_key}/customers/{id}",
            params=params,
            response_schema_cls=CustomerSchema,
            force_delete=force_delete,
        )

    def customer_delete_by_key(
        self,
        store_key,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> Customer:
        params = self._serialize_params(
            {"version": version, "expand": expand, "data_erasure": data_erasure},
            _In_StoreDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"in-store/key={store_key}/customers/key={key}",
            params=params,
            response_schema_cls=CustomerSchema,
            force_delete=force_delete,
        )

    def order_delete_by_id(
        self,
        store_key,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> Order:
        params = self._serialize_params(
            {"version": version, "expand": expand, "data_erasure": data_erasure},
            _In_StoreDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"in-store/key={store_key}/orders/{id}",
            params=params,
            response_schema_cls=OrderSchema,
            force_delete=force_delete,
        )

    def order_delete_by_order_number(
        self,
        store_key,
        order_number: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> Order:
        params = self._serialize_params(
            {"version": version, "expand": expand, "data_erasure": data_erasure},
            _In_StoreDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"in-store/key={store_key}/orders/order-number={order_number}",
            params=params,
            response_schema_cls=OrderSchema,
            force_delete=force_delete,
        )

    def customer_email_confirm(self, action: CustomerEmailVerify) -> Customer:
        """Verifies customer's email using a token."""
        params: typing.Dict[str, str] = {}
        return self._client._post(
            endpoint=f"in-store/key={store_key}/customers/email/confirm",
            params=params,
            data_object=action,
            request_schema_cls=CustomerEmailVerifySchema,
            response_schema_cls=CustomerSchema,
        )

    def customer_email_token(self, action: CustomerCreateEmailToken) -> CustomerToken:
        """Create a Token for verifying the Customer's Email in store

        To verify a customer's email, an email token can be created. This should
        be embedded in a link and sent to the customer via email. When the
        customer clicks on the link, the "verify customer's email" endpoint
        should be called, which sets customer's isVerifiedEmail field to true.
        """
        params: typing.Dict[str, str] = {}
        return self._client._post(
            endpoint=f"in-store/key={store_key}/customers/email-token",
            params=params,
            data_object=action,
            request_schema_cls=CustomerCreateEmailTokenSchema,
            response_schema_cls=CustomerTokenSchema,
        )

    def customer_password(self, action: CustomerChangePassword) -> Customer:
        """Change a customers password"""
        params: typing.Dict[str, str] = {}
        return self._client._post(
            endpoint=f"in-store/key={store_key}/customers/password",
            params=params,
            data_object=action,
            request_schema_cls=CustomerChangePasswordSchema,
            response_schema_cls=CustomerSchema,
        )

    def customer_password_reset(self, action: CustomerResetPassword) -> Customer:
        """Set a new password using a token."""
        params: typing.Dict[str, str] = {}
        return self._client._post(
            endpoint=f"in-store/key={store_key}/customers/password/reset",
            params=params,
            data_object=action,
            request_schema_cls=CustomerResetPasswordSchema,
            response_schema_cls=CustomerSchema,
        )

    def customer_password_token(
        self, action: CustomerCreatePasswordResetToken
    ) -> CustomerToken:
        """The token value is used to reset the password of the customer with the
        given email.

        The token is valid only for 10 minutes.   The following workflow can be
        used to reset the customer's password:  * Create a password reset token
        and send it embedded in a link to the customer. * When the customer
        clicks on the link, the customer is retrieved with the token. * The
        customer enters a new password and the "reset customer's password"
        endpoint is called.
        """
        params: typing.Dict[str, str] = {}
        return self._client._post(
            endpoint=f"in-store/key={store_key}/customers/password-token",
            params=params,
            data_object=action,
            request_schema_cls=CustomerCreatePasswordResetTokenSchema,
            response_schema_cls=CustomerTokenSchema,
        )

    def login(self, action: CustomerSignin) -> CustomerSignInResult:
        """Authenticate Customer (Sign In) in store

        Retrieves the authenticated customer.
        """
        params: typing.Dict[str, str] = {}
        return self._client._post(
            endpoint=f"in-store/key={store_key}/login",
            params=params,
            data_object=action,
            request_schema_cls=CustomerSigninSchema,
            response_schema_cls=CustomerSignInResultSchema,
        )

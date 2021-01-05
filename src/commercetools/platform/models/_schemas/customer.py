# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from ..customer import AnonymousCartSignInMode
from .common import BaseResourceSchema, ReferenceSchema, ResourceIdentifierSchema
from .type import FieldContainerField

# Fields


# Marshmallow Schemas


class CustomerSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="createdBy",
    )
    customer_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerNumber"
    )
    email = marshmallow.fields.String(allow_none=True, missing=None)
    password = marshmallow.fields.String(allow_none=True, missing=None)
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )
    middle_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="middleName"
    )
    title = marshmallow.fields.String(allow_none=True, missing=None)
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )
    vat_id = marshmallow.fields.String(allow_none=True, missing=None, data_key="vatId")
    addresses = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    default_shipping_address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="defaultShippingAddressId"
    )
    shipping_address_ids = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="shippingAddressIds",
    )
    default_billing_address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="defaultBillingAddressId"
    )
    billing_address_ids = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="billingAddressIds",
    )
    is_email_verified = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isEmailVerified"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    salutation = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    stores = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreKeyReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Customer(**data)


class CustomerChangePasswordSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    current_password = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="currentPassword"
    )
    new_password = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="newPassword"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerChangePassword(**data)


class CustomerCreateEmailTokenSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    ttl_minutes = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="ttlMinutes"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerCreateEmailToken(**data)


class CustomerCreatePasswordResetTokenSchema(marshmallow.Schema):
    email = marshmallow.fields.String(allow_none=True, missing=None)
    ttl_minutes = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="ttlMinutes"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerCreatePasswordResetToken(**data)


class CustomerDraftSchema(marshmallow.Schema):
    customer_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerNumber"
    )
    email = marshmallow.fields.String(allow_none=True, missing=None)
    password = marshmallow.fields.String(allow_none=True, missing=None)
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )
    middle_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="middleName"
    )
    title = marshmallow.fields.String(allow_none=True, missing=None)
    anonymous_cart_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousCartId"
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )
    vat_id = marshmallow.fields.String(allow_none=True, missing=None, data_key="vatId")
    addresses = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    default_shipping_address = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="defaultShippingAddress"
    )
    shipping_addresses = marshmallow.fields.List(
        marshmallow.fields.Integer(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="shippingAddresses",
    )
    default_billing_address = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="defaultBillingAddress"
    )
    billing_addresses = marshmallow.fields.List(
        marshmallow.fields.Integer(allow_none=True),
        allow_none=True,
        missing=None,
        data_key="billingAddresses",
    )
    is_email_verified = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isEmailVerified"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".customer_group.CustomerGroupResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    salutation = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    stores = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreResourceIdentifierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerDraft(**data)


class CustomerEmailVerifySchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    token_value = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="tokenValue"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerEmailVerify(**data)


class CustomerPagedQueryResponseSchema(marshmallow.Schema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomerSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerPagedQueryResponse(**data)


class CustomerReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomerSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CustomerReference(**data)


class CustomerResetPasswordSchema(marshmallow.Schema):
    token_value = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="tokenValue"
    )
    new_password = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="newPassword"
    )
    version = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerResetPassword(**data)


class CustomerResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.CustomerResourceIdentifier(**data)


class CustomerSignInResultSchema(marshmallow.Schema):
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomerSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    cart = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerSignInResult(**data)


class CustomerSigninSchema(marshmallow.Schema):
    email = marshmallow.fields.String(allow_none=True, missing=None)
    password = marshmallow.fields.String(allow_none=True, missing=None)
    anonymous_cart_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousCartId"
    )
    anonymous_cart_sign_in_mode = marshmallow_enum.EnumField(
        AnonymousCartSignInMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="anonymousCartSignInMode",
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )
    update_product_data = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="updateProductData"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerSignin(**data)


class CustomerTokenSchema(marshmallow.Schema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    created_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="createdAt"
    )
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="lastModifiedAt"
    )
    customer_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerId"
    )
    expires_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="expiresAt"
    )
    value = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerToken(**data)


class CustomerUpdateSchema(marshmallow.Schema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addAddress": helpers.absmod(
                    __name__, ".CustomerAddAddressActionSchema"
                ),
                "addBillingAddressId": helpers.absmod(
                    __name__, ".CustomerAddBillingAddressIdActionSchema"
                ),
                "addShippingAddressId": helpers.absmod(
                    __name__, ".CustomerAddShippingAddressIdActionSchema"
                ),
                "addStore": helpers.absmod(__name__, ".CustomerAddStoreActionSchema"),
                "changeAddress": helpers.absmod(
                    __name__, ".CustomerChangeAddressActionSchema"
                ),
                "changeEmail": helpers.absmod(
                    __name__, ".CustomerChangeEmailActionSchema"
                ),
                "removeAddress": helpers.absmod(
                    __name__, ".CustomerRemoveAddressActionSchema"
                ),
                "removeBillingAddressId": helpers.absmod(
                    __name__, ".CustomerRemoveBillingAddressIdActionSchema"
                ),
                "removeShippingAddressId": helpers.absmod(
                    __name__, ".CustomerRemoveShippingAddressIdActionSchema"
                ),
                "removeStore": helpers.absmod(
                    __name__, ".CustomerRemoveStoreActionSchema"
                ),
                "setCompanyName": helpers.absmod(
                    __name__, ".CustomerSetCompanyNameActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".CustomerSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".CustomerSetCustomTypeActionSchema"
                ),
                "setCustomerGroup": helpers.absmod(
                    __name__, ".CustomerSetCustomerGroupActionSchema"
                ),
                "setCustomerNumber": helpers.absmod(
                    __name__, ".CustomerSetCustomerNumberActionSchema"
                ),
                "setDateOfBirth": helpers.absmod(
                    __name__, ".CustomerSetDateOfBirthActionSchema"
                ),
                "setDefaultBillingAddress": helpers.absmod(
                    __name__, ".CustomerSetDefaultBillingAddressActionSchema"
                ),
                "setDefaultShippingAddress": helpers.absmod(
                    __name__, ".CustomerSetDefaultShippingAddressActionSchema"
                ),
                "setExternalId": helpers.absmod(
                    __name__, ".CustomerSetExternalIdActionSchema"
                ),
                "setFirstName": helpers.absmod(
                    __name__, ".CustomerSetFirstNameActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".CustomerSetKeyActionSchema"),
                "setLastName": helpers.absmod(
                    __name__, ".CustomerSetLastNameActionSchema"
                ),
                "setLocale": helpers.absmod(__name__, ".CustomerSetLocaleActionSchema"),
                "setMiddleName": helpers.absmod(
                    __name__, ".CustomerSetMiddleNameActionSchema"
                ),
                "setSalutation": helpers.absmod(
                    __name__, ".CustomerSetSalutationActionSchema"
                ),
                "setStores": helpers.absmod(__name__, ".CustomerSetStoresActionSchema"),
                "setTitle": helpers.absmod(__name__, ".CustomerSetTitleActionSchema"),
                "setVatId": helpers.absmod(__name__, ".CustomerSetVatIdActionSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerUpdate(**data)


class CustomerUpdateActionSchema(marshmallow.Schema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerUpdateAction(**data)


class CustomerAddAddressActionSchema(CustomerUpdateActionSchema):
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerAddAddressAction(**data)


class CustomerAddBillingAddressIdActionSchema(CustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerAddBillingAddressIdAction(**data)


class CustomerAddShippingAddressIdActionSchema(CustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerAddShippingAddressIdAction(**data)


class CustomerAddStoreActionSchema(CustomerUpdateActionSchema):
    store = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerAddStoreAction(**data)


class CustomerChangeAddressActionSchema(CustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )
    address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerChangeAddressAction(**data)


class CustomerChangeEmailActionSchema(CustomerUpdateActionSchema):
    email = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerChangeEmailAction(**data)


class CustomerRemoveAddressActionSchema(CustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerRemoveAddressAction(**data)


class CustomerRemoveBillingAddressIdActionSchema(CustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerRemoveBillingAddressIdAction(**data)


class CustomerRemoveShippingAddressIdActionSchema(CustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerRemoveShippingAddressIdAction(**data)


class CustomerRemoveStoreActionSchema(CustomerUpdateActionSchema):
    store = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerRemoveStoreAction(**data)


class CustomerSetCompanyNameActionSchema(CustomerUpdateActionSchema):
    company_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="companyName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetCompanyNameAction(**data)


class CustomerSetCustomFieldActionSchema(CustomerUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetCustomFieldAction(**data)


class CustomerSetCustomTypeActionSchema(CustomerUpdateActionSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetCustomTypeAction(**data)


class CustomerSetCustomerGroupActionSchema(CustomerUpdateActionSchema):
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".customer_group.CustomerGroupResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customerGroup",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetCustomerGroupAction(**data)


class CustomerSetCustomerNumberActionSchema(CustomerUpdateActionSchema):
    customer_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="customerNumber"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetCustomerNumberAction(**data)


class CustomerSetDateOfBirthActionSchema(CustomerUpdateActionSchema):
    date_of_birth = marshmallow.fields.Date(
        allow_none=True, missing=None, data_key="dateOfBirth"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetDateOfBirthAction(**data)


class CustomerSetDefaultBillingAddressActionSchema(CustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetDefaultBillingAddressAction(**data)


class CustomerSetDefaultShippingAddressActionSchema(CustomerUpdateActionSchema):
    address_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressId"
    )
    address_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="addressKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetDefaultShippingAddressAction(**data)


class CustomerSetExternalIdActionSchema(CustomerUpdateActionSchema):
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetExternalIdAction(**data)


class CustomerSetFirstNameActionSchema(CustomerUpdateActionSchema):
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetFirstNameAction(**data)


class CustomerSetKeyActionSchema(CustomerUpdateActionSchema):
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetKeyAction(**data)


class CustomerSetLastNameActionSchema(CustomerUpdateActionSchema):
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetLastNameAction(**data)


class CustomerSetLocaleActionSchema(CustomerUpdateActionSchema):
    locale = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetLocaleAction(**data)


class CustomerSetMiddleNameActionSchema(CustomerUpdateActionSchema):
    middle_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="middleName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetMiddleNameAction(**data)


class CustomerSetSalutationActionSchema(CustomerUpdateActionSchema):
    salutation = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetSalutationAction(**data)


class CustomerSetStoresActionSchema(CustomerUpdateActionSchema):
    stores = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreResourceIdentifierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetStoresAction(**data)


class CustomerSetTitleActionSchema(CustomerUpdateActionSchema):
    title = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetTitleAction(**data)


class CustomerSetVatIdActionSchema(CustomerUpdateActionSchema):
    vat_id = marshmallow.fields.String(allow_none=True, missing=None, data_key="vatId")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.CustomerSetVatIdAction(**data)

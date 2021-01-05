# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from .common import ImportResourceSchema

# Fields


# Marshmallow Schemas
class CustomerImportSchema(ImportResourceSchema):
    customer_number = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customerNumber",
    )
    email = marshmallow.fields.String(allow_none=True, missing=None)
    password = marshmallow.fields.String(allow_none=True, missing=None)
    first_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="firstName",
    )
    last_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="lastName",
    )
    middle_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="middleName",
    )
    title = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    salutation = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    external_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="externalId",
    )
    date_of_birth = marshmallow.fields.Date(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="dateOfBirth",
    )
    company_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="companyName",
    )
    vat_id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None, data_key="vatId"
    )
    is_email_verified = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="isEmailVerified",
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CustomerGroupKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customerGroup",
    )
    addresses = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    default_billing_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="defaultBillingAddress",
    )
    billing_addresses = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="billingAddresses",
    )
    default_shipping_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="defaultShippingAddress",
    )
    shipping_addresses = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingAddresses",
    )
    locale = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customfields.CustomSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerImport(**data)

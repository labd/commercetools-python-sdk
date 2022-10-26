# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen

import datetime
import enum
import typing

from ._abstract import _BaseType

__all__ = ["Amount", "PaymentAction", "PaymentOperation", "Region"]


class Region(enum.Enum):
    """The Region in which the Checkout application is [hosted](/../checkout/installing-checkout#regions-and-hosts)."""

    EUROPE_WEST1.GCP = "europe-west1.gcp"
    US_CENTRAL1.GCP = "us-central1.gcp"
    AUSTRALIA_SOUTHEAST1.GCP = "australia-southeast1.gcp"


class Amount(_BaseType):
    """The amount related to a [payment action](ctp:checkout:type:PaymentAction)."""

    #: Amount in the smallest indivisible unit of a currency, such as:
    #:
    #: * Cents for EUR and USD, pence for GBP, or centime for CHF (5 CHF is specified as `500`).
    #: * The value in the major unit for currencies without minor units, like JPY (5 JPY is specified as `5`).
    cent_amount: int
    #: Currency code compliant to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).
    currency_code: str

    def __init__(self, *, cent_amount: int, currency_code: str):
        self.cent_amount = cent_amount
        self.currency_code = currency_code

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Amount":
        from ._schemas.common import AmountSchema

        return AmountSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import AmountSchema

        return AmountSchema().dump(self)


class PaymentOperation(enum.Enum):
    """The possible values for a [payment action](ctp:checkout:type:PaymentAction)."""

    CAPTURE_PAYMENT = "capturePayment"
    REFUND_PAYMENT = "refundPayment"
    CANCEL_PAYMENT = "cancelPayment"


class PaymentAction(_BaseType):
    """Depending on the action specified, Checkout requests the [payment service provider](/../checkout/configuring-checkout#supported-psps) (PSP) to capture, refund, or cancel the authorization for the given Payment."""

    #: Action to execute for the given Payment.
    action: "PaymentOperation"
    #: Amount to be captured or refunded.
    amount: typing.Optional["Amount"]

    def __init__(
        self, *, action: "PaymentOperation", amount: typing.Optional["Amount"] = None
    ):
        self.action = action
        self.amount = amount

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PaymentAction":
        from ._schemas.common import PaymentActionSchema

        return PaymentActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import PaymentActionSchema

        return PaymentActionSchema().dump(self)
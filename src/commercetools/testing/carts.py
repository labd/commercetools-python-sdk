import copy
import datetime
import typing
import uuid

from commercetools import schemas, types
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import set_custom_field


class CartsModel(BaseModel):
    _resource_schema = schemas.CartSchema
    _primary_type_name = "cart"

    def _create_line_item_from_draft(
        self, draft: types.CartDraft, line_item_draft: types.LineItemDraft
    ) -> types.LineItem:
        line_id = str(uuid.uuid4())
        price = 1000
        return types.LineItem(
            id=line_id,
            name=types.LocalizedString({"en": line_id}),
            price=types.Price(
                value=types.CentPrecisionMoney(
                    currency_code=draft.currency, cent_amount=price
                )
            ),
            taxed_price=types.TaxedItemPrice(
                total_net=types.CentPrecisionMoney(
                    currency_code=draft.currency,
                    cent_amount=price * (line_item_draft.quantity or 0),
                    fraction_digits=2,
                ),
                total_gross=types.CentPrecisionMoney(
                    currency_code=draft.currency,
                    cent_amount=price * (line_item_draft.quantity or 0),
                    fraction_digits=2,
                ),
            ),
            total_price=types.CentPrecisionMoney(
                currency_code=draft.currency,
                cent_amount=price * (line_item_draft.quantity or 0),
            ),
            quantity=line_item_draft.quantity,
            price_mode=types.LineItemPriceMode.PLATFORM,
            line_item_mode=types.LineItemMode.STANDARD,
            custom=utils.create_from_draft(line_item_draft.custom),
        )

    def _create_from_draft(
        self, draft: types.CartDraft, id: typing.Optional[str] = None
    ) -> types.Cart:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        line_items = [
            self._create_line_item_from_draft(draft, line_item)
            for line_item in draft.line_items
        ]
        total_price = None
        taxed_price = None
        if line_items:

            total_price = types.CentPrecisionMoney(
                currency_code=draft.currency,
                cent_amount=sum(
                    line_item.taxed_price.total_gross.cent_amount
                    for line_item in line_items
                    if line_item.taxed_price and line_item.taxed_price.total_gross
                ),
                fraction_digits=2,
            )
            taxed_price = types.TaxedPrice(
                total_net=types.CentPrecisionMoney(
                    currency_code=draft.currency,
                    cent_amount=sum(
                        line_item.taxed_price.total_net.cent_amount
                        for line_item in line_items
                        if line_item.taxed_price and line_item.taxed_price.total_net
                    ),
                ),
                total_gross=types.CentPrecisionMoney(
                    currency_code=draft.currency,
                    cent_amount=sum(
                        line_item.taxed_price.total_gross.cent_amount
                        for line_item in line_items
                        if line_item.taxed_price and line_item.taxed_price.total_gross
                    ),
                ),
                tax_portions=[
                    types.TaxPortion(
                        name="0% VAT",
                        amount=types.CentPrecisionMoney(
                            currency_code=draft.currency, cent_amount=0
                        ),
                    )
                ],
            )

        # Some fields such as itemShippingAddresses are currently missing. See
        # https://docs.commercetools.com/http-api-projects-carts for a complete overview
        return types.Cart(
            id=str(object_id),
            version=1,
            cart_state=types.CartState.ACTIVE,
            customer_id=draft.customer_id,
            customer_email=draft.customer_email,
            customer_group=draft.customer_group,
            anonymous_id=draft.anonymous_id,
            country=draft.country,
            inventory_mode=draft.inventory_mode,
            tax_mode=draft.tax_mode,
            tax_rounding_mode=draft.tax_rounding_mode,
            tax_calculation_mode=draft.tax_calculation_mode,
            line_items=line_items,
            shipping_address=draft.shipping_address,
            billing_address=draft.billing_address,
            locale=draft.locale,
            origin=draft.origin,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            custom=utils.create_from_draft(draft.custom),
            total_price=total_price,
            taxed_price=taxed_price,
        )


def add_payment():
    def updater(self, obj, action):
        value = getattr(action, "payment")
        value = schemas.PaymentResourceIdentifierSchema().dump(value)
        if not obj["paymentInfo"]:
            obj["paymentInfo"] = schemas.PaymentInfoSchema().dump(
                types.PaymentInfo(payments=[])
            )
        if value not in obj["paymentInfo"]["payments"]:
            new = copy.deepcopy(obj)
            new["paymentInfo"]["payments"].append(value)
            return new
        return obj

    return updater


class CartsBackend(ServiceBackend):
    service_path = "carts"
    model_class = CartsModel
    _schema_draft = schemas.CartDraftSchema
    _schema_update = schemas.CartUpdateSchema
    _schema_query_response = schemas.CartPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]

    _actions = {"addPayment": add_payment(), "setCustomField": set_custom_field()}

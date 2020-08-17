import copy
import datetime
import typing
import uuid

from commercetools import types
from commercetools._schemas._cart import (
    CartDraftSchema,
    CartPagedQueryResponseSchema,
    CartSchema,
    CartUpdateSchema,
)
from commercetools._schemas._order import PaymentInfoSchema
from commercetools._schemas._payment import PaymentResourceIdentifierSchema
from commercetools._schemas._product import ProductSchema
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class CartsModel(BaseModel):
    _resource_schema = CartSchema
    _primary_type_name = "cart"

    def _create_line_item_from_draft(
        self, draft: types.CartDraft, line_item_draft: types.LineItemDraft
    ) -> types.LineItem:
        line_id = str(uuid.uuid4())
        price = 1000

        product_data = self._storage.get_by_resource_identifier(
            types.ProductResourceIdentifier(id=line_item_draft.product_id)
        )
        product: types.Product = ProductSchema().load(product_data)

        variant = None
        for v in product.master_data.current.variants:
            if v.id == line_item_draft.variant_id:
                variant = v

        return types.LineItem(
            id=line_id,
            name=types.LocalizedString({"en": line_id}),
            product_id=line_item_draft.product_id,
            product_type=product.product_type,
            variant=variant,
            price=types.Price(
                id=str(uuid.uuid4()),
                value=types.CentPrecisionMoney(
                    currency_code=draft.currency, cent_amount=price, fraction_digits=2
                ),
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
                fraction_digits=2,
            ),
            quantity=line_item_draft.quantity,
            discounted_price_per_quantity=[],
            state=[],
            price_mode=types.LineItemPriceMode.PLATFORM,
            line_item_mode=types.LineItemMode.STANDARD,
            custom=utils.create_from_draft(line_item_draft.custom),
        )

    def _create_from_draft(
        self, draft: types.CartDraft, id: typing.Optional[str] = None
    ) -> types.Cart:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        if draft.line_items:
            line_items = [
                self._create_line_item_from_draft(draft, line_item)
                for line_item in draft.line_items
            ]
        else:
            line_items = []

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
                    fraction_digits=2,
                ),
                total_gross=types.CentPrecisionMoney(
                    currency_code=draft.currency,
                    cent_amount=sum(
                        line_item.taxed_price.total_gross.cent_amount
                        for line_item in line_items
                        if line_item.taxed_price and line_item.taxed_price.total_gross
                    ),
                    fraction_digits=2,
                ),
                tax_portions=[
                    types.TaxPortion(
                        name="0% VAT",
                        rate=0,
                        amount=types.CentPrecisionMoney(
                            currency_code=draft.currency,
                            cent_amount=0,
                            fraction_digits=2,
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
            tax_mode=draft.tax_mode or types.TaxMode.PLATFORM,
            tax_rounding_mode=draft.tax_rounding_mode or types.RoundingMode.HALF_EVEN,
            tax_calculation_mode=draft.tax_calculation_mode
            or types.TaxCalculationMode.LINE_ITEM_LEVEL,
            line_items=line_items,
            custom_line_items=[],
            refused_gifts=[],
            shipping_address=draft.shipping_address,
            billing_address=draft.billing_address,
            locale=draft.locale,
            origin=draft.origin or types.CartOrigin.CUSTOMER,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            custom=utils.create_from_draft(draft.custom),
            total_price=total_price,
            taxed_price=taxed_price,
        )


def add_payment():
    def updater(self, obj, action):
        value = getattr(action, "payment")
        value = PaymentResourceIdentifierSchema().dump(value)
        if not obj["paymentInfo"]:
            obj["paymentInfo"] = PaymentInfoSchema().dump(
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
    _schema_draft = CartDraftSchema
    _schema_update = CartUpdateSchema
    _schema_query_response = CartPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]

    def set_custom_field(self, obj, action: types.CartSetCustomFieldAction):
        if not obj["custom"]:
            raise ValueError(
                "This resource has no custom type set - please use "
                "setCustomType first to set the type of the custom fields"
            )

        name = action.name
        value = action.value

        # real API always increments version, so always apply new value.
        new = copy.deepcopy(obj)
        new["custom"]["fields"][name] = value
        return new

    def set_custom_type(self, obj, action: types.CartSetCustomTypeAction):
        custom_type = self.model._storage.get_by_resource_identifier(action.type)

        # real API always increments version, so always apply new value.
        new = copy.deepcopy(obj)
        new["custom"] = {
            "type": {"id": custom_type["id"], "typeId": "type"},
            "fields": {},
        }
        return new

    _actions = {
        "addPayment": add_payment(),
        "setCustomField": set_custom_field,
        "setCustomType": set_custom_type,
    }

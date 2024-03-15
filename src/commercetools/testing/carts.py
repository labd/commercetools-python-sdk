import copy
import datetime
import typing
import uuid

from commercetools.platform import models
from commercetools.platform.models._schemas.cart import (
    CartDraftSchema,
    CartPagedQueryResponseSchema,
    CartSchema,
    CartUpdateSchema,
)
from commercetools.platform.models._schemas.order import PaymentInfoSchema
from commercetools.platform.models._schemas.payment import (
    PaymentResourceIdentifierSchema,
)
from commercetools.platform.models._schemas.product import ProductSchema
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class CartsModel(BaseModel):
    _resource_schema = CartSchema
    _primary_type_name = "cart"

    def _create_line_item_from_draft(
        self, draft: models.CartDraft, line_item_draft: models.LineItemDraft
    ) -> models.LineItem:
        line_id = str(uuid.uuid4())
        price = 1000

        product_data = self._storage.get_by_resource_identifier(
            models.ProductResourceIdentifier(id=line_item_draft.product_id)
        )
        product: models.Product = ProductSchema().load(product_data)

        variant = None
        for v in product.master_data.current.variants:
            if v.id == line_item_draft.variant_id:
                variant = v

        return models.LineItem(
            id=line_id,
            name=models.LocalizedString({"en": line_id}),
            product_id=line_item_draft.product_id,
            product_type=product.product_type,
            variant=variant,
            price=models.Price(
                id=str(uuid.uuid4()),
                value=models.CentPrecisionMoney(
                    currency_code=draft.currency, cent_amount=price, fraction_digits=2
                ),
            ),
            taxed_price=models.TaxedItemPrice(
                total_net=models.CentPrecisionMoney(
                    currency_code=draft.currency,
                    cent_amount=price * (line_item_draft.quantity or 0),
                    fraction_digits=2,
                ),
                total_gross=models.CentPrecisionMoney(
                    currency_code=draft.currency,
                    cent_amount=price * (line_item_draft.quantity or 0),
                    fraction_digits=2,
                ),
                tax_portions=[]
            ),
            taxed_price_portions=[],
            per_method_tax_rate=[],
            total_price=models.CentPrecisionMoney(
                currency_code=draft.currency,
                cent_amount=price * (line_item_draft.quantity or 0),
                fraction_digits=2,
            ),
            quantity=line_item_draft.quantity or 1,
            discounted_price_per_quantity=[],
            state=[],
            price_mode=models.LineItemPriceMode.PLATFORM,
            line_item_mode=models.LineItemMode.STANDARD,
            custom=utils.create_from_draft(line_item_draft.custom),
        )

    def _create_from_draft(
        self, draft: models.CartDraft, id: typing.Optional[str] = None
    ) -> models.Cart:
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
            total_price = models.CentPrecisionMoney(
                currency_code=draft.currency,
                cent_amount=sum(
                    line_item.taxed_price.total_gross.cent_amount
                    for line_item in line_items
                    if line_item.taxed_price and line_item.taxed_price.total_gross
                ),
                fraction_digits=2,
            )
            taxed_price = models.TaxedPrice(
                total_net=models.CentPrecisionMoney(
                    currency_code=draft.currency,
                    cent_amount=sum(
                        line_item.taxed_price.total_net.cent_amount
                        for line_item in line_items
                        if line_item.taxed_price and line_item.taxed_price.total_net
                    ),
                    fraction_digits=2,
                ),
                total_gross=models.CentPrecisionMoney(
                    currency_code=draft.currency,
                    cent_amount=sum(
                        line_item.taxed_price.total_gross.cent_amount
                        for line_item in line_items
                        if line_item.taxed_price and line_item.taxed_price.total_gross
                    ),
                    fraction_digits=2,
                ),
                tax_portions=[
                    models.TaxPortion(
                        name="0% VAT",
                        rate=0,
                        amount=models.CentPrecisionMoney(
                            currency_code=draft.currency,
                            cent_amount=0,
                            fraction_digits=2,
                        ),
                    )
                ],
            )

        # Some fields such as itemShippingAddresses are currently missing. See
        # https://docs.commercetools.com/http-api-projects-carts for a complete overview
        return models.Cart(
            id=str(object_id),
            key=None,
            version=1,
            cart_state=models.CartState.ACTIVE,
            customer_id=draft.customer_id,
            customer_email=draft.customer_email,
            customer_group=draft.customer_group,
            anonymous_id=draft.anonymous_id,
            country=draft.country,
            inventory_mode=draft.inventory_mode,
            discount_codes=[],
            direct_discounts=[],
            tax_mode=draft.tax_mode or models.TaxMode.PLATFORM,
            tax_rounding_mode=draft.tax_rounding_mode or models.RoundingMode.HALF_EVEN,
            tax_calculation_mode=draft.tax_calculation_mode
            or models.TaxCalculationMode.LINE_ITEM_LEVEL,
            item_shipping_addresses=[],
            line_items=line_items,
            custom_line_items=[],
            refused_gifts=[],
            shipping_address=draft.shipping_address,
            shipping_mode=models.ShippingMode.SINGLE,
            shipping=[],
            billing_address=draft.billing_address,
            locale=draft.locale,
            origin=draft.origin or models.CartOrigin.CUSTOMER,
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
        if not obj.get("paymentInfo"):
            obj["paymentInfo"] = PaymentInfoSchema().dump(
                models.PaymentInfo(payments=[])
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

    def set_custom_type(self, obj, action: models.CartSetCustomTypeAction):
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
        "setCustomField": utils.set_custom_field(),
        "setLineItemCustomField": utils.set_line_item_custom_field(),
        "setCustomType": set_custom_type,
    }

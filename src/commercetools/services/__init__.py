# DO NOT EDIT! This file is automatically generated
from commercetools.services.api_clients import ApiClientService
from commercetools.services.cart_discounts import CartDiscountService
from commercetools.services.carts import CartService
from commercetools.services.categories import CategoryService
from commercetools.services.channels import ChannelService
from commercetools.services.custom_object import CustomObjectService
from commercetools.services.customer_groups import CustomerGroupService
from commercetools.services.customers import CustomerService
from commercetools.services.discount_codes import DiscountCodeService
from commercetools.services.extensions import ExtensionService
from commercetools.services.graphqls import GraphqlService
from commercetools.services.in_stores import In_StoreService
from commercetools.services.inventory_entries import InventoryEntryService
from commercetools.services.login import LoginService
from commercetools.services.me import MeService
from commercetools.services.messages import MessageService
from commercetools.services.orders import OrderService
from commercetools.services.payments import PaymentService
from commercetools.services.product_discounts import ProductDiscountService
from commercetools.services.product_projections import ProductProjectionService
from commercetools.services.product_types import ProductTypeService
from commercetools.services.products import ProductService
from commercetools.services.reviews import ReviewService
from commercetools.services.shipping_methods import ShippingMethodService
from commercetools.services.shopping_lists import ShoppingListService
from commercetools.services.states import StateService
from commercetools.services.stores import StoreService
from commercetools.services.subscriptions import SubscriptionService
from commercetools.services.tax_categories import TaxCategoryService
from commercetools.services.types import TypeService
from commercetools.services.zones import ZoneService


class ServiceMixin:
    category: CategoryService
    cart: CartService
    cart_discount: CartDiscountService
    channel: ChannelService
    customer: CustomerService
    customer_group: CustomerGroupService
    custom_object: CustomObjectService
    discount_code: DiscountCodeService
    graphql: GraphqlService
    inventory_entry: InventoryEntryService
    login: LoginService
    message: MessageService
    order: OrderService
    payment: PaymentService
    product: ProductService
    product_discount: ProductDiscountService
    product_projection: ProductProjectionService
    product_type: ProductTypeService
    review: ReviewService
    shipping_method: ShippingMethodService
    shopping_list: ShoppingListService
    state: StateService
    subscription: SubscriptionService
    tax_category: TaxCategoryService
    type: TypeService
    zone: ZoneService
    me: MeService
    extension: ExtensionService
    api_client: ApiClientService
    store: StoreService
    in_store: In_StoreService

    def register_services(self):
        self.category = CategoryService(self)
        self.cart = CartService(self)
        self.cart_discount = CartDiscountService(self)
        self.channel = ChannelService(self)
        self.customer = CustomerService(self)
        self.customer_group = CustomerGroupService(self)
        self.custom_object = CustomObjectService(self)
        self.discount_code = DiscountCodeService(self)
        self.graphql = GraphqlService(self)
        self.inventory_entry = InventoryEntryService(self)
        self.login = LoginService(self)
        self.message = MessageService(self)
        self.order = OrderService(self)
        self.payment = PaymentService(self)
        self.product = ProductService(self)
        self.product_discount = ProductDiscountService(self)
        self.product_projection = ProductProjectionService(self)
        self.product_type = ProductTypeService(self)
        self.review = ReviewService(self)
        self.shipping_method = ShippingMethodService(self)
        self.shopping_list = ShoppingListService(self)
        self.state = StateService(self)
        self.subscription = SubscriptionService(self)
        self.tax_category = TaxCategoryService(self)
        self.type = TypeService(self)
        self.zone = ZoneService(self)
        self.me = MeService(self)
        self.extension = ExtensionService(self)
        self.api_client = ApiClientService(self)
        self.store = StoreService(self)
        self.in_store = In_StoreService(self)

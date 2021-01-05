# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .cart_discount import CartDiscountReference, CartDiscountResourceIdentifier
    from .common import (
        CreatedBy,
        LastModifiedBy,
        LocalizedString,
        Reference,
        ReferenceTypeId,
    )
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )


class DiscountCode(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    name: typing.Optional["LocalizedString"]
    description: typing.Optional["LocalizedString"]
    #: Unique identifier of this discount code.
    #: This value is added to the cart
    #: to enable the related cart discounts in the cart.
    code: "str"
    #: The referenced matching cart discounts can be applied to the cart once the DiscountCode is added.
    cart_discounts: typing.List["CartDiscountReference"]
    #: The discount code can only be applied to carts that match this predicate.
    cart_predicate: typing.Optional["str"]
    is_active: "bool"
    #: The platform will generate this array from the cart predicate.
    #: It contains the references of all the resources that are addressed in the predicate.
    references: typing.List["Reference"]
    #: The discount code can only be applied `maxApplications` times.
    max_applications: typing.Optional["int"]
    #: The discount code can only be applied `maxApplicationsPerCustomer` times per customer.
    max_applications_per_customer: typing.Optional["int"]
    custom: typing.Optional["CustomFields"]
    #: The groups to which this discount code belong.
    groups: typing.List["str"]
    #: The time from which the discount can be applied on a cart.
    #: Before that time the code is invalid.
    valid_from: typing.Optional["datetime.datetime"]
    #: The time until the discount can be applied on a cart.
    #: After that time the code is invalid.
    valid_until: typing.Optional["datetime.datetime"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        code: "str",
        cart_discounts: typing.List["CartDiscountReference"],
        cart_predicate: typing.Optional["str"] = None,
        is_active: "bool",
        references: typing.List["Reference"],
        max_applications: typing.Optional["int"] = None,
        max_applications_per_customer: typing.Optional["int"] = None,
        custom: typing.Optional["CustomFields"] = None,
        groups: typing.List["str"],
        valid_from: typing.Optional["datetime.datetime"] = None,
        valid_until: typing.Optional["datetime.datetime"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.name = name
        self.description = description
        self.code = code
        self.cart_discounts = cart_discounts
        self.cart_predicate = cart_predicate
        self.is_active = is_active
        self.references = references
        self.max_applications = max_applications
        self.max_applications_per_customer = max_applications_per_customer
        self.custom = custom
        self.groups = groups
        self.valid_from = valid_from
        self.valid_until = valid_until
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DiscountCode":
        from ._schemas.discount_code import DiscountCodeSchema

        return DiscountCodeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeSchema

        return DiscountCodeSchema().dump(self)


class DiscountCodeDraft(_BaseType):
    name: typing.Optional["LocalizedString"]
    description: typing.Optional["LocalizedString"]
    #: Unique identifier of this discount code.
    #: This value is added to the cart
    #: to enable the related cart discounts in the cart.
    code: "str"
    #: The referenced matching cart discounts can be applied to the cart once the discount code is added.
    #: The number of cart discounts in a discount code is limited to **10**.
    cart_discounts: typing.List["CartDiscountResourceIdentifier"]
    #: The discount code can only be applied to carts that match this predicate.
    cart_predicate: typing.Optional["str"]
    is_active: typing.Optional["bool"]
    max_applications: typing.Optional["int"]
    max_applications_per_customer: typing.Optional["int"]
    custom: typing.Optional["CustomFieldsDraft"]
    #: The groups to which this discount code shall belong to.
    groups: typing.Optional[typing.List["str"]]
    #: The time from which the discount can be applied on a cart.
    #: Before that time the code is invalid.
    valid_from: typing.Optional["datetime.datetime"]
    #: The time until the discount can be applied on a cart.
    #: After that time the code is invalid.
    valid_until: typing.Optional["datetime.datetime"]

    def __init__(
        self,
        *,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        code: "str",
        cart_discounts: typing.List["CartDiscountResourceIdentifier"],
        cart_predicate: typing.Optional["str"] = None,
        is_active: typing.Optional["bool"] = None,
        max_applications: typing.Optional["int"] = None,
        max_applications_per_customer: typing.Optional["int"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        groups: typing.Optional[typing.List["str"]] = None,
        valid_from: typing.Optional["datetime.datetime"] = None,
        valid_until: typing.Optional["datetime.datetime"] = None
    ):
        self.name = name
        self.description = description
        self.code = code
        self.cart_discounts = cart_discounts
        self.cart_predicate = cart_predicate
        self.is_active = is_active
        self.max_applications = max_applications
        self.max_applications_per_customer = max_applications_per_customer
        self.custom = custom
        self.groups = groups
        self.valid_from = valid_from
        self.valid_until = valid_until
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DiscountCodeDraft":
        from ._schemas.discount_code import DiscountCodeDraftSchema

        return DiscountCodeDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeDraftSchema

        return DiscountCodeDraftSchema().dump(self)


class DiscountCodePagedQueryResponse(_BaseType):
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["DiscountCode"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["DiscountCode"]
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodePagedQueryResponse":
        from ._schemas.discount_code import DiscountCodePagedQueryResponseSchema

        return DiscountCodePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodePagedQueryResponseSchema

        return DiscountCodePagedQueryResponseSchema().dump(self)


class DiscountCodeReference(Reference):
    obj: typing.Optional["DiscountCode"]

    def __init__(self, *, id: "str", obj: typing.Optional["DiscountCode"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.DISCOUNT_CODE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DiscountCodeReference":
        from ._schemas.discount_code import DiscountCodeReferenceSchema

        return DiscountCodeReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeReferenceSchema

        return DiscountCodeReferenceSchema().dump(self)


class DiscountCodeResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional["str"] = None, key: typing.Optional["str"] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.DISCOUNT_CODE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeResourceIdentifier":
        from ._schemas.discount_code import DiscountCodeResourceIdentifierSchema

        return DiscountCodeResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeResourceIdentifierSchema

        return DiscountCodeResourceIdentifierSchema().dump(self)


class DiscountCodeUpdate(_BaseType):
    version: "int"
    actions: typing.List["DiscountCodeUpdateAction"]

    def __init__(
        self, *, version: "int", actions: typing.List["DiscountCodeUpdateAction"]
    ):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DiscountCodeUpdate":
        from ._schemas.discount_code import DiscountCodeUpdateSchema

        return DiscountCodeUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeUpdateSchema

        return DiscountCodeUpdateSchema().dump(self)


class DiscountCodeUpdateAction(_BaseType):
    action: "str"

    def __init__(self, *, action: "str"):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeUpdateAction":
        from ._schemas.discount_code import DiscountCodeUpdateActionSchema

        return DiscountCodeUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeUpdateActionSchema

        return DiscountCodeUpdateActionSchema().dump(self)


class DiscountCodeChangeCartDiscountsAction(DiscountCodeUpdateAction):
    cart_discounts: typing.List["CartDiscountResourceIdentifier"]

    def __init__(
        self, *, cart_discounts: typing.List["CartDiscountResourceIdentifier"]
    ):
        self.cart_discounts = cart_discounts
        super().__init__(action="changeCartDiscounts")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeChangeCartDiscountsAction":
        from ._schemas.discount_code import DiscountCodeChangeCartDiscountsActionSchema

        return DiscountCodeChangeCartDiscountsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeChangeCartDiscountsActionSchema

        return DiscountCodeChangeCartDiscountsActionSchema().dump(self)


class DiscountCodeChangeGroupsAction(DiscountCodeUpdateAction):
    #: The groups to which this discount code shall belong to.
    #: Use empty array to remove the code from all groups.
    groups: typing.List["str"]

    def __init__(self, *, groups: typing.List["str"]):
        self.groups = groups
        super().__init__(action="changeGroups")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeChangeGroupsAction":
        from ._schemas.discount_code import DiscountCodeChangeGroupsActionSchema

        return DiscountCodeChangeGroupsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeChangeGroupsActionSchema

        return DiscountCodeChangeGroupsActionSchema().dump(self)


class DiscountCodeChangeIsActiveAction(DiscountCodeUpdateAction):
    is_active: "bool"

    def __init__(self, *, is_active: "bool"):
        self.is_active = is_active
        super().__init__(action="changeIsActive")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeChangeIsActiveAction":
        from ._schemas.discount_code import DiscountCodeChangeIsActiveActionSchema

        return DiscountCodeChangeIsActiveActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeChangeIsActiveActionSchema

        return DiscountCodeChangeIsActiveActionSchema().dump(self)


class DiscountCodeSetCartPredicateAction(DiscountCodeUpdateAction):
    #: If the `cartPredicate` parameter is not included, the field will be emptied.
    cart_predicate: typing.Optional["str"]

    def __init__(self, *, cart_predicate: typing.Optional["str"] = None):
        self.cart_predicate = cart_predicate
        super().__init__(action="setCartPredicate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeSetCartPredicateAction":
        from ._schemas.discount_code import DiscountCodeSetCartPredicateActionSchema

        return DiscountCodeSetCartPredicateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeSetCartPredicateActionSchema

        return DiscountCodeSetCartPredicateActionSchema().dump(self)


class DiscountCodeSetCustomFieldAction(DiscountCodeUpdateAction):
    name: "str"
    value: typing.Optional["any"]

    def __init__(self, *, name: "str", value: typing.Optional["any"] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeSetCustomFieldAction":
        from ._schemas.discount_code import DiscountCodeSetCustomFieldActionSchema

        return DiscountCodeSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeSetCustomFieldActionSchema

        return DiscountCodeSetCustomFieldActionSchema().dump(self)


class DiscountCodeSetCustomTypeAction(DiscountCodeUpdateAction):
    #: If absent, the custom type and any existing CustomFields are removed.
    type: typing.Optional["TypeResourceIdentifier"]
    #: A valid JSON object, based on the FieldDefinitions of the Type.
    #: Sets the custom fields to this value.
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeSetCustomTypeAction":
        from ._schemas.discount_code import DiscountCodeSetCustomTypeActionSchema

        return DiscountCodeSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeSetCustomTypeActionSchema

        return DiscountCodeSetCustomTypeActionSchema().dump(self)


class DiscountCodeSetDescriptionAction(DiscountCodeUpdateAction):
    #: If the `description` parameter is not included, the field will be emptied.
    description: typing.Optional["LocalizedString"]

    def __init__(self, *, description: typing.Optional["LocalizedString"] = None):
        self.description = description
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeSetDescriptionAction":
        from ._schemas.discount_code import DiscountCodeSetDescriptionActionSchema

        return DiscountCodeSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeSetDescriptionActionSchema

        return DiscountCodeSetDescriptionActionSchema().dump(self)


class DiscountCodeSetMaxApplicationsAction(DiscountCodeUpdateAction):
    #: If the `maxApplications` parameter is not included, the field will be emptied.
    max_applications: typing.Optional["int"]

    def __init__(self, *, max_applications: typing.Optional["int"] = None):
        self.max_applications = max_applications
        super().__init__(action="setMaxApplications")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeSetMaxApplicationsAction":
        from ._schemas.discount_code import DiscountCodeSetMaxApplicationsActionSchema

        return DiscountCodeSetMaxApplicationsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeSetMaxApplicationsActionSchema

        return DiscountCodeSetMaxApplicationsActionSchema().dump(self)


class DiscountCodeSetMaxApplicationsPerCustomerAction(DiscountCodeUpdateAction):
    #: If the `maxApplicationsPerCustomer` parameter is not included, the field will be emptied.
    max_applications_per_customer: typing.Optional["int"]

    def __init__(self, *, max_applications_per_customer: typing.Optional["int"] = None):
        self.max_applications_per_customer = max_applications_per_customer
        super().__init__(action="setMaxApplicationsPerCustomer")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeSetMaxApplicationsPerCustomerAction":
        from ._schemas.discount_code import (
            DiscountCodeSetMaxApplicationsPerCustomerActionSchema,
        )

        return DiscountCodeSetMaxApplicationsPerCustomerActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import (
            DiscountCodeSetMaxApplicationsPerCustomerActionSchema,
        )

        return DiscountCodeSetMaxApplicationsPerCustomerActionSchema().dump(self)


class DiscountCodeSetNameAction(DiscountCodeUpdateAction):
    #: If the `name` parameter is not included, the field will be emptied.
    name: typing.Optional["LocalizedString"]

    def __init__(self, *, name: typing.Optional["LocalizedString"] = None):
        self.name = name
        super().__init__(action="setName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeSetNameAction":
        from ._schemas.discount_code import DiscountCodeSetNameActionSchema

        return DiscountCodeSetNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeSetNameActionSchema

        return DiscountCodeSetNameActionSchema().dump(self)


class DiscountCodeSetValidFromAction(DiscountCodeUpdateAction):
    #: If absent, the field with the value is removed in case a value was set before.
    valid_from: typing.Optional["datetime.datetime"]

    def __init__(self, *, valid_from: typing.Optional["datetime.datetime"] = None):
        self.valid_from = valid_from
        super().__init__(action="setValidFrom")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeSetValidFromAction":
        from ._schemas.discount_code import DiscountCodeSetValidFromActionSchema

        return DiscountCodeSetValidFromActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeSetValidFromActionSchema

        return DiscountCodeSetValidFromActionSchema().dump(self)


class DiscountCodeSetValidFromAndUntilAction(DiscountCodeUpdateAction):
    #: If absent, the field with the value is removed in case a value was set before.
    valid_from: typing.Optional["datetime.datetime"]
    #: If absent, the field with the value is removed in case a value was set before.
    valid_until: typing.Optional["datetime.datetime"]

    def __init__(
        self,
        *,
        valid_from: typing.Optional["datetime.datetime"] = None,
        valid_until: typing.Optional["datetime.datetime"] = None
    ):
        self.valid_from = valid_from
        self.valid_until = valid_until
        super().__init__(action="setValidFromAndUntil")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeSetValidFromAndUntilAction":
        from ._schemas.discount_code import DiscountCodeSetValidFromAndUntilActionSchema

        return DiscountCodeSetValidFromAndUntilActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeSetValidFromAndUntilActionSchema

        return DiscountCodeSetValidFromAndUntilActionSchema().dump(self)


class DiscountCodeSetValidUntilAction(DiscountCodeUpdateAction):
    #: If absent, the field with the value is removed in case a value was set before.
    valid_until: typing.Optional["datetime.datetime"]

    def __init__(self, *, valid_until: typing.Optional["datetime.datetime"] = None):
        self.valid_until = valid_until
        super().__init__(action="setValidUntil")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeSetValidUntilAction":
        from ._schemas.discount_code import DiscountCodeSetValidUntilActionSchema

        return DiscountCodeSetValidUntilActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.discount_code import DiscountCodeSetValidUntilActionSchema

        return DiscountCodeSetValidUntilActionSchema().dump(self)

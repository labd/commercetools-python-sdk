# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import (
        CreatedBy,
        LastModifiedBy,
        LocalizedString,
        Money,
        QueryPrice,
        Reference,
        ReferenceTypeId,
        TypedMoney,
    )


class ProductDiscount(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    name: "LocalizedString"
    #: User-specific unique identifier for a product discount.
    #: Must be unique across a project.
    key: typing.Optional["str"]
    description: typing.Optional["LocalizedString"]
    value: "ProductDiscountValue"
    #: A valid ProductDiscount Predicate.
    predicate: "str"
    #: The string contains a number between 0 and 1.
    #: A discount with greater sortOrder is prioritized higher than a discount with lower sortOrder.
    #: A sortOrder must be unambiguous.
    sort_order: "str"
    #: Only active discount will be applied to product prices.
    is_active: "bool"
    #: The platform will generate this array from the predicate.
    #: It contains the references of all the resources that are addressed in the predicate.
    references: typing.List["Reference"]
    #: The time from which the discount should be effective.
    #: Please take Eventual Consistency into account for calculated product discount values.
    valid_from: typing.Optional["datetime.datetime"]
    #: The time from which the discount should be ineffective.
    #: Please take Eventual Consistency into account for calculated undiscounted values.
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
        name: "LocalizedString",
        key: typing.Optional["str"] = None,
        description: typing.Optional["LocalizedString"] = None,
        value: "ProductDiscountValue",
        predicate: "str",
        sort_order: "str",
        is_active: "bool",
        references: typing.List["Reference"],
        valid_from: typing.Optional["datetime.datetime"] = None,
        valid_until: typing.Optional["datetime.datetime"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.name = name
        self.key = key
        self.description = description
        self.value = value
        self.predicate = predicate
        self.sort_order = sort_order
        self.is_active = is_active
        self.references = references
        self.valid_from = valid_from
        self.valid_until = valid_until
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductDiscount":
        from ._schemas.product_discount import ProductDiscountSchema

        return ProductDiscountSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountSchema

        return ProductDiscountSchema().dump(self)


class ProductDiscountDraft(_BaseType):
    name: "LocalizedString"
    #: User-specific unique identifier for a product discount.
    #: Must be unique across a project.
    #: The field can be reset using the Set Key UpdateAction
    key: typing.Optional["str"]
    description: typing.Optional["LocalizedString"]
    value: "ProductDiscountValueDraft"
    #: A valid ProductDiscount Predicate.
    predicate: "str"
    #: The string must contain a decimal number between 0 and 1.
    #: A discount with greater sortOrder is prioritized higher than a discount with lower sortOrder.
    sort_order: "str"
    #: If set to `true` the discount will be applied to product prices.
    is_active: "bool"
    #: The time from which the discount should be effective.
    #: Please take Eventual Consistency into account for calculated product discount values.
    valid_from: typing.Optional["datetime.datetime"]
    #: The time from which the discount should be effective.
    #: Please take Eventual Consistency into account for calculated undiscounted values.
    valid_until: typing.Optional["datetime.datetime"]

    def __init__(
        self,
        *,
        name: "LocalizedString",
        key: typing.Optional["str"] = None,
        description: typing.Optional["LocalizedString"] = None,
        value: "ProductDiscountValueDraft",
        predicate: "str",
        sort_order: "str",
        is_active: "bool",
        valid_from: typing.Optional["datetime.datetime"] = None,
        valid_until: typing.Optional["datetime.datetime"] = None
    ):
        self.name = name
        self.key = key
        self.description = description
        self.value = value
        self.predicate = predicate
        self.sort_order = sort_order
        self.is_active = is_active
        self.valid_from = valid_from
        self.valid_until = valid_until
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductDiscountDraft":
        from ._schemas.product_discount import ProductDiscountDraftSchema

        return ProductDiscountDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountDraftSchema

        return ProductDiscountDraftSchema().dump(self)


class ProductDiscountMatchQuery(_BaseType):
    product_id: "str"
    variant_id: "int"
    staged: "bool"
    price: "QueryPrice"

    def __init__(
        self,
        *,
        product_id: "str",
        variant_id: "int",
        staged: "bool",
        price: "QueryPrice"
    ):
        self.product_id = product_id
        self.variant_id = variant_id
        self.staged = staged
        self.price = price
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountMatchQuery":
        from ._schemas.product_discount import ProductDiscountMatchQuerySchema

        return ProductDiscountMatchQuerySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountMatchQuerySchema

        return ProductDiscountMatchQuerySchema().dump(self)


class ProductDiscountPagedQueryResponse(_BaseType):
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["ProductDiscount"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["ProductDiscount"]
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
    ) -> "ProductDiscountPagedQueryResponse":
        from ._schemas.product_discount import ProductDiscountPagedQueryResponseSchema

        return ProductDiscountPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountPagedQueryResponseSchema

        return ProductDiscountPagedQueryResponseSchema().dump(self)


class ProductDiscountReference(Reference):
    obj: typing.Optional["ProductDiscount"]

    def __init__(self, *, id: "str", obj: typing.Optional["ProductDiscount"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.PRODUCT_DISCOUNT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountReference":
        from ._schemas.product_discount import ProductDiscountReferenceSchema

        return ProductDiscountReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountReferenceSchema

        return ProductDiscountReferenceSchema().dump(self)


class ProductDiscountResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional["str"] = None, key: typing.Optional["str"] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.PRODUCT_DISCOUNT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountResourceIdentifier":
        from ._schemas.product_discount import ProductDiscountResourceIdentifierSchema

        return ProductDiscountResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountResourceIdentifierSchema

        return ProductDiscountResourceIdentifierSchema().dump(self)


class ProductDiscountUpdate(_BaseType):
    version: "int"
    actions: typing.List["ProductDiscountUpdateAction"]

    def __init__(
        self, *, version: "int", actions: typing.List["ProductDiscountUpdateAction"]
    ):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductDiscountUpdate":
        from ._schemas.product_discount import ProductDiscountUpdateSchema

        return ProductDiscountUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountUpdateSchema

        return ProductDiscountUpdateSchema().dump(self)


class ProductDiscountUpdateAction(_BaseType):
    action: "str"

    def __init__(self, *, action: "str"):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountUpdateAction":
        from ._schemas.product_discount import ProductDiscountUpdateActionSchema

        return ProductDiscountUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountUpdateActionSchema

        return ProductDiscountUpdateActionSchema().dump(self)


class ProductDiscountValue(_BaseType):
    type: "str"

    def __init__(self, *, type: "str"):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductDiscountValue":
        from ._schemas.product_discount import ProductDiscountValueSchema

        return ProductDiscountValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountValueSchema

        return ProductDiscountValueSchema().dump(self)


class ProductDiscountValueAbsolute(ProductDiscountValue):
    money: typing.List["TypedMoney"]

    def __init__(self, *, money: typing.List["TypedMoney"]):
        self.money = money
        super().__init__(type="absolute")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountValueAbsolute":
        from ._schemas.product_discount import ProductDiscountValueAbsoluteSchema

        return ProductDiscountValueAbsoluteSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountValueAbsoluteSchema

        return ProductDiscountValueAbsoluteSchema().dump(self)


class ProductDiscountValueDraft(_BaseType):
    type: "str"

    def __init__(self, *, type: "str"):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountValueDraft":
        from ._schemas.product_discount import ProductDiscountValueDraftSchema

        return ProductDiscountValueDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountValueDraftSchema

        return ProductDiscountValueDraftSchema().dump(self)


class ProductDiscountValueAbsoluteDraft(ProductDiscountValueDraft):
    money: typing.List["Money"]

    def __init__(self, *, money: typing.List["Money"]):
        self.money = money
        super().__init__(type="absolute")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountValueAbsoluteDraft":
        from ._schemas.product_discount import ProductDiscountValueAbsoluteDraftSchema

        return ProductDiscountValueAbsoluteDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountValueAbsoluteDraftSchema

        return ProductDiscountValueAbsoluteDraftSchema().dump(self)


class ProductDiscountValueExternal(ProductDiscountValue):
    def __init__(self):

        super().__init__(type="external")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountValueExternal":
        from ._schemas.product_discount import ProductDiscountValueExternalSchema

        return ProductDiscountValueExternalSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountValueExternalSchema

        return ProductDiscountValueExternalSchema().dump(self)


class ProductDiscountValueExternalDraft(ProductDiscountValueDraft):
    def __init__(self):

        super().__init__(type="external")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountValueExternalDraft":
        from ._schemas.product_discount import ProductDiscountValueExternalDraftSchema

        return ProductDiscountValueExternalDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountValueExternalDraftSchema

        return ProductDiscountValueExternalDraftSchema().dump(self)


class ProductDiscountValueRelative(ProductDiscountValue):
    permyriad: "int"

    def __init__(self, *, permyriad: "int"):
        self.permyriad = permyriad
        super().__init__(type="relative")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountValueRelative":
        from ._schemas.product_discount import ProductDiscountValueRelativeSchema

        return ProductDiscountValueRelativeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountValueRelativeSchema

        return ProductDiscountValueRelativeSchema().dump(self)


class ProductDiscountValueRelativeDraft(ProductDiscountValueDraft):
    permyriad: "int"

    def __init__(self, *, permyriad: "int"):
        self.permyriad = permyriad
        super().__init__(type="relative")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountValueRelativeDraft":
        from ._schemas.product_discount import ProductDiscountValueRelativeDraftSchema

        return ProductDiscountValueRelativeDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountValueRelativeDraftSchema

        return ProductDiscountValueRelativeDraftSchema().dump(self)


class ProductDiscountChangeIsActiveAction(ProductDiscountUpdateAction):
    is_active: "bool"

    def __init__(self, *, is_active: "bool"):
        self.is_active = is_active
        super().__init__(action="changeIsActive")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountChangeIsActiveAction":
        from ._schemas.product_discount import ProductDiscountChangeIsActiveActionSchema

        return ProductDiscountChangeIsActiveActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountChangeIsActiveActionSchema

        return ProductDiscountChangeIsActiveActionSchema().dump(self)


class ProductDiscountChangeNameAction(ProductDiscountUpdateAction):
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString"):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountChangeNameAction":
        from ._schemas.product_discount import ProductDiscountChangeNameActionSchema

        return ProductDiscountChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountChangeNameActionSchema

        return ProductDiscountChangeNameActionSchema().dump(self)


class ProductDiscountChangePredicateAction(ProductDiscountUpdateAction):
    #: A valid ProductDiscount Predicate.
    predicate: "str"

    def __init__(self, *, predicate: "str"):
        self.predicate = predicate
        super().__init__(action="changePredicate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountChangePredicateAction":
        from ._schemas.product_discount import (
            ProductDiscountChangePredicateActionSchema,
        )

        return ProductDiscountChangePredicateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import (
            ProductDiscountChangePredicateActionSchema,
        )

        return ProductDiscountChangePredicateActionSchema().dump(self)


class ProductDiscountChangeSortOrderAction(ProductDiscountUpdateAction):
    #: The string must contain a number between 0 and 1.
    #: A discount with greater sortOrder is prioritized higher than a discount with lower sortOrder.
    sort_order: "str"

    def __init__(self, *, sort_order: "str"):
        self.sort_order = sort_order
        super().__init__(action="changeSortOrder")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountChangeSortOrderAction":
        from ._schemas.product_discount import (
            ProductDiscountChangeSortOrderActionSchema,
        )

        return ProductDiscountChangeSortOrderActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import (
            ProductDiscountChangeSortOrderActionSchema,
        )

        return ProductDiscountChangeSortOrderActionSchema().dump(self)


class ProductDiscountChangeValueAction(ProductDiscountUpdateAction):
    value: "ProductDiscountValueDraft"

    def __init__(self, *, value: "ProductDiscountValueDraft"):
        self.value = value
        super().__init__(action="changeValue")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountChangeValueAction":
        from ._schemas.product_discount import ProductDiscountChangeValueActionSchema

        return ProductDiscountChangeValueActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountChangeValueActionSchema

        return ProductDiscountChangeValueActionSchema().dump(self)


class ProductDiscountSetDescriptionAction(ProductDiscountUpdateAction):
    description: typing.Optional["LocalizedString"]

    def __init__(self, *, description: typing.Optional["LocalizedString"] = None):
        self.description = description
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountSetDescriptionAction":
        from ._schemas.product_discount import ProductDiscountSetDescriptionActionSchema

        return ProductDiscountSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountSetDescriptionActionSchema

        return ProductDiscountSetDescriptionActionSchema().dump(self)


class ProductDiscountSetKeyAction(ProductDiscountUpdateAction):
    #: The key to set.
    #: If you provide a `null` value or do not set this field at all, the existing `key` field is removed.
    key: typing.Optional["str"]

    def __init__(self, *, key: typing.Optional["str"] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountSetKeyAction":
        from ._schemas.product_discount import ProductDiscountSetKeyActionSchema

        return ProductDiscountSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountSetKeyActionSchema

        return ProductDiscountSetKeyActionSchema().dump(self)


class ProductDiscountSetValidFromAction(ProductDiscountUpdateAction):
    #: The time from which the discount should be effective.
    #: Please take Eventual Consistency into account for calculated product discount values.
    valid_from: typing.Optional["datetime.datetime"]

    def __init__(self, *, valid_from: typing.Optional["datetime.datetime"] = None):
        self.valid_from = valid_from
        super().__init__(action="setValidFrom")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountSetValidFromAction":
        from ._schemas.product_discount import ProductDiscountSetValidFromActionSchema

        return ProductDiscountSetValidFromActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountSetValidFromActionSchema

        return ProductDiscountSetValidFromActionSchema().dump(self)


class ProductDiscountSetValidFromAndUntilAction(ProductDiscountUpdateAction):
    valid_from: typing.Optional["datetime.datetime"]
    #: The timeframe for which the discount should be effective.
    #: Please take Eventual Consistency into account for calculated undiscounted values.
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
    ) -> "ProductDiscountSetValidFromAndUntilAction":
        from ._schemas.product_discount import (
            ProductDiscountSetValidFromAndUntilActionSchema,
        )

        return ProductDiscountSetValidFromAndUntilActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import (
            ProductDiscountSetValidFromAndUntilActionSchema,
        )

        return ProductDiscountSetValidFromAndUntilActionSchema().dump(self)


class ProductDiscountSetValidUntilAction(ProductDiscountUpdateAction):
    #: The time from which the discount should be ineffective.
    #: Please take Eventual Consistency into account for calculated undiscounted values.
    valid_until: typing.Optional["datetime.datetime"]

    def __init__(self, *, valid_until: typing.Optional["datetime.datetime"] = None):
        self.valid_until = valid_until
        super().__init__(action="setValidUntil")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountSetValidUntilAction":
        from ._schemas.product_discount import ProductDiscountSetValidUntilActionSchema

        return ProductDiscountSetValidUntilActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_discount import ProductDiscountSetValidUntilActionSchema

        return ProductDiscountSetValidUntilActionSchema().dump(self)

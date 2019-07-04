# DO NOT EDIT! This file is automatically generated

import datetime
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    LoggedResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._common import CreatedBy, LastModifiedBy, LocalizedString, Money, Price
__all__ = [
    "ProductDiscount",
    "ProductDiscountChangeIsActiveAction",
    "ProductDiscountChangeNameAction",
    "ProductDiscountChangePredicateAction",
    "ProductDiscountChangeSortOrderAction",
    "ProductDiscountChangeValueAction",
    "ProductDiscountDraft",
    "ProductDiscountMatchQuery",
    "ProductDiscountPagedQueryResponse",
    "ProductDiscountReference",
    "ProductDiscountResourceIdentifier",
    "ProductDiscountSetDescriptionAction",
    "ProductDiscountSetKeyAction",
    "ProductDiscountSetValidFromAction",
    "ProductDiscountSetValidFromAndUntilAction",
    "ProductDiscountSetValidUntilAction",
    "ProductDiscountUpdate",
    "ProductDiscountUpdateAction",
    "ProductDiscountValue",
    "ProductDiscountValueAbsolute",
    "ProductDiscountValueExternal",
    "ProductDiscountValueRelative",
]


class ProductDiscount(LoggedResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountSchema`."
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: :class:`commercetools.types.ProductDiscountValue`
    value: typing.Optional["ProductDiscountValue"]
    #: :class:`str`
    predicate: typing.Optional[str]
    #: :class:`str` `(Named` ``sortOrder`` `in Commercetools)`
    sort_order: typing.Optional[str]
    #: :class:`bool` `(Named` ``isActive`` `in Commercetools)`
    is_active: typing.Optional[bool]
    #: List of :class:`commercetools.types.Reference`
    references: typing.Optional[typing.List["Reference"]]
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        name: typing.Optional["LocalizedString"] = None,
        key: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None,
        value: typing.Optional["ProductDiscountValue"] = None,
        predicate: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        references: typing.Optional[typing.List["Reference"]] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None
    ) -> None:
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
            last_modified_by=last_modified_by,
            created_by=created_by,
        )

    def __repr__(self) -> str:
        return (
            "ProductDiscount(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, name=%r, key=%r, description=%r, value=%r, predicate=%r, sort_order=%r, is_active=%r, references=%r, valid_from=%r, valid_until=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.name,
                self.key,
                self.description,
                self.value,
                self.predicate,
                self.sort_order,
                self.is_active,
                self.references,
                self.valid_from,
                self.valid_until,
            )
        )


class ProductDiscountDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountDraftSchema`."
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: :class:`commercetools.types.ProductDiscountValue`
    value: typing.Optional["ProductDiscountValue"]
    #: :class:`str`
    predicate: typing.Optional[str]
    #: :class:`str` `(Named` ``sortOrder`` `in Commercetools)`
    sort_order: typing.Optional[str]
    #: :class:`bool` `(Named` ``isActive`` `in Commercetools)`
    is_active: typing.Optional[bool]
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        name: typing.Optional["LocalizedString"] = None,
        key: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None,
        value: typing.Optional["ProductDiscountValue"] = None,
        predicate: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None
    ) -> None:
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

    def __repr__(self) -> str:
        return (
            "ProductDiscountDraft(name=%r, key=%r, description=%r, value=%r, predicate=%r, sort_order=%r, is_active=%r, valid_from=%r, valid_until=%r)"
            % (
                self.name,
                self.key,
                self.description,
                self.value,
                self.predicate,
                self.sort_order,
                self.is_active,
                self.valid_from,
                self.valid_until,
            )
        )


class ProductDiscountMatchQuery(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountMatchQuerySchema`."
    #: :class:`str` `(Named` ``productId`` `in Commercetools)`
    product_id: typing.Optional[str]
    #: :class:`int` `(Named` ``variantId`` `in Commercetools)`
    variant_id: typing.Optional[int]
    #: :class:`bool`
    staged: typing.Optional[bool]
    #: :class:`commercetools.types.Price`
    price: typing.Optional["Price"]

    def __init__(
        self,
        *,
        product_id: typing.Optional[str] = None,
        variant_id: typing.Optional[int] = None,
        staged: typing.Optional[bool] = None,
        price: typing.Optional["Price"] = None
    ) -> None:
        self.product_id = product_id
        self.variant_id = variant_id
        self.staged = staged
        self.price = price
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ProductDiscountMatchQuery(product_id=%r, variant_id=%r, staged=%r, price=%r)"
            % (self.product_id, self.variant_id, self.staged, self.price)
        )


class ProductDiscountPagedQueryResponse(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountPagedQueryResponseSchema`."
    #: :class:`int`
    count: typing.Optional[int]
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: typing.Optional[int]
    #: List of :class:`commercetools.types.ProductDiscount`
    results: typing.Optional[typing.Sequence["ProductDiscount"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["ProductDiscount"]] = None
    ) -> None:
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ProductDiscountPagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)"
            % (self.count, self.total, self.offset, self.results)
        )


class ProductDiscountReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountReferenceSchema`."
    #: Optional :class:`commercetools.types.ProductDiscount`
    obj: typing.Optional["ProductDiscount"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        obj: typing.Optional["ProductDiscount"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.PRODUCT_DISCOUNT, id=id)

    def __repr__(self) -> str:
        return "ProductDiscountReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class ProductDiscountResourceIdentifier(ResourceIdentifier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountResourceIdentifierSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.PRODUCT_DISCOUNT, id=id, key=key)

    def __repr__(self) -> str:
        return "ProductDiscountResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class ProductDiscountUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountUpdateSchema`."
    #: :class:`int`
    version: typing.Optional[int]
    #: :class:`list`
    actions: typing.Optional[list]

    def __init__(
        self,
        *,
        version: typing.Optional[int] = None,
        actions: typing.Optional[list] = None
    ) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "ProductDiscountUpdate(version=%r, actions=%r)" % (
            self.version,
            self.actions,
        )


class ProductDiscountUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountUpdateActionSchema`."
    #: :class:`str`
    action: typing.Optional[str]

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "ProductDiscountUpdateAction(action=%r)" % (self.action,)


class ProductDiscountValue(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountValueSchema`."
    #: :class:`str`
    type: typing.Optional[str]

    def __init__(self, *, type: typing.Optional[str] = None) -> None:
        self.type = type
        super().__init__()

    def __repr__(self) -> str:
        return "ProductDiscountValue(type=%r)" % (self.type,)


class ProductDiscountChangeIsActiveAction(ProductDiscountUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountChangeIsActiveActionSchema`."
    #: :class:`bool` `(Named` ``isActive`` `in Commercetools)`
    is_active: typing.Optional[bool]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None
    ) -> None:
        self.is_active = is_active
        super().__init__(action="changeIsActive")

    def __repr__(self) -> str:
        return "ProductDiscountChangeIsActiveAction(action=%r, is_active=%r)" % (
            self.action,
            self.is_active,
        )


class ProductDiscountChangeNameAction(ProductDiscountUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountChangeNameActionSchema`."
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "ProductDiscountChangeNameAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


class ProductDiscountChangePredicateAction(ProductDiscountUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountChangePredicateActionSchema`."
    #: :class:`str`
    predicate: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        predicate: typing.Optional[str] = None
    ) -> None:
        self.predicate = predicate
        super().__init__(action="changePredicate")

    def __repr__(self) -> str:
        return "ProductDiscountChangePredicateAction(action=%r, predicate=%r)" % (
            self.action,
            self.predicate,
        )


class ProductDiscountChangeSortOrderAction(ProductDiscountUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountChangeSortOrderActionSchema`."
    #: :class:`str` `(Named` ``sortOrder`` `in Commercetools)`
    sort_order: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None
    ) -> None:
        self.sort_order = sort_order
        super().__init__(action="changeSortOrder")

    def __repr__(self) -> str:
        return "ProductDiscountChangeSortOrderAction(action=%r, sort_order=%r)" % (
            self.action,
            self.sort_order,
        )


class ProductDiscountChangeValueAction(ProductDiscountUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountChangeValueActionSchema`."
    #: :class:`commercetools.types.ProductDiscountValue`
    value: typing.Optional["ProductDiscountValue"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        value: typing.Optional["ProductDiscountValue"] = None
    ) -> None:
        self.value = value
        super().__init__(action="changeValue")

    def __repr__(self) -> str:
        return "ProductDiscountChangeValueAction(action=%r, value=%r)" % (
            self.action,
            self.value,
        )


class ProductDiscountSetDescriptionAction(ProductDiscountUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountSetDescriptionActionSchema`."
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.description = description
        super().__init__(action="setDescription")

    def __repr__(self) -> str:
        return "ProductDiscountSetDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )


class ProductDiscountSetKeyAction(ProductDiscountUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountSetKeyActionSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "ProductDiscountSetKeyAction(action=%r, key=%r)" % (
            self.action,
            self.key,
        )


class ProductDiscountSetValidFromAction(ProductDiscountUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountSetValidFromActionSchema`."
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        valid_from: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.valid_from = valid_from
        super().__init__(action="setValidFrom")

    def __repr__(self) -> str:
        return "ProductDiscountSetValidFromAction(action=%r, valid_from=%r)" % (
            self.action,
            self.valid_from,
        )


class ProductDiscountSetValidFromAndUntilAction(ProductDiscountUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountSetValidFromAndUntilActionSchema`."
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.valid_from = valid_from
        self.valid_until = valid_until
        super().__init__(action="setValidFromAndUntil")

    def __repr__(self) -> str:
        return (
            "ProductDiscountSetValidFromAndUntilAction(action=%r, valid_from=%r, valid_until=%r)"
            % (self.action, self.valid_from, self.valid_until)
        )


class ProductDiscountSetValidUntilAction(ProductDiscountUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountSetValidUntilActionSchema`."
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        valid_until: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.valid_until = valid_until
        super().__init__(action="setValidUntil")

    def __repr__(self) -> str:
        return "ProductDiscountSetValidUntilAction(action=%r, valid_until=%r)" % (
            self.action,
            self.valid_until,
        )


class ProductDiscountValueAbsolute(ProductDiscountValue):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountValueAbsoluteSchema`."
    #: List of :class:`commercetools.types.Money`
    money: typing.Optional[typing.List["Money"]]

    def __init__(
        self,
        *,
        type: typing.Optional[str] = None,
        money: typing.Optional[typing.List["Money"]] = None
    ) -> None:
        self.money = money
        super().__init__(type="absolute")

    def __repr__(self) -> str:
        return "ProductDiscountValueAbsolute(type=%r, money=%r)" % (
            self.type,
            self.money,
        )


class ProductDiscountValueExternal(ProductDiscountValue):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountValueExternalSchema`."

    def __init__(self, *, type: typing.Optional[str] = None) -> None:
        super().__init__(type="external")

    def __repr__(self) -> str:
        return "ProductDiscountValueExternal(type=%r)" % (self.type,)


class ProductDiscountValueRelative(ProductDiscountValue):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ProductDiscountValueRelativeSchema`."
    #: :class:`int`
    permyriad: typing.Optional[int]

    def __init__(
        self,
        *,
        type: typing.Optional[str] = None,
        permyriad: typing.Optional[int] = None
    ) -> None:
        self.permyriad = permyriad
        super().__init__(type="relative")

    def __repr__(self) -> str:
        return "ProductDiscountValueRelative(type=%r, permyriad=%r)" % (
            self.type,
            self.permyriad,
        )

# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, ReferenceTypeId


class SubRate(_BaseType):
    name: "str"
    amount: "float"

    def __init__(self, *, name: "str", amount: "float"):
        self.name = name
        self.amount = amount
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SubRate":
        from ._schemas.tax_category import SubRateSchema

        return SubRateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import SubRateSchema

        return SubRateSchema().dump(self)


class TaxCategory(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not tracked.
    created_by: typing.Optional["CreatedBy"]
    name: "str"
    description: typing.Optional["str"]
    #: The tax rates have unique IDs in the rates list
    rates: typing.List["TaxRate"]
    #: User-specific unique identifier for the category.
    key: typing.Optional["str"]

    def __init__(
        self,
        *,
        id: "str",
        version: "int",
        created_at: "datetime.datetime",
        last_modified_at: "datetime.datetime",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        name: "str",
        description: typing.Optional["str"] = None,
        rates: typing.List["TaxRate"],
        key: typing.Optional["str"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.name = name
        self.description = description
        self.rates = rates
        self.key = key
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxCategory":
        from ._schemas.tax_category import TaxCategorySchema

        return TaxCategorySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategorySchema

        return TaxCategorySchema().dump(self)


class TaxCategoryDraft(_BaseType):
    name: "str"
    description: typing.Optional["str"]
    rates: typing.List["TaxRateDraft"]
    key: typing.Optional["str"]

    def __init__(
        self,
        *,
        name: "str",
        description: typing.Optional["str"] = None,
        rates: typing.List["TaxRateDraft"],
        key: typing.Optional["str"] = None
    ):
        self.name = name
        self.description = description
        self.rates = rates
        self.key = key
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxCategoryDraft":
        from ._schemas.tax_category import TaxCategoryDraftSchema

        return TaxCategoryDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategoryDraftSchema

        return TaxCategoryDraftSchema().dump(self)


class TaxCategoryPagedQueryResponse(_BaseType):
    limit: "int"
    count: "int"
    total: typing.Optional["int"]
    offset: "int"
    results: typing.List["TaxCategory"]

    def __init__(
        self,
        *,
        limit: "int",
        count: "int",
        total: typing.Optional["int"] = None,
        offset: "int",
        results: typing.List["TaxCategory"]
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
    ) -> "TaxCategoryPagedQueryResponse":
        from ._schemas.tax_category import TaxCategoryPagedQueryResponseSchema

        return TaxCategoryPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategoryPagedQueryResponseSchema

        return TaxCategoryPagedQueryResponseSchema().dump(self)


class TaxCategoryReference(Reference):
    obj: typing.Optional["TaxCategory"]

    def __init__(self, *, id: "str", obj: typing.Optional["TaxCategory"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.TAX_CATEGORY)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxCategoryReference":
        from ._schemas.tax_category import TaxCategoryReferenceSchema

        return TaxCategoryReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategoryReferenceSchema

        return TaxCategoryReferenceSchema().dump(self)


class TaxCategoryResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional["str"] = None, key: typing.Optional["str"] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.TAX_CATEGORY)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TaxCategoryResourceIdentifier":
        from ._schemas.tax_category import TaxCategoryResourceIdentifierSchema

        return TaxCategoryResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategoryResourceIdentifierSchema

        return TaxCategoryResourceIdentifierSchema().dump(self)


class TaxCategoryUpdate(_BaseType):
    version: "int"
    actions: typing.List["TaxCategoryUpdateAction"]

    def __init__(
        self, *, version: "int", actions: typing.List["TaxCategoryUpdateAction"]
    ):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxCategoryUpdate":
        from ._schemas.tax_category import TaxCategoryUpdateSchema

        return TaxCategoryUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategoryUpdateSchema

        return TaxCategoryUpdateSchema().dump(self)


class TaxCategoryUpdateAction(_BaseType):
    action: "str"

    def __init__(self, *, action: "str"):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TaxCategoryUpdateAction":
        from ._schemas.tax_category import TaxCategoryUpdateActionSchema

        return TaxCategoryUpdateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategoryUpdateActionSchema

        return TaxCategoryUpdateActionSchema().dump(self)


class TaxRate(_BaseType):
    #: The ID is always set if the tax rate is part of a TaxCategory.
    #: The external tax rates in a
    #: Cart do not contain an `id`.
    id: typing.Optional["str"]
    name: "str"
    #: Percentage in the range of [0..1].
    #: The sum of the amounts of all `subRates`, if there are any.
    amount: "float"
    included_in_price: "bool"
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: "str"
    #: The state in the country
    state: typing.Optional["str"]
    #: For countries (e.g.
    #: the US) where the total tax is a combination of multiple taxes (e.g.
    #: state and local taxes).
    sub_rates: typing.Optional[typing.List["SubRate"]]

    def __init__(
        self,
        *,
        id: typing.Optional["str"] = None,
        name: "str",
        amount: "float",
        included_in_price: "bool",
        country: "str",
        state: typing.Optional["str"] = None,
        sub_rates: typing.Optional[typing.List["SubRate"]] = None
    ):
        self.id = id
        self.name = name
        self.amount = amount
        self.included_in_price = included_in_price
        self.country = country
        self.state = state
        self.sub_rates = sub_rates
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxRate":
        from ._schemas.tax_category import TaxRateSchema

        return TaxRateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxRateSchema

        return TaxRateSchema().dump(self)


class TaxRateDraft(_BaseType):
    name: "str"
    #: Percentage in the range of [0..1].
    #: Must be supplied if no `subRates` are specified.
    #: If `subRates` are specified
    #: then the `amount` can be omitted or it must be the sum of the amounts of all `subRates`.
    amount: typing.Optional["float"]
    included_in_price: "bool"
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: "str"
    #: The state in the country
    state: typing.Optional["str"]
    #: For countries (e.g.
    #: the US) where the total tax is a combination of multiple taxes (e.g.
    #: state and local taxes).
    sub_rates: typing.Optional[typing.List["SubRate"]]

    def __init__(
        self,
        *,
        name: "str",
        amount: typing.Optional["float"] = None,
        included_in_price: "bool",
        country: "str",
        state: typing.Optional["str"] = None,
        sub_rates: typing.Optional[typing.List["SubRate"]] = None
    ):
        self.name = name
        self.amount = amount
        self.included_in_price = included_in_price
        self.country = country
        self.state = state
        self.sub_rates = sub_rates
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxRateDraft":
        from ._schemas.tax_category import TaxRateDraftSchema

        return TaxRateDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxRateDraftSchema

        return TaxRateDraftSchema().dump(self)


class TaxCategoryAddTaxRateAction(TaxCategoryUpdateAction):
    tax_rate: "TaxRateDraft"

    def __init__(self, *, tax_rate: "TaxRateDraft"):
        self.tax_rate = tax_rate
        super().__init__(action="addTaxRate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TaxCategoryAddTaxRateAction":
        from ._schemas.tax_category import TaxCategoryAddTaxRateActionSchema

        return TaxCategoryAddTaxRateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategoryAddTaxRateActionSchema

        return TaxCategoryAddTaxRateActionSchema().dump(self)


class TaxCategoryChangeNameAction(TaxCategoryUpdateAction):
    name: "str"

    def __init__(self, *, name: "str"):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TaxCategoryChangeNameAction":
        from ._schemas.tax_category import TaxCategoryChangeNameActionSchema

        return TaxCategoryChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategoryChangeNameActionSchema

        return TaxCategoryChangeNameActionSchema().dump(self)


class TaxCategoryRemoveTaxRateAction(TaxCategoryUpdateAction):
    tax_rate_id: "str"

    def __init__(self, *, tax_rate_id: "str"):
        self.tax_rate_id = tax_rate_id
        super().__init__(action="removeTaxRate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TaxCategoryRemoveTaxRateAction":
        from ._schemas.tax_category import TaxCategoryRemoveTaxRateActionSchema

        return TaxCategoryRemoveTaxRateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategoryRemoveTaxRateActionSchema

        return TaxCategoryRemoveTaxRateActionSchema().dump(self)


class TaxCategoryReplaceTaxRateAction(TaxCategoryUpdateAction):
    tax_rate_id: "str"
    tax_rate: "TaxRateDraft"

    def __init__(self, *, tax_rate_id: "str", tax_rate: "TaxRateDraft"):
        self.tax_rate_id = tax_rate_id
        self.tax_rate = tax_rate
        super().__init__(action="replaceTaxRate")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TaxCategoryReplaceTaxRateAction":
        from ._schemas.tax_category import TaxCategoryReplaceTaxRateActionSchema

        return TaxCategoryReplaceTaxRateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategoryReplaceTaxRateActionSchema

        return TaxCategoryReplaceTaxRateActionSchema().dump(self)


class TaxCategorySetDescriptionAction(TaxCategoryUpdateAction):
    description: typing.Optional["str"]

    def __init__(self, *, description: typing.Optional["str"] = None):
        self.description = description
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TaxCategorySetDescriptionAction":
        from ._schemas.tax_category import TaxCategorySetDescriptionActionSchema

        return TaxCategorySetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategorySetDescriptionActionSchema

        return TaxCategorySetDescriptionActionSchema().dump(self)


class TaxCategorySetKeyAction(TaxCategoryUpdateAction):
    #: If `key` is absent or `null`, it is removed if it exists.
    key: typing.Optional["str"]

    def __init__(self, *, key: typing.Optional["str"] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TaxCategorySetKeyAction":
        from ._schemas.tax_category import TaxCategorySetKeyActionSchema

        return TaxCategorySetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.tax_category import TaxCategorySetKeyActionSchema

        return TaxCategorySetKeyActionSchema().dump(self)

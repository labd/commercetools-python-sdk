# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResourceType

if typing.TYPE_CHECKING:
    from .categories import CategoryImport
    from .common import ImportResourceType
    from .customers import CustomerImport
    from .importoperations import ImportOperationStatus
    from .inventories import InventoryImport
    from .orders import OrderImport
    from .prices import PriceImport
    from .productdrafts import ProductDraftImport
    from .products import ProductImport
    from .producttypes import ProductTypeImport
    from .productvariants import ProductVariantImport, ProductVariantPatch


class ImportRequest(_BaseType):
    """An import request batches multiple import resources of the same import resource type for processing by an import sink.
    
    """

    #: The type of the import resource.
    type: "ImportResourceType"

    def __init__(self, *, type: "ImportResourceType"):
        self.type = type
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImportRequest":
        from ._schemas.importrequests import ImportRequestSchema

        return ImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ImportRequestSchema

        return ImportRequestSchema().dump(self)


class ImportResponse(_BaseType):
    """The import response contains an import operation for each import resource sent with an import request. Use it for tracking the progress of imports to a commercetools project.
    
    This is a generic parent type. In practice, send a specific import request type (`CategoryImportRequest`, `OrderImportRequest`, etc.) to an import sink with a matching import type.
    
    """

    operation_status: typing.List["ImportOperationStatus"]

    def __init__(self, *, operation_status: typing.List["ImportOperationStatus"]):
        self.operation_status = operation_status
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImportResponse":
        from ._schemas.importrequests import ImportResponseSchema

        return ImportResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ImportResponseSchema

        return ImportResponseSchema().dump(self)


class CategoryImportRequest(ImportRequest):
    """An import request for multiple category import resources.
    
    """

    #: The category import resources of this request.
    resources: typing.List["CategoryImport"]

    def __init__(self, *, resources: typing.List["CategoryImport"]):
        self.resources = resources
        super().__init__(type=ImportResourceType.CATEGORY)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CategoryImportRequest":
        from ._schemas.importrequests import CategoryImportRequestSchema

        return CategoryImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import CategoryImportRequestSchema

        return CategoryImportRequestSchema().dump(self)


class ProductImportRequest(ImportRequest):
    """An import request for multiple product import resources.
    
    """

    #: The product import resources of this request.
    resources: typing.List["ProductImport"]

    def __init__(self, *, resources: typing.List["ProductImport"]):
        self.resources = resources
        super().__init__(type=ImportResourceType.PRODUCT)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductImportRequest":
        from ._schemas.importrequests import ProductImportRequestSchema

        return ProductImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ProductImportRequestSchema

        return ProductImportRequestSchema().dump(self)


class ProductDraftImportRequest(ImportRequest):
    """An import request for multiple product draft import resources.
    
    """

    #: The product draft import resources of this request.
    resources: typing.List["ProductDraftImport"]

    def __init__(self, *, resources: typing.List["ProductDraftImport"]):
        self.resources = resources
        super().__init__(type=ImportResourceType.PRODUCT_DRAFT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDraftImportRequest":
        from ._schemas.importrequests import ProductDraftImportRequestSchema

        return ProductDraftImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ProductDraftImportRequestSchema

        return ProductDraftImportRequestSchema().dump(self)


class ProductTypeImportRequest(ImportRequest):
    """An import request for multiple product type import resources.
    
    """

    #: The product type import resources of this request.
    resources: typing.List["ProductTypeImport"]

    def __init__(self, *, resources: typing.List["ProductTypeImport"]):
        self.resources = resources
        super().__init__(type=ImportResourceType.PRODUCT_TYPE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeImportRequest":
        from ._schemas.importrequests import ProductTypeImportRequestSchema

        return ProductTypeImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ProductTypeImportRequestSchema

        return ProductTypeImportRequestSchema().dump(self)


class ProductVariantImportRequest(ImportRequest):
    """An import request for multiple product variant import resources.
    
    """

    #: The product variant import resources of this request.
    resources: typing.List["ProductVariantImport"]

    def __init__(self, *, resources: typing.List["ProductVariantImport"]):
        self.resources = resources
        super().__init__(type=ImportResourceType.PRODUCT_VARIANT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantImportRequest":
        from ._schemas.importrequests import ProductVariantImportRequestSchema

        return ProductVariantImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ProductVariantImportRequestSchema

        return ProductVariantImportRequestSchema().dump(self)


class PriceImportRequest(ImportRequest):
    """An import request for multiple price import resources.
    
    """

    #: The price import resources of this request.
    resources: typing.List["PriceImport"]

    def __init__(self, *, resources: typing.List["PriceImport"]):
        self.resources = resources
        super().__init__(type=ImportResourceType.PRICE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceImportRequest":
        from ._schemas.importrequests import PriceImportRequestSchema

        return PriceImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import PriceImportRequestSchema

        return PriceImportRequestSchema().dump(self)


class OrderImportRequest(ImportRequest):
    """An import request for multiple order import resources.
    
    """

    #: The order import resources of this request.
    resources: typing.List["OrderImport"]

    def __init__(self, *, resources: typing.List["OrderImport"]):
        self.resources = resources
        super().__init__(type=ImportResourceType.ORDER)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderImportRequest":
        from ._schemas.importrequests import OrderImportRequestSchema

        return OrderImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import OrderImportRequestSchema

        return OrderImportRequestSchema().dump(self)


class ProductVariantPatchRequest(ImportRequest):
    """An import request for multiple product variant patch resources.
    
    """

    #: The product variant patches of this request.
    patches: typing.List["ProductVariantPatch"]

    def __init__(self, *, patches: typing.List["ProductVariantPatch"]):
        self.patches = patches
        super().__init__(type=ImportResourceType.PRODUCT_VARIANT_PATCH)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantPatchRequest":
        from ._schemas.importrequests import ProductVariantPatchRequestSchema

        return ProductVariantPatchRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ProductVariantPatchRequestSchema

        return ProductVariantPatchRequestSchema().dump(self)


class CustomerImportRequest(ImportRequest):
    """An import request for multiple customer import resources.
    
    """

    #: The customer import resources of this request.
    resources: typing.List["CustomerImport"]

    def __init__(self, *, resources: typing.List["CustomerImport"]):
        self.resources = resources
        super().__init__(type=ImportResourceType.CUSTOMER)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerImportRequest":
        from ._schemas.importrequests import CustomerImportRequestSchema

        return CustomerImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import CustomerImportRequestSchema

        return CustomerImportRequestSchema().dump(self)


class InventoryImportRequest(ImportRequest):
    """An import request for multiple inventory import resources.
    
    """

    #: The inventory import resources of this request.
    resources: typing.List["InventoryImport"]

    def __init__(self, *, resources: typing.List["InventoryImport"]):
        self.resources = resources
        super().__init__(type=ImportResourceType.INVENTORY)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryImportRequest":
        from ._schemas.importrequests import InventoryImportRequestSchema

        return InventoryImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import InventoryImportRequestSchema

        return InventoryImportRequestSchema().dump(self)

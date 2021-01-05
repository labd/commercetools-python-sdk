# Generated file, please do not change!!!

import datetime
import enum
import typing

from ._abstract import _BaseType


class ImportSummary(_BaseType):
    """An import summary describes the states of import resources of a given import sink.
    
    It is used to track the overall progress of import resources.
    
    """

    #: The states summary for this import summary.
    states: "OperationStates"
    #: The total number of import operations received for this import group.
    total: "int"

    def __init__(self, *, states: "OperationStates", total: "int"):
        self.states = states
        self.total = total
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImportSummary":
        from ._schemas.importsummaries import ImportSummarySchema

        return ImportSummarySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importsummaries import ImportSummarySchema

        return ImportSummarySchema().dump(self)


class OperationStates(_BaseType):
    #: The number of import operations that are in the state `ValidationFailed`.
    validation_failed: "int"
    #: The number of import operations that are in the state `Unresolved`.
    unresolved: "int"
    #: The number of import operations that are in the state `WaitForMasterVariant`.
    wait_for_master_variant: "int"
    #: The number of import operations that are in the state `Imported`.
    imported: "int"
    #: The number of import operations that are in the state `Delete`.
    delete: "int"
    #: The number of import operations that are in the state `Deleted`.
    deleted: "int"
    #: The number of import operations that are in the state `Rejected`.
    rejected: "int"

    def __init__(
        self,
        *,
        validation_failed: "int",
        unresolved: "int",
        wait_for_master_variant: "int",
        imported: "int",
        delete: "int",
        deleted: "int",
        rejected: "int"
    ):
        self.validation_failed = validation_failed
        self.unresolved = unresolved
        self.wait_for_master_variant = wait_for_master_variant
        self.imported = imported
        self.delete = delete
        self.deleted = deleted
        self.rejected = rejected
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OperationStates":
        from ._schemas.importsummaries import OperationStatesSchema

        return OperationStatesSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importsummaries import OperationStatesSchema

        return OperationStatesSchema().dump(self)

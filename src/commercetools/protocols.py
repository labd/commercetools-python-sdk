import typing

from marshmallow.base import SchemaABC


class ClientProtocol(typing.Protocol):
    def _get(
        self,
        endpoint: str,
        params: typing.Dict[str, typing.Any],
        schema_cls: typing.Type[SchemaABC],
    ) -> typing.Any:
        ...

    def _post(
        self,
        endpoint: str,
        params: typing.Dict[str, str],
        data_object: typing.Any,
        request_schema_cls: typing.Optional[typing.Type[SchemaABC]],
        response_schema_cls: typing.Type[SchemaABC],
        form_encoded: bool = False,
        force_update: bool = False,
    ) -> typing.Any:
        ...

    def _upload(
        self,
        endpoint: str,
        params: typing.Dict[str, str],
        file: typing.IO,
        response_schema_cls: typing.Type[SchemaABC],
    ) -> typing.Any:
        ...

    def _delete(
        self,
        endpoint: str,
        params: typing.Dict[str, str],
        response_schema_cls: typing.Type[SchemaABC],
        force_delete: bool = False,
    ) -> typing.Any:
        ...

import importlib
import inspect
import typing

from marshmallow import Schema, class_registry, fields, missing, post_dump
from marshmallow.exceptions import (
    RegistryError,
    StringNotCollectionError,
    ValidationError,
)
from marshmallow.fields import Field, Nested
from marshmallow.utils import RAISE, is_collection
from marshmallow.utils import missing as missing_

from commercetools.exceptions import CommercetoolsError


def absmod(source, target):
    """We generate relative paths, but Marshmallow needs absolute
    paths for imports.

    So let's combine it this way. Using inspect and analyzing the
    stacktrace is way to slow, so we consume __name__ for source
    """
    if target.startswith(".") and target.count(".") == 1:
        return source + target

    source_parts = source.split(".")
    for i, char in enumerate(target):
        if char == ".":
            source_parts.pop()
        else:
            break
    modname = ".".join(source_parts) + "." + target[i:]
    return modname


class BaseSchema(Schema):
    @post_dump
    def remove_omit_empty(self, data, many, **kwargs):
        omit_fields = [
            field.data_key or field_name
            for field_name, field in self.fields.items()
            if field.metadata.get("omit_empty", False)
        ]
        for field in omit_fields:
            if data.get(field) is None:
                data.pop(field, None)

        return data


class OptionalList(fields.List):
    def _serialize(
        self, value, attr, obj, **kwargs
    ) -> typing.Optional[typing.List[typing.Any]]:
        if not isinstance(value, list):
            value = [value]
        return super()._serialize(value, attr, obj, **kwargs)

    def _deserialize(self, value, attr, data, **kwargs):
        if not isinstance(value, list):
            value = [value]
        return super()._deserialize(value, attr, data, **kwargs)


class MappingField(Field):
    def _serialize(self, nested_obj, attr, obj):
        result = {}
        values = obj.get(attr) or {}
        for key, value in values.items():
            result["var.%s" % key] = value
        return result


class RemoveEmptyValuesMixin:
    @post_dump
    def remove_empty_values(self, data, **kwargs):
        """Remove the key, value pairs for which the value is None.

        This doesn't work if allow_none is set. And in the future we might also
        want to remove values which are already the default to minimise the
        params.

        """
        result = {}
        for k, v in data.items():
            if isinstance(v, list):
                result[k] = [x for x in v if x is not None]
            elif v is not None:
                result[k] = v
        return result


class RegexField(Field):
    def _serialize(self, nested_obj, attr, obj):
        result = {}
        data = obj[attr]

        for key, subvalue in data.items():
            result[key] = self.metadata["type"].serialize(
                key, data, lambda obj, key, default: obj.get(key) or missing
            )
            assert result[key]
        return result

    def _deserialize(self, value, attr, data, **kwargs):
        result = {}
        for key, subvalue in value.items():
            result[key] = self.metadata["type"].deserialize(subvalue, **kwargs)
        return result

    def postprocess(self, data):
        extra_data = data.pop(self.name)
        data.update(extra_data)
        return data

    def preprocess(self, data):
        name = str(self.name)
        new: typing.Dict[str, typing.Any] = {name: {}}
        for k, v in data.items():
            if self.metadata["pattern"].match(k):
                new[name][k] = v
            else:
                new[k] = v
        return new


class LazyNestedField(Nested):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def schema(self):
        try:
            return super().schema
        except RegistryError:
            if isinstance(self.nested, str):
                _load_schema_by_name(self.nested)
                return super().schema
            raise


class Discriminator(Field):
    default_error_messages = {"type": "Invalid type."}

    def __init__(
        self,
        default=missing_,
        exclude=tuple(),
        only=None,
        discriminator_field=None,
        discriminator_schemas=None,
        **kwargs,
    ):
        # Raise error if only or exclude is passed as string, not list of strings
        if only is not None and not is_collection(only):
            raise StringNotCollectionError('"only" should be a list of strings')
        if exclude is not None and not is_collection(exclude):
            raise StringNotCollectionError('"exclude" should be a list of strings')
        self.only = only
        self.exclude = exclude
        self.many = kwargs.get("many", False)
        self.unknown = kwargs.get("unknown", RAISE)
        self.discriminator_field = discriminator_field
        self.discriminator_schemas = discriminator_schemas
        self.__updated_fields = False
        super().__init__(default=default, **kwargs)

    def get_schema(self, name):
        context = getattr(self.parent, "context", {})
        try:
            schema_class = class_registry.get_class(name)
        except RegistryError:
            schema_class = _load_schema_by_name(name)

        # Class registry can return a list if multiple classes with the same
        # name are registered. We shouldn't do that so lets assert it.
        # and make mypy happy :-)
        assert not isinstance(schema_class, list)

        schema = schema_class(
            many=self.many,
            only=self.only,
            exclude=self.exclude,
            context=context,
            load_only=self._nested_normalized_option("load_only"),
            dump_only=self._nested_normalized_option("dump_only"),
        )
        schema.ordered = getattr(self.parent, "ordered", False)
        return schema

    def _nested_normalized_option(self, option_name):
        nested_field = "%s." % self.name
        return [
            field.split(nested_field, 1)[1]
            for field in getattr(self.root, option_name, set())
            if field.startswith(nested_field)
        ]

    def _serialize(self, nested_obj, attr, obj):
        if nested_obj is None:
            return None

        try:
            discriminator_value = getattr(nested_obj, self.discriminator_field[1])
        except AttributeError:

            # We could make the error a bit more descriptive in the future
            raise ValueError(
                "The value of %s.%s doesn't have the attribute %r (expected object of %s)"
                % (
                    obj.__class__.__name__,
                    attr,
                    self.discriminator_field[1],
                    ", ".join(self.discriminator_schemas.keys()),
                )
            )

        if discriminator_value is None:
            raise ValueError(
                "The value of %s.%s doesn't have a value (are you using a base class?)"
                % (obj.__class__.__name__, attr)
            )

        if isinstance(discriminator_value, str):
            schema_name = self.discriminator_schemas[discriminator_value]
        else:
            schema_name = self.discriminator_schemas[discriminator_value.value]
        schema = self.get_schema(schema_name)

        try:
            return schema.dump(nested_obj, many=self.many)
        except ValidationError as exc:
            raise ValidationError(exc.messages, data=obj, valid_data=exc.valid_data)

    def _test_collection(self, value):
        if self.many and not is_collection(value):
            self.fail("type", input=value, type=value.__class__.__name__)

    def _load(self, value, data, **kwargs):
        if not value:
            return None

        discriminator_value = value[self.discriminator_field[0]]
        try:
            schema_name = self.discriminator_schemas[discriminator_value]
        except KeyError:
            raise ValueError(
                f"Could not find discriminator schema {discriminator_value} for field '{self.name}' ({value})"
            )

        schema = self.get_schema(schema_name)

        try:
            valid_data = schema.load(value, unknown=self.unknown)
        except ValidationError as exc:
            raise ValidationError(exc.messages, data=data, valid_data=exc.valid_data)
        return valid_data

    def _deserialize(self, value, attr, data, **kwargs):
        self._test_collection(value)
        return self._load(value, data, **kwargs)


def _concurrent_retry(num, source):
    """Decorator to add retry logic for concurrent modifications.

    The num field is used to indicate how many times it should be retried. When
    0 is given then it doesn't retry at all.

    """
    # Shortcut the decorator when we don't want to retry. This is the usual
    # flow.
    if num == 0:
        return lambda func: func

    def _wrapper(func):
        def _handler(*args, **kwargs):
            nonlocal num

            # When there is no version set we can skip the retry logic
            if not kwargs.get(source) or not kwargs[source].get("version"):
                return func(*args, **kwargs)

            # Loop while we explicity either return or raise an error when the
            # num value is decreated to <= 0.
            while True:
                response = func(*args, **kwargs)
                if response.status_code == 409 and num > 0:
                    response_data = response.json()
                    if response_data.get("errors"):
                        kwargs[source]["version"] = next(
                            x.get("currentVersion") for x in response_data["errors"]
                        )
                    else:
                        return response
                    num -= 1
                else:
                    return response

        return _handler

    return _wrapper


def _load_schema_by_name(name):
    names = name.rsplit(".", 1)
    importlib.import_module(names[0])
    return class_registry.get_class(name)

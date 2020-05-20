import typing

from marshmallow import class_registry, fields, missing
from marshmallow.exceptions import StringNotCollectionError, ValidationError
from marshmallow.fields import Field
from marshmallow.utils import RAISE, is_collection
from marshmallow.utils import missing as missing_

from commercetools.exceptions import CommercetoolsError


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
        new: typing.Dict[str, typing.Any] = {self.name: {}}
        for k, v in data.items():
            if self.metadata["pattern"].match(k):
                new[self.name][k] = v
            else:
                new[k] = v
        return new


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
        schema_class = class_registry.get_class(name)
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


def _concurrent_retry(num):
    """Decorator to add retry logic for concurrent modifications.

    The num field is used to indicate how many times it should be retried. When
    0 is given then it doesn't retry at all.

    """
    # Shortcut the decorator when we don't want to retry. This is the usual
    # flow.
    if num == 0:
        return lambda func: func

    def _wrapper(func):
        def _handler(data):
            nonlocal num

            # When there is no version set we can skip the retry logic
            if "version" not in data:
                return func(data)

            # Loop while we explicity either return or raise an error when the
            # num value is decreated to <= 0.
            while True:
                try:
                    return func(data)
                except CommercetoolsError as exc:
                    if num <= 0:
                        raise

                    if exc.response.status_code == 409:
                        data["version"] = exc.response.errors[0].current_version
                    else:
                        raise
                    num -= 1

        return _handler

    return _wrapper

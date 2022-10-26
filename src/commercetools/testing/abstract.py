import copy
import re
import typing
import uuid

import marshmallow
from marshmallow import fields
from requests_mock.request import _RequestObjectProxy

from commercetools import CommercetoolsError
from commercetools.helpers import OptionalList
from commercetools.platform import models
from commercetools.platform.models._schemas.common import BaseResourceSchema
from commercetools.platform.models._schemas.error import (
    DuplicateFieldErrorSchema,
    ErrorResponseSchema,
)
from commercetools.testing import traits, utils
from commercetools.testing.predicates import PredicateFilter
from commercetools.testing.utils import create_commercetools_response


class BaseModel:
    _resource_schema: typing.Type[BaseResourceSchema]
    _unique_values: typing.List[str] = []

    def __init__(self, storage):
        self._storage = storage
        self.objects = storage.init_store(self._primary_type_name)

        assert (
            self._resource_schema
        ), f"{self.__class__.__name__} has no resource schema defined"

    def add_existing(self, obj):
        """Add an 'existing' object to the storage.

        This can be used to set a certain initial state in your test case.
        """
        return self._store_obj(obj)

    def add(self, draft, id=None):
        """Add a new object to the storage.

        This will take a draft and generate an unique ID.
        """
        obj = self._create_from_draft(draft, id)
        return self._store_obj(obj)

    def _store_obj(self, obj):
        key = self._generate_key(obj)
        document = self._resource_schema().dump(obj)

        for field in self._unique_values:
            # Check if a document already exists with a duplicate unique value
            if document.get(field) in [
                o[field] for o in self.objects.values() if field in o
            ]:
                value = document[field]
                if not value:
                    continue

                msg = f"A duplicate value '{value}' exists for field '{field}'."
                error = models.DuplicateFieldError(
                    message=msg,
                    field=field,
                    duplicate_value=value,
                    conflicting_resource=None,
                )
                serialized_errors = [DuplicateFieldErrorSchema().dump(error)]
                raise CommercetoolsError(
                    msg,
                    errors=serialized_errors,
                    response=models.ErrorResponse(
                        status_code=400,
                        message=msg,
                        error=error.code,
                        errors=serialized_errors,
                    ),
                )

        self.objects[key] = document
        return document

    def _generate_key(self, obj):
        return uuid.UUID(obj.id)

    def _create_from_draft(self, draft, id=None):
        raise NotImplementedError()

    def query(self, where=None):
        objects = list(self.objects.values())
        if not where:
            return objects
        where_clause = " AND ".join(where)
        predicate_filter = PredicateFilter(where_clause, schema=self._resource_schema)
        return [obj for obj in objects if predicate_filter.match(obj)]

    def get_by_id(self, id):
        try:
            return self.objects.get(uuid.UUID(id))
        except ValueError:
            return None

    def get_by_key(self, key):
        for obj in self.objects.values():
            if obj["key"] == key:
                return obj

    def delete_by_id(self, id):
        obj = self.objects.pop(uuid.UUID(id))
        return obj

    def delete_by_key(self, key):
        for obj_id, obj in self.objects.items():
            if obj["key"] == key:
                return self.objects.pop(obj_id)

    def delete_by_container_and_key(self, container, key):
        item = None
        for obj_id, obj in list(self.objects.items()):
            if obj["container"] == container and obj["key"] == key:
                item = self.objects.pop(obj_id)
        return item

    def save(self, obj):
        assert obj["id"]
        obj["version"] += 1
        key = uuid.UUID(obj["id"])
        self.objects[key] = obj


class BaseBackend:
    path = None
    _actions: typing.Dict[str, typing.Callable] = {}
    model_class: typing.Any = None

    def __init__(self, storage=None, model=None):
        if model:
            self.model = model
        elif self.model_class:
            if storage:
                self.model = self.model_class(storage)
            else:
                self.model = self.model_class()

    def register(self, adapter):
        adapter.add_matcher(self._matcher)

    def _matcher(self, request, skip_port_check=False):
        if not skip_port_check and request.port != 443:
            return

        if request.hostname not in self.hostnames:
            return
            if not request.route_kwargs["path"]:
                request.route_kwargs["path"] = "/"

        match = re.match(self.path_prefix, request.path)
        if match:
            request.kwargs = match.groupdict()
            try:
                request_path = match.groupdict()["path"]
            except KeyError:
                request_path = ""

            for path, method, callback in self.urls():
                path_match = re.match(path, request_path)

                # Call the view
                if path_match and request.method == method:
                    response = callback(request, **path_match.groupdict())
                    if response is None:
                        raise NotImplementedError(
                            "No response returned by %r" % callback
                        )
                    return response
            return create_commercetools_response(request, status_code=404)


class GenericSchema(traits.QuerySchema, traits.SortableSchema, traits.PagingSchema):
    where = OptionalList(fields.String())
    sort = OptionalList(fields.String())
    expand = OptionalList(fields.String())
    limit = fields.Int()
    offset = fields.Int()


class ServiceBackend(BaseBackend):
    hostnames = ["api.europe-west1.gcp.commercetools.com", "api.sphere.io", "localhost"]
    model_class: typing.Any = None
    _schema_draft: typing.Optional[typing.Type[marshmallow.Schema]] = None
    _schema_update: typing.Optional[typing.Type[marshmallow.Schema]] = None
    _schema_query_response: typing.Optional[typing.Type[marshmallow.Schema]] = None
    _schema_query_params: marshmallow.Schema = GenericSchema
    _query_default_limit = 20

    _verify_version: bool = True

    @property
    def path_prefix(self):
        return f"/(?P<project>[^/]+)/{self.service_path}/?(?P<path>.*)?"

    def add_existing(self, obj):
        return self.model.add_existing(obj)

    def create(self, request):
        obj = self._schema_draft().loads(request.body)
        data = self.model.add(obj)
        expanded_data = self._expand(request, data)
        return create_commercetools_response(
            request, json=expanded_data, status_code=201
        )

    def get_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            expanded_data = self._expand(request, obj)
            return create_commercetools_response(request, json=expanded_data)
        return create_commercetools_response(request, status_code=404)

    def get_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            expanded_data = self._expand(request, obj)
            return create_commercetools_response(request, json=expanded_data)
        return create_commercetools_response(request, status_code=404)

    def query(self, request):
        params = utils.parse_request_params(self._schema_query_params, request)
        results = self.model.query(params.get("where"))
        total_count = len(results)
        limit = params.get("limit", self._query_default_limit)
        if limit:
            results = results[:limit]

        if params.get("expand"):
            expanded_results = []
            for result in results:
                expanded_results.append(self._expand(request, result))
            results = expanded_results

        data = {
            "count": len(results),
            "total": total_count,
            "offset": 0,
            "limit": limit,
            "results": self.model._resource_schema().load(results, many=True),
        }
        content = self._schema_query_response().dumps(data)
        return create_commercetools_response(request, text=content)

    def update_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        return self._update(request, obj)

    def update_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        return self._update(request, obj)

    def delete_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            if self._verify_version:
                response = self._validate_resource_version(request, obj)
                if response is not None:
                    return response

            obj = self.model.delete_by_id(id)
            return create_commercetools_response(request, json=obj)
        return create_commercetools_response(request, status_code=404)

    def delete_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            if self._verify_version:
                response = self._validate_resource_version(request, obj)
                if response is not None:
                    return response

            obj = self.model.delete_by_key(key)
            return create_commercetools_response(request, json=obj)
        return create_commercetools_response(request, status_code=404)

    def delete_by_container_and_key(self, request, container, key):
        obj = self.model.get_by_container_and_key(container, key)
        if obj:
            if self._verify_version:
                response = self._validate_resource_version(request, obj)
                if response is not None:
                    return response

            obj = self.model.delete_by_container_and_key(key)
            return create_commercetools_response(request, json=obj)
        return create_commercetools_response(request, status_code=404)

    def _expand(self, request: _RequestObjectProxy, raw_obj):
        params = utils.parse_request_params(self._schema_query_params, request)
        if "expand" not in params:
            return raw_obj

        expanded_obj = copy.deepcopy(raw_obj)

        for expand_term in params["expand"]:
            self._expand_obj(expanded_obj, expand_term)

        return expanded_obj

    def _expand_obj(self, obj, expand_term):
        resource_ids_to_expand = self._determine_resource_identifiers(
            [obj], expand_term.split(".")
        )
        for resource_identifier in resource_ids_to_expand:
            if "typeId" in resource_identifier and "id" in resource_identifier:
                try:
                    for document in self.model._storage._stores[
                        resource_identifier["typeId"]
                    ].values():
                        if document["id"] == resource_identifier["id"]:
                            resource_identifier["obj"] = copy.deepcopy(document)
                except KeyError:
                    continue

    def _determine_resource_identifiers(self, resource_id_list, terms):
        term = terms[0]
        multiple = False

        if term.endswith("[*]"):
            multiple = True
            term = term[:-3]

        if term.endswith("]"):
            if "[" not in term:
                return []

            index = int(term.split("[")[1][:-1])
            term = term[:-3]

            try:
                resource_identifiers = [
                    resource_id[term][index]
                    for resource_id in resource_id_list
                    if resource_id[term][index]
                ]
            except (KeyError, IndexError):
                return []
        else:
            try:
                resource_identifiers = [
                    resource_id[term]
                    for resource_id in resource_id_list
                    if resource_id[term]
                ]
            except KeyError:
                return []

        if multiple:
            resource_identifiers = [
                item for resource_id in resource_identifiers for item in resource_id
            ]
        if len(terms) == 1:
            return resource_identifiers

        if len(terms) > 1:
            return self._determine_resource_identifiers(resource_identifiers, terms[1:])

    def _update(self, request, obj):
        if not obj:
            return create_commercetools_response(request, status_code=404)

        update = self._schema_update().load(request.json())

        if self._verify_version:
            response = self._validate_resource_version(request, obj)
            if response is not None:
                return response

        if update.actions:
            obj, err = self._apply_update_actions(obj, update)
            if err:
                return create_commercetools_response(
                    request, json=err, status_code=err["statusCode"]
                )
        expanded_obj = self._expand(request, obj)
        return create_commercetools_response(request, json=expanded_obj)

    def _validate_resource_version(self, request, obj):
        update_version = self._get_version_from_request(request)
        if update_version != obj["version"]:
            data = self._create_version_error_response(obj["version"])
            return create_commercetools_response(request, json=data, status_code=409)

    def _get_version_from_request(self, request):
        version_data = request.qs.get("version")
        if version_data:
            return int(version_data[0])
        return request.json().get("version")

    def _apply_update_actions(self, obj, update):
        original_obj = obj

        for action in update.actions:
            func = self._actions.get(action.action)
            if not func:
                print("Missing action for", action.action)
                continue
            try:
                obj = func(self, obj, action)
            except utils.InternalUpdateError as exc:
                return None, self._create_data_error_response(str(exc), obj)

        # Save the updated object to the model
        if obj != original_obj:
            if self._verify_version and obj["version"] != update.version:
                return None, self._create_version_error_response(obj["version"])
            self.model.save(obj)

        # Temporary
        elif not self._actions:
            self.model.save(obj)

        return obj, None

    def _create_data_error_response(self, message, obj):
        return ErrorResponseSchema().dump(
            models.ErrorResponse(
                status_code=400,
                message=message,
                errors=[
                    models.ConcurrentModificationError(
                        message=message, current_version=obj["version"]
                    )
                ],
            )
        )

    def _create_version_error_response(self, version):
        return ErrorResponseSchema().dump(
            models.ErrorResponse(
                status_code=409,
                message="Version mismatch. Concurrent modification.",
                errors=[
                    models.ConcurrentModificationError(
                        message="Version mismatch. Concurrent modification.",
                        current_version=version,
                    )
                ],
            )
        )

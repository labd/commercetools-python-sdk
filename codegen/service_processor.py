import typing

import attr

from codegen.utils import (
    class_name,
    create_codename,
    create_method_name,
    extract_name,
    snakeit,
)


@attr.s(auto_attribs=True)
class ServiceParameter:
    name: str
    type: str
    required: bool
    multiple: bool = False
    extra_data: dict = None

    @property
    def pytype(self):
        if self.type == "string":
            return str
        return self.type


@attr.s(auto_attribs=True)
class ServiceMethod:
    name: str
    path: str
    method: str
    type: str
    context_name: str = None
    description: str = None
    path_params: typing.List[ServiceParameter] = attr.Factory(list)
    query_params: typing.List[ServiceParameter] = attr.Factory(list)
    extra_params: typing.List[ServiceParameter] = attr.Factory(list)
    input_type: str = None
    returns: str = None
    is_fileupload: bool = False
    traits: typing.List["TraitInfo"] = attr.Factory(list)


@attr.s(auto_attribs=True)
class ServiceDomain:
    path: str
    parent: "ServiceDomain" = None
    context_name: str = None
    description: str = None
    path_parameters: typing.List[ServiceParameter] = None
    methods: typing.List[ServiceMethod] = None
    resource_draft: str = None
    resource_type: str = None
    resource_querytype: str = None

    def add_method(self, *methods):
        for method in methods:
            method.context_name = self.context_name
            self.methods.append(method)


@attr.s(auto_attribs=True)
class TraitInfo:
    name: str
    class_name: str
    params: typing.List[ServiceParameter] = attr.Factory(list)


class ServiceProcessor:
    def __init__(self):
        pass

    def load(self, source):
        self._source = source["/{projectKey}"]
        self.traits = self._parse_traits(source["traits"])
        self._resource_types = source["resourceTypes"]

    def __iter__(self):
        for path, data in self._source.items():
            if path.startswith("/"):
                yield self._parse_service(path, data)

    def _parse_traits(self, source) -> typing.Dict[str, TraitInfo]:
        result = {}
        for name, data in source.items():
            param_data = data.get("queryParameters", {})
            params = _parse_query_parameters(param_data)
            for param in params:
                param.multiple = True
            result[name] = TraitInfo(
                name=name, class_name=class_name(name), params=params
            )
        return result

    def _parse_service(self, path, source, parent=None):
        domain = ServiceDomain(
            path=path if not parent else parent.path + path,
            parent=parent,
            methods=[],
            description=source.get("description"),
            path_parameters=self._get_parameters(source),
            resource_draft=extract_name(
                _get_value(source, "type", "baseDomain", "resourceDraft")
            ),
            resource_type=extract_name(
                _get_value(source, "type", "baseDomain", "resourceType")
            ),
            resource_querytype=extract_name(
                _get_value(source, "type", "baseDomain", "resourceQueryType")
            ),
        )
        if parent and parent.path_parameters:
            domain.path_parameters = parent.path_parameters + domain.path_parameters
        domain.context_name = domain.resource_type or create_codename(path).title()

        for endpoint, endpoint_data in source.items():
            endpoint_type = _get_item_type(endpoint_data)

            if endpoint_type == "baseDomain":
                child = self._parse_service(endpoint, endpoint_data, domain)
                domain.add_method(*child.methods)
                del child

            elif endpoint in ["post", "get", "delete"]:
                method = self._get_domain_methods(
                    domain, endpoint, endpoint_data, source
                )
                if method:
                    domain.add_method(method)
            elif endpoint.startswith("/"):
                subparams = self._get_parameters(endpoint_data)
                if not subparams:
                    method = self._get_action_method(
                        domain, endpoint, endpoint_data, source, path_params=[]
                    )
                    if method:
                        domain.add_method(method)
                else:
                    for method in self._get_resource_methods(
                        domain, endpoint, endpoint_data
                    ):
                        domain.add_method(method)
        return domain

    def _get_domain_methods(self, service_domain, method, method_data, parent_data):
        method_name = ""
        if service_domain.parent:
            method_name = snakeit(service_domain.context_name) + "_"

        if method == "get":
            method = ServiceMethod(
                name=method_name + "query",
                path=service_domain.path,
                path_params=list(service_domain.path_parameters),
                query_params=[],
                type="query",
                method=method,
                returns=_get_return_type(
                    method_data, service_domain.resource_querytype
                ),
            )
            return self._add_metadata(method, method_data, parent_data)

        elif method == "post":
            method = ServiceMethod(
                name=method_name + "create",
                path=service_domain.path,
                path_params=list(service_domain.path_parameters),
                query_params=[],
                type="create",
                method=method,
                input_type=service_domain.resource_draft,
                returns=_get_return_type(method_data, service_domain.resource_type),
            )
            return self._add_metadata(method, method_data, parent_data)

    def _get_action_method(self, service_domain, path, data, parent_data, path_params):
        if "get" in data and "post" in data:
            if data["post"].get("responses"):
                endpoint_data = data["post"]
                method = "post"
            else:
                endpoint_data = data["get"]
                method = "get"
        elif "post" in data:
            endpoint_data = data["post"]
            method = "post"
        elif "get" in data:
            endpoint_data = data["get"]
            method = "get"
        else:
            return None

        method_name = create_method_name(path)
        if service_domain.parent:
            method_name = snakeit(service_domain.context_name) + "_" + method_name

        method = ServiceMethod(
            name=method_name,
            path=service_domain.path + path,
            path_params=path_params,
            query_params=[],
            type="action",
            method=method,
            input_type=_get_input_type(endpoint_data),
            returns=_get_return_type(endpoint_data, service_domain.resource_type),
        )
        return self._add_metadata(method, endpoint_data, data)

    def _get_resource_methods(self, service_domain, path, data):
        params = list(service_domain.path_parameters)
        params.extend(self._get_parameters(data))
        method_name = "_%s" % snakeit(data["(methodName)"])
        method_name = method_name.replace("with", "by")
        type_name = _get_item_type(data)

        name_prefix = ""
        if service_domain.parent:
            name_prefix = snakeit(service_domain.context_name) + "_"

        for endpoint_path, endpoint_data in data.items():
            if endpoint_path == "post":
                input_type = data["type"][type_name]["resourceUpdateType"]
                method = ServiceMethod(
                    name=name_prefix + "update" + method_name,
                    path=service_domain.path + path,
                    path_params=list(params),
                    type="update",
                    method="post",
                    input_type=service_domain.resource_type + input_type,
                    returns=_get_return_type(
                        endpoint_data, service_domain.resource_type
                    ),
                )
                yield self._add_metadata(method, endpoint_data, data)

            elif endpoint_path == "get":
                method = ServiceMethod(
                    name=name_prefix + "get" + method_name,
                    path=service_domain.path + path,
                    path_params=list(params),
                    type="get",
                    method="get",
                    returns=_get_return_type(
                        endpoint_data, service_domain.resource_type
                    ),
                )
                yield self._add_metadata(method, endpoint_data, data)

            elif endpoint_path == "delete":
                method = ServiceMethod(
                    name=name_prefix + "delete" + method_name,
                    path=service_domain.path + path,
                    path_params=list(params),
                    type="delete",
                    method="delete",
                    returns=_get_return_type(
                        endpoint_data, service_domain.resource_type
                    ),
                )
                yield self._add_metadata(method, endpoint_data, data)

            elif endpoint_path.startswith("/"):
                yield self._get_action_method(
                    service_domain, endpoint_path, endpoint_data, data,
                    path_params=params,
                )

    def _get_parameters(self, data) -> typing.List[ServiceParameter]:
        if isinstance(data, str):
            return []

        if "uriParameters" in data:
            params = []
            for key, val in data["uriParameters"].items():
                param = ServiceParameter(name=key, type=val, required=True)
                params.append(param)
            return params

        type_name = _get_item_type(data)

        if not isinstance(data.get("type"), dict):
            return []

        value = data["type"][type_name].get("uriParameterName")
        if value:
            param = ServiceParameter(name=value, type="string", required=True)
            return [param]
        return []

    def _add_metadata(self, method: ServiceMethod, data, parent_data):
        if isinstance(data, str):
            return method

        method.description = data.get("description", "")
        if parent_data.get("description"):
            method.description += "\n\n" + parent_data["description"].strip()

        type_name = _get_item_type(parent_data)

        traits = []

        # Get traits from base resource
        type_data = self._resource_types[type_name]

        type_data = type_data.get(method.method) or type_data.get(method.method + "?")
        traits.extend(type_data.get("is", []))

        # Missing in raml specs?
        if method.type == "update":
            traits.append("versioned")

        # Get params from traits
        traits.extend(data.get("is", []))
        for trait in traits:
            if isinstance(trait, str):
                trait_info = self.traits[trait]
            else:
                trait_key = list(trait.keys())[0]
                trait_info = self.traits[trait_key]

            method.query_params.extend(trait_info.params)
            method.traits.append(trait_info)

        # Get params specified on method
        params = data.get("queryParameters", {})
        if params:
            method.extra_params = _parse_query_parameters(params)
            method.query_params.extend(method.extra_params)

        # Check if this is a file upload (?)
        if data.get("body", {}).get("type") == "file":
            method.is_fileupload = True
            method.query_params.append(
                ServiceParameter(name="fh", type="file", required=True, extra_data=None)
            )

        # De-duplicate param names
        deduplicated = {}
        for param in method.query_params:
            deduplicated[param.name] = param
        method.query_params = list(deduplicated.values())

        return method


def _parse_query_parameters(params):
    result = []
    for name, value in params.items():
        required = value.get("required", True)
        if name.endswith("?"):
            name = name[:-1]
            required = False

        param = ServiceParameter(
            name=name,
            type=value.get("type", "string"),
            required=required,
            extra_data=value,
        )
        result.append(param)
    return result


def _get_value(data, *keys):
    val = data
    for key in keys:
        try:
            val = val[key]
        except (KeyError, TypeError):
            return None
    return val


def _get_input_type(data, default=None):
    for code in [200, 201]:
        try:
            return data["body"]["application/json"]["type"]
        except (KeyError, TypeError):
            continue
    return default


def _get_return_type(data, default=None):
    for code in [200, 201]:
        try:
            return data["responses"][code]["body"]["application/json"]["type"]
        except (KeyError, TypeError):
            continue
    return default


def _get_item_type(data):
    if isinstance(data, str):
        return "base"
    try:
        typeval = data.get("type")
        if not typeval:
            return "base"
        if isinstance(typeval, str):
            return typeval
        return list(typeval.keys())[0]
    except (TypeError, KeyError):
        pass
    return "base"

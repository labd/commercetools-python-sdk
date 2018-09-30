from .gen import TypeProcessor
from .yaml import read_raml_file


def parse_raml_file(filename):
    data = read_raml_file(filename)
    types = TypeProcessor()
    types.load(data["types"])
    return {"types": types, "resources": data}

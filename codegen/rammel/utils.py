import keyword
import re


def snakeit(name):
    if not name:
        return
    # https://stackoverflow.com/questions/1175208/
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    val = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
    if keyword.iskeyword(val):
        val = val + "_"
    return val

from uonrevisedtypes.uon_value import UonValue
from uonrevisedtypes.uon_custom_type import UonCustomType


def python_to_uon(input_):
    """Convert an input to uon. If the input is one of the uon-parser defined
    custom Uon Python objects, instance of UonBase just return the string 
    representation which is the equivalent representation of the object
    in Uon.

    Otherwise if it is a built-in type, convert it to its closest equivalent
    in Uon. For numeric types precision is by default 64. For container types,
    the function is called recursively on its content.

    No support for remaining built-in types, especially bytes, since Uon
    has its own binary interpretation.

    Args:
        input_ (object): the Python object to serialize to uon
    """
    # TODO: check if uon type in general
    if isinstance(input_, UonValue) or isinstance(input_, UonCustomType):
        return str(input_)
    elif isinstance(input_, dict):
        dict_to_uon = {}
        for k, v in input_.items():
            if not isinstance(k, str):
                raise UonSerializerError("Uon dictionary keys must be "
                                         "hashable strings.")
            dict_to_uon[k] = python_to_uon(v)
        return ("{"
                + ", ".join("{}: {}"
                            .format(k, v) for k, v in dict_to_uon.items())
                + "}")
    elif isinstance(input_, list):
        return "[" + ", ".join(list(map(python_to_uon, input_))) + "]"
    elif isinstance(input_, int):
        return f"!int64 {input_}"
    elif isinstance(input_, float):
        return f"!float64 {input_}"
    elif isinstance(input_, str):
        return f"!str {input_}"
    elif isinstance(input_, bool):
        bool_result = "true" if input_ else "false"
        return f"!bool {bool_result}"
    elif input_ is None:
        return "null"
    else:
        raise ValueError("Unsupported type")


class UonSerializerError(Exception):
    pass

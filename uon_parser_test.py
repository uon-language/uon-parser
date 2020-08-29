from uon_parser import (
    validate, load, dump,
    UonParser
)

schema = """
!!person: !schema {
    name (description: name of the person, optional: false): !str(min:3,
     max:25),
    age: !uint(min: 0, max: 125),
    minor (optional: false): !bool,
    linkedin link: !url
}
"""

schema_validation = """
{p: !!person {
        name: Stephane,
        age: !uint32 135,
        minor: !bool true
    }
}
"""

schema_with_quantity = """
!!temperature: !schema {
    t(description: The temperature of the room): !int (quantity: temperature)
}
"""

schema_with_quantity_validation = """
{t: !!temperature {
    t: !int 32 K
    }
}

"""


def parser_test():
    validate(schema_validation, schema_raw=schema,
             show_tree=True, debug=True)
    validate(schema_with_quantity,
             schema_raw=None, debug=False)

    uon = UonParser()
    uon.load(schema_with_quantity_validation)
    uon.load_schema(schema_with_quantity)
    uon.load(schema_with_quantity_validation)


if __name__ == '__main__':
    parser_test()

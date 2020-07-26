from uon_parser import (
    validate, load, dump,
    UonParser
)

test_schema = """
!!person: !schema {
    name (description: name of the person, optional: false): !str(min:3,
     max:25),
    age: !uint(min: 0, max: 125),
    minor (optional: false): !bool,
    linkedin link: !url 
}
"""

test_schema_validation = """
{p: !!person {
        name: Stephane, 
        age: !uint32 25,
        minor: !bool true,
        linkedin link: www.google.com
    }
}
"""

test_schema_with_quantity = """
!!temperature: !schema {
    t(description: The temperature of the room): !int (quantity: temperature)
}
"""

test_schema_with_quantity_validation = """
{t: !!temperature {
    t: !int 32 km
    }
}

"""


def test():
    validate(test_schema_with_quantity,
             schema_raw=None, debug=False)
    
    uon = UonParser()
    uon.load(test_schema_with_quantity_validation)
    uon.load_schema(test_schema_with_quantity)
    uon.load(test_schema_with_quantity_validation)
    

if __name__ == '__main__':
    test()

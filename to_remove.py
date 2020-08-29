import uon_parser

test_user_type = """
{
    p : !!person {
    name: John,
    age : !uint32 59
    }
}
"""

test_person_schema = """
!!person: !schema {
    name (description: name of the person): !str(min:3, max:25),
    age (optional: True): !uint(min: 0, max: 125),
    minor: !bool
}
"""

p = uon_parser.load(test_user_type)
uon_parser.dump_to_file(p, filename="person.uon")
uon_parser.to_binary(test_user_type)
uon_parser.validate(test_user_type, test_person_schema)

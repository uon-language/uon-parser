# uon-parser
A parser for UON written in Python.

UON ™ (short for Unified Object Notation) is a serialization format that aims to bring together the best features of all available serialization formats out there, to create the one to unify them all. 

Features of Uon:
- JSON-style grammar or YAML-style grammar.
- Unambiguous grammar.
- Schema and data validation.
- Binary encoding and minimal payload size.

[See here for UON specs](https://github.com/uon-language/specification/blob/master/spec.md)

Note that this parser is still a work in progress and is in early stages of development.

## Quick Start

The main module is accessible from `uon_parser.py`. The interface offers the following methods:
- `parse(input)`: parse UON in a correctly formatted python string and returns the corresponding python object.
- `load(filename)`: read a uon file, parse it and return the corresponding python object.

- `load`: parse a raw (string) uon input.
- `load_from_file`: parse a uon input from file.
- `dump`: Dump a Python built-in object or a Uon type object to Uon. Returns the result as a string.
- `dump_to_file`: Same as `dump` but writes it to a file.
- `validate`: Take a raw uon input as well as a raw schema and validates
the input with the schema.
- `to_binary`: encodes a raw uon input to binary.
- `from_binary`: decodes a uon-encoded binary_input and returns the corresponding Uon Object.

The interface offers as well a class `UonParser`. The `UonParser` provides the above methods. In reality,  the above methods instantiate at each time a `ÙonParser` and call the corresponding method from this class. But it's advantageous to have a parse a `UonParser` instance, since it keeps track of all the schemas you parse and it uses them to validate future input.


To start the project in develop mode, you can start by installing the dependencies from `requiremenets_dev.txt`:
```
pip install -r requirements_dev.txt
```

Now you can start experimenting with the library in your favourite Python IDE or in a REPL.

For example (after having the installed the requirements):

Open a python REPL interface: 

```
python -i uon_parser.py
```

Create a UON parser instance:

```
u = UonParser()
```

Then parse the `example.uon` file that is provided with the repo:

```
t = u.load_from_file('example.uon')
print(t)
```

Try to write your own uon file and parse it. 

## Schema validation
In UON, you can define schemas to validate your data. With schemas you can define a custom type, with each field having a uon type and certain properties that it must validate. Currently the only native data types readily supported are:
- Float32, Float64: 32 and 64 bit precision floating point numbers.
- Integer32, Integer64: 32 and 64 bits integer numbers.
- Uint32, Uint64: 32 and 64 bits unsigned integer numbers.
- UonBoolean
- UonString
- UonUrl
- UonNull
- UonMapping
- UonSeq

**N.B.**: All UON numeric datatypes Python objects encapsulate the value that is actually represented using numpy. For example, a Float64 instance contains a numpy.float64.

Here is an example of a schema definition:
```
!!person: !schema {
    name (description: name of the person): !str(min:3, max:25),
    age (optional: False): !uint(min: 0, max: 125),
    minor: !bool
}
```

This defines a schema for a custom type `person`, which describes a person having a name of `str` (string) type of length 3 to 25 characters, an age of `uint` (unsigned integer) type ranging from 0 to 125 and a minor flag that is described by a `bool` (boolean). The `optional` property on some of the fields like `age` mark it as optional or not, that means an instance of that type must define that field if the `optional` property is set to false. By default, `optional` is set to false.

Any instance of type `person` must verify the above properties, otherwise the proper exception will be raised.

Here is an example of a valid `person` instance in UON:

```
{
    p : !!person {
    name: John,
    age : !uint32 59
    }
}
```

Here is an example of a `person` instance that doesn't validate the above schema:
```
{
    p : !!person {
    name: John,
    age : !uint32 130,
    minor: True
    }
}
```
We can verify this against the above schema using the `validate` method from our interface:

```
import uon_parser

uon_parser.validate(
    """{
        p : !!person {
        name: John,
        age : !uint32 130,
        minor: True
        }
    }""", schema_raw="""!!person: !schema {
            name (description: name of the person): !str(min:3, max:25),
            age (optional: True): !uint(min: 0, max: 125),
            minor: !bool
    }"""
)
```

This would trigger the following exception `MaxNumberValidationError: The following input !uint32 130 is bigger than 125`


The current supported properties are:
- Maximum and minimum numeric quantities.
- Maximum and minimum length strings.
- Type validations for native UON types except for collection types.

## Binary encoding
UON comes in textual format but also comes with binary encoding. Every UON type has its binary encoding (refer to the [different binary encodings in ](binary/binary_serialization.uon) `binary` package).

Here is an example of a binary encoding:
```
import uon_parser

test_user_type = """
{
    p : !!person {
    name: John,
    age : !uint32 59
    }
}
"""

uon_parser.to_binary(test_user_type)
```

which gives `\x02\x12\x01\x00p\x1a\x06\x00person\x02\x12\x04\x00name\x11\x04\x00John\x12\x03\x00age9;\x00\x00\x00\x00\x00\x00`.

Each UON object has its own binary encoding, and the encoding happens recursively.

# Acknowledgement
The grammar and the parser for UON for this library have been implemented using the excellent [lark parser](https://github.com/lark-parser/lark) available on Python. Lark is a parsing toolkit in Python, that can parse any context-free grammars. It is very user-friendly and a very compelling choice for beginners and experts in CFG alike. 

Notice how you can write the whole grammar for your language in a `lark` grammar file aside with no code involved. Needless to say, Lark has many more features. The author has done a great job implementing a parsing toolkit to make your life easier and just focus on the grammar of your language. I cannot recommend it enough. Check out its github page [here](https://github.com/lark-parser/lark) as well as the [gitter forum](https://gitter.im/lark-parser/Lobby) for all that is Lark.

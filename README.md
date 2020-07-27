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

## Binary encoding
[TODO]

## Schema validation
[TODO]
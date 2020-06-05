# uon-parser
A parser for UON written in Python.

UON ™ (short for Unified Object Notation) is a serialization format that aims to bring together the best features of all available serialization formats out there, to create the one to unify them all. 

[See here for UON specs](https://github.com/uon-language/specification/blob/master/spec.md)

Note that this parser is still a work in progress and is in early stages of development.

## Quick Start

The main module is accessible from `uon.py`. With it you can use it parse uon to python objects. The interface at the moment offers the following methods:
- `parse(input)`: parse UON in a correctly formatted python string and returns the corresponding python object.
- `load(filename)`: read a uon file, parse it and return the corresponding python object.

For example:

Open a python REPL interface: 

```
python -i uon.py
```

Create a UON parser instance:

```
u = UON()
```

Then parse the `examples.uon` file that is provided with the repo:

```
t = u.load('example.uon')
print(t)
```

Try to write your own uon file and parse it. At the moment, the following uon features are supported:
- YAML-like indented dictionaries and sequences 
- Dictionary key-value pairs with key properties such as `description` and `optional`.
- Scalar values with basic type coercion between the following types: Float128, Float64, Float32, Int32, Int64, Int128, String.

This list will be updated accordingly.
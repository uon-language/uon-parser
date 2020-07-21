import re
import pprint

numpy_docstring = """
My numpydoc description of a kind
of very exhautive numpydoc format docstring.

Parameters
----------
first : array_like
    the 1st param name `first`
second :
    the 2nd param
third : {'value', 'other'}, optional
    the 3rd param, by default 'value'

Returns
-------
string
    a value in a string

Raises
------
KeyError
    when a key error
OtherError
    when an other error
"""

tel = {'jack': 4098, 'sape': 4139}
print(tel["jack"])

data = [('key', ['item0', 'item1', 3.14])]

d = dict(data)

tup = ('Jackie', 4000)
# dict keys can also be strings since strings are hashable
tup2 = ('Jacko Lo', 4400)
d2 = dict([tup, tup2])
print(d2)
print(d2['Jacko Lo'])

ls = [1, 2, None]

print("==================================================")

class A:
    def __init__(self, otherObject):
        otherObject.doSomething()
        self.otherObject = otherObject

    def doSomething(self):
        print("do Something in A")


class B:
    def doSomething(self):
        print("do Something in B")


class C:
    def doSomething(self):
        print("do Something in C")


b = B()
c = C()
a = A(c)

print("==================================================")


class E:
    def __init__(self, att1, att2=None):
        self.att1 = att1
        self.att2 = att2

    def __repr__(self):
        return "att1: {}, att2: {}".format(
            self.att1, self.att2
        )


class F(E):
    def __init__(self, att1, att3,  att2=None):
        super().__init__(att1, att2)
        self.att3 = att3

    def __repr__(self):
        return super().__repr__() + ", att3: {}".format(
            self.att3
        )

e = E(2)
f = F(2, 3, att2=5)

print(e)
print(f)

print("==================================================")

indented = """
  hello
    bye
  Ok
"""
left_braced = re.sub('\n\s+', "{", indented)
right_braced = re.sub('\s+\n', "}", indented)
print(left_braced)


def replaceSpaces(multiline, pastSpaces, result):
    if (multiline == []):
        return result + "}"
    else:
        head, tail = multiline[0], multiline[1:]
        print(head)
        print(tail)
        numberOfSpaces = getWhitespaces(head)
        print(numberOfSpaces)
        if (numberOfSpaces > pastSpaces):
            return replaceSpaces(tail, numberOfSpaces, result + "\n{" + head)
        elif (numberOfSpaces < pastSpaces):
            return replaceSpaces(tail, numberOfSpaces, result + "}\n{" + head)
        else:
            return replaceSpaces(tail, numberOfSpaces, result + "\n" + head)


def getWhitespaces(s):
    return len(s) - len(s.lstrip(' '))


print(replaceSpaces(indented.splitlines(), 0, ""))

print(type((tel, [])))


print("==================================================")


class L:
    @staticmethod
    def doL():
        """
        This is a long method documentation to see how
        it prints out when we use the built-in __doc__ method
        """
        pass


print("==================================================")
print("None argument does not evaluate to its default value in constructor")


class M:
    def __init__(self, d={}):
        self.d = d


i = M(None)
print(i.d)

print("==================================================")
print("Containers calling repr on contained objects")


class PrettyPrinter2(pprint.PrettyPrinter):
    def _format_dict_items(self, items, stream, indent, allowance, context,
                           level):
        write = stream.write
        indent += self._indent_per_level
        delimnl = ',\n' + ' ' * indent
        last_index = len(items) - 1
        for i, (key, ent) in enumerate(items):
            last = i == last_index
            rep = self._repr(key, context, level)
            write(rep)
            write(': ')
            self._format(str(ent), stream, indent + len(rep) + 2,
                         allowance if last else 1,
                         context, level)
            if not last:
                write(delimnl)


class H:
    def __str__(self):
        return "This is my H class string representation"

    def __repr__(self):
        return "H()"
    #__repr__ = __str__


m = [H(), H(), H()]
print(m)
s = ""
for h in m:
    s += str(h)

print(s)

m = map(lambda x: str(x), m)
print(",".join(m))

d = {
    'a': H(),
    'b': {
        'c': H(),
        'd': H()
    }
}

d_simple = {
    'a': H(),
    'b': H()
}

pp2 = PrettyPrinter2()
print("\n")
print("With Pretty Printer2: ")
print(pp2.pformat(d_simple))
pp2.pprint(d)
pprint.pprint(d)

print("\n")
print("d_simple: ")
print("{" + "\n".join("{!r}: {!s},".format(k, v) for k, v in d.items()) + "}")

print("Pretty printed d: ")
pprint.pprint(d, width=10)

d_prepped = {k: str(v) for k, v in d.items()}
print("d_prepped", d_prepped)

d = {"two": 2, "a": {"one": 1, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8}}
print(d)
pprint.pprint(d)

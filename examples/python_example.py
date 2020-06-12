import re

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

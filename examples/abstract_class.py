from abc import ABC, abstractmethod


# TODO: evacuate examples folder
class A(ABC):
    @abstractmethod
    def do(self):
        print("hello")


class B(A):
    @abstractmethod
    def do(self):
        super().do()
        print("Hello I'm also B")

    @abstractmethod
    def doB(self):
        super().do()


class C(B):
    def do(self):
        super().do()
        print("I'm C")

    def doB(self):
        super().doB()
        print("I'm not B")

    def __str__(self):
        return "C"

    def __repr__(self):
        return "C()"


class D:
    """
    It's a class D
    """
    def __init__(self, q, p):
        self.q = q
        self.p = p

    def do(self):
        print("I'm D")


c = C()
c.do()
print(B.__dict__)
d = {"c": c}
print(c)
print(d)

#b = object.__new__(B)

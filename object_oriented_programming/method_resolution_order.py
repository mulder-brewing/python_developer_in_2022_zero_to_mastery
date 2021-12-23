class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


# order of B, C matter to MRO
class D(B, C):
    pass


# MRO is D, B, C, A, object
print(D.mro())
print(D().num)


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


# Depth first search algorithm
print(M.mro())

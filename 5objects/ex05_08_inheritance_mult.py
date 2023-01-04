# Moniperintä

class A:
    def f(self):
        print("A")


class B(A):
    pass  # Tämä vaikuttaa moniperintään
    #
    # def f(self):
    #     print("B")


class C(A):
    def f(self):
        print("C")


class D(A):
    def f(self):
        print("D")


class E(B, C, D, A):
    pass


class G(D, C, B):
    pass


class H(B, C):
    def f(self):
        print("H")


e = E()
print(e)
e.f()

g = G()
print(g)
g.f()

h = H()
print(h)
h.f()

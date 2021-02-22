# Depth first MRO
class A(object):
    def do_this(self):
        print('A is doing')

class B(A):
    pass

class C(object):
    def do_this(self):
        print('B is doing')

class D(C, B):
    pass

d_instance = D()
d_instance.do_this()

print(D.mro()) # [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]


# Diamond shape MRO
class P(object):
    def do_this(self):
        print('P is doing')

class Q(P):
    pass

class R(P):
    def do_this(self):
        print('R is doing')

class S(Q, R):
    pass

d_instance = S()
d_instance.do_this()

print(S.mro()) # [<class '__main__.S'>, <class '__main__.Q'>, <class '__main__.R'>, <class '__main__.P'>, <class 'object'>]
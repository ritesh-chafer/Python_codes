# Diamond shape problem in inheritance = Which method is used by which class 

class A:
    def met(self):
        print("This is method from class A")

class B(A):
    def met(self):
        print("This is method from class B")

class C(A):
    def met(self):
        print("This is method from class C")

class D(B,C):
    def met(self):
        print("This is method from class D")

a = A()
b = B()
c = C()
d = D()

d.met()
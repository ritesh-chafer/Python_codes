# super() and overriding in class
class A:
    classvar1 = "I am a calss variable in class A"
    def __init__(self):
        self.var1 = "I am insde clas A's constructor"
        self.classvar1 = "Instance variable in class A"
        self.special = "special"
        
class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        self.var1 = "I am insde clas B's constructor"
        self.classvar1 = "Instance variable in class B"
        super().__init__()
        print(super().classvar1)

    
    
a = A()
b = B()

print(b.special, b.var1, b.classvar1)
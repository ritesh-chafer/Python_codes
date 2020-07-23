# super() and overriding in class
class A:
    classvar1 = "I am a calss variable in class A"
    def __init__(self):
        self.var1 = "I am insde clas A's constructor"
        
class B(A):
    classvar2 = "I am in class B"
    
    
a = A()
b = B()
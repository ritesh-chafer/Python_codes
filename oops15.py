# abstract base class

from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0
        
class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    
    def __init__(self):
        self.length = 6
        self.breadth = 4
            
    def printarea(self):
        return self.length * self.breadth
    
r = Rectangle()
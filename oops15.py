# abstract base class

class Rectangle:
    type = "Rectangle"
    sides = 4
    
    def __init__(self):
        self.length = 6
        self.breadth = 4
            
    def printarea(self):
        return self.length * self.breadth
    
r = Rectangle()
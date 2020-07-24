# Operator Overloading and Dunder method
# Method starting with "__" and ending with "__" is known as dunder method e.g., "__init__ "(known as dunter init) and helps in operator overloading

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
    def __add__(self, other):
        return self.salary + other.salary
        
emp1 = Employee("Harry", 777, "Programmer")
emp2 = Employee("Ritesh", 545, "Learner")

print(emp1 + emp2)
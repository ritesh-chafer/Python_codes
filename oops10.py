# concept for Public, Protected and Private access specifiers

class Employee:
    no_of_leaves = 8
    var = 8                            # Public variable (Simple nomenclature)  Any class can acess this
    _protected_var = 9                 # Protected variable (starts with a underscore "_")  Only derived vclass can access this
    __private_var = 10                 # Private variable (starts with double underscore "__")   No one can access excpet the parent class

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
        
    @classmethod
    def from_dash(cls, string):                        #constructor
        # params = string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
    
    @staticmethod
    def printgood(string):
        print("This is good", string)

emp = Employee("Harry", 455, "Instructor")
print(emp._protected_var)
print(emp._Employee__private_var)                  # To print private variable we add "_EMployee" or "_classname"
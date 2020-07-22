# Static method

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
        
    @classmethod
    def from_dash(cls, string):                        #constructor
        # params = string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
    
    @staticmethod
    def printgood(string):
        print("This is good", string)

class Programmer(Employee):
    def __init__(self, aname, asalary, arole, alaunage):
        super().__init__(aname, asalary, arole)
        self.languages = alaunage
        
    def printprog(self):
        return f"The Programmer's name is {self.name}, salary is {self.salary} and role is {self.role}. He do programming in {self.languages}"

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rofhan", 455, "student")
shubham = Programmer("Shubham", 555, "Programmer",["Python"])
rahul = Programmer("Rahul", 700, "Programmer", ["Python", "C++"])

print(rahul.printprog())
print(rahul.printdetails())
print(rahul.printgood("Hello"))
print(":::::::")
print(shubham.printprog())

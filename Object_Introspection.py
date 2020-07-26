# Object Introspection

# Setters & Property Decorators

class Employee:
    def __init__(self, f_name, l_name):
        self.fname = f_name
        self.lname = l_name
        # self.email = f"{self.fname}.{self.lname}@chafer.com"
        
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    @property
    def email(self):
        if self.fname== None or self.lname == None:
            return "Email is not set. Please set it using setter."
        return f"{self.fname}.{self.lname}@chafer.com"
    
    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]\
    
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("Skill", "F_")

# print(skillf.email)
print(type(skillf))
print(id(skillf))

x = "This is a string"
print(id("This is a string"))
print(dir(x))

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
    
E1 = Employee("Rahul", "Singh")
E2 = Employee("Raj", "Kapoor")

print(E1.email)

E1.fname = "Mayank"

print(E1.email)

E1.email = "this.that@chafer.com"

del E1.email

print(E1.email)

E1.email = "Harry.Perry@chafer.com"
print(E1.email)
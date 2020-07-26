# Setters & Property Decorators

class Employee:
    def __init__(self, f_name, l_name):
        self.fname = f_name
        self.lname = l_name
        # self.email = f"{self.fname}.{self.lname}@chafer.com"
        
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    def email(self):
        return f"{self.fname}.{self.lname}@chafer.com"
    
    
    
E1 = Employee("Rahul", "Singh")
E2 = Employee("Raj", "Kapoor")

print(E1.email())

E1.fname = "Mayank"

print(E1.email())
class Employee:
    def __init__(self, f_name, l_name):
        self.fname = f_name
        self.lname = l_name
        
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    def printemail(self):
        pass
    
E1 = Employee("Rahul", "Singh")
E2 = Employee("Raj", "Kapoor")

print(E1.explain())
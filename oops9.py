# Multilevel Inheritance

class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes I dance {self.dance} number of times."

class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"I love Jackson!" \
            f"Yes I dance too {self.dance} number of times."
            
harry = Dad()
marrie = Son()
jenny = Grandson() 

print(jenny.isdance())
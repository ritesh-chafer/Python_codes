# Multiple Inheritence

class Employee:
    no_of_leaves = 8
    var = 8

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

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, pname, pgame):
        self.name = pname
        self.game = pgame
    
    def printdetails(self):
        return f"The name is {self.name}. Game is {self.game}"
    
class Cool_programmer(Employee, Player):
    var = 10
    language = "C++"
    def printlanguage(self):
        print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rofhan", 455, "student")
ritesh = Player("Ritesh", ["Cricket", "Football", "Chess"])
sourav = Cool_programmer("Sourav", 800, "CoolProgrammer")


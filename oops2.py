class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 5000
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 2000
rohan.role = "Student"

print(harry.name,end=" ")
print(harry.role,end=" ")
print(harry.no_of_leaves)

print(rohan.name,end=" ")
print(rohan.role,end=" ")
print(rohan.no_of_leaves)


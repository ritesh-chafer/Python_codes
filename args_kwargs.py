def funargs(normal,*args, **kwargs):          #args can named anything like "n" and always placed after the normal argument
    print(type(args))   #args are taken as tuple irrespective of the type
    print(normal)
    print(args)
    print(args[0])
    print(args[2])
    print(args[4])
    print("......")
    for item in args:
        print(item)
    print("......")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
    
    

Objects = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam", "The Programmer"]
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor", "The Programmer":"Coordinater"}

marks = 90

funargs(marks,*Objects, **kw)
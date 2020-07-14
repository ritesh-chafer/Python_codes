def funargs(normal,*args):          #args can named anything like "n" and always placed after the normal argument
    print(type(args))   #args are taken as tuple irrespective of the type
    print(normal)
    print(args)
    print(args[0])
    print(args[2])
    print(args[4])
    print("......")
    for item in args:
        print(item)
    
    

Objects = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam", "The Programmer"]

marks = 90

funargs(marks,*Objects)
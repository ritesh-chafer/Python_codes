def funargs(*args):
    print(type(args))   #args are taken as tuple irrespective of the type
    print(args)
    
Objects = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam", "The Programmer"]

funargs(*Objects)
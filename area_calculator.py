import math
print("Menu")
print("""1.Area of Rectangle
    1(a).Area through length and breadth
    1(b).Area through diagonals 
2.Area of squares
    2(a).Area through side
    2(b).Area through diagonal 
3.Area of circle""" )

def choose():
    print(input("Enter to continue....."))
    Value = input("Enter the option from menu:")
    return Value

item = choose()

if(item == "1"):
    print("""1.Area rectangle
        1(a).Area through length and breadth
        1(b).Area through diagonals""" )
    print(input("Enter to continue....."))

if(item == "1(a)"):
    print("1(a).Area through length and breadth")
    length = int(input("Enter Length:"))
    width = int(input("enter Width:"))
    area = length * width
    print(area)

if(item == "1(b)"):
    print("1(b).Area through Diagonals")
    d1 = int(input("Enter first diagonal:"))
    d2 = int(input("Enter second diagonal:"))
    area = math.sqrt(d1 ** 2 + d2 ** 2)
    print(area)

if(item == "2"):
    print("""2.Area of Square
        2(a).Area through side
        2(b).Area through diagonal""" )
    print(input("Enter to continue....."))

if(item == "2(a)"):
    print("2(a).Area through side")
    side = int(input("Enter length of side:"))
    area = math.pow(side,2)
    print(area)

if(item == "2(b)"):
    print("2(b).Area through Diagonals")
    d = int(input("Enter length of diagonal:"))
    area = math.pow(2,1/2)*d
    print(area)
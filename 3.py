#inp = input('Enter Fahrenheit Temperature: ')
#try:
#    fahr = float(inp)
#    cel = (fahr - 32.0) * 5.0 / 9.0
#    print(cel)
#except:
#    print('Please enter a number')
#


#try:
#    Hours = int(input("Enter Hours: "))
#    Rate = int(input("Enter Rate: "))
#    if Hours > 40:
#        Pay = (40 * Rate) +((Hours - 40) * Rate * 1.5)
#    else:
#        Pay = Hours * Rate
#    Pay = round(Pay,1)
#    print("Pay: ", Pay)
#except:
#    print("Please enter numeric digit")

try:

    n = float(input("Enter score: "))

    if n >= 0.9:
        print("A")
    elif n >= 0.8:
        print("B")
    elif n >= 0.7:
        print("C")
    elif n >= 0.6:
        print("D")
    elif n < 0.6:
        print("F")
    else:
        print("Bad score")
except:
    print(" ")

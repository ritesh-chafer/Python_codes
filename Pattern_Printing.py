R= int(input("Enter Row: "))
N = int(input("Enter Boolean 1/0 :"))
b = bool(N)
if b:
    for i in range(R):
        print("*" * i)
else:
    for j in range(R):
        print((R-j) * "*")
# def function1():
#     print("Decorators")
    
# func2 = function1
# del function1
# func2()

def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return int
a = funcret(1)
print(a)
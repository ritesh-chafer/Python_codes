# def function1():
#     print("Decorators")
    
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return int
# a = funcret(1)
# print(a)

# def executor(func):
#     func("this")
    
# executor(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("func1 executed")
    return nowexec

@dec1
def who_is_ritesh():
    print("He is a good boy")
    
# who_is_ritesh = dec1(who_is_ritesh)

who_is_ritesh()
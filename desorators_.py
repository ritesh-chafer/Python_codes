def function1():
    print("Decorators")
    
func2 = function1
del function1
func2()
t = int(input("Enter number of test cases: "));
for i in range(0, t): 
    X = [] 
    N = int(input("Enter number of elements : ")) 
    for j in range(0, N): 
        ele = int(input()) 
        X.append(ele)
    min = 0
    max=0
    if (len(X) <= 2):
        if (len(X) == 1):
            min = 1
            max = 1
            print(min, max)
        elif (((X[i] - X[i + 1]) > 2) or ((X[i + 1] - X[i]) > 2)):
            min = 1
            max = 1
            print(min, max)
        elif (((X[i] - X[i + 1]) <= 2) or ((X[i + 1] - X[i]) <= 2)):
            min = 1
            max = 2
            print(min, max)

            
            

        




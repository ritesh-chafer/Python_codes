import time

initial = time.time()
print(initial)
k = 0
while(k<45):
    print(f"Hi {k}")
    k+=1
print(time.time()-initial,"seconds")
    
initial2 = time.time()
for i in range(45):
    print("Hi")
    k+=1
print(time.time()-initial2,"seconds")
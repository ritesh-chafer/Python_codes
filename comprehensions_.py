# python comprehensions

# ls = []
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)
        
# ls = [i for i in range(100) if( i%3 == 0)]        

# print(ls)

dict = {i:f"item{i}" for i in range(1000) if i%100==0}
print(dict)
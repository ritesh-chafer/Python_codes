# python comprehensions

# ls = []
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)
        
# ls = [i for i in range(100) if( i%3 == 0)]        

# print(ls)

dict = { i:f"Item{i}" for i in range(5) }
dict1 = { value:key for key,value in dict.items() }
print(dict, "\n", dict1)
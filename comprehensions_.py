# python comprehensions(list, dict, set)

# ls = []
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)
        
# list comprehension
# ls = [i for i in range(100) if( i%3 == 0)]        
# print(ls)

# dict comprehension
# dict = { i:f"Item{i}" for i in range(5) }
# dict1 = { value:key for key,value in dict.items() }
# print(dict, "\n", dict1)


# set comprehension
dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress3", "dress0", "dress2", "dress4"]}
print(dresses)

"""
Iterable => __iter__() or __getitem__()
Iterator => __next__()
Iteration => 

"""

def gen(n):
    for i in range(n):
        yield i
        
g = gen(20)
print(g)
"""
Iterable => __iter__() or __getitem__()
Iterator => __next__()
Iteration => 

"""

def gen(n):
    for i in range(n):
        yield i
        
g = gen(4)
print(g.__next__())
print(g.__next__())



# numbers = ["3","4","1"]

# numbers = list(map(int, numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1

# print(numbers[2])

# num = [1,2,3,4,5,6,7,8,9]
# square = list(map(lambda x:x*x,num))
# print(square)

# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func = [square,cube]
# numbers = ["3","4","1"]

# for i in range(5):
#     val = list(map(lambda x:x(i),func))
#     print(val)

# list_1 = [1,2,3,4,5,6,7,8,9]

# def is_greater_5(num):
#     return num>5

# gr_than_5 = list(filter(is_greater_5, list_1))
# print(gr_than_5)

#------------REDUCE----------

from functools import reduce

list1 = [1,2,3,4]

# num = 0
# for i in list1:
#     num = num + i
# print(num)

num = reduce(lambda x,y: x + y, list1)
print(num)
numbers = ["3","4","1"]

numbers = list(map(int, numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1

# print(numbers[2])

num = [1,2,3,4,5,6,7,8,9]
square = list(map(lambda x:x*x,num))
print(square)
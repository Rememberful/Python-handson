# double = lambda x: x * 2
# print(double(5))

# sum = lambda a, b, c: a + b + c
# print(sum(1, 2, 3))

# print((lambda x: x ** 2)(4))

# def cube(x):
#     return x*x*x
# old = [1,2,3,4,5]
# new = list(map(cube,old))
# print(new)

# numbers = [1, 2, 3, 4, 5]
# def square(x):
#     return x * x
# result = map(square, numbers)
# print(list(result))

# numbers = [1, 2, 3, 4, 5]
# result = map(lambda x: x * x, numbers)
# print(list(result))

# numbers = [1, 2, 3, 4, 5, 6]
# def is_even(x):
#     return x % 2 == 0
# result = filter(is_even, numbers)
# print(list(result))

# numbers = [1, 2, 3, 4, 5, 6]
# result = filter(lambda x: x % 2 == 0, numbers)
# print(list(result))

# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# def add(x, y):
#     return x + y
# result = reduce(add, numbers)
# print(result)

from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)






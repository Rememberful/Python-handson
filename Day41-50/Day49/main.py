# # def get_numbers():
# #     return [1, 2, 3, 4, 5]

# def count_up_to(n):
#     yield 1
#     yield 2
#     yield 3
# gen = count_up_to(3)
# print(gen)          # <generator object>
# print(next(gen))    # 1
# print(next(gen))    # 2
# print(next(gen))    # 3
# # next(gen)           # StopIteration error

# cache = {}
# def add(a, b):
#     if (a, b) in cache:
#         return cache[(a, b)]
#     result = a + b
#     cache[(a, b)] = result
#     return result
# add(3,4)
# add(4,5)
# print(cache)

# from functools import lru_cache
# @lru_cache
# def add(a, b):
#     print("Computing...")
#     return a + b
# print(add(2, 3))  # Computing... → 5
# print(add(2, 3))  # Cached → 5

# import re
# result = re.search("Python", "I love Python")   # ✔ Match
# result2 = re.match("Python", "I love Python")    # ❌ No match
# print(result)
# print(result2)

import re
result = re.split(r"[,\s]+", "apple, banana orange")
print(result)


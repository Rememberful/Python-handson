# t = (10, 20, 30, 40)
# print(t[0])    # 10
# print(t[-1])   # 40

# t = (10, 20, 30, 40, 20, 30)
# res = t.index(20, 1, 5)
# print(res)

# t = (10, 20, 30, 40, 20, 30)
# print(len(t))

# t1 = (10, 20, 30)
# t2 = (40, 50, 60)
# t3 = t1 + t2
# print(t3)

# t = (1, 2)
# print(t * 3)

# a = (1, 2, 3)
# b = (1, 2, 4)

# print(a == b)
# print(a < b)

t = (1, 2, 3)

lst = list(t)
lst.append(4)
t = tuple(lst)
print(t)



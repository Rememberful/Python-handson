# l = [1,2,6]
# print(l)  # Output: [1, 2.6]
# l.append(3)
# print(l)  # Output: [1, 2.6, 3]

# l.sort(reverse=True)
# l.reverse()


# l = [44,5,4,388]
# print(l.index(4))
# print(l.index(388))

# l = [3,4,5,6,7,7,8,8,8,8,8]
# print(l.count(8))  # Output: 5

# l = [1,2,3]
# m = l
# m[0] = 0
# print(l)  # Output: [0, 2, 3]
# print(m)  # Output: [0, 2, 3]

# l = [3,4,5,6]
# m = l.copy()
# m[0] = 0
# print(l)  # Output: [3, 4, 5, 6]
# print(m)  # Output: [0, 4, 5, 6]

# l = [4,5,6]
# l.insert(1, 10)
# print(l)  # Output: [4, 10, 5, 6]

# l = [1,2,3,4,5]
# m = [6,7,8]
# l.extend(m)
# print(l)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

l = [1,2,3,4,5]
m = [6,7,8]
k = l+m
print(k)

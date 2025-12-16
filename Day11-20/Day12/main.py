# l = [1,3,2]
# print(type(l))

# l = [1, 3, 2]
# l[1] = 5
# print(l)

# l = [1, 3, 2, "Aditya", 'Utsav', True, 5.6]
# print(l)

# l =  [1, 3, 2]
# print(l[-1])  # This will print the last element of the list which is 2
# print(l[-2])  # This will print the second last element of the list which is 3

# l = [1, 3, 2, 5, 4]
# l[5] = 6  # This will raise an IndexError because index 5 is out of range
# print(l)
#check if an element is present in the list
# l = [1, 3, 2, 5, 4]
# if 3 in l:
#     print("3 is present in the list")

# numbers = [10, 20, 30, 40, 50]
# print(numbers[1:4])   # [20, 30, 40]
# print(numbers[:3])    # [10, 20, 30]
# print(numbers[::2])   # [10, 30, 50]


# nums = [1, 2, 3]
# print(len(nums))     # length
# print(3 in nums)     # membership
# print(nums + [4,5])  # concatenation
# print(nums * 2)      # repetition

numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)

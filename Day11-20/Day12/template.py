# =====================================================
# MASTER TEMPLATE: PYTHON LISTS (FROM BASICS)
# =====================================================

# -----------------------------
# 1️⃣ Creating Lists
# -----------------------------
numbers = [1, 2, 3, 4, 5]
names = ["Aditya", "Python", "Code"]
mixed = [1, "Hello", 3.5, True]

print(numbers)
print(names)
print(mixed)

# -----------------------------
# 2️⃣ Indexing & Negative Indexing
# -----------------------------
print(numbers[0])    # First element
print(numbers[-1])   # Last element

# -----------------------------
# 3️⃣ Slicing
# -----------------------------
print(numbers[1:4])
print(numbers[:3])
print(numbers[::2])

# -----------------------------
# 4️⃣ Lists are Mutable
# -----------------------------
numbers[1] = 99
print(numbers)

# -----------------------------
# 5️⃣ Common List Operations
# -----------------------------
print(len(numbers))        # Length
print(99 in numbers)       # Membership
print(numbers + [6, 7])    # Concatenation
print(numbers * 2)         # Repetition

# -----------------------------
# 6️⃣ Looping Through a List
# -----------------------------
for n in numbers:
    print("Value:", n)

# -----------------------------
# 7️⃣ Taking List Input from User
# -----------------------------
user_list = input("Enter values separated by space: ").split()
print(user_list)

# -----------------------------
# 8️⃣ List Methods
# -----------------------------
nums = [10, 20, 30]

nums.append(40)
nums.insert(1, 15)
nums.extend([50, 60])

nums.remove(20)
popped_value = nums.pop()
nums.sort()
nums.reverse()

print(nums)
print("Popped:", popped_value)

# -----------------------------
# 9️⃣ Copying a List
# -----------------------------
copy1 = nums.copy()
copy2 = nums[:]

print(copy1)
print(copy2)

# -----------------------------
# 🔟 Nested Lists
# -----------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0][1])

# -----------------------------
# 1️⃣1️⃣ List Comprehension
# -----------------------------
squares = [x * x for x in range(1, 6)]
print(squares)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# -----------------------------
# 1️⃣2️⃣ List Comparison
# -----------------------------
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)    # True (values)
print(a is b)    # False (memory)

# -----------------------------
# 1️⃣3️⃣ Clearing & Deleting
# -----------------------------
temp = [1, 2, 3]
temp.clear()
print(temp)

del temp

# -----------------------------
# 1️⃣4️⃣ Real-Life Example
# -----------------------------
shopping_cart = ["milk", "bread", "eggs"]

if "milk" in shopping_cart:
    print("Milk is available")

# =====================================================
# END OF LIST TEMPLATE
# =====================================================

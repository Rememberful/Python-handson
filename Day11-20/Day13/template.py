# =====================================================
# MASTER TEMPLATE: PYTHON LISTS (ALL MAJOR CONCEPTS)
# =====================================================

# -----------------------------
# 1️⃣ Creating Lists
# -----------------------------
numbers = [1, 2, 3, 4, 5]
strings = ["Python", "Java", "C"]
mixed = [1, "Hello", 3.5, True]

print(numbers)
print(strings)
print(mixed)

# -----------------------------
# 2️⃣ Indexing & Negative Indexing
# -----------------------------
print(numbers[0])     # First element
print(numbers[-1])    # Last element

# -----------------------------
# 3️⃣ Slicing
# -----------------------------
print(numbers[1:4])   # From index 1 to 3
print(numbers[:3])    # First 3 elements
print(numbers[::2])   # Step slicing

# -----------------------------
# 4️⃣ Lists are Mutable
# -----------------------------
numbers[1] = 99
print(numbers)

# -----------------------------
# 5️⃣ Common List Operations
# -----------------------------
print(len(numbers))          # Length
print(99 in numbers)         # Membership
print(numbers + [6, 7])      # Concatenation
print(numbers * 2)           # Repetition

# -----------------------------
# 6️⃣ Looping Through List
# -----------------------------
for n in numbers:
    print("Value:", n)

# -----------------------------
# 7️⃣ List Methods (Add Elements)
# -----------------------------
nums = [10, 20, 30]

nums.append(40)
nums.insert(1, 15)
nums.extend([50, 60])

print(nums)

# -----------------------------
# 8️⃣ List Methods (Remove Elements)
# -----------------------------
nums.remove(20)
removed_item = nums.pop()
print("Removed:", removed_item)
print(nums)

# -----------------------------
# 9️⃣ Sorting & Reversing
# -----------------------------
nums.sort()
nums.reverse()
print(nums)

# -----------------------------
# 🔟 Searching & Counting
# -----------------------------
print(nums.index(15))
print(nums.count(15))

# -----------------------------
# 1️⃣1️⃣ Copying Lists
# -----------------------------
copy_list1 = nums.copy()
copy_list2 = nums[:]

print(copy_list1)
print(copy_list2)

# -----------------------------
# 1️⃣2️⃣ Clearing List
# -----------------------------
temp = [1, 2, 3]
temp.clear()
print(temp)

# -----------------------------
# 1️⃣3️⃣ Nested Lists
# -----------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[1][2])

# -----------------------------
# 1️⃣4️⃣ List Comprehension
# -----------------------------
squares = [x * x for x in range(1, 6)]
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

print(squares)
print(even_numbers)

# -----------------------------
# 1️⃣5️⃣ User Input to List
# -----------------------------
user_list = input("Enter values separated by space: ").split()
print(user_list)

# -----------------------------
# 1️⃣6️⃣ Comparison of Lists
# -----------------------------
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True (same values)
print(a is b)   # False (different memory)

# -----------------------------
# 1️⃣7️⃣ Real-Life Example
# -----------------------------
shopping_cart = ["milk", "bread"]

shopping_cart.append("eggs")

if "milk" in shopping_cart:
    print("Milk is in the cart")

print(shopping_cart)

# =====================================================
# END OF LIST TEMPLATE
# =====================================================

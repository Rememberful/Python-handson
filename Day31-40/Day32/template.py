"""
=========================================
PYTHON TEMPLATE: `is` vs `==`
=========================================

==  → VALUE equality
is  → IDENTITY (memory location)

Use this as a revision / interview template
"""

# -------------------------------
# 1️⃣ BASIC EXAMPLE (NUMBERS)
# -------------------------------
a = 10
b = 10

print("a == b :", a == b)   # True → same value
print("a is b :", a is b)   # True → small integer caching


# -------------------------------
# 2️⃣ LARGE INTEGER (CACHING GOTCHA)
# -------------------------------
x = 1000
y = 1000

print("x == y :", x == y)   # True → values equal
print("x is y :", x is y)   # False (usually) → different objects


# -------------------------------
# 3️⃣ LIST EXAMPLE (MOST IMPORTANT)
# -------------------------------
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("list1 == list2 :", list1 == list2)  # True → same content
print("list1 is list2 :", list1 is list2)  # False → different memory


# -------------------------------
# 4️⃣ SAME OBJECT REFERENCE
# -------------------------------
list3 = list1

print("list1 == list3 :", list1 == list3)  # True
print("list1 is list3 :", list1 is list3)  # True → same object


# -------------------------------
# 5️⃣ STRING EXAMPLE
# -------------------------------
s1 = "hello"
s2 = "hello"

print("s1 == s2 :", s1 == s2)  # True
print("s1 is s2 :", s1 is s2)  # Often True (string interning)


# -------------------------------
# 6️⃣ STRING CREATED DYNAMICALLY
# -------------------------------
s3 = "".join(["hel", "lo"])

print("s1 == s3 :", s1 == s3)  # True
print("s1 is s3 :", s1 is s3)  # False → different memory


# -------------------------------
# 7️⃣ SLICE COPY (INTERVIEW TRAP)
# -------------------------------
copy_list = list1[:]

print("list1 == copy_list :", list1 == copy_list)  # True
print("list1 is copy_list :", list1 is copy_list)  # False


# -------------------------------
# 8️⃣ NONE COMPARISON (BEST PRACTICE)
# -------------------------------
value = None

print("value == None :", value == None)   # Works, but NOT recommended
print("value is None :", value is None)   # ✅ Correct way


# -------------------------------
# 9️⃣ BOOLEAN SINGLETONS
# -------------------------------
flag1 = True
flag2 = True

print("flag1 == flag2 :", flag1 == flag2)  # True
print("flag1 is flag2 :", flag1 is flag2)  # True


# -------------------------------
# 🔟 MEMORY CHECK (OPTIONAL)
# -------------------------------
print("id(list1):", id(list1))
print("id(list2):", id(list2))


# -------------------------------
# 🔹 KEY RULES (IMPORTANT)
# -------------------------------
"""
✔ Use `==` to compare VALUES
✔ Use `is` to compare IDENTITIES
✔ Always use `is` for None
✔ Never use `is` for numeric/string comparison
✔ Lists with same data are NOT same objects
"""

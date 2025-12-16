# =====================================================
# MASTER TEMPLATE: TUPLE METHODS & OPERATIONS
# =====================================================

# -----------------------------
# 1️⃣ Creating Tuples
# -----------------------------
t = (10, 20, 30, 20, 40)

single = (5,)        # single-element tuple
packed = 1, 2, 3     # tuple packing

print(t)
print(single)
print(packed)

# -----------------------------
# 2️⃣ Indexing & Negative Indexing
# -----------------------------
print(t[0])      # First element
print(t[-1])     # Last element

# -----------------------------
# 3️⃣ Slicing
# -----------------------------
print(t[1:4])
print(t[:3])
print(t[::2])

# -----------------------------
# 4️⃣ Iterating Through Tuple
# -----------------------------
for value in t:
    print("Value:", value)

# -----------------------------
# 5️⃣ Membership Test
# -----------------------------
print(20 in t)
print(99 not in t)

# -----------------------------
# 6️⃣ Length of Tuple
# -----------------------------
print(len(t))

# -----------------------------
# 7️⃣ Tuple Methods (ONLY TWO)
# -----------------------------

# count() → count occurrences
print(t.count(20))

# index() → find position
print(t.index(30))

# -----------------------------
# 8️⃣ Tuple Operations
# -----------------------------
a = (1, 2)
b = (3, 4)

print(a + b)    # Concatenation
print(a * 2)    # Repetition

# -----------------------------
# 9️⃣ Nested Tuples
# -----------------------------
nested = ((1, 2), (3, 4))
print(nested[1][0])

# -----------------------------
# 🔟 Tuple Unpacking
# -----------------------------
person = ("Aditya", 21, "India")
name, age, country = person

print(name)
print(age)
print(country)

# -----------------------------
# 1️⃣1️⃣ Tuple Comparison
# -----------------------------
x = (1, 2, 3)
y = (1, 2, 4)

print(x == y)
print(x < y)

# -----------------------------
# 1️⃣2️⃣ Converting Tuple to List and Back
# -----------------------------
t1 = (1, 2, 3)
lst = list(t1)
lst.append(4)

t1 = tuple(lst)
print(t1)

# -----------------------------
# 1️⃣3️⃣ Real-Life Example
# -----------------------------
coordinates = (28.61, 77.20)  # latitude, longitude
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])

# =====================================================
# END OF TUPLE TEMPLATE
# =====================================================

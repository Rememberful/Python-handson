# =====================================================
# MASTER TEMPLATE: SETS & SET METHODS IN PYTHON
# =====================================================

# -----------------------------
# 1️⃣ Creating Sets
# -----------------------------
my_set = {1, 2, 3, 3}        # duplicates removed
print("Set:", my_set)

empty_set = set()           # correct way
print("Empty set:", empty_set)


# -----------------------------
# 2️⃣ Accessing Set Elements (Using Loop)
# -----------------------------
for item in my_set:
    print("Item:", item)


# -----------------------------
# 3️⃣ Adding Elements
# -----------------------------
my_set.add(4)               # add single element
my_set.update([5, 6])       # add multiple elements
print("After adding:", my_set)


# -----------------------------
# 4️⃣ Removing Elements
# -----------------------------
my_set.remove(2)            # error if not present
my_set.discard(10)          # no error
my_set.pop()                # removes random element
print("After removing:", my_set)


# -----------------------------
# 5️⃣ Copying & Clearing Set
# -----------------------------
new_set = my_set.copy()
print("Copied set:", new_set)

new_set.clear()
print("Cleared set:", new_set)


# -----------------------------
# 6️⃣ Set Operations
# -----------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference A-B:", A.difference(B))
print("Symmetric Difference:", A.symmetric_difference(B))


# -----------------------------
# 7️⃣ Updating Original Set
# -----------------------------
A.intersection_update(B)
print("After intersection update:", A)

A = {1, 2, 3, 4}
A.difference_update(B)
print("After difference update:", A)

A = {1, 2, 3, 4}
A.symmetric_difference_update(B)
print("After symmetric difference update:", A)


# -----------------------------
# 8️⃣ Set Relationship Methods
# -----------------------------
X = {1, 2}
Y = {1, 2, 3}

print("Is subset:", X.issubset(Y))
print("Is superset:", Y.issuperset(X))
print("Is disjoint:", X.isdisjoint({5, 6}))


# -----------------------------
# 9️⃣ Membership Testing
# -----------------------------
print(2 in Y)
print(10 not in Y)


# -----------------------------
# 🔟 Set Comprehension
# -----------------------------
squares = {x * x for x in range(1, 6)}
print("Set comprehension:", squares)


# -----------------------------
# 1️⃣1️⃣ Frozen Set (Read-Only Set)
# -----------------------------
frozen = frozenset([1, 2, 3])
print("Frozen set:", frozen)
# frozen.add(4)  ❌ Not allowed


# -----------------------------
# 1️⃣2️⃣ Real-Life Example (Remove Duplicates)
# -----------------------------
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]
unique_emails = set(emails)
print("Unique emails:", unique_emails)

# =====================================================
# END OF SET TEMPLATE
# =====================================================

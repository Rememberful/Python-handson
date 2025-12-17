# =====================================================
# MASTER TEMPLATE: DICTIONARIES & DICTIONARY METHODS
# =====================================================

# -----------------------------
# 1️⃣ Creating Dictionaries
# -----------------------------
student = {
    "name": "Aditya",
    "age": 22,
    "course": "Python"
}

print("Student:", student)

empty_dict = {}
print("Empty dictionary:", empty_dict)


# -----------------------------
# 2️⃣ Accessing Values
# -----------------------------
print("Name:", student["name"])          # direct access
print("Age:", student.get("age"))         # safe access
print("City:", student.get("city", "NA")) # default value


# -----------------------------
# 3️⃣ Adding & Updating Values
# -----------------------------
student["grade"] = "A"        # add new key
student["age"] = 23           # update existing key
student.update({"city": "Delhi", "year": 2025})

print("Updated student:", student)


# -----------------------------
# 4️⃣ Removing Elements
# -----------------------------
student.pop("course")         # remove specific key
student.popitem()             # remove last key-value pair
del student["age"]             # delete key

print("After deletion:", student)


# -----------------------------
# 5️⃣ Dictionary Methods
# -----------------------------
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# -----------------------------
# 6️⃣ Looping Through Dictionary
# -----------------------------
for key in student:
    print(key, ":", student[key])

for key, value in student.items():
    print(key, "->", value)


# -----------------------------
# 7️⃣ Checking Key Existence
# -----------------------------
print("name" in student)
print("salary" not in student)


# -----------------------------
# 8️⃣ Copying & Clearing Dictionary
# -----------------------------
student_copy = student.copy()
print("Copied dictionary:", student_copy)

student_copy.clear()
print("Cleared dictionary:", student_copy)


# -----------------------------
# 9️⃣ Nested Dictionary
# -----------------------------
students = {
    "s1": {"name": "A", "marks": 90},
    "s2": {"name": "B", "marks": 85}
}

print("Nested access:", students["s1"]["name"])


# -----------------------------
# 🔟 Dictionary Comprehension
# -----------------------------
squares = {x: x * x for x in range(1, 6)}
print("Dictionary comprehension:", squares)


# -----------------------------
# 1️⃣1️⃣ Using setdefault()
# -----------------------------
student.setdefault("country", "India")
print("After setdefault:", student)


# -----------------------------
# 1️⃣2️⃣ Real-Life Example
# -----------------------------
marks = {
    "math": 90,
    "science": 85,
    "english": 88
}

total_marks = sum(marks.values())
average = total_marks / len(marks)

print("Total marks:", total_marks)
print("Average:", average)

# =====================================================
# END OF DICTIONARY TEMPLATE
# =====================================================

# ==============================
# STRING BASICS & METHODS TEMPLATE
# ==============================

# 1️⃣ Creating Strings
name = "Python Programming"
course = 'Python'
multi_line = """This is
a multi-line
string"""

print(name)
print(course)
print(multi_line)

# ------------------------------

# 2️⃣ String Length
print("Length:", len(name))

# ------------------------------

# 3️⃣ Indexing
print("First character:", name[0])
print("Last character:", name[-1])

# ------------------------------

# 4️⃣ String Slicing
print("Slice (0:6):", name[0:6])
print("Slice (:6):", name[:6])
print("Slice (7:):", name[7:])
print("Reverse:", name[::-1])

# ------------------------------

# 5️⃣ String Concatenation
a = "Hello"
b = "World"
print(a + " " + b)

# ------------------------------

# 6️⃣ String Repetition
print("Hi " * 3)

# ------------------------------

# 7️⃣ Membership Operator
print("Python" in name)
print("Java" not in name)

# ------------------------------

# 8️⃣ Case Methods
text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

# ------------------------------

# 9️⃣ Removing Spaces
space_text = "   hello python   "
print(space_text.strip())
print(space_text.lstrip())
print(space_text.rstrip())

# ------------------------------

# 🔟 Finding and Counting
print(name.find("Program"))
print(name.count("m"))

# ------------------------------

# 1️⃣1️⃣ Replacing Text
msg = "I like Java"
print(msg.replace("Java", "Python"))

# ------------------------------

# 1️⃣2️⃣ Checking String Content
print("python".isalpha())
print("123".isdigit())
print("abc123".isalnum())
print("python".islower())
print("PYTHON".isupper())

# ------------------------------

# 1️⃣3️⃣ startswith() and endswith()
file_name = "code.py"
print(file_name.startswith("code"))
print(file_name.endswith(".py"))

# ------------------------------

# 1️⃣4️⃣ Split and Join
sentence = "Python is very easy"
words = sentence.split()
print(words)

joined = " ".join(words)
print(joined)

# ------------------------------

# 1️⃣5️⃣ String Formatting (Best Practice)
name = "Aditya"
age = 21
print(f"My name is {name} and I am {age} years old")

# ------------------------------

# 1️⃣6️⃣ Looping Through a String
for ch in "Python":
    print(ch)

# ==============================
# END OF STRING TEMPLATE
# ==============================

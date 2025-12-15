# =====================================================
# MASTER TEMPLATE: FOR LOOP & WHILE LOOP IN PYTHON
# =====================================================

# -----------------------------
# FOR LOOP SECTION
# -----------------------------

# 1️⃣ Basic for loop with range
for i in range(5):
    print("For loop basic:", i)

# -----------------------------

# 2️⃣ for loop with start, stop, step
for i in range(1, 10, 2):
    print("For with step:", i)

# -----------------------------

# 3️⃣ Looping through a string
for ch in "Python":
    print("Character:", ch)

# -----------------------------

# 4️⃣ Looping through a list
items = ["apple", "banana", "mango"]
for item in items:
    print("Item:", item)

# -----------------------------

# 5️⃣ for loop with if condition
for i in range(1, 6):
    if i % 2 == 0:
        print("Even number:", i)

# -----------------------------

# 6️⃣ break in for loop
for i in range(1, 6):
    if i == 3:
        break
    print("Break example:", i)

# -----------------------------

# 7️⃣ continue in for loop
for i in range(1, 6):
    if i == 3:
        continue
    print("Continue example:", i)

# -----------------------------

# 8️⃣ for loop with else
for i in range(3):
    print("Loop value:", i)
else:
    print("For loop finished normally")

# -----------------------------

# 9️⃣ Nested for loop
for i in range(1, 4):
    for j in range(1, 3):
        print("Nested for:", i, j)

# -----------------------------

# 🔟 for loop with user input
n = int(input("Enter number for for-loop: "))
for i in range(1, n + 1):
    print("User loop:", i)

# =====================================================
# WHILE LOOP SECTION
# =====================================================

# 1️⃣ Basic while loop
i = 1
while i <= 5:
    print("While loop basic:", i)
    i += 1

# -----------------------------

# 2️⃣ while loop with condition
i = 1
while i <= 10:
    if i % 2 == 0:
        print("Even using while:", i)
    i += 1

# -----------------------------

# 3️⃣ Infinite loop example (controlled with break)
i = 1
while True:
    print("Infinite loop value:", i)
    if i == 3:
        break
    i += 1

# -----------------------------

# 4️⃣ continue in while loop
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("Continue while:", i)

# -----------------------------

# 5️⃣ while loop with else
i = 1
while i <= 3:
    print("While value:", i)
    i += 1
else:
    print("While loop finished normally")

# -----------------------------

# 6️⃣ Nested while loop
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print("Nested while:", i, j)
        j += 1
    i += 1

# -----------------------------

# 7️⃣ while loop with user input
count = int(input("Enter count for while-loop: "))
i = 1
while i <= count:
    print("User while:", i)
    i += 1

# -----------------------------

# 8️⃣ Real-life while loop example (password check)
password = "python123"
user_input = ""

while user_input != password:
    user_input = input("Enter password: ")

print("Login successful")

# =====================================================
# END OF MASTER LOOP TEMPLATE
# =====================================================

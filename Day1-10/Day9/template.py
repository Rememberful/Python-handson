# =====================================================
# MASTER TEMPLATE: break & continue IN PYTHON
# =====================================================

# -----------------------------
# 1️⃣ break in for loop
# -----------------------------
for i in range(1, 6):
    if i == 4:
        break
    print("Break (for):", i)

# -----------------------------
# 2️⃣ continue in for loop
# -----------------------------
for i in range(1, 6):
    if i == 3:
        continue
    print("Continue (for):", i)

# -----------------------------
# 3️⃣ break in while loop
# -----------------------------
i = 1
while i <= 5:
    if i == 4:
        break
    print("Break (while):", i)
    i += 1

# -----------------------------
# 4️⃣ continue in while loop (CORRECT way)
# -----------------------------
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("Continue (while):", i)

# -----------------------------
# 5️⃣ break & continue together
# -----------------------------
for i in range(1, 10):
    if i == 3:
        continue
    if i == 7:
        break
    print("Both:", i)

# -----------------------------
# 6️⃣ Loop with else (no break)
# -----------------------------
for i in range(3):
    print("For loop:", i)
else:
    print("For loop finished normally")

# -----------------------------
# 7️⃣ Loop with else (break used)
# -----------------------------
for i in range(3):
    if i == 1:
        break
    print("For with break:", i)
else:
    print("This will NOT execute")

# -----------------------------
# 8️⃣ Infinite loop with break (safe)
# -----------------------------
i = 1
while True:
    print("Infinite loop value:", i)
    if i == 3:
        break
    i += 1

# -----------------------------
# 9️⃣ Real-life example (password check)
# -----------------------------
password = "python123"
attempt = ""

while True:
    attempt = input("Enter password: ")
    if attempt != password:
        print("Wrong password, try again")
        continue
    else:
        print("Login successful")
        break

# -----------------------------
# 🔟 Nested loop with break
# -----------------------------
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print("Nested loop:", i, j)

# =====================================================
# END OF break & continue TEMPLATE
# =====================================================

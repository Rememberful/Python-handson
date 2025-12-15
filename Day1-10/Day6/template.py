# =========================================
# CONDITIONAL STATEMENTS TEMPLATE IN PYTHON
# =========================================

# 1️⃣ Basic if statement
age = 20

if age >= 18:
    print("Eligible to vote")

# -----------------------------------------

# 2️⃣ if - else statement
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# -----------------------------------------

# 3️⃣ if - elif - else (Multiple conditions)
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

# -----------------------------------------

# 4️⃣ Comparison Operators
a = 10
b = 20

if a < b:
    print("a is smaller than b")

# -----------------------------------------

# 5️⃣ Logical Operators (and, or, not)
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")

day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Holiday")

is_raining = False
if not is_raining:
    print("Go outside")

# -----------------------------------------

# 6️⃣ Nested if (if inside if)
age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")

# -----------------------------------------

# 7️⃣ User Input with if-else
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# -----------------------------------------

# 8️⃣ Membership Operator (in / not in)
text = "Python Programming"

if "Python" in text:
    print("Python found")

# -----------------------------------------

# 9️⃣ Ternary Operator (Short if-else)
age = 16
status = "Adult" if age >= 18 else "Minor"
print(status)

# -----------------------------------------

# 🔟 Boolean Conditions
is_logged_in = True

if is_logged_in:
    print("Welcome user")
else:
    print("Please login")

# =========================================
# END OF CONDITIONAL TEMPLATE
# =========================================

# =========================================
# MATCH - CASE STATEMENTS TEMPLATE IN PYTHON
# (Python 3.10+)
# =========================================

# 1️⃣ Basic match-case with string
day = "Monday"

match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("End of the week")
    case _:
        print("Normal day")

# -----------------------------------------

# 2️⃣ Match-case with numbers
num = 2

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid number")

# -----------------------------------------

# 3️⃣ Match-case with user input
choice = int(input("Enter choice (1-3): "))

match choice:
    case 1:
        print("Add")
    case 2:
        print("Update")
    case 3:
        print("Delete")
    case _:
        print("Invalid choice")

# -----------------------------------------

# 4️⃣ Multiple values in one case
day = "Sunday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")

# -----------------------------------------

# 5️⃣ Match-case with condition (Guard)
age = 25

match age:
    case x if x < 18:
        print("Minor")
    case x if x >= 18 and x <= 60:
        print("Adult")
    case _:
        print("Senior")

# -----------------------------------------

# 6️⃣ Match-case with strings (Case-sensitive)
color = "red"

match color:
    case "Red":
        print("Color is Red")
    case "red":
        print("Color is red")
    case _:
        print("Unknown color")

# -----------------------------------------

# 7️⃣ Match-case with boolean
is_logged_in = True

match is_logged_in:
    case True:
        print("User logged in")
    case False:
        print("User not logged in")

# -----------------------------------------

# 8️⃣ Real-life menu example
print("1. Tea")
print("2. Coffee")
print("3. Juice")

order = int(input("Enter your order: "))

match order:
    case 1:
        print("You ordered Tea")
    case 2:
        print("You ordered Coffee")
    case 3:
        print("You ordered Juice")
    case _:
        print("Invalid order")

# =========================================
# END OF MATCH - CASE TEMPLATE
# =========================================

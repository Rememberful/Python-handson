# =====================================================
# MASTER TEMPLATE: FUNCTIONS, PARAMETERS & ARGUMENTS
# =====================================================

# -----------------------------
# 1️⃣ Simple function (no arguments)
# -----------------------------
def greet():
    print("Hello, Welcome!")

greet()

# -----------------------------
# 2️⃣ Function with parameters (positional arguments)
# -----------------------------
def add(a, b):          # a, b → parameters
    return a + b

print("Add:", add(10, 20))   # 10, 20 → arguments

# -----------------------------
# 3️⃣ Positional arguments (order matters)
# -----------------------------
def info(name, age):
    print("Name:", name)
    print("Age:", age)

info("Aditya", 21)

# -----------------------------
# 4️⃣ Keyword arguments (order does NOT matter)
# -----------------------------
info(age=21, name="Aditya")

# -----------------------------
# 5️⃣ Default arguments
# -----------------------------
def greet_user(name="User"):
    print("Hello", name)

greet_user()
greet_user("Python")

# -----------------------------
# 6️⃣ Function returning value
# -----------------------------
def square(n):
    return n * n

result = square(5)
print("Square:", result)

# -----------------------------
# 7️⃣ Function without return (returns None)
# -----------------------------
def show_message():
    print("This function returns nothing")

x = show_message()
print("Returned value:", x)

# -----------------------------
# 8️⃣ Variable-length arguments (*args)
# -----------------------------
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("Sum:", sum_all(1, 2))
print("Sum:", sum_all(1, 2, 3, 4, 5))

# -----------------------------
# 9️⃣ Keyword variable-length arguments (**kwargs)
# -----------------------------
def user_info(**details):
    for key, value in details.items():
        print(key, ":", value)

user_info(name="Aditya", age=21, city="Delhi")

# -----------------------------
# 🔟 Mixing all types of arguments
# -----------------------------
def full_function(a, b=10, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

full_function(5, 20, 30, 40, name="Aditya", role="Admin")

# -----------------------------
# 1️⃣1️⃣ Function taking user input
# -----------------------------
def multiply(x, y):
    return x * y

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Multiply:", multiply(a, b))

# -----------------------------
# 1️⃣2️⃣ Function calling another function
# -----------------------------
def add_numbers(x, y):
    return x + y

def double_sum(p, q):
    return add_numbers(p, q) * 2

print("Double Sum:", double_sum(3, 4))

# -----------------------------
# 1️⃣3️⃣ Local vs Global variables
# -----------------------------
x = 100   # global variable

def show_value():
    x = 50   # local variable
    print("Inside function:", x)

show_value()
print("Outside function:", x)

# =====================================================
# END OF FUNCTIONS TEMPLATE
# =====================================================

# =====================================================
# MASTER TEMPLATE: RECURSION IN PYTHON
# =====================================================

# -----------------------------
# 1️⃣ Basic Recursion Structure
# -----------------------------
def basic_recursion(n):
    # Base case
    if n == 0:
        return

    print("Value:", n)

    # Recursive call
    basic_recursion(n - 1)

basic_recursion(3)


# -----------------------------
# 2️⃣ Understanding Call Order (Before & After)
# -----------------------------
def call_order(n):
    if n == 0:
        return

    print("Before call:", n)
    call_order(n - 1)
    print("After call:", n)

call_order(3)


# -----------------------------
# 3️⃣ Factorial Using Recursion
# -----------------------------
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# -----------------------------
# 4️⃣ Sum of First N Numbers
# -----------------------------
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print("Sum:", sum_n(5))


# -----------------------------
# 5️⃣ Fibonacci Using Recursion
# -----------------------------
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci:", fibonacci(6))


# -----------------------------
# 6️⃣ Recursion with User Input
# -----------------------------
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

num = int(input("Enter a number for countdown: "))
countdown(num)


# -----------------------------
# 7️⃣ Infinite Recursion Example (DON'T RUN)
# -----------------------------
# def infinite():
#     infinite()   # No base case → Error


# -----------------------------
# 8️⃣ Recursion vs Loop
# -----------------------------
def loop_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("Loop Sum:", loop_sum(5))


# -----------------------------
# 9️⃣ Tail Recursion Example
# -----------------------------
def tail_recursion(n):
    if n == 0:
        return
    print(n)
    tail_recursion(n - 1)

tail_recursion(3)


# -----------------------------
# 🔟 Real-Life Example (Menu System)
# -----------------------------
def menu():
    print("\n1. Say Hello")
    print("2. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print("Hello!")
        menu()   # recursive call
    else:
        return

menu()

# =====================================================
# END OF RECURSION TEMPLATE
# =====================================================

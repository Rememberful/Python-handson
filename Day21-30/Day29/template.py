"""
SINGLE TEMPLATE: LOCAL vs GLOBAL VARIABLES IN PYTHON
Covers:
1. Global variable
2. Local variable
3. Accessing global inside function
4. Local variable shadowing global
5. Modifying global using 'global' keyword
6. Function parameters as local variables
7. Best practice demonstration
"""

# -----------------------------
# 1. GLOBAL VARIABLE
# -----------------------------
x = 100   # Global variable (accessible everywhere)


def show_global():
    """
    Accessing global variable inside function
    (No 'global' keyword needed for reading)
    """
    print("Inside show_global(): x =", x)


# -----------------------------
# 2. LOCAL VARIABLE
# -----------------------------
def local_example():
    y = 50   # Local variable (exists only inside this function)
    print("Inside local_example(): y =", y)


# -----------------------------
# 3. LOCAL SHADOWING GLOBAL
# -----------------------------
def shadow_example():
    x = 20   # Local variable with same name as global
    print("Inside shadow_example(): x =", x)


# -----------------------------
# 4. MODIFY GLOBAL VARIABLE
# -----------------------------
def modify_global():
    global x   # Declaring that we want to modify global x
    x = 500
    print("Inside modify_global(): x =", x)


# -----------------------------
# 5. FUNCTION PARAMETERS (LOCAL)
# -----------------------------
def add(a, b):
    """
    a and b are local variables
    result is also local
    """
    result = a + b
    return result


# -----------------------------
# MAIN EXECUTION
# -----------------------------
print("GLOBAL x before function calls:", x)

show_global()        # Reading global variable
local_example()      # Using local variable
shadow_example()     # Local variable does not affect global

print("GLOBAL x before modification:", x)
modify_global()      # Modifying global variable
print("GLOBAL x after modification:", x)

sum_result = add(10, 20)
print("Result from add() function:", sum_result)

# -----------------------------
# ERROR DEMONSTRATION (COMMENTED)
# -----------------------------
# print(y)  # NameError: y is local to local_example()

"""
KEY TAKEAWAYS:
- Local variables exist only inside functions
- Global variables exist throughout the program
- Reading global variables inside functions is allowed
- Modifying global variables requires 'global' keyword
- Local variables can have same name as global (shadowing)
- Function parameters are always local
- Prefer local variables for clean and safe code
"""

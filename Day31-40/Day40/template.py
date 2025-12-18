"""
PYTHON INTROSPECTION BASICS
--------------------------
This script demonstrates:
1. dir()      -> List attributes and methods of objects
2. __dict__   -> View an object's namespace (attributes storage)
3. help()     -> Access documentation and help system
"""

# -------------------------------------------------
# 1. BASIC OBJECT FOR DEMONSTRATION
# -------------------------------------------------

class Person:
    """This is a simple Person class for introspection demo."""

    species = "Human"   # class attribute

    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age

    def greet(self):
        """Return a greeting message."""
        return f"Hello, my name is {self.name}"

# Create an object
p = Person("Alice", 25)


# -------------------------------------------------
# 2. dir() – INSPECT ATTRIBUTES & METHODS
# -------------------------------------------------

print("\n=== dir() EXAMPLES ===")

# dir() on a built-in type
print("dir(list):")
print(dir(list))

# dir() on a class
print("\ndir(Person):")
print(dir(Person))

# dir() on an instance
print("\ndir(p):")
print(dir(p))

"""
KEY POINTS:
- dir() returns a sorted list of attribute names
- Includes methods, variables, and magic methods (__init__, __str__, etc.)
- Useful for exploring unknown objects
"""


# -------------------------------------------------
# 3. __dict__ – OBJECT NAMESPACE
# -------------------------------------------------

print("\n=== __dict__ EXAMPLES ===")

# Instance __dict__
print("p.__dict__:")
print(p.__dict__)

# Class __dict__
print("\nPerson.__dict__:")
print(Person.__dict__)

"""
KEY POINTS:
- __dict__ is a dictionary that stores an object's attributes
- Instance __dict__ contains instance variables
- Class __dict__ contains class variables & methods
- Not all objects have __dict__ (e.g., int, list)
"""

# Example: dynamically adding attributes
p.city = "New York"
print("\nAfter adding p.city dynamically:")
print(p.__dict__)


# -------------------------------------------------
# 4. help() – DOCUMENTATION & HELP SYSTEM
# -------------------------------------------------

print("\n=== help() EXAMPLES ===")

# Help on a built-in function
print("help(len):")
help(len)

# Help on a class
print("\nhelp(Person):")
help(Person)

# Help on a method
print("\nhelp(Person.greet):")
help(Person.greet)

"""
KEY POINTS:
- help() shows documentation, parameters, and descriptions
- Uses docstrings (\"\"\" \"\"\")
- Extremely useful for learning libraries interactively
"""


# -------------------------------------------------
# 5. COMBINED PRACTICAL USE CASE
# -------------------------------------------------

print("\n=== PRACTICAL INTROSPECTION EXAMPLE ===")

obj = p

# List attributes
print("Attributes using dir():")
for attr in dir(obj):
    if not attr.startswith("__"):
        print(attr)

# Access attribute values safely
print("\nAttribute values from __dict__:")
for key, value in obj.__dict__.items():
    print(f"{key} = {value}")

# Get help dynamically
print("\nGetting help for greet():")
help(obj.greet)


# -------------------------------------------------
# SUMMARY
# -------------------------------------------------
"""
dir()     -> WHAT attributes/methods exist
__dict__  -> WHERE attributes are stored and their values
help()    -> HOW to use them (documentation)

Together, these form Python's core introspection toolkit.
"""

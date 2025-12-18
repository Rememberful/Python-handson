"""
METHOD OVERRIDING IN PYTHON – COMPLETE SINGLE FILE TEMPLATE
==========================================================

This script demonstrates:
1. What method overriding is
2. Inheritance requirement
3. Basic overriding
4. Using super() in overriding
5. Overriding with different behavior
6. Overriding constructors (__init__)
7. Method overriding in multiple inheritance
8. Method Resolution Order (MRO)
9. Best practices & rules
"""

# --------------------------------------------------
# 1. BASE CLASS (PARENT)
# --------------------------------------------------

class Parent:
    def greet(self):
        print("Hello from Parent")

    def info(self):
        print("Parent class information")


# --------------------------------------------------
# 2. BASIC METHOD OVERRIDING
# --------------------------------------------------

class Child(Parent):
    def greet(self):                     # Overridden method
        print("Hello from Child")        # New behavior


print("\n--- Basic Method Overriding ---")
obj = Child()
obj.greet()      # Calls Child's method
obj.info()       # Inherited method (not overridden)


# --------------------------------------------------
# 3. METHOD OVERRIDING USING super()
# --------------------------------------------------

class ChildWithSuper(Parent):
    def greet(self):
        super().greet()                  # Call Parent method
        print("Extended greeting from Child")


print("\n--- Method Overriding with super() ---")
obj2 = ChildWithSuper()
obj2.greet()


# --------------------------------------------------
# 4. OVERRIDING CONSTRUCTOR (__init__)
# --------------------------------------------------

class Base:
    def __init__(self):
        print("Base constructor")

class Derived(Base):
    def __init__(self):
        super().__init__()               # Call parent constructor
        print("Derived constructor")


print("\n--- Constructor Overriding ---")
d = Derived()


# --------------------------------------------------
# 5. OVERRIDING WITH PARAMETERS
# --------------------------------------------------

class Person:
    def details(self, name):
        print("Person name:", name)

class Student(Person):
    def details(self, name, roll):
        print("Student name:", name)
        print("Roll number:", roll)


print("\n--- Overriding with Parameters ---")
s = Student()
s.details("Alice", 101)


# --------------------------------------------------
# 6. OVERRIDING WITH DIFFERENT BEHAVIOR
# --------------------------------------------------

class Shape:
    def area(self):
        print("Area formula not defined")

class Rectangle(Shape):
    def area(self):
        print("Area = length × breadth")


print("\n--- Overriding with Different Logic ---")
r = Rectangle()
r.area()


# --------------------------------------------------
# 7. METHOD OVERRIDING IN MULTIPLE INHERITANCE
# --------------------------------------------------

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(B):
    def show(self):
        print("Class C")

print("\n--- Method Overriding in Multiple Inheritance ---")
c = C()
c.show()


# --------------------------------------------------
# 8. METHOD RESOLUTION ORDER (MRO)
# --------------------------------------------------

print("\n--- Method Resolution Order (MRO) ---")
print(C.__mro__)


# --------------------------------------------------
# 9. RULES & BEST PRACTICES (READ-ONLY)
# --------------------------------------------------

"""
IMPORTANT RULES:
----------------
✔ Method name must be SAME
✔ Parameters should be compatible
✔ Inheritance is REQUIRED
✔ Child method is called first
✔ super() allows parent method access
✔ Python decides order using MRO

WHEN TO USE:
------------
✔ To change or extend parent behavior
✔ To provide specific implementation

WHEN NOT TO USE:
----------------
✘ If behavior is completely unrelated
✘ If no inheritance exists
"""


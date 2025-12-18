"""
SUPER() IN PYTHON – COMPLETE SINGLE FILE DEMO
============================================

This script covers:
1. What super() is
2. super() with constructors (__init__)
3. Method overriding
4. Passing arguments using super()
5. Avoiding direct parent class calls
6. Multiple inheritance
7. Method Resolution Order (MRO)
8. Cooperative inheritance
9. When to use and when not to use super()
"""

# --------------------------------------------------
# 1. BASIC SINGLE INHERITANCE
# --------------------------------------------------

class Parent:
    def __init__(self):
        print("Parent constructor")

    def show(self):
        print("Method from Parent")


class Child(Parent):
    def __init__(self):
        super().__init__()      # Calling Parent constructor
        print("Child constructor")

    def show(self):
        super().show()          # Calling Parent method
        print("Method from Child")


print("\n--- Basic super() Example ---")
obj1 = Child()
obj1.show()


# --------------------------------------------------
# 2. super() WITH PARAMETERS
# --------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name
        print("Person initialized")


class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)  # Passing argument to parent
        self.roll = roll
        print("Student initialized")

    def details(self):
        print("Name:", self.name)
        print("Roll:", self.roll)


print("\n--- super() with Arguments ---")
s = Student("Alice", 101)
s.details()


# --------------------------------------------------
# 3. METHOD OVERRIDING USING super()
# --------------------------------------------------

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        super().sound()         # Extend parent behavior
        print("Dog barks")


print("\n--- Method Overriding ---")
d = Dog()
d.sound()


# --------------------------------------------------
# 4. WHY super() IS BETTER THAN DIRECT CALL
# --------------------------------------------------

class A:
    def show(self):
        print("Class A show")


class B(A):
    def show(self):
        # A.show(self)  # ❌ Not recommended
        super().show()  # ✅ Recommended
        print("Class B show")


print("\n--- super() vs Direct Parent Call ---")
b = B()
b.show()


# --------------------------------------------------
# 5. MULTIPLE INHERITANCE + super()
# --------------------------------------------------

class X:
    def process(self):
        print("Process from X")


class Y(X):
    def process(self):
        super().process()
        print("Process from Y")


class Z(Y):
    def process(self):
        super().process()
        print("Process from Z")


print("\n--- Multiple Inheritance with super() ---")
z = Z()
z.process()


# --------------------------------------------------
# 6. METHOD RESOLUTION ORDER (MRO)
# --------------------------------------------------

print("\n--- Method Resolution Order (MRO) ---")
print(Z.__mro__)


# --------------------------------------------------
# 7. COOPERATIVE MULTIPLE INHERITANCE
# --------------------------------------------------

class Base:
    def __init__(self):
        print("Base initialized")


class Left(Base):
    def __init__(self):
        super().__init__()
        print("Left initialized")


class Right(Base):
    def __init__(self):
        super().__init__()
        print("Right initialized")


class Final(Left, Right):
    def __init__(self):
        super().__init__()
        print("Final initialized")


print("\n--- Cooperative Multiple Inheritance ---")
f = Final()
print("MRO:", Final.__mro__)


# --------------------------------------------------
# 8. OLD vs NEW super() SYNTAX
# --------------------------------------------------

class OldStyle(Parent):
    def __init__(self):
        # Old Python 2 style (still works in Python 3)
        super(OldStyle, self).__init__()
        print("Old style super()")


print("\n--- Old vs New super() Syntax ---")
old = OldStyle()


# --------------------------------------------------
# 9. WHEN NOT TO USE super()
# --------------------------------------------------

class Independent:
    def display(self):
        print("No inheritance here")

# ❌ super() cannot be used because there is no parent


# --------------------------------------------------
# 10. FINAL SUMMARY (READ-ONLY)
# --------------------------------------------------

"""
KEY TAKEAWAYS:
-------------
✔ super() calls parent class methods safely
✔ Avoids hard-coded parent class names
✔ Essential for multiple inheritance
✔ Follows Method Resolution Order (MRO)
✔ Enables cooperative inheritance
✔ super() works only with inheritance
"""


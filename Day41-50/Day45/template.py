"""
MASTER TEMPLATE: TYPES OF INHERITANCE IN PYTHON
------------------------------------------------
This single file demonstrates:
1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
------------------------------------------------
"""

# =================================================
# 1. SINGLE INHERITANCE
# =================================================

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Single inheritance
    def bark(self):
        print("Dog barks")

print("\n--- Single Inheritance ---")
d = Dog()
d.speak()
d.bark()


# =================================================
# 2. MULTILEVEL INHERITANCE
# =================================================

class LivingBeing:
    def live(self):
        print("Living being lives")

class Human(LivingBeing):
    def think(self):
        print("Human thinks")

class Student(Human):  # Multilevel inheritance
    def study(self):
        print("Student studies")

print("\n--- Multilevel Inheritance ---")
s = Student()
s.live()
s.think()
s.study()


# =================================================
# 3. MULTIPLE INHERITANCE
# =================================================

class Father:
    def skill(self):
        print("Father: Driving")

class Mother:
    def skill(self):
        print("Mother: Cooking")

class Child(Father, Mother):  # Multiple inheritance
    pass

print("\n--- Multiple Inheritance ---")
c = Child()
c.skill()  # Resolved using MRO (Father first)


# =================================================
# 4. HIERARCHICAL INHERITANCE
# =================================================

class Employee:
    def work(self):
        print("Employee works")

class Developer(Employee):
    def code(self):
        print("Developer codes")

class Manager(Employee):
    def manage(self):
        print("Manager manages")

print("\n--- Hierarchical Inheritance ---")
dev = Developer()
mgr = Manager()

dev.work()
dev.code()

mgr.work()
mgr.manage()


# =================================================
# 5. HYBRID INHERITANCE (Combination)
#    (Multiple + Multilevel)
# =================================================

class A:
    def show(self):
        print("Class A")
        super().show()

class B(A):
    def show(self):
        print("Class B")
        super().show()

class C(A):
    def show(self):
        print("Class C")
        super().show()

class D(B, C):  # Hybrid inheritance
    def show(self):
        print("Class D")
        super().show()

class Base:
    def show(self):
        pass

# Fixing end of super() chain
A.__bases__ = (Base,)

print("\n--- Hybrid Inheritance ---")
obj = D()
obj.show()


# =================================================
# METHOD RESOLUTION ORDER (MRO)
# =================================================

print("\n--- Method Resolution Order ---")
print(D.mro())


"""
OUTPUT SUMMARY:
---------------
Single Inheritance       -> One parent, one child
Multilevel Inheritance   -> Parent → Child → Grandchild
Multiple Inheritance     -> One child, many parents
Hierarchical Inheritance -> One parent, many children
Hybrid Inheritance       -> Combination of inheritance types

IMPORTANT RULE:
---------------
Always use super() properly in
Multiple & Hybrid inheritance
to avoid ambiguity.
"""

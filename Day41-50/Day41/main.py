# class Parent:
#     def __init__(self):
#         print("Parent constructor")
#     def show(self):
#         print("This is Parent class")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()   # Call Parent's constructor
#         print("Child constructor")
#     def show(self):
#         super().show()       # Call Parent's method
#         print("This is Child class")

# obj = Child()
# obj.show()

# class Parent:
#     def __init__(self, name):
#         self.name = name

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

# c = Child("Alice", 25)
# print(c.name, c.age)

class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        super().show()
        print("Class B")
class C(B):
    def show(self):
        super().show()
        print("Class C")
obj = C()
obj.show()


# class Parent:
#     def show(self):
#         print("This is Parent method")

# class Child(Parent):
#     def show(self):
#         print("This is Child method (overridden)")
# obj = Child()
# obj.show()

# 
# class Parent:
#     def show(self):
#         print("Parent show method")
# class Child(Parent):
#     def show(self):
#         super().show()      # Calls Parent method
#         print("Child show method")
# obj = Child()
# obj.show()


# class Parent:
#     def __init__(self):
#         print("Parent constructor")
# class Child(Parent):
#     def __init__(self):
#         super().__init__()  # Call Parent constructor
#         print("Child constructor")
# obj = Child()

# class Parent:
#     def display(self, name):
#         print("Name:", name)
# class Child(Parent):
#     def display(self, name):
#         super().display(name)
#         print("Welcome,", name)
# obj = Child()
# obj.display("Alice")

class Shape:
    def area(self):
        print("Area of shape")
class Rectangle(Shape):
    def area(self):
        print("Area of rectangle")
class Circle(Shape):
    def area(self):
        print("Area of circle")
shapes = [Rectangle(), Circle()]
for shape in shapes:
    shape.area()


# class Example:
#     def instance_method(self):
#         print("This is an instance method")
# # Create an object
# obj = Example()
# # Call the instance method
# obj.instance_method()

# class Example:
#     @staticmethod
#     def static_method():
#         print("This is a static method")
# # Call without creating an object
# Example.static_method()
# # Also possible using an object
# obj = Example()
# obj.static_method()

# class Employee:
#     def __init__(self, name):
#         self.name = name
#     def showDetails(self):
#         print(f"Name is {self.name}")

# emp1 = Employee("Aditya")
# emp1.showDetails()
# Employee.showDetails(emp1)

class Example:
    class_var = "I am a class variable"   # shared by all objects
    def __init__(self, value):
        self.instance_var = value        # unique to each object
# Create objects
obj1 = Example(10)
obj2 = Example(20)
# Access variables
print(obj1.instance_var)   # 10
print(obj2.instance_var)   # 20
print(obj1.class_var)      # I am a class variable
print(obj2.class_var)      # I am a class variable


# class Animal:
#     def speak(self):
#         print("Animal makes a sound")
#     def bark(self):
#         print("Dog barks")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# d = Dog()
# d.bark()
# d.speak()

# class Father:
#     def skills(self):
#         print("Gardening, Driving")
# class Mother:
#     def skills2(self):
#         print("Cooking, Painting")
# class Child(Father, Mother):
#     def speak(self):
#         print("Aditya")
# c = Child()
# print(Father.mro())

# class A:
#     def show(self):
#         print("A")
# class B:
#     def show(self):
#         print("B")
# class C(A, B):
#     def show(self):
#         super().show()
#         print("C")
# z = C()
# z.show()

# class Animal:
#     def eat(self):
#         print("Animal eats")
# class Mammal(Animal):
#     def walk(self):
#         print("Mammal walks")
# class Dog(Mammal):
#     def bark(self):
#         print("Dog barks")
# d = Dog()
# d.eat()
# d.walk()
# d.bark()

# class Person:
#     def __init__(self, name):
#         self.name = name
# class Employee(Person):
#     def __init__(self, name, emp_id):
#         super().__init__(name)
#         self.emp_id = emp_id
# class Manager(Employee):
#     def show(self):
#         print(self.name, self.emp_id)
# m = Manager("Alice", 101)
# m.show()

# class A:
#     def show(self):
#         print("Class A")
# class B(A):
#     def show(self):
#         super().show()
#         print("Class B")
# class C(B):
#     def show(self):
#         super().show()
#         print("Class C")
# obj = C()
# obj.show()

# class A:
#     def __init__(self):
#         print("A init")
# class B(A):
#     def __init__(self):
#         super().__init__()
# #         print("B init")
# # class C(B):
# #     def __init__(self):
# #         super().__init__()
# #         print("C init")
# # c = C()

# class Animal:
#     def speak(self):
#         print("Animal speaks")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")
# d = Dog()
# d.speak()
# d.bark()
# c = Cat()
# c.speak()
# c.meow()


class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        print("Class B")
        super().show()
class C(A):
    def show(self):
        print("Class C")
        super().show()
class D(B, C):
    pass
obj = D()
obj.show()

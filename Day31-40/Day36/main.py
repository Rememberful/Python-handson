# class Person:
#     def __init__(self, name, age):
#         self.name = name  # public attribute
#         self.age = age    # public attribute
# p = Person("Alice", 25)
# print(p.age)  # 25
# p.age = -5    # Oops! Age shouldn't be negative
# print(p.age)  # -5

class Person:
    def __init__(self, age):
        self._age = age   # private attribute (by convention)
    @property
    def age(self):       # getter
        return self._age
    @age.setter
    def age(self, value):  # setter
        self._age = value
p = Person(20)
print(p.age)   # getter is called → 20
p.age = 25     # setter is called
print(p.age)   # 25

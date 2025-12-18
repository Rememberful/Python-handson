# class Person:
#     def __init__(self, name):
#         self.name = name
# p = Person("Alice")
# print(p.name)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return f"Person name is {self.name}"
# p = Person("Bob")
# print(p)   # calls __str__()

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def __repr__(self):
#         return f"Person('{self.name}')"
# p = Person("Charlie")
# print(repr(p))


# class Number:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return self.value + other.value
# a = Number(10)
# b = Number(20)
# print(a + b)

# class Number:
#     def __init__(self, value):
#         self.value = value
#     def __sub__(self, other):
#         return self.value - other.value
# a = Number(50)
# b = Number(20)
# print(a - b)

class MyList:
    def __init__(self, items):
        self.items = items
    def __len__(self):
        return len(self.items)
obj = MyList([1, 2, 3, 4])
print(len(obj))





# class Person:
#     #constructor
#     def __init__(self, n, o):
#         print("Hey I am a person")
#         self.name = n
#         self.occ = o
#     #method
#     def info(self):
#         print(f"{self.name} is of {self.occ}")
# #creating the object
# a = Person("Aditya")
# b = Person("Utsav", "BHMS") #2nd object
# a.info()
# b.info()

# class Demo:
#     def __init__(self):
#         self.x = 10
# d = Demo()
# print(d.x)

class Demo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
d = Demo(5, 10)
print(d.x, d.y)

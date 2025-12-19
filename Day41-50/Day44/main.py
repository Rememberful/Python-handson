# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#     def __str__(self):
#         return f"({self.x}, {self.y})"
# p1 = Point(2, 3)
# p2 = Point(4, 5)
# print(p1 + p2)

class Number:
    def __init__(self, value):
        self.value = value
    def __sub__(self, other):
        return Number(self.value - other.value)
    def __mul__(self, other):
        return Number(self.value * other.value)
    def __str__(self):
        return str(self.value)
a = Number(10)
b = Number(3)
print(a - b)
print(a * b)

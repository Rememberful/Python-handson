# 

# class Student:
#     school_name = "ABC School"
#     @classmethod
#     def change_school(cls, new_name):
#         cls.school_name = new_name
# Student.change_school("XYZ School")
# print(Student.school_name)

# class
#  Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def from_string(cls, data):
#         name, age = data.split(",")
#         return cls(name, int(age))
# s1 = Student.from_string("Aditya,22")
# print(s1.name, s1.age)


class Student:
    def __init__(self, name):
        self.name = name
    @classmethod
    def from_string(cls, data):
        return cls(data)

s1 = Student("Aditya")          # normal constructor
s2 = Student.from_string("Rahul")  # alternative constructor
print(s1.name)
print(s2.name)

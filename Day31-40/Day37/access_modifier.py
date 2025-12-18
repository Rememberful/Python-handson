# class Student:
#     def __init__(self, name):
#         self.name = name   # Public attribute
#     def show(self):        # Public method
#         print(self.name)
# s = Student("Alice")
# print(s.name)   # Allowed
# s.show()        # Allowed

# class Employee:
#     def __init__(self, salary):
#         self._salary = salary   # Protected attribute
# class Manager(Employee):
#     def show_salary(self):
#         print(self._salary)    # Allowed
# m = Manager(50000)
# m.show_salary()
# print(m._salary)  # Allowed (but discouraged)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private attribute
    def show_balance(self):
        print(self.__balance)
acc = BankAccount(1000)
acc.show_balance()   # Allowed
# print(acc.__balance)  ❌ AttributeError


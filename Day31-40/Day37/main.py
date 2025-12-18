class Employee:
    def __init__(self,name,id):
        self.name = name 
        self.id = id
    #method
    def showDetails(self):
        print(f"Name is {self.name} whose id is {self.id} ")
class Programmer(Employee):
    def showLang(self):
        print("Python is the lang")
#object for employee 
e = Employee("Aditya", 111)
e.showDetails()
#object for programmer
f = Programmer("Utsav", 112)
f.showDetails()
f.showLang()
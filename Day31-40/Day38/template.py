class Employee:
    # -------- Class Variable --------
    company_name = "TechCorp"

    def __init__(self, name, salary):
        # -------- Instance Variables --------
        self.name = name
        self.salary = salary

    # -------- Instance Method --------
    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company_name}")

    # -------- Class Method --------
    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

    # -------- Static Method --------
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


# -------- Creating Objects --------
e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

# Instance variables (different for each object)
e1.show_details()
e2.show_details()

# Static method (no self / cls)
print(Employee.is_valid_salary(45000))

# Class variable (shared)
Employee.change_company("NextGenTech")

# Affects all objects
e1.show_details()
e2.show_details()

# Modifying class variable wrongly using object (creates instance variable)
e1.company_name = "WrongCompany"

print(e1.company_name)  # Instance variable
print(e2.company_name)  # Class variable

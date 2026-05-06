class Employee:
    def __init__(self, name, salary, company):
        self.name = name
        self.salary = salary
        self.company = company


harry = Employee("harry", 1200000, "Google")
print(harry.name, harry.salary, harry.company)
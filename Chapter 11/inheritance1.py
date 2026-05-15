class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of Employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "ITC - Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")

a = Employee()
b = Programmer()
b.name = "Harry"
b.salary = 1200000
b.show()

print(a.company, b.company)
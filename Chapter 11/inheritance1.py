class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of Employee is {self.name} and the salary is {self.company}")

class Programmer(Employee):
    company = "ITC - Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good in {self.company} language")

a = Programmer()
a.name = "Harry"
a.show()
a.showLanguage()
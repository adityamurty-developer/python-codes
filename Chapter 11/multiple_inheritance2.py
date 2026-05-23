class Employee:
    company1 = "Ex - ITC"

    def show(self):
        print(f"The name of employee is: {self.name} and the salary is: {self.salary}")


class Coder:
    lang1 = "Python"
    lang2 = "Django"
    lang3 = "Flask"

    def printLang(self):
        print(f"I am good in: {self.lang1} , {self.lang2} , {self.lang3}")


class Programmer(Employee, Coder):
    company2 = "\nCurrent - Google"

    def showLang(self):
        print(f"I have done my DSA in {self.lang1} language")


a = Programmer()

a.name = "Harry"
a.salary = 1200000

print(a.company1, a.company2)
a.show()
a.printLang()
a.showLang()
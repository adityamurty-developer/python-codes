class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self): #dunder method which is automatically called
        print("Hello good morning, this is harry!")

    def getInfo(self):
        print(f"The language is: {self.language} and salary is: {self.salary}")

harry = Employee()
harry.language = "Java Script"

harry.getInfo()
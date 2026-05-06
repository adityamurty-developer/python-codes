class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is: {self.language} and salary is: {self.salary}")

    @staticmethod
    def greet():
        print("Hello World!")

harry = Employee()
harry.language = "Java Script"

harry.getInfo()
harry.greet()
class Employee:
    language = "Py"
    salary = 1200000  # This is a class attribute

rohan = Employee()
rohan.name = "Rohan"  # This is an instance attribute
print(rohan.name, rohan.language, rohan.salary)

Amit = Employee()
Amit.name = "Amit"  # This is an instance attribute
Amit.language = "C++" # overrides the class attribute for Amit (instance attribute)
print(Amit.name, Amit.language, Amit.salary)

Priya = Employee()
print(Priya.language)

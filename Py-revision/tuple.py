# tuple --> tuple also store multiple values just like list, but the difference is tuple is immutable

student = ("Aditya", 20, 7.6, True)

print(f"What is your name: {student[0]}. age is: {student[1]}, cgpa is: {student[2]}, is student age 20 ?? : {student[3]}")

# in tuple, for a single element --> comma is mandatory 
# x = (10) --> this is simple int 
x = (10,) # this is a tuple

# Methods of tuple:

a = (1, 2, 3, 1)

print(a.count(1))
print(a.index(1))

# tuple packing and unpacking 

employee1 = "Rohan", 1200000, 7.8

print(employee1)  # Tuple packing: multiple values are packed into a tuple

employee2 = ("Shreya", 800000, 7.6)

name, salary, cgpa = employee2

print(name, salary, cgpa) # Tuple unpacking: tuple values are assigned to separate variables
# Number of variables should match the number of tuple elements
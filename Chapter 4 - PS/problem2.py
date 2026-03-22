# Program to accept marks of 6 students and display them in sorted manner
marks = []

f1 = int(input("Enter first student marks: "))
marks.append(f1)

f2 = int(input("Enter second student marks: "))
marks.append(f2)

f3 = int(input("Enter third student marks: "))
marks.append(f3)

f4 = int(input("Enter fourth student student marks: "))
marks.append(f4)

f5 = int(input("Enter fifth student marks: "))
marks.append(f5)

f6 = int(input("Enter sixth student marks: "))
marks.append(f6)

marks.sort()
print(marks)
print("START")
print("THIS FILE IS RAINING.PY")

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if b == 0:
    raise ZeroDivisionError("No division by zero allowed")
else:
    print(a / b)
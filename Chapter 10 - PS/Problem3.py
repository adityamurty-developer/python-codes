class demo:
    a = 4

b = demo()
print(b.a)  # Prints the class attribute because instance attribute is not present

b.a = 2
print(b.a)  # Prints the instance attribute for object b

print(demo.a)  # Prints the class attribute
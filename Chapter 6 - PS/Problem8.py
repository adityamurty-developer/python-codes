a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

choice = int(input("1. Add 2. Subtract 3. Multiply 4. Divide\nEnter your choice: "))

if(choice == 1):
    print("Result: ", a+b)
elif(choice == 2):
    print("Result: ", a-b)
elif(choice == 3):
    print("Result: ", a*b)
elif(choice == 4):
    if(b==0):
        print("Division by 0!")
    else:
        print("Result: ", a/b)
else:
    print("Invalid choice!")
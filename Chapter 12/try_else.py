try:
    a = int(input("Enter value of a: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")
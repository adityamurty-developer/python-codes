def multiply(n):
    i = 1
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")
    
n = int(input("Enter a number: "))
multiply(n)
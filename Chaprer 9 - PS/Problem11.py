# program to store the sum in a file

def sum(n):
    add = 0
    for i in range(0, n+1):
        add+=i
    return add

n = int(input("Enter a number: "))
result = sum(n)

with open("sum.txt", "w") as f:
    f.write("Sum is: " +str(result))
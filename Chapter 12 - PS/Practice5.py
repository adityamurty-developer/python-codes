n = int(input("Enter value of n: "))

table = [n*i for i in range(1, 11)]
with open("tables.txt", "a") as f:
    f.write(f"Table of {n} is: {str(table)} \n")
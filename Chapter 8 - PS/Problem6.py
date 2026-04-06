# Same problem using recursive function

def pattern(n):
    if n == 0:
        return
    print("* " * n)  # this prints the existing row
    pattern(n-1)   # this is recursive call which makes n = n-1

n = int(input("Enter a number: "))
pattern(n)
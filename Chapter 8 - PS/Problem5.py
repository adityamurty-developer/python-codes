''' function to print first n lines of the following pattern:
* * *
* *
*
n = 3
'''

def pattern(n):
    for i in range(1, n+1):
        print("* " * (n - i + 1))

n = int(input("Enter a number: "))
    
pattern(n)
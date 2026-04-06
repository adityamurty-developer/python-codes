# using functions, find the greatest of three numbers 

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = 8
b = 5
c = 10

print(f"Greatest of three number is: {greatest(a, b, c)}")
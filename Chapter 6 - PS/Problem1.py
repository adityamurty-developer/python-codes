# To find the greatest of four numbers entered by the user
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
d = int(input("Enter number d: "))

if(a>b and a>c and a>d):
    print("greatest number is a: ", a)

elif(b>a and b>c and b>d):
    print("greatest number is b: ", b)

elif(c>a and c>b and c>d):
    print("greatest number is c: ", c)

else:
    print("greatest number is d: ", d)

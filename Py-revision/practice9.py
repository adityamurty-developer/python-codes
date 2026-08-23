# check the type of variable assigned using input() function. Also tell why input() addition of two different variables gives wrong sum

a = input("Enter value of a: ")
b = input("Enter value of b: ")

print((a+b), type(a), type(b)) # because the type the input type is str we get the result 1 + 2 = 12 because we are not adding two int numbers, we are adding two strings

x = int(input("Enter value of a: "))
y = int(input("Enter value of b: "))

print((x+y), type(x), type(y)) # here we are getting the correct result because here we use input typecasting 
age = int(input("Enter your age: "))

# if statement no. 1
if(age%2==0):
    print("age is even")
# end of if statement no. 1

# if statement no. 2
if(age>=18):
    print("You are above the age consent")
    print("Good for you")

elif(age<0):
    print("You are entering an invalid negative age")

elif(age==0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age consent")
# end of if statement no. 2

print("End of Program")
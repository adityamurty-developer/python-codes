age = int(input("Enter your age: "))

if(age>=18):
    print("You are above the age consent")
    print("Good for you")

elif(age<0):
    print("You are entering an invalid negative age")

elif(age==0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age consent")

print("End of Program")
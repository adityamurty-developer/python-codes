t1 = "Make a lot of money"
t2 = "buy now"
t3 = "subscribe this"
t4 = "click this"

message = input("Enter your message: ")

if((t1 in message) or (t2 in message) or (t3 in message) or (t4 in message)):
    print("This is a spam comment")

else:
    print("This is not a spam comment")
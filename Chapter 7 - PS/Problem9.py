''' Star Pattern for n = 3

  *
 ***
*****

'''

n = 3

i = 1
while(i<=n):
    print(" "* (n-i), end="")    # (n-i) --> Spaces print in each row 
    print("*"* (2*i-1), end="")  # (2*i-1) --> To print stars in each row
    print("")
    i+=1
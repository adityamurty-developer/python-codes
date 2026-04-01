''' Star Pattern for n = 3

  *
 ***
*****

'''

n = 3

for i in range(1, n+1):
    print(" "* (n-i), end="")    # (n-i) --> Spaces print in each row 
    print("*"* (2*i-1), end="")  # (2*i-1) --> To print stars in each row
    print("")
# List methods
# 12. copy() --> it create a separate list for a variable and copy the list element from the assigned list

a = [10, 20, 30]
b = a   # normal assignment (both a and b refers to same object)

b.append(40)

print(a, " ", b)

# using copy() method 

x = [10, 20, 30]
y = x.copy()

y.append(40)

print(x, " ", y)

# 13. Nested list

matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

print(matrix[0][0], matrix[1][1], matrix[2][2])
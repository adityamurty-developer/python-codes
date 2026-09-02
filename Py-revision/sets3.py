# set operations

a = {1, 2, 3}
b = {3, 4, 5}

# 1. union() --> all the unique elements of both sets
print(a.union(b))  # can be written as (a | b)  

# 2. intersection() --> common elements in both sets
print(a.intersection(b))  # can be written as (a & b)

# 3. difference --> a - b means elements present in a but not in b
print(a.difference(b))  # can be written as a - b

# 4. symmetric_difference() --> common elements are removed
print(a.symmetric_difference(b))
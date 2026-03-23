a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a ^ b)  # All elements from both sets except the common ones is symmetric difference
print(a.symmetric_difference(b))  # This will also give same output
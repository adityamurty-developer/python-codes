s = {1, 5, 32, 22.34, 5, "Aditya"}

print(s, type(s))

s.add(45)
print(s, type(s))

l = len(s)  # Returns the length of a set
print(l)

s.remove(32)  # Removes a specific element from set s
print(s)

s.pop()  # Removes a random element from set s but it is not a recommended
print(s)

s.clear()
print(s, type(s))
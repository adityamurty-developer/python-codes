# ============================================
# STRING CONCATENATION & FORMATTING
# ============================================

name = "Aditya"
age = 20


# 1. STRING CONCATENATION (+)
# Joining strings using the + operator

print("My name is " + name + " and I am " + str(age) + " years old.")


# 2. STRING FORMATTING (%)
# Old-style string formatting
# %s -> string
# %d -> integer
# %f -> float

print("My name is %s and I am %d years old." % (name, age))


# 3. F-STRING
# Modern and commonly preferred method
# Available since Python 3.6+

print(f"My name is {name} and I am {age} years old.")
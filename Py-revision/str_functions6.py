# STRING VALIDATION METHODS

text1 = "Python"
text2 = "12345"
text3 = "Python123"
text4 = "     "
text5 = "Python@123"


# 1. isalpha()
# Checks whether ALL characters are alphabets
print(text1.isalpha())       # True
print(text3.isalpha())       # False


# 2. isdigit()
# Checks whether ALL characters are digits
print(text2.isdigit())       # True
print(text1.isdigit())       # False


# 3. isalnum()
# Checks whether ALL characters are alphabets or digits
# No spaces or special characters allowed
print(text3.isalnum())       # True
print(text5.isalnum())       # False


# 4. isspace()
# Checks whether ALL characters are whitespace
print(text4.isspace())       # True
print(text1.isspace())       # False
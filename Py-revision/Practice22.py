# String Comparison

word1 = "Python"
word2 = "Python"
print(word1 == word2)

word3, word4 = "Cpp", "cpp"
print(word3 == word4)  # gives false result because python is case-sensitive

x = "A"
y = "a"
print(y>x) # a > A because ascii value of a is greater than A
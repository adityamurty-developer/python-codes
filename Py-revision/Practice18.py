# String Immutability 

word = "Python"

# word[0] = "J"
# print(word) # this will give error because string is immutable and we cannot change a existing string

# changing a string using string slicing

word = "Python"

word = "J" + word[1:]
print(word) # now this works because we are not changing an existing string but we are breaking it and then adding our new word --> "J" + "ython"
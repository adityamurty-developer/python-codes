# Take a word as input from user and print:
# first, last, second, second-last character

word = input("Enter a word: ")

print(word[0]) # first char
print(word[len(word)-1]) # last char
print(word[1]) # second char
print(word[len(word)-2]) # second-last char
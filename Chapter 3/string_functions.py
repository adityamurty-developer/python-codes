name = "aditya"

print(len(name))   # returns the length of the string

print(name.endswith("ya"))
print(name.startswith("Ad"))

print(name.capitalize())

print(name.count("a"))  # count total occurrence of any char

word = "Hello World"
print(word.find("o"))  # return the index of first occurrence of that word

print(name.replace("a", "b"))  # replaces the old word with new word in entire string

char = ["H", "E", "L", "L", "O"]
print("".join(char))   # "" --> this is a separator 

text = "H E L L O"
print(text.split(" "))  
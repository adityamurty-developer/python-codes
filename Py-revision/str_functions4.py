# str replace()

text = "I love Java"

new_text = text.replace("Java", "Python")

print(new_text)

# due to string immutability if we perform only text.replace("Java", "Python"), and print the text it will not modify original string. So, we have to store .replace() function inside a new variable and then print that new variable to get the modified string
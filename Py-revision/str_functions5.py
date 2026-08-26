# str .split() 
text = "Python is easy"

words1 = text.split()  # .split() --> breaks the string into pieces and makes it a list
print(words1)

date = "26-08-2026"
print(date.split("-")) # "-" --> it's a separator

# str .join() 
words2 = ["Python", "is", "easy"]

sentence = " ".join(words2)
print(sentence)

words3 = ["26", "8", "2026"]

new_date = "-".join(words3)
print(new_date)
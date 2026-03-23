# What if languages of 2 friends are same?

d = {}

name = input("Enter friends name: ")
lang = input("Enter your favorite language: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter your favorite language: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter your favorite language: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter your favorite language: ")
d.update({name: lang})

print(d)

# if two values are same of two different keys then there is no change in the values because key must be unique but not value
f = open("poem.txt")
c = f.read()

if ("Twinkle" in c):
    print("The word Twinkle is present!")
else:
    print("The word Twinkle is not present!")

f.close()
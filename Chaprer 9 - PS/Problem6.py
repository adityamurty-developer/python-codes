with open("log.txt") as f:
    content = f.read()

if("Python" in content):
    print("Yes Python is present")
else:
    print("Python is not present!")
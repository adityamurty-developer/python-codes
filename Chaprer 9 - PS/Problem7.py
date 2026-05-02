with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
# this loops check if python is present in any of the line
for line in lines:
    if("Python" in line):
        print(f"Yes Python is present in line: {lineno}")
        break
    lineno+=1
# if not then loop exits and else will runs
else:
    print("Python is not present")
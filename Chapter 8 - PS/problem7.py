# convert inches to cm using function

def scale(inches):
    if inches < 0:
        return "Invalid value entered!"
    return inches * 2.54

inches = float(input("Enter a value in inches: "))
print(f"{scale(inches)}")
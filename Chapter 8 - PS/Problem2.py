# Python program to convert Celsius to Fahrenheit using function

def fahrenheit(celsius):
    if celsius < -273.15:
        return None
    return (9/5) * celsius + 32

celsius = float(input("Enter temperature in celsius: "))
result = fahrenheit(celsius)

if result is None:
    print("Invalid temperature!")
else:
    print(f"{round(result, 2)} °F")
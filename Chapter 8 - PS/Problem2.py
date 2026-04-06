# Python program to convert Celsius to Fahrenheit using function

def fahrenheit(celsius):
    if celsius < -273.15:
        return "Invalid temperature!"
    return (9/5) * celsius + 32

celsius = float(input("Enter temperature in celsius: "))
print(f"Conversion of C to F is: {fahrenheit(celsius)}")
subjects = ["maths", "physics", "chemistry", "english"]
weekend = ("saturday", "sunday")
weekday = ("monday", "tuesday", "wednesday", "thursday", "friday")

subject = input("Enter subject: ").lower()
day = input("Enter day: ").lower()

if subject not in subjects:
    print("Invalid subject entered!")

elif day not in weekend and day not in weekday:
    print("Invalid day entered!")

elif day in weekend:
    print("Study light it's a weekend!")

elif day in weekday:
    print("Study hard it's weekday!")
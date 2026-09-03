# if - elif
marks = int(input("Enter your percentage: "))

if marks >= 90 and marks <= 100:
    print("A grade")
elif marks >= 80:
    print("B grade")
elif marks >= 70:
    print("C grade")
elif marks >= 60:
    print("D grade")
elif marks >= 0:
    print("You failed in exam, Study hard")
else:
    print("Invalid marks entered")
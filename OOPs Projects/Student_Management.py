class Student:
    def __init__(self, name, enrollment, marks):
        self.name = name
        self.enrollment = enrollment
        self.marks = marks

    def getAverage(self):
        total = sum(self.marks)
        average = total/len(self.marks)
        return average
    
    def getGrade(self):
        avg = self.getAverage()
        if (avg >= 90):
            return "A"
        elif (avg >=75):
            return "B"
        elif (avg >= 60):
            return "C"
        else:
            return "Fail"
        
    def showDetails(self):
        print("...Student Details...\n")
        print(f"Name: {self.name}\nEnrollment: {self.enrollment}\nMarks:{self.marks}\nAverage: {self.getAverage():.2f}\nGrade: {self.getGrade()}\n")

s1 = Student("Harry", 1234, [78, 92, 99])
s1.showDetails()

s2 = Student("Rohan", 1235, [95, 96, 91])
s2.showDetails()

s3 = Student("Priya", 1236, [62, 61, 56])
s3.showDetails()
from random import randint

class Train:
    def __init__(slf, trainNo, trainName):
        slf.trainNo = trainNo
        slf.trainName = trainName

    def book(self, fro, to):
        print(f"Train is booked from {fro} to {to}")
    
    def getStatus(self):
        print(f"Train no. {self.trainNo} is running on time.")

    def getFare(self, fro, to):
        print(f"Ticket fare in train {self.trainNo} from {fro} to {to} is {randint(222, 888)}")

    
t1 = Train(12345, "Shatabdi Express")
t1.book("Mumbai", "Delhi")
t1.getStatus()
t1.getFare("Mumbai", "Delhi")
class Train:
    def __init__(self, trainNo, trainName, bookingStatus, trainStatus, fare):
        self.trainNo = trainNo
        self.trainName = trainName
        self.bookingStatus = bookingStatus
        self.trainStatus = trainStatus
        self.fare = fare

    def bookTicket(self):
        self.fro = input("Enter From station: ")
        self.to = input("Enter To station: ")

    def getFare(self):
        print(f"Ticket Fare    : {self.fare}")
    
    def show_details(self):
        print("\n.....Train Details.....")
        print(f"Train no.      : {self.trainNo}")
        print(f"Train name     : {self.trainName}")
        print(f"From           : {self.fro}")
        print(f"To             : {self.to}")
        print(f"Booking Status : {self.bookingStatus}")
        print(f"Running Status : {self.trainStatus}")



t1 = Train(12345, "Rajdhani Express", "Available", "Running on Time", 1500)
t1.bookTicket()
t1.show_details()
t1.getFare()
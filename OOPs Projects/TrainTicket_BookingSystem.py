class Train:
    def __init__(self, trainName, trainNo, source, destination, seatAvailability):
        self.trainName = trainName
        self.trainNo = trainNo
        self.source = source
        self.destination = destination
        self.seatAvailability = seatAvailability

    def showTrainDetails(self):
        print("....Train Details.....\n")
        print(f"Train name: {self.trainName}")
        print(f"Train num: {self.trainNo}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Seat Availability: {self.seatAvailability}")


class Passenger:
    def __init__(self, name, age, BookedTrain):
        self.name = name
        self.age = age
        self.BookedTrain = BookedTrain

    def showPassengerDetails(self):
        print("....Passenger Details....\n")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Booking Status: {self.BookedTrain}")


class RailwaySystem:
    def __init__(self, trains, bookings):
        self.trains = trains
        self.bookings = bookings

    def add_trains(self, train):
        self.trains.append(train)

    def show_trains(self):
        for train in self.trains:
            train.showTrainDetails()

    def book_ticket(self):

        self.show_trains()
        train_no = int(input("\nEnter Train Number to Book Ticket: "))

        for train in self.trains:
            if(train.trainNo == train_no):
                if(train.seatAvailability > 0):
                    name = input("Enter Passenger Name: ")
                    age = int(input("Enter Passenger Age: "))

                    train.seatAvailability -= 1
                    p = Passenger(name, age, train.trainName)
                    self.bookings.append(p)
                    print("\nTicket Booked Successfully!!")
                    print(f"Remaining Seats: {train.seatAvailability}")

                else:
                    print("No Seats Available")
                return

        print("Train not found")

    def show_bookings(self):
        print("\n....Booked Tickets....\n")
        for booking in self.bookings:
            booking.showPassengerDetails()

    def menu(self):
        while True:
            print("\n.....Indian Railway System.....\n")
            choice = int(input("1. Show Trains\n2. Book Ticket\n3. Show Bookings\n4. Exit\n\nEnter your choice: "))
            if(choice == 1):
                self.show_trains()
            elif(choice == 2):
                self.book_ticket()
            elif(choice == 3):
                self.show_bookings()
            elif(choice == 4):
                print("\nThank You for using Indian Railway System")
                break
            else:
                print("\nInvalid Choice Entered")

t1 = Train("Vande Bharat", 12345, "Jabalpur", "Bhopal", 15)
t2 = Train("Indore - Jabalpur Express", 54321, "jabalpur", "Indore", 15)
t3 = Train("Somnath Express", 67890, "Jabalpur", "Veraval", 13)

r = RailwaySystem([], [])

r.add_trains(t1)
r.add_trains(t2)
r.add_trains(t3)

r.menu()
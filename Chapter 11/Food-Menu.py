class Cafe:

    def showDetails(self):
        print("....WELCOME TO MY Cafe....")
        print("1. Maggie")
        print("2. Burger")
        print("3. Pizza")
        print("4. Sandwich")


class Choice(Cafe):

    def yourChoice(self):

        self.choice = int(input("Enter your choice: "))

        if(self.choice == 1):
            self.item = "Maggie"
            self.price = 70

        elif(self.choice == 2):
            self.item = "Burger"
            self.price = 120

        elif(self.choice == 3):
            self.item = "Pizza"
            self.price = 250

        elif(self.choice == 4):
            self.item = "Sandwich"
            self.price = 90

        else:
            print("Invalid Choice")


class Bill(Choice):

    def generateBill(self):

        print(f"\nItem Ordered : {self.item}")
        print(f"Total Bill   : {self.price} Rs")


class Thanks(Bill):

    def visitAgain(self):

        print("\nThank You For Visiting!!")
        print("Visit Again 😊")


c = Thanks()

c.showDetails()
c.yourChoice()
c.generateBill()
c.visitAgain()
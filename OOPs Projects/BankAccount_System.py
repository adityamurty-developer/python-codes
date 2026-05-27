class BankAccount:
    def __init__(self, name, num, balance):
        self.name = name
        self.num = num
        self.balance = balance

    def methods(self):
        while True:

            print("\n.....Choose the options.....")
            choice = int(input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\nEnter your choice: "))

            if(choice == 1):
                self.deposit()
            elif(choice == 2):
                self.withdraw()
            elif(choice == 3):
                self.checkBalance()
            elif(choice == 4):
                print("Thank You for using our bank service.")
                break

            else:
                print("Invalid choice entered!!")

    def deposit(self):
        amount = int(input("\nEnter Amount to Deposit: "))

        if(amount <= 0):
            print("Invalid Amount")
        else:
            self.balance += amount
            print(f"{amount} is deposited. Updated Balance: {self.balance}")

    def withdraw(self):
        amount = int(input("\nEnter Amount to Withdraw: "))

        if(amount <= 0):
            print("Invalid Amount")
        elif(amount > self.balance):
            print(f"Insufficient Balance. Your current balance is: {self.balance}")
        else:
            self.balance -= amount
            print(f"{amount} is Withdrawn. Updated Balance: {self.balance}")

    def checkBalance(self):
        print(f"\nCurrent Balance: {self.balance}")


c = BankAccount("Harry", 123456, 1200)
c.methods()
cost_price = int(input("Enter cost price of chocolate: "))
selling_price = int(input("Enter selling price of chocolate: "))

if (selling_price > cost_price):
    profit = selling_price - cost_price
    print("Shopkeeper has a profit of:", profit)

elif (selling_price == cost_price):
    print("Neither profit, nor loss.")

else:
    loss = cost_price - selling_price
    print("Shopkeeper is in a loss of:", loss)
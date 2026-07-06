# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 170,
    "MSFT": 200
}

print("===== STOCK PORTFOLIO TRACKER =====")

stock = input("Enter Stock Name (AAPL/TSLA/GOOGLE/AMZN/MSFT): ").upper()
quantity = int(input("Enter Quantity: "))

if stock in stock_prices:
    total = stock_prices[stock] * quantity

    print("\nStock Name:", stock)
    print("Price per Share:", stock_prices[stock])
    print("Quantity:", quantity)
    print("Total Investment:", total)

    choice = input("\nDo you want to save the result? (yes/no): ").lower()

    if choice == "yes":
        file = open("portfolio.txt", "w")
        file.write("Stock Portfolio Tracker\n")
        file.write("Stock Name: " + stock + "\n")
        file.write("Price per Share: " + str(stock_prices[stock]) + "\n")
        file.write("Quantity: " + str(quantity) + "\n")
        file.write("Total Investment: " + str(total))
        file.close()
        print("Result saved in portfolio.txt")
    else:
        print("Result not saved.")

else:
    print("Invalid Stock Name!")

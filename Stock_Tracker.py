# Simple Stock Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0

print("===== STOCK TRACKER =====")
print("Available Stocks:")
print("AAPL, TSLA, GOOGL, MSFT, AMZN")

while True:

    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    # Check whether stock exists
    if stock in stock_prices:

        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment

        print("Stock Price:", price)
        print("Investment:", investment)

    else:
        print("Stock not found!")

print("\n===== RESULT =====")
print("Total Investment Value: $", total_investment)
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 350
}

total = 0

print("Available Stocks:")
for stock, price in stocks.items():
    print(stock, ":", price)

n = int(input("How many stocks do you own? "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))

    if name in stocks:
        total += stocks[name] * qty

print("\nTotal Investment Value = $", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total}")

print("Result saved to portfolio.txt")
money_available = int(input("how much money you got in lankan rupees? : "))
exchange_rate =  float(input("whats the exchange rate per usd? : "))

convertion = money_available * exchange_rate

print(f"You currently have {money_available} lankan rupees, and when converted you get {round(convertion, 2)} amount of USD")
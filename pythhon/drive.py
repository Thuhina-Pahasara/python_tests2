range = int(input("How many kilometres you wanna ride? :"))
consumption = float(input("What is your fuel consumption?? :"))
fuel_price = int(input("Price per litre? :"))


litres_needed = range / consumption
total_cost = litres_needed * fuel_price

print(f"In order for you to travel {round(range)}km you gonna need {round(litres_needed)} litres of fuel and cost of {round (total_cost)} rupees")
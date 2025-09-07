
distance = float(input(f"How Far is the distance? : "))
fuel_consumption = float(input("What is your fuel consumption? :"))
fuel_price = float(input("Price of fuel per litre? :"))
extra_costs = float(input("Extra costs? :"))

fuel_needed = distance / fuel_consumption
fuel_cost = fuel_needed * fuel_price
grand_total = fuel_cost + extra_costs

print(f"For your {distance} km you gonna need {round(fuel_needed, 2)} litres of fuel so you need {round (fuel_cost, 2)} rupees in order to fuel and total cost will come to {round(grand_total, 2)} totally with other costs")
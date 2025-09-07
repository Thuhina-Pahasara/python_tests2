# Broken code - party budget calculator

num_guests = int(input("How many guests are coming? "))
ticket_price = float(input("Price per ticket: "))
budget = 5000

total_cost = ticket_price * num_guests

if total_cost >= budget :
    print(f"You are over budget! You need   {total_cost - budget} more rupees")
else :
    print(f"You are good! You will have  {budget - total_cost}  left")

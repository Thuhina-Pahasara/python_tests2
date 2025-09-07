price = float(input(" What is the price of the laptop?"))
balance = float(input(" How much money you got??"))
months_more = int(input("How long more you need to collect?"))
monthly_save = float(input(" How much you save monthly??"))

target_budget = balance + (months_more * monthly_save)

if target_budget >= price:
    print(f"Congrats on your new laptop in {months_more} months its yours and {target_budget - price} is left over for more,  game hard gamer!!!")

else :
   print(f"nah bruh you still need {price - target_budget} and must wait {months_more}, try increasing your monthly save of {monthly_save} for faster save")







friends = int(input(" How many friends are goin:? :"))
ticket_cost = float(input(" Total Price of tickets? : "))
snacks_cost = float(input(" Total Price of Snacks? : "))


grand_total = ticket_cost + snacks_cost

print(f" the total cost is {ticket_cost}, split between {friends}. so each friend must pay {grand_total / friends}")
friends = int(input("how many friends are coming? :"))
hours = float(input("how long does the party last? :"))
drinks = float(input("how many drinks will each friend drinks per hour? :"))
snacks = int(input("how many snacks will each your friends eat? : "))

total_drinks = friends * hours * drinks
total_snacks = friends * snacks

print(f" for {friends} at {hours} party, you will need a total of {total_drinks} and {total_snacks} in snacks bro ")
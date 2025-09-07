membership = 2500

user = float(input("How Much Money You got? :"))
sigup_for = int(input(" How Many Months you need this for? :"))

total_cost = membership * sigup_for


if total_cost <= user :
    print(f"welcome to the gym homie, you had {user} amount and now you have {membership - user} as balance")
else:
    print(f"nah bruh you broke, you need {membership - user} more to join this gym")    
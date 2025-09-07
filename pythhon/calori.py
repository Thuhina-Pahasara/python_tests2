



excercise = int(input("How many Different type of excersises you had? :"))

num_of_sets = int(input("how many sets you did? :"))
num_of_reps = int(input("how many reps you did? :"))
calori_burnt = float(input("how many calories you burnt? :"))


total_reps = num_of_sets * num_of_reps
total_calories = total_reps * calori_burnt

print(f"You did a total of {total_reps} and you burnt {total_calories}")
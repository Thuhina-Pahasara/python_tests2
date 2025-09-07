exercise_count = int(input("How many different types of exercises you did? : "))

total_reps = 0
total_calories = 0

for i in range(exercise_count):
    print(f"\nExercise {i+1}:")
    sets = int(input("  How many sets? : "))
    reps = int(input("  How many reps per set? : "))
    calories_per_rep = float(input("  How many calories per rep? : "))
    
    total_reps += sets * reps
    total_calories += sets * reps * calories_per_rep

print(f"\nYou did a total of {total_reps} reps today, burning {total_calories} calories!")

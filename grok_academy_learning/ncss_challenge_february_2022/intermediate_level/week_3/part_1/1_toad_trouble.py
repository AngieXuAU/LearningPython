initial_population = float(input("Initial population: "))
final_population = float(input("Final population: "))
counter = 0

while initial_population < final_population:
    initial_population = initial_population * 1.14
    counter += 1

final_population = int(final_population)

print(f"It would take {counter} years for there to be {final_population} cane toads.")

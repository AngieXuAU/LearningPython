plant_name = input("Which plant did you survey? ").lower()
number_of_plants = int(input("Count: "))

if 'fern' in plant_name:
    print("Fantastic! Keep looking for ferns!")
elif number_of_plants < 6:
    print(f"That's low. We'll put {plant_name} on the watch list.")
elif number_of_plants > 1:
    print(f"Great! Recorded {number_of_plants} {plant_name}s in this area.")
else:
    print(f"Great! Recorded {number_of_plants} {plant_name} in this area.")
    

list_of_birds = []
city_name = input("Enter a city file: ")

print("And the nominees are...")
with open(city_name) as whole_file:
    for line in whole_file:
        line = line.strip()
        if line not in list_of_birds:
            list_of_birds.append(line)

list_of_birds.sort()
for bird in list_of_birds:
    print(f"🐦 {bird}")

tour_name = input("Tour name: ")
city_names = input("Cities: ")
city_list = city_names.split()

print(f"Announcing the national {tour_name} tour!")
print("Visiting these cities...")

for city in city_list:
    print(f"🏙️ {city}")

print(f"Get excited for {tour_name}!")

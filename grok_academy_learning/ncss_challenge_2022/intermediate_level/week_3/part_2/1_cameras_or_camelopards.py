
item_list = []
counter = 0
index = 0

while counter < 3:
    new_item = input("Shop stock: ")
    if "cam" in new_item.lower():
        item_list.append(new_item)
        counter += 1

item_list.sort()
item_list.reverse()

print(f"Proposals: {item_list[0]}, {item_list[1]}, {item_list[2]}")

def buy_skins(dam):
    # Finish the function to convert DAM to skins
    return int(dam / 40)


# Write the rest of your program here
player_list = {}
print("Who's playing Dangerous Mafia?")
name_of_player = input("Name: ")

while name_of_player != "":
    starting_number_of_DAM = int(input("Starting number of DAM: "))
    print(f"{name_of_player}'s here, starting with {buy_skins(starting_number_of_DAM)} skins worth of DAM!")
    player_list[name_of_player] = starting_number_of_DAM
    name_of_player = input("Name: ")

print("Let's play!")
player_participated = input("Who played? ")

while player_participated != "":
    DAM_gained = int(input("DAM won/lost: "))
    if player_participated in player_list.keys():
        player_list[player_participated] += DAM_gained
    else:
        player_list[player_participated] = DAM_gained
    player_participated = input("Who played? ")

print("End of the game! Let's see how everyone did!")
for name_of_player, player_list[name_of_player] in player_list.items():
    print(f"{name_of_player} can buy {buy_skins(player_list[name_of_player])} skins.")

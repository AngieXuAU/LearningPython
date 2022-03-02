
players = ['Nicola', 'Penny', 'Dom', 'Nathan', 'Josie']

friend_found = input("Who did you find? ")


def is_zombie_present(name_of_friend_found):
    for i in players:
        if name_of_friend_found == i:
            position_index = players.index(friend_found)
            players[position_index] = "Zombie"
            print(f"{name_of_friend_found} has turned into a zombie!")
            return 1

    return 0


if is_zombie_present(friend_found) == 0:
    print("Everyone is still in the game!")

print(f"Remaining players: {players[0]}, {players[1]}, {players[2]}, {players[3]}, {players[4]}")

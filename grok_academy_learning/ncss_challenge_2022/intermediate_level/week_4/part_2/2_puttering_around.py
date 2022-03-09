
scores = {}
name_of_player = input("Player: ")

while name_of_player != "":
    points_earned = int(input("Score: "))
    if name_of_player in scores:
        scores[name_of_player] += points_earned
    else:
        scores[name_of_player] = points_earned
    name_of_player = input("Player: ")

print("Final results:")
for name_of_player, scores[name_of_player] in scores.items():
    print(f"{name_of_player}: {scores[name_of_player]}")

# Calculate the power of a team
def team_power(team):
    power = 0

    for letter in team:
        power += ord(letter)

    average_power = int(power / len(team))

    return average_power


# Add your code after this.
first_team_power = team_power(input("Team 1: "))
second_team_power = team_power(input("Team 2: "))

if first_team_power == second_team_power:
    print("A tie!")
elif first_team_power > second_team_power:
    print("Team 1 wins!")
else:
    print("Team 2 wins!")

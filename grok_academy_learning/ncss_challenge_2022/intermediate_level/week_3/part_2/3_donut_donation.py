
total_donated_value = 0
donor_list = []
print("Thanks all for coming to donut donation day!")

next_donor = input("Who's next to donate? ")
while next_donor:
    donated_value = float(input("How much are you donating? "))
    if next_donor in donor_list:
        print(f"Another generous donation from {next_donor} of ${donated_value:.2f}!")
    else:
        donor_list.append(next_donor)
        print(f"Thanks {next_donor}! A first donation of ${donated_value:.2f}!")
    total_donated_value += donated_value
    next_donor = input("Who's next to donate? ")

print(f"That's it folks! We raised ${total_donated_value:.2f}!\nAll thanks to our delicious donors:")

donor_list.sort()
for individual_donor in donor_list:
    print(f"🍩 {individual_donor}")


name_said = input("Spy name: ")

if "Smart" not in name_said:
    print("Identity safe.")
else:
    print(name_said.replace("Smart", "SURNAME"))

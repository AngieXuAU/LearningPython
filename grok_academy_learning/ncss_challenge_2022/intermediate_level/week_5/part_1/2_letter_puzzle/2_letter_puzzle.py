
beginning_letter = input("Letter: ").upper()
hidden_message = ''

with open("puzzle.txt") as puzzle_document:
    for line in puzzle_document:
        line = line.strip()
        if line[0] == beginning_letter:
            hidden_message += line[-1]

print(f"Hidden message: {hidden_message}")

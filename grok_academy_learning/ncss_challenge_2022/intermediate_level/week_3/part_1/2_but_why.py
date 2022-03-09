answer = input("Why does the sun rise in the east? ")

while "i don't know" not in answer.lower():
    print("hmm...")
    answer = input("But why? ")

print("Let's find out!")

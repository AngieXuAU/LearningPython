
cypher_key = {}
deciphered_message = ""

with open("substitution.txt")as file:
    for line in file:
        value, key = line.split()
        cypher_key[key] = value

secret_message = input("Secret Message: ")

for letter in secret_message:
    if letter.isalpha():
        deciphered_message = deciphered_message + cypher_key[letter]
    else:
        deciphered_message = deciphered_message + letter

print(f"Translation: {deciphered_message}")

# Encrypt word with a cipher
def encrypt(word):
    if word == '':
        return '<no-input>'

    first_letter = chr(ord(word[0]) + 2)
    last_letter = chr(ord(word[-1]) + 2)
    middle = word[-2:0:-1]  # this takes the middle out of the word and reverses it
    return f'{first_letter}{middle}{last_letter}'


# Add your code after this.
input_word = input("Person? ")
print(f"Find {encrypt(input_word)}.")

input_location = input("Location? ")
print(f"They will be at {encrypt(input_location)}.")

input_password = input("Password? ")
print(f"The password is {encrypt(input_password)}.")

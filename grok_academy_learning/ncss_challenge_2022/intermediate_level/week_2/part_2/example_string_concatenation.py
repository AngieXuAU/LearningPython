word = input('Enter a word: ').upper()
last_letter = word[-1]

if last_letter in 'AEIOU':
    # Make the word echo
    for i in range(3):
        word = word + f'-{last_letter}'
print(f'{word}!')

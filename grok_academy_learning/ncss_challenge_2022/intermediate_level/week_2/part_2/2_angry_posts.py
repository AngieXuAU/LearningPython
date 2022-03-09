post_by_word = input("Post: ").split()
number_of_angry_words = 0

for word in post_by_word:
    if word.isupper():
        number_of_angry_words += 1

print(f"Number of angry words: {number_of_angry_words}")


counter = 0

text_name = input("Speech file: ")
with open(text_name, encoding="utf8") as whole_file:
    for file_line in whole_file:
        words = file_line.split()
        for word in words:
            if counter > 199:
                break
            if counter % 5 == 0:
                if counter == 195:
                    print(word)
                else:
                    print(word, end=" ")
            counter += 1

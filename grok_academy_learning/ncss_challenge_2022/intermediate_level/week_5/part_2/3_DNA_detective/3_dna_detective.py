
def get_sample(sample_filename):
    # Given the name of a sample file, get the DNA chunk from the file
    with open(sample_filename) as file:
        file_contents = file.read()
    # Return the DNA chunk as a string
    return file_contents


def get_known_dna_pairs(pair_filename):
    dna_dictionary_list = {}
    with open(pair_filename) as known_pairs_file:
        for pairing in known_pairs_file:
            animal_name, corresponding_dna = pairing.split()
            dna_dictionary_list[animal_name] = corresponding_dna
    return dna_dictionary_list


def match_dna(sample_dna, dna_dict):
    matched = []
    for key in dna_dict:
        if sample_dna in dna_dict[key]:
            matched.append(key)
    return matched


dna_dictionary = get_known_dna_pairs("dna_pairs.txt")
sample = get_sample(input("Enter sample file name: "))
result = match_dna(sample, dna_dictionary)
result.sort()

# Display results
if len(result) == 1:
    print(f"That appears to be from a {result[0]}.")
elif len(result) > 1:
    print(f"It could be for any of these animals: {', '.join(result)}.")
else:
    print("This is a new one!")

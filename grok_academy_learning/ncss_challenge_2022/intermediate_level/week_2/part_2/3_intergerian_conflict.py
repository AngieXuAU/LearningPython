primeans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
            97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
            199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
            331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
            457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]


def check_domain(number):
    domains_function_output = ''
    # Find the domains this number belongs to
    if number % 5 == 0:
        domains_function_output = domains_function_output + "Pentadian "
    # Check if it belongs to other domains after this
    if number < 0:
        domains_function_output = domains_function_output + "Minutian "
    # Check if it has 2
    if "2" in str(number):
        domains_function_output = domains_function_output + "Disiphine "
    # Check if it is prime
    for n in primeans:
        if n == number:
            domains_function_output = domains_function_output + "Primean "
    # Return function output
    return domains_function_output


# Write the rest of your program after this

integer_list_as_string = input("Enter numbers: ").split()
number_of_free_numbers = 0

for i in integer_list_as_string:
    domains = check_domain(int(i))
    if domains != "":
        print(f"{i} is a {domains}citizen.")
    else:
        number_of_free_numbers += 1

print(f"Free numbers: {number_of_free_numbers}")

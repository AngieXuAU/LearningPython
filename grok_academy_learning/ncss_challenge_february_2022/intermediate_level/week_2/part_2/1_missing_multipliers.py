# input of base and step
base_value = int(input("Times table: "))
step_value = int(input("Step: "))

# loop for output
for n in range(3, 13, step_value):
    product = n * base_value
    print(f"{base_value} x [ ] = {product}")

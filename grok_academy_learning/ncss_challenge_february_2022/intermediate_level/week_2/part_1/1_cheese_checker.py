cheeses = ['Cheddar', 'Bocconcini', 'Haloumi', 'Paneer', 'Gorgonzola', 'Mozzarella', 'Parmesan', 'Brie', 'Gruyere']

# Add your code after this.

cheese_in_question = input("Cheese: ")

if cheese_in_question in cheeses:
    print(f"{cheese_in_question} is a cheese!")
else:
    print(f"{cheese_in_question} might not be a cheese.")
    
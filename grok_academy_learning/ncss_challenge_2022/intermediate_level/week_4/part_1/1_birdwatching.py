
journal = {'ibis': 'Bin near the beach.', 'magpie': 'Swooping in local park.', 'noisy miner': 'Outside kitchen window.', 'seagull': 'Stealing my chips.', 'cockatoo': 'Neighbours lemon tree.', 'lorikeet': 'Palm tree.', 'peregrine falcon': 'On the livestream.', 'emu': 'Mutawintji National Park.', 'wedge-tailed eagle': 'Driving to Freycinet.', 'penguin': 'Middle Island.', 'kookaburra': 'Old gumtree.', 'nativehen': 'Being a turbo chook.'}

name_of_bird = input("Enter a bird: ").lower()
if name_of_bird in journal:
    print(f"{journal[name_of_bird]}")
else:
    print("Never seen that bird!")


recommendations = {}

while len(recommendations) < 5:
    name_of_friend = input("Name: ")
    stream_recommended = input("Which stream did they recommend? ")
    if stream_recommended in recommendations:
        print("Someone else already recommended that.")
    else:
        print(f"{name_of_friend} recommended {stream_recommended}!")
        recommendations[stream_recommended] = name_of_friend

print("Playlist complete! Subscribe to:")
for stream_recommended, name_of_friend in recommendations.items():
    print(f"{stream_recommended}: recommended by {name_of_friend}")

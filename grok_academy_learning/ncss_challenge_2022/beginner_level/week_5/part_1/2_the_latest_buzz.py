
# Write your function here
def is_positive(review):
    review_result = "neutral"

    if "fun" in review or "exciting" in review or "friendly" in review:
        review_result = "positive"

    return review_result


###


if __name__ == '__main__':
    print(is_positive('It was lots of fun!'))
    print(is_positive('Such a friendly beekeeper!'))

    # Add more testing here.
    print(is_positive('Such an exciting adventure!'))
    print(is_positive('It was fun, exciting and the workers were friendly!'))
    print(is_positive("blah blah it was super boring I hated it"))


def weight_class(n):
    if n > 67:
        result = 'Heavyweight'
    elif n > 57:
        result = 'Welterweight'
    elif n > 49:
        result = 'Featherweight'
    else:
        result = 'Flyweight'
    return result


if __name__ == '__main__':
    print(weight_class(100))
    print(weight_class(42))
    print(weight_class(71))
    print(weight_class(59))

    # Add your own testing after this.
    print(weight_class(55))

def to_celsius(f):
    # Calculate the temperature in Celsius
    return round(((f - 32) * 5 / 9), 1)


def aussie_phrase_output(temp_in_fahrenheit):
    celsius = to_celsius(temp_in_fahrenheit)
    if celsius < 5:
        return "Crikey it's cold!"
    elif celsius < 20:
        return "Getting a bit nippy!"
    elif celsius < 35:
        return "You beaut beach weather!"
    else:
        return "Strewth, it's a scorcher!"


# Write the rest of your program here
temperature_in_fahrenheit = float(input("Temp (F): "))
print(f"{to_celsius(temperature_in_fahrenheit)} C - {aussie_phrase_output(temperature_in_fahrenheit)}")

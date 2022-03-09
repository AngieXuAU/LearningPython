def is_crowd(people):
  # Write your function here.
  if people == 3:
    return 'a crowd'
  elif people >= 30:
    return 'a crowd'
  else:
    return 'no crowd'

# Write the rest of your program here.

number_of_people = int(input("Number of people: "))
print("There's " + is_crowd(number_of_people) + " here!")
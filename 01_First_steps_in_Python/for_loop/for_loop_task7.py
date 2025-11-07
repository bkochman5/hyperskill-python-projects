# Keanu wants to create a Python program that recommends one of his movies to the user, based on their age:
#
#     Age <= 14 | "Toy Story 4"
#
#     Age 15 - 18 | "The Matrix"
#
#     Age 19 - 25 | "John Wick"
#
#     Age 26 - 35 | "Constantine"
#
#     Age > 35 | "Speed"
#
# Help him write the code by using an if...elif...else statement to evaluate the user's age and recommend them a movie.

age = int(input("How old are you?: "))

if age <= 14:
    print("Toy Story 4")
elif age > 14 and age <= 18:
    print("The Matrix")
elif age >= 19 and age <= 25:
    print("John Wick")
elif age >= 26 and age <= 35:
    print("Constantine")
else:
    print("Speed")
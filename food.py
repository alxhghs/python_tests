from random import randint

unagi, katsu = 0, 1
food_choice = randint(0, 1)

if food_choice == 0:
    print("You're getting unagi!")
elif food_choice == 1:
    print("You're geting katsu!")

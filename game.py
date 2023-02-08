from random import randint

name = input("Hi! whats your name?")

for guess_number in range(1, 6):
    mounth_number = randint(1,12)
    day_number = randint(1, 31)
    year_number = randint(1995, 2008)

    print("Guess",guess_number, "were you born in ",mounth_number,"/", year_number,"/",day_number, "?")

    response = input("yes or no? ")

    if response == "yes":
        print("i knew it!")
        exit()
    elif guess_number == 5:
        print("i have other things to do. good bye.")
    else:
        print("drat! leme try again!")

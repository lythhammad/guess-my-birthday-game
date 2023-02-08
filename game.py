from random import randint

name = input("Hi! whats your name!")

guess_number = 1
mounth_number = randint(1,12)
day_number = randint(1, 31)
year_number = randint(1995, 2008)

print("Guess 1 :", name, "were you born in ",mounth_number,"/", year_number,"/",day_number, "?")

response = input("yes or no? ")

if response == "yes":
    print("i knew it")
    exit()
else:
    print("drat! leme try again!")


mounth_number = randint(1, 12)
year_number = randint(1995, 2008)
day_number = randint(1, 31)

print("guess 2 :",name, "were you born in", mounth_number, "/", year_number,"/",day_number, "?")

response = input("yes or no? ")

if response == "yes":
    print("i knew it!")
    exit()
else:
    print("drat! lemme try again!")


mounth_number = randint(1, 12)
year_number = randint(1995, 2008)
day_number = randint(1, 31)

print("guess 3 :",name, "were you born in", mounth_number, "/", year_number,"/",day_number, "?")

response = input("yes or no? ")

if response == "yes":
    print("i knew it!")
    exit()
else:
    print("drat! lemme try again!")

mounth_number = randint(1, 12)
year_number = randint(1995, 2008)
day_number = randint(1, 31)

print("guess  :",name, "were you born in", mounth_number, "/", year_number,"/",day_number, "?")

response = input("yes or no? ")

if response == "yes":
    print("i knew it!")
    exit()
else:
    print("drat! lemme try again!")

mounth_number = randint(1, 12)
year_number = randint(1995, 2008)
day_number = randint(1, 31)

print("guess 5 :",name, "were you born in", mounth_number, "/", year_number,"/",day_number, "?")

response = input("yes or no? ")

if response == "yes":
    print("took a min but i got it!")
    exit()
else:
    print("I have batter thing to do in life bye!")

# Guess That Number

import random

print("Welcome to Guess That Number!")
print(" ")
print("Put a 1, 2, or 3, to start guessing! ")
print(" ")
print(" ")

random_number_1 = 0
answer = 0


def number_guess_game(mode):
    
    global random_number_1, answer
    
    sd = True
    lives = 10

    starting_hint = False

    if mode == 1:
        answer = random.randint(1, 1000)
        print("Mode selected: Hard")
        print(" ")

    elif mode == 2:
        answer = random.randint(1, 100)
        print("Mode selected: Medium")
        print(" ")

    elif mode == 3:
        answer = random.randint(1, 50)
        print("Mode selected: Easy")
        print(" ")

    else:
        print("Something Wrong Happened!")
        input("Restart Code")

    if sd:
        print("Sudden Death Active!")
        print(" ")
    trys = 0

    # STARTING HINT
    coin_flip_1 = random.randint(1, 2)
    
    if coin_flip_1 == 1:
        random_number_1 = random.randint(answer, answer + 30)
    random_number_1 = random.randint(answer, answer + 15)
    
    if starting_hint:
        print(" ")
        print("The number you seek is around " + str(random_number_1))
        print(" ")

    while True:
        g = int(input("Guess: "))
        print(" ")

        if sd:
            if trys >= lives:
                print("You lost!")
                print("Number was: " + str(answer))
                print(" ")
                input("Restart Code if you dare!")
                
        if g == answer:
            print("GGs! You got it!")
            if trys == 1:
                print("You guessed it first try!")
                print(" ")
                input("Restart Code")

            else:
                print("You guessed it in " + str(trys) + " trys!")
                print(" ")
                input("Restart Code")

        elif g < answer:
            print("Guess is too low!")
            print(" ")
            trys += 1
            
            if sd:
                print("You have " + str(lives - trys) + " lives left")
                print(" ")

        elif g > answer:
            print("Guess is too high!")
            print(" ")
            trys += 1
            
            if sd:
                print("You have " + str(lives - trys) + " lives left")
                print(" ")

        elif str(input("Guess: ")) == "":
            print("Something wrong happened!")


print("3 modes, (1) HARD 1-1000, (2) MEDIUM 1-100, (3) EASY 1-50")
print(" ")
ok = int(input("mode: "))

number_guess_game(ok)

# Extra Info/Tips

# If you every see a hint above the range, thats perfectly normal, the actual number can never be above the maximum 
# for that mode.

# NEVER use space when putting in answers, it will cause the code to send an error.

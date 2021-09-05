# Import the random module so we can use its randint function
import random

while True:

    upper = input("Choose an upper bound for the random number (q to exit): ")
    if upper == "q":
        break

    random_num = random.randint(0, int(upper))
    guesses = int(upper) / 3
    guess = -1

    while guess != random_num and guesses > 0:
        guess = int(input("Guess a number between 0 and " + upper + ": "))
        guesses -= 1
        if guess == random_num:
            print("Congratulations! " + str(guess) + " is correct!\n")
        elif guesses == 0:
            print("Oops... you ran out of guesses. The correct number was " + str(random_num) + ".\n")
        elif guess < random_num:
            print("Too low!")
        else:
            print("Too high!")
print("Thanks for playing!")
import random

def guessing_game():
    number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


guessing_game()
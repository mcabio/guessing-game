"""A number-guessing game."""

import random

# player = input("What's your name? ")
# print(f"Nice to meet you, {player}, let's play a guessing game!")

# secret = random.randint(1,100)


# guess = int(input("Guess a number between 1 to 100. "))

# while guess != secret:
#     if guess < secret:
#         print()
#         guess = int(input("Try again, the secret number is higher. Guess a number between 1 and 100. "))

#     elif guess > secret:
#         print()
#         guess = int(input("Try again, the secret number is lower. Guess a number between 1 and 100. "))

     
    
# print("CONGRATULATIONS YOU GOT THE NUMBER!")

def guessing_game(guess):
    """Guessing game function"""
    player = input("Hello, what's your name? >>> ")
    print()
    print(f"Nice to meet you, {player}, let's play a guessing game!")

    while True:
        secret_num = random.randint(1,100)
        print()
        guess = int(input("Guess a number between 1 to 100. >>> "))

        while secret_num != guess:
            if secret_num < guess:
                guess = int(input("Guess again, the secret number is lower. >>> "))
            elif secret_num > guess:
                guess = int(input("Guess again, the secret number is higher. >>> "))

        print("CONGRATULATIONS, YOU GUESSED CORRECTLY!")
        print()

        replay = input("Would you like to play again? y/n? >>> ")
        if replay.lower() != "y":
            print("Thanks for playing!")
            break

guessing_game(50)




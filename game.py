"""A number-guessing game."""

import random

player = input("What's your name? ")
print(f"Nice to meet you, {player}, let's play a guessing game!")

secret = random.randint(1,100)


guess = int(input("Guess a number between 1 to 100. "))

while guess != secret:
    if guess < secret:
        print()
        guess = int(input("Try again, the secret number is higher. Guess a number between 1 and 100. "))

    elif guess > secret:
        print()
        guess = int(input("Try again, the secret number is lower. Guess a number between 1 and 100. "))

     
    
print("CONGRATULATIONS YOU GOT THE NUMBER!")


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
    scores = []

    while True:
        secret_num = random.randint(1,100)
        print()
        guess = int(input("Guess a number between 1 to 100. >>> "))
        guesses = 0 # This counts how many guesses it takes for player to get to the correct number
        

        while secret_num != guess:
            if secret_num < guess:
                guesses += 1
                guess = int(input("Guess again, the secret number is lower. >>> "))
            elif secret_num > guess:
                guesses += 1
                guess = int(input("Guess again, the secret number is higher. >>> "))

        print(f"CONGRATULATIONS, YOU GUESSED CORRECTLY! You guessed {guesses} times to get to the secret number!")
        scores.append(guesses)
        print()

        replay = input("Would you like to play again? y/n? >>> ")
        if replay.lower() != "y": # if replay doesn't equal "y", the loop exits
            best_score = scores[0]
            for i in scores[1:]:
                if i < best_score:
                    best_score = i
            print("Thanks for playing!")
            print(f"You're best score is {best_score}")
            break

guessing_game(50)




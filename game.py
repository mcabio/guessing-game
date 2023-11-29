user_name = input("Hi, there, what's your name?: ")
print("Hello, " + user_name + "! Nice to meet you. Let's play a game.")

import random

random_num = random.randint(1,100)
guess_num = int(input("Pick a number between 1 and 100. >>> "))

while guess_num != random_num:
    if guess_num < random_num:
        print()
        guess_num = int(input("Sorry, guess again...the number is higher. >>> "))
        print()
    elif guess_num > random_num:
        print()
        guess_num = int(input("Sorry, guess again...the number is lower. >>> "))
        print()

print("Congratulations, you guessed it!")
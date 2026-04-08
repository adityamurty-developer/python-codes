# number guessing game

import random

computer = random.randint(1, 100)
chances = 10

print("🕹️  Number Guessing Game! You have 10 chances.")

while chances > 0:
    guess = int(input("Choose a number between (1-100): "))

    if guess < 1 or guess > 100:
        print(f"{guess} is invalid! Choose a valid number.")
        continue   

    chances -= 1

    if guess > computer:
        print(f"{guess} is too high!")
    elif guess < computer:
        print(f"{guess} is too low!")
    else:
        print(f"{guess} is correct! You won🥳")
        break

    print(f"Chances left: {chances}")

else:
    print(f"Oops! You lose. The number was {computer}")
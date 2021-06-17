import random

number = random.randint(1, 100)
numberOfGuesses = 0
while(numberOfGuesses < 10):
    print("Guess a number between 1 and 100 \n")
    guess = input()
    guess = int(guess)
    if guess == number:
        print(f"You guessed it! The number was {number}")
        break
    numberOfGuesses += 1

print(f"Sorry you didn't guess the right number the answer was {number}")
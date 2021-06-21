import random
number = random.randint(1, 100)
numberOfGuesses = 0
print("Welcome to the guess the number game! You only have 10 tries so guess wisely")
while(numberOfGuesses < 10):
    print("Guess a number between 1 and 100 \n")
    guess = input()
    guess = int(guess)
    if guess == number:
        print(f"You guessed it! The number was {number} You took {numberOfGuesses} tries to guess the answer.")
        break
    elif guess != number:
        if guess < number:
            print("That number is too low guess again")
        else:
            print("That number is too high guess again")
    else:
        print(f"Sorry you didn't guess the right number the answer was {number}.")
    numberOfGuesses += 1

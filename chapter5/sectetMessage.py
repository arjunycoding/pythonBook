password = "cupcakes"
guesses = 10
secret = "Tomorrow I will bring cookies for you and me to share at lunch"
i = 0
while(i < guesses):
    guess = input("What is the password \n")
    if(guess == password):
        print(secret)
        break
    i += 1
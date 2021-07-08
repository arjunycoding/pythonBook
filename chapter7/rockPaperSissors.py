print("Welcome to the Rock Paper Sissors Game!")
print("What is your name?")
player1 = input()
print("Type what you chose(Rock Paper or Sissors)")
import random
player2 = "the computer"
opaitons = ["rock", "paper", "scissors"]
def compare(item1, item2):
    if item1 == item2:
        print("It's a tie")
    elif item1 == "rock" and item2 == "paper" or item1 == "paper" and item2 == "rock":
        print("paper wins")
    elif item1 == "rock" and item2 == "scissors" or item1 == "scissors" and item2 == "rock":
        print("rock wins")
    elif item1 == "paper" and item2 == "scissors" or item1 == "scissors" and item2 == "paper":
        print("rock scissors")
    else:
        print("Not a vialid item")
    
player1Choice = input()
player2Choice = opaitons[random.randint(0, 2)]
print(f"{player1} chose {player1Choice}.{player2} chose {player2Choice}")
print(compare(player1Choice, player2Choice))
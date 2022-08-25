'''
(formatted file at google drive: https://docs.google.com/document/d/1Fhru_t7CyJsmgPzxcSLpL8PyrHx6TDdGSdUiSfKolF8/edit?usp=sharing )

1. Rock, paper and scissors game
In the rock, paper and scissors game the goal is to create a command-line game where a user has the option to choose between rock, paper and scissors.The program also selects randomly one of the three options. Then the program adds the point to the computer or a player (if someone is the winner) and displays actual scores. The user is is asked if he wants to play again or not.

Hints:

At the beginning create a list with all options (rock, paper and scissors as strings). Then you can choose one of the options randomly using the code:
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)

Remember that in python ‘Paper’ is not the same as ‘paper’.
'''
import random
new_game = "y"
while new_game == "y":
    user_action = input("Pick your choice - Rock/Paper/Scissors: ")
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    if user_action == computer:
        print("It's a draw! Computer has also picked: " + computer)
    elif user_action == "Rock":
        if computer == "Scissors":
            print("You won! Computer has picked: " + computer)
        else:
            print("You loose! Computer has picked: " + computer)
    elif user_action == "Scissors":
        if computer == "Paper":
            print("You won! Computer has picked: " + computer)
        else:
            print("You loose! Computer has picked: " + computer)
    elif user_action == "Paper":
        if computer == "Rock":
            print("You won! Computer has picked: " + computer)
        else:
            print("You loose! Computer has picked: " + computer)
    new_game = input("Wanna play again? y/n: ")
    if new_game == "y":
        print("have fun!")
    else: 
        print("thank you!")
        break
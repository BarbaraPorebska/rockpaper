import random

user_points = 0
comp_points = 0

while(True):
    user_action = input("Chose your destiny (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print ("You have chosen: " + user_action)
    print ("Program have chosen: " + computer_action)
    if user_action == computer_action:
        print("Both players selected " + user_action + ". It's a draw!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You win!")
            user_points += 1
        else:
            print("You lose.")
            comp_points += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("You win!")
            user_points += 1
        else:
            print("You lose.")
            comp_points += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You win!")
            user_points += 1
        else:
            print("You lose.")
            comp_points += 1
    print ("Your points: " + str(user_points))
    print ("Computer points: " + str(comp_points))
    new_game = input("Would you like to play again? y/n")
    if new_game == "y":
        print("ok, cool")
    else:
        print("thanks, bye")
        break
    


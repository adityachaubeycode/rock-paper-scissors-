print(" Welcome to rock,  paper , scissors  game ")
print(" this is my own game ")

import random

def get_choices():
    player_choices =input(" enter your choice (rock , paper , scissors : ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choices  = random.choice(options)
    choices = {"player": player_choices, "computer": computer_choices}
    return choices


def check_win(player , computer):
    print(f"\nYou chose {player}, computer chose {computer}.")
    if player == computer:
        print( " it is a tie !")
    elif player == "rock"  :
      if computer == "scissors":
        print(" Player has won")
      else :
         print(" Computer has won ") 
    elif player == "paper"  :
      if computer == "scissors":
        print(" Computer has won")
      else :
         print(" Player has won ")
    elif player == "scissors"  :
      if computer == "rock":
        print(" Computer has won")
      else :
         print(" Player has won ")
   
choices = get_choices()
check_win(choices["player"], choices["computer"])

def play_game():
   print("welcomr to rock paper scissors !")
while True:
        choices = get_choices()
        check_win(choices["player"], choices["computer"])

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
play_game()




    
    
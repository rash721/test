import random


def check_win(player, computer):
  print(f"You chose {player} and computer chose {computer}")
  if player == computer:
    print("It's a tie!")
  elif player == "rock":
    if computer == "scissors":
      print("Rock smashes scissors! You win!")
    else:
      print("Paper covers rock! You lose.")
  elif player == "paper":
    if computer == "rock":
      print("Paper covers rock! You win!")
    else:
      print("Scissors cuts paper! You lose.")
  elif player == "scissors":
    if computer == "paper":
      print("Scissors cuts paper! You win!")
    else:
      print("Rock smashes scissors! You lose.")
  else:
    print("Invalid input")


def get_choices():
  player_choice = input("Enter a choice(rock,paper,scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  check_win(player_choice, computer_choice)
  #print(isinstance(player_choice,int))
  return choices


get_choices()

import random

def get_choises():
  player_choice = input("Enter a choice (Rock, Paper, Scissors): ")
  
  computer_options = ["Paper","Rock","Scissors"]
  computer_choice = random.choice(computer_options)
  
  choices = {"player": player_choice, "computer": computer_choice}
  return choices
  
def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie"
  elif player == "Rock":
    if computer == "Scissors":
      return "Rock smashes scissors! You Win!"
    else:
      return "Paper covers rock! You lose"

  
  elif player == "Paper":
    if computer == "Rock":
      return "Paper covers rock! You Win!"
    else:
      return "Scissors cuts Paper! You lose"

  
  elif player == "Scissors":
    if computer == "Paper":
      return "Scissors cuts Paper! You Win!"
    else:
      return "Rock smashes scissors! You lose."


choices = get_choises()
result = check_win(choices["player"], choices["computer"])
print(result)


  

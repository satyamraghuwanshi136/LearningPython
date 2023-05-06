import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#### Rules of the game ###
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

#Logic

print("Welcome to the Rock 🪨, Paper 📃 and Scissors ✂️  Game....")
game_elements = ["Rock", "Paper", "Scissors"]
game_graphics = [rock, paper, scissors]

while True:
  print("Please enter 5 to exit the game 🎮")
  client_input = int(input("Please select 0 for Rock 🪨, 1 for Paper 📃 and 2 for Scissors ✂️ \n"))

  if client_input == 5:
    exit()
  
  if client_input != 0 and client_input != 1 and client_input != 2:
    print("Please select a valid number! \n\n")
    continue

  # -1 for draw, 0 for client won, 1 for computer won
  winner = -1

  computer_input = random.randint(0,2)

  print(f"You selected: {game_elements[client_input]} \n {game_graphics[client_input]}")
  print(f"Computer selected: {game_elements[computer_input]} \n {game_graphics[computer_input]}")

  if client_input == 0 and computer_input == 2:
    winner = 0
  elif computer_input == 0 and client_input == 2:
    winner = 1
  elif computer_input > client_input:
    winner = 1
  elif client_input > computer_input:
    winner = 0
  elif computer_input == client_input:
    winner = -1
 
  if winner == 0:
    print("You Won 🏆")
  elif winner == 1:
    print("Computer Won 🏆")
  else:
    print("Draw 🥱")
    
  print("\n_______________________________________________________________________\n")
  

# if game_elements[client_input] == "Rock":
#   if game_elements[computer_input] == "Rock":
#     winner = -1
#   elif game_elements[computer_input] == "Paper":
#     winner = 1
#   else:
#     winner = 0
# elif game_elements[client_input] == "Paper":
#   if game_elements[computer_input] == "Rock":
#     winner = 0
#   elif game_elements[computer_input] == "Paper":
#     winner = -1
#   else:
#     winner = 1
# else:
#   if game_elements[computer_input] == "Rock":
#     winner = 1
#   elif game_elements[computer_input] == "Paper":
#     winner = 0
#   else:
#     winner = -1

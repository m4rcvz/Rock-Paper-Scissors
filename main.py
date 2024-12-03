import random 

def get_user_choice():
  choice = input("Choose Rock Paper or Scissors: ")
  return choice


def get_computer_choice():
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  return computer_choice
  
def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    print("It's a tie!")

  elif (user_choice == "scissors" and computer_choice == "paper") or \
  (user_choice == "rock" and computer_choice == "scissors") or \
  (user_choice == "paper" and computer_choice == "rock"): 
    print("You won!")

  else:
    print("The computer won!")

user_choice = get_user_choice()
computer_choice = get_computer_choice()
print(f"You chose: {user_choice}")
print(f"The computer chose: {computer_choice}")
determine_winner(user_choice, computer_choice)

while True:
  try:
   choice = input("Choose 'rock', 'paper', or 'scissors' : ")
  if choice not in ["rock", "paper", "scissors"]:
raise ValueError

except ValueError:
  print("Please enter 'rock', 'paper', or 'scissors',")

else:
  print(choice)
  break

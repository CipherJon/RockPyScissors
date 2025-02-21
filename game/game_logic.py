import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"

def play_game():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    winner = get_winner(player_choice, computer_choice)
    if winner == "draw":
        print("It's a draw!")
    elif winner == "player":
        print("You win!")
    else:
        print("Computer wins!")
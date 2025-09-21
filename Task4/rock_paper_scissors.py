# Rock-Paper-Scissors Game

import random

def get_computer_choice():
    """Randomly selects a choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on the game rules."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0

    print("--- ROCK, PAPER, SCISSORS ---")
    
    while True:
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = get_computer_choice()
        
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final score -> You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()
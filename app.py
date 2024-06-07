import random

def get_computer_choice():
    """Randomly selects and returns one of 'rock', 'paper', or 'scissors' for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    """Prompts the user to enter a choice and returns it if valid, or informs them if it's invalid."""
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid option. Please choose rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    """Determines and returns the outcome of the game ('win', 'lose', or 'tie')."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    else:
        return 'lose'

def play_game():
    """Runs the Rock, Paper, Scissors game, tracks scores, and allows for repeated play."""
    player_score = 0
    rounds_played = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        print(f"Computer chose: {computer_choice}")
        if result == 'win':
            print("You won this round!")
            player_score += 1
        elif result == 'lose':
            print("You lost this round!")
        else:
            print("It's a tie!")

        rounds_played += 1

        play_again = input("Do you want to play again? (yes or no): ").lower()
        if play_again != 'yes':
            break

    print(f"Game over. You played {rounds_played} rounds and won {player_score} times.")

if __name__ == "__main__":
    play_game()

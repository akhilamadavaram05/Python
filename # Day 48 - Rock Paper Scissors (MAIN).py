# Day 48 - Rock Paper Scissors (MAIN)
import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    if (player == "Rock" and computer == "Scissors") or
       (player == "Paper" and computer == "Rock") or
       (player == "Scissors" and computer == "Paper"):
        return "You win"
    return "Computer wins"

def main():
    print("Rock, Paper, Scissors")
    player_wins = 0
    computer_wins = 0

    while True:
        player = input("Choose Rock, Paper, or Scissors (or quit): ").strip()
        if player.lower() in ["quit", "q"]:
            break
        if player not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice")
            continue

        computer = get_computer_choice()
        print(f"Computer: {computer}")

        result = determine_winner(player, computer)
        print(result)

        if result == "You win":
            player_wins += 1
        elif result == "Computer wins":
            computer_wins += 1

    print(f"\nFinal: You {player_wins} - {computer_wins} Computer")

if __name__ == "__main__":
    main()
#Day 33 - Game Helper
import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    score = {"player": 0, "computer": 0}
    
    for i in range(3):
        computer = random.choice(choices)
        player = input(f"Round {i+1} - rock/paper/scissors: ").lower()
        print(f"Computer chose: {computer}")
        
        if player == computer:
            print("Tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            score["player"] += 1
            print("You win this round!")
        else:
            score["computer"] += 1
            print("Computer wins this round!")
    
    print(f"Final score - You: {score['player']}, Computer: {score['computer']}")

play_game()
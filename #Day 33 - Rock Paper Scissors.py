#Day 33 - Rock Paper Scissors
import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("rock/paper/scissors: ").lower()

if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins!")
print(f"You: {player}, Computer: {computer}")
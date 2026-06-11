# Day 48 - Game Helper
import random

def quick_demo():
    choices = ["Rock", "Paper", "Scissors"]
    print("Quick demo:")
    for player in ["Rock", "Paper", "Scissors"]:
        computer = random.choice(choices)
        print(f"You: {player}, Computer: {computer}")

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

if __name__ == "__main__":
    quick_demo()
    print("Computer picks:", get_computer_choice())
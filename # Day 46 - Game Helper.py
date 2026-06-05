# Day 46 - Game Helper
import random

def play_demo():
    secret = random.randint(1, 20)
    print("Demo: Guess 1–20 (secret =", secret, ")")
    for g in [5, 10, 15, secret]:
        if g < secret:
            print(g, "-> Too low!")
        elif g > secret:
            print(g, "-> Too high!")
        else:
            print(g, "-> Correct!")

def get_random_number(min_val=1, max_val=100):
    return random.randint(min_val, max_val)

if __name__ == "__main__":
    play_demo()
    print("Random 1–50:", get_random_number(1, 50))
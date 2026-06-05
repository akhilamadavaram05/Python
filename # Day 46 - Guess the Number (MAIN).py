# Day 46 - Guess the Number (MAIN)
import random

def main():
    secret = random.randint(1, 100)
    attempts = 0
    print("Guess the Number (1–100)")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Enter an integer.")
            continue

        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
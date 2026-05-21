# Day 40 - Guess the Number (MAIN)
import random

def main():
    target = random.randint(1, 100)
    guesses = 0

    print("Guess the number (1–100)")
    while True:
        try:
            guess = int(input("Guess: "))
            guesses += 1
            if guess < target:
                print("Too low")
            elif guess > target:
                print("Too high")
            else:
                print(f"You got it in {guesses} guesses!")
                break
        except ValueError:
            print("Enter a number")

if __name__ == "__main__":
    main()
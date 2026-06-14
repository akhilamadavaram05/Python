# Day 49 - Secure Password Generator (MAIN)
import random
import string

def generate_password(length=12, use_special=True):
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("Secure Password Generator")
    while True:
        try:
            length = int(input("Password length (e.g. 12): "))
            if length <= 0:
                print("Length must be positive")
                continue
        except ValueError:
            print("Enter an integer")
            continue

        use_special = input("Include special chars? (y/n): ").strip().lower() == "y"
        pwd = generate_password(length, use_special)
        print("Your password:", pwd)

        again = input("Generate another? (y/n): ").strip().lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
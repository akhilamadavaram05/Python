# Day 49 - Password Helper
import random
import string

def quick_demo():
    print("Quick demo:")
    for length in [8, 12, 16]:
        pwd = generate_password(length, True)
        print(f"{length} chars:", pwd)

def generate_password(length=12, use_special=True):
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def count_char_types(pwd):
    lower = sum(1 for c in pwd if c in string.ascii_lowercase)
    upper = sum(1 for c in pwd if c in string.ascii_uppercase)
    digits = sum(1 for c in pwd if c in string.digits)
    special = sum(1 for c in pwd if c in string.punctuation)
    return {"lower": lower, "upper": upper, "digits": digits, "special": special}

if __name__ == "__main__":
    quick_demo()
    pwd = generate_password(12)
    print("Analysis:", count_char_types(pwd))
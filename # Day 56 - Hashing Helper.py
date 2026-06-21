# Day 56 - Hashing Helper
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_password(pwd):
    errors = []
    if len(pwd) < 8:
        errors.append("At least 8 characters")
    if not any(c.islower() for c in pwd):
        errors.append("At least one lowercase letter")
    if not any(c.isupper() for c in pwd):
        errors.append("At least one uppercase letter")
    if not any(c.isdigit() for c in pwd):
        errors.append("At least one digit")
    return errors

def quick_demo():
    print("Quick demo:")
    for pwd in ["abc", "Abc12345", "ValidPass1"]:
        errs = validate_password(pwd)
        print(f"{pwd}:")
        if errs:
            print(" Invalid:", errs)
        else:
            print(" Valid, hash:", hash_password(pwd)[:16], "...")

if __name__ == "__main__":
    quick_demo()
# Day 56 - Hashing & Password Validator (MAIN)
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

def main():
    print("Hashing & Password Validator")
    while True:
        pwd = input("Enter password (or quit): ").strip()
        if pwd.lower() in ["quit", "q"]:
            break

        errors = validate_password(pwd)
        if errors:
            print("Invalid password:")
            for e in errors:
                print(" -", e)
        else:
            print("✅ Valid password")
            print("Hash (SHA-256):", hash_password(pwd))

if __name__ == "__main__":
    main()
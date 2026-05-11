#Day 32 - Password Manager
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$"
    return ''.join(random.choice(chars) for _ in range(length))

passwords = {}
passwords["github"] = generate_password()
passwords["email"] = generate_password(16)

print("GitHub password:", passwords["github"])
print("All passwords:", passwords)
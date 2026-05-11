#Day 32 - Password Helper
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$"
    return ''.join(random.choice(chars) for _ in range(length))

user_passwords = {
    "netflix": generate_password(),
    "bank": generate_password(16)
}
user_passwords["instagram"] = generate_password(14)

print("Total passwords:", len(user_passwords))
for site, pwd in user_passwords.items():
    print(f"{site}: {pwd[:8]}...")
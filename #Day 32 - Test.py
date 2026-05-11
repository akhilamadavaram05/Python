#Day 32 - Test
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$"
    return ''.join(random.choice(chars) for _ in range(length))

test_pwd = generate_password(12)
test_dict = {"test": test_pwd}

print("Password length 12:", len(test_pwd) == 12)
print("Dict has key:", "test" in test_dict)
print("Day 32 test ok")
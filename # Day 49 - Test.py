# Day 49 - Test
from day49_helper import generate_password, count_char_types
import string

def test_password_length():
    for length in [8, 12, 16, 20]:
        pwd = generate_password(length)
        assert len(pwd) == length
    print("✅ Length tests OK")

def test_password_chars():
    pwd = generate_password(12, use_special=True)
    stats = count_char_types(pwd)
    total = stats["lower"] + stats["upper"] + stats["digits"] + stats["special"]
    assert total == len(pwd)
    print("✅ Char type counts OK")
    print("Day 49 test ok")

test_password_length()
test_password_chars()
# Day 56 - Test
from day56_helper import hash_password, validate_password

def test_hash():
    pwd = "TestPass123"
    h = hash_password(pwd)
    assert len(h) == 64  # SHA-256 hex length
    assert h == hash_password(pwd)  # same input → same hash
    print("✅ Hash OK")

def test_validation():
    assert validate_password("abc") != []  # invalid
    assert validate_password("Abc12345") == []  # valid
    assert validate_password("validpass1") != []  # no uppercase
    assert validate_password("UpperPass") != []   # no digit
    print("✅ Validation OK")
    print("Day 56 test ok")

test_hash()
test_validation()
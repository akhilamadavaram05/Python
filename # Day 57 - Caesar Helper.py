# Day 57 - Caesar Helper

def caesar_encrypt(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def quick_demo():
    print("Quick demo (shift=3):")
    msg = "Hello World 123"
    enc = caesar_encrypt(msg, 3)
    dec = caesar_decrypt(enc, 3)
    print("Original:", msg)
    print("Encrypted:", enc)
    print("Decrypted:", dec)

if __name__ == "__main__":
    quick_demo()
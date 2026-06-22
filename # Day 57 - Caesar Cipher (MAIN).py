# Day 57 - Caesar Cipher (MAIN)

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

def main():
    print("Caesar Cipher (Encrypt/Decrypt)")
    while True:
        print("\n1. Encrypt  2. Decrypt  3. Quit")
        choice = input("Choice: ")
        if choice == "3":
            break

        text = input("Text: ")
        try:
            shift = int(input("Shift (1–25): "))
            if shift <= 0 or shift >= 26:
                print("Shift must be 1–25")
                continue
        except ValueError:
            print("Enter an integer")
            continue

        if choice == "1":
            print("Encrypted:", caesar_encrypt(text, shift))
        elif choice == "2":
            print("Decrypted:", caesar_decrypt(text, shift))
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
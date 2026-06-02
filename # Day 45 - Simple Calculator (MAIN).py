# Day 45 - Simple Calculator (MAIN)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: divide by zero"
    return a / b

def main():
    print("Simple Calculator")
    while True:
        print("\n1. +  2. -  3. *  4. /  5. Quit")
        choice = input("Choice: ")
        if choice == "5":
            break
        if choice not in ("1", "2", "3", "4"):
            print("Invalid option")
            continue
        try:
            x = float(input("First number: "))
            y = float(input("Second number: "))
        except ValueError:
            print("Invalid number")
            continue

        if choice == "1":
            print("Result:", add(x, y))
        elif choice == "2":
            print("Result:", sub(x, y))
        elif choice == "3":
            print("Result:", mul(x, y))
        elif choice == "4":
            print("Result:", div(x, y))

if __name__ == "__main__":
    main()
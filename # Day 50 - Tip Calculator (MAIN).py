# Day 50 - Tip Calculator (MAIN)

def calculate_tip(bill, tip_percent, people):
    tip_amount = bill * (tip_percent / 100)
    total = bill + tip_amount
    per_person = total / people
    return tip_amount, total, per_person

def main():
    print("Tip Calculator")
    try:
        bill = float(input("What was the total bill? $"))
        tip_percent = int(input("How much tip (10, 12, or 15)? "))
        people = int(input("How many people to split the bill? "))

        if people <= 0:
            print("People must be positive")
            return

        tip_amount, total, per_person = calculate_tip(bill, tip_percent, people)

        print(f"\nTip amount: $%.2f" % tip_amount)
        print(f"Total bill: $%.2f" % total)
        print(f"Each person pays: $%.2f" % per_person)

    except ValueError:
        print("Invalid input. Use numbers only.")

if __name__ == "__main__":
    main()
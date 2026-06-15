# Day 50 - Tip Helper

def quick_demo():
    print("Quick demo:")
    for bill, tip, people in [
        (100, 10, 2),
        (200, 15, 4),
        (50, 12, 1)
    ]:
        tip_amt, total, per = calculate_tip(bill, tip, people)
        print(f"Bill $%.2f, {tip}% tip, {people} people -> each pays $%.2f" % (bill, tip_amt, per))

def calculate_tip(bill, tip_percent, people):
    tip_amount = bill * (tip_percent / 100)
    total = bill + tip_amount
    per_person = total / people
    return tip_amount, total, per_person

def validate_inputs(bill, tip_percent, people):
    if bill <= 0:
        return "Bill must be positive"
    if tip_percent not in (10, 12, 15):
        return "Tip should be 10, 12, or 15"
    if people <= 0:
        return "People must be positive"
    return None

if __name__ == "__main__":
    quick_demo()
    print("Validate (100, 12, 2):", validate_inputs(100, 12, 2))
    print("Validate (100, 20, 2):", validate_inputs(100, 20, 2))
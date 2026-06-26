# Day 61 - Simple Budget Tracker (MAIN)
import json
from pathlib import Path

FILE = Path("day61_budget.json")

def load_data():
    if FILE.exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return {"income": 0, "expenses": []}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_income(data, amount):
    data["income"] += amount
    save_data(data)

def add_expense(data, title, amount):
    data["expenses"].append({"title": title, "amount": amount})
    save_data(data)

def total_expenses(data):
    return sum(e["amount"] for e in data["expenses"])

def balance(data):
    return data["income"] - total_expenses(data)

def show_report(data):
    print(f"Income: {data['income']}")
    print("Expenses:")
    for e in data["expenses"]:
        print(f"- {e['title']}: {e['amount']}")
    print("Total expenses:", total_expenses(data))
    print("Balance:", balance(data))

def main():
    data = load_data()
    while True:
        print("\n1. Add income\n2. Add expense\n3. Show report\n4. Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            try:
                amt = float(input("Income amount: "))
                add_income(data, amt)
            except ValueError:
                print("Enter a number")
        elif choice == "2":
            title = input("Expense title: ").strip()
            try:
                amt = float(input("Expense amount: "))
                add_expense(data, title, amt)
            except ValueError:
                print("Enter a number")
        elif choice == "3":
            show_report(data)
        elif choice == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
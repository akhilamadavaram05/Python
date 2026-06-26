# Day 61 - Budget Helper
import json
from pathlib import Path

FILE = Path("day61_budget.json")

def load_data():
    if FILE.exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return {"income": 0, "expenses": []}

def seed_sample():
    data = {
        "income": 5000,
        "expenses": [
            {"title": "Rent", "amount": 1500},
            {"title": "Food", "amount": 800},
            {"title": "Travel", "amount": 300},
        ]
    }
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def total_expenses(data):
    return sum(e["amount"] for e in data["expenses"])

def balance(data):
    return data["income"] - total_expenses(data)

if __name__ == "__main__":
    seed_sample()
    data = load_data()
    print("Total expenses:", total_expenses(data))
    print("Balance:", balance(data))
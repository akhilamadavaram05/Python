# Day 58 - Todo Helper
import json
from pathlib import Path

FILE = Path("day58_tasks.json")

def load_tasks():
    if FILE.exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def stats(tasks):
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    pending = total - done
    return {"total": total, "done": done, "pending": pending}

def seed_sample():
    tasks = [
        {"title": "Learn Python", "done": True},
        {"title": "Build project", "done": False},
        {"title": "Push to Git", "done": False},
    ]
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

if __name__ == "__main__":
    seed_sample()
    tasks = load_tasks()
    print("Stats:", stats(tasks))
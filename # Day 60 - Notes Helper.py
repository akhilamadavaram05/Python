# Day 60 - Notes Helper
import json
from pathlib import Path

FILE = Path("day60_notes.json")

def load_notes():
    if FILE.exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def seed_sample():
    notes = [
        {"title": "Python", "body": "Practice functions and files"},
        {"title": "Git", "body": "Commit day60 project"},
        {"title": "Shopping", "body": "Buy milk and eggs"},
    ]
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=2)

def search_notes(notes, term):
    term = term.lower()
    return [n for n in notes if term in n["title"].lower() or term in n["body"].lower()]

if __name__ == "__main__":
    seed_sample()
    notes = load_notes()
    print("Loaded:", len(notes))
    print("Search 'py':", search_notes(notes, "py"))
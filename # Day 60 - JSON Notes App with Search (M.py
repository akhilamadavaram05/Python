 # Day 60 - JSON Notes App with Search (MAIN)
import json
from pathlib import Path

FILE = Path("day60_notes.json")

def load_notes():
    if FILE.exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(notes, title, body):
    notes.append({"title": title, "body": body})
    save_notes(notes)

def list_notes(notes):
    if not notes:
        print("No notes yet")
        return
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['title']}")

def search_notes(notes, term):
    term = term.lower()
    return [n for n in notes if term in n["title"].lower() or term in n["body"].lower()]

def main():
    notes = load_notes()
    while True:
        print("\n1. Add note\n2. List notes\n3. Search notes\n4. Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            body = input("Body: ").strip()
            add_note(notes, title, body)
        elif choice == "2":
            list_notes(notes)
        elif choice == "3":
            term = input("Search term: ").strip()
            results = search_notes(notes, term)
            if not results:
                print("No matching notes")
            else:
                for note in results:
                    print(f"- {note['title']}: {note['body']}")
        elif choice == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
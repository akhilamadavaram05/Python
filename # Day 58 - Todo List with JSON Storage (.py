# Day 58 - Todo List with JSON Storage (MAIN)
import json
from pathlib import Path

FILE = Path("day58_tasks.json")

def load_tasks():
    if FILE.exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")

def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        return True
    return False

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add task\n2. Show tasks\n3. Mark done\n4. Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task(tasks, input("Task title: ").strip())
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                n = int(input("Task number to mark done: ")) - 1
                if not mark_done(tasks, n):
                    print("Invalid task number")
            except ValueError:
                print("Enter an integer")
        elif choice == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
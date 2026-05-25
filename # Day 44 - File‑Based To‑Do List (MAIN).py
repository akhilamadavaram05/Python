# Day 44 - File‑Based To‑Do List (MAIN)
from datetime import datetime

def add_task(task):
    with open("day44_tasks.txt", "a") as f:
        f.write(f"{task},{datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

def show_tasks():
    print("Tasks:")
    try:
        with open("day44_tasks.txt", "r") as f:
            line_num = 1
            for line in f:
                print(f"{line_num}. {line.strip()}")
                line_num += 1
    except FileNotFoundError:
        print("No tasks yet")

def main():
    while True:
        print("\n1. Add task\n2. Show tasks\n3. Quit")
        choice = input("Choice: ")
        if choice == "1":
            add_task(input("Task: "))
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
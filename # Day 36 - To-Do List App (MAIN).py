# Day 36 - To-Do List App (MAIN)
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def show_tasks(self):
        if not self.tasks:
            print("No tasks!")
            return
        for i, t in enumerate(self.tasks, 1):
            status = "✅" if t["done"] else "❌"
            print(f"{i}. {t['task']} {status}")

    def complete_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index-1]["done"] = True

if __name__ == "__main__":
    todo = ToDoList()
    while True:
        print("\n1. Add task\n2. Show tasks\n3. Complete task\n4. Quit")
        choice = input("Choice: ")
        if choice == "1":
            todo.add_task(input("Task: "))
        elif choice == "2":
            todo.show_tasks()
        elif choice == "3":
            todo.show_tasks()
            num = int(input("Task number: "))
            todo.complete_task(num)
        elif choice == "4":
            break
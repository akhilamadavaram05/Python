# Day 36 - To-Do Helper
from day36 import ToDoList

def demo_list():
    td = ToDoList()
    for t in ("Learn Python", "Build project", "Deploy"):
        td.add_task(t)
    td.show_tasks()
    td.complete_task(1)
    print("\nAfter completing first task:")
    td.show_tasks()

if __name__ == "__main__":
    demo_list()
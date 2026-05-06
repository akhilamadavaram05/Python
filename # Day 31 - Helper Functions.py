# Day 31 - Helper Functions
from day31_todo_class import TodoManager

def print_tasks(manager):
    """Helper: Pretty print tasks"""
    print("\n📋 TASKS:")
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks!")
        return
    
    for tid, task, done in tasks:
        status = "✅" if done else "❌"
        print(f"{tid:2d}. {task:<20} {status}")

def add_sample_tasks(manager):
    """Helper: Add demo tasks"""
    samples = ["Learn Python", "Build app", "Deploy project"]
    for task in samples:
        manager.add_task(task)
    print("Added sample tasks!")

def run_demo():
    """Helper: Full demo"""
    todo = TodoManager()
    add_sample_tasks(todo)
    print_tasks(todo)
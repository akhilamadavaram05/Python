# Day 44 - Test
from day44 import add_task, show_tasks

def test_file_based_todo():
    add_task("Test task 44")
    print("Task added; check day44_tasks.txt")
    print("Day 44 test ok")

test_file_based_todo()
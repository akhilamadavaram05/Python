# Day 36 - Test
from day36 import ToDoList

def test_todo_list():
    td = ToDoList()
    # Test add
    td.add_task("Test task")
    assert len(td.tasks) == 1
    # Test complete
    td.complete_task(1)
    assert td.tasks[0]["done"] is True
    print("✅ To‑Do tests OK")
    print("Day 36 test ok")

test_todo_list()
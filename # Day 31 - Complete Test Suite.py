# Day 31 - Complete Test Suite
from day31_todo_class import TodoManager
from day31_todo_helper import print_tasks

def test_todo_class():
    print("🔍 Testing TodoManager...")
    
    # Test 1: Add task
    todo = TodoManager()
    todo.add_task("Test task")
    assert len(todo.tasks) == 1, "Add failed"
    print("✅ Add task OK")
    
    # Test 2: List tasks
    tasks = todo.list_tasks()
    assert len(tasks) == 1, "List failed"
    print("✅ List tasks OK")
    
    # Test 3: Complete task
    todo.complete(1)
    assert todo.tasks[0]["done"] == True, "Complete failed"
    print("✅ Complete task OK")
    
    # Test 4: Stats
    total, done = todo.get_stats()
    assert total == 1 and done == 1, "Stats failed"
    print("✅ Stats OK")
    
    print("🎉 ALL TESTS PASSED!")

# Run tests
test_todo_class()
print_tasks(TodoManager())  # Demo empty
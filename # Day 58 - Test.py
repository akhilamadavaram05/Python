# Day 58 - Test
from day58_helper import seed_sample, load_tasks, stats

def test_stats():
    seed_sample()
    tasks = load_tasks()
    s = stats(tasks)
    assert s["total"] == 3
    assert s["done"] == 1
    assert s["pending"] == 2
    print("✅ Stats OK")
    print("Day 58 test ok")

test_stats()
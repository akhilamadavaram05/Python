# Day 44 - To‑Do Helper
def demo_tasks():
    print("Sample tasks way:")
    print("1. Learn Python")
    print("2. Build project")
    print("3. Deploy")

def count_tasks():
    try:
        with open("day44_tasks.txt", "r") as f:
            count = sum(1 for _ in f)
    except FileNotFoundError:
        count = 0
    print(f"Total tasks: {count}")

if __name__ == "__main__":
    demo_tasks()
    count_tasks()
# Day 31 - Todo Class (Main)
class TodoManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"id": len(self.tasks)+1, "task": task, "done": False})
    
    def list_tasks(self):
        return [(t["id"], t["task"], t["done"]) for t in self.tasks]
    
    def complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                return True
        return False
    
    def get_stats(self):
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t["done"])
        return total, done
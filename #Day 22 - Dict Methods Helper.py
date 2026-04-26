#Day 22 - Dict Methods Helper
data = {"a": 1, "b": 2}

# get() method - safe access
print("A value:", data.get("a", 0))
print("Z value:", data.get("z", 0))